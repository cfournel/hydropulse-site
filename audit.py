#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the built site: indexability checks in every language, plus Lighthouse.

    python3 audit.py                 # static checks on the built files
    python3 audit.py --lighthouse    # + Lighthouse on a sample (home + 1 topic per language)
    python3 audit.py --lighthouse --all
    python3 audit.py --live          # audit https://gethydropulse.com instead of the build

Exit code is 1 if anything failed, so this can gate a deploy.

Two halves, because no single tool covers both:

* **Lighthouse** (Google's own, run headless against the installed Chrome) scores
  performance, accessibility, best practices and SEO per page. Its SEO category is
  deliberately generic — it checks that a page *can* be indexed, not that a
  23-page trilingual site is wired together correctly. It has no idea that
  `/fr/hydratation/au-bureau/` and `/hydration/forgetting-to-drink-water-at-work/` are the same page in two
  languages.
* **The static checks here** cover exactly that gap, and they are the ones that
  actually break silently: an hreflang set that is not reciprocal, a canonical
  pointing at the wrong language, a page missing from the sitemap, two languages
  sharing a description. None of it is visible in a browser, and all of it costs
  rankings.

Lighthouse needs `npx` and Chrome; the static checks need neither, so the useful
half still runs anywhere.
"""

import argparse
import collections
import glob
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import xml.etree.ElementTree as ET
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from content import SITE, TOPICS, LANGS

ROOT = os.path.dirname(os.path.abspath(__file__))
ORIGIN = SITE["origin"]

# Google truncates around these; over is not an error, just wasted space.
TITLE_MAX = 60
DESC_MIN, DESC_MAX = 70, 160
THIN_CONTENT_WORDS = 300

errors, warnings = [], []


def fail(page, msg):
    errors.append((page, msg))


def warn(page, msg):
    warnings.append((page, msg))


# ------------------------------------------------------------- local serve ----

def free_port():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def serve(directory):
    """Serve the build so root-absolute paths (/assets/…) resolve like on Pages."""
    port = free_port()
    handler = lambda *a, **kw: QuietHandler(*a, directory=directory, **kw)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, "http://127.0.0.1:%d" % port


# ------------------------------------------------------------ page parsing ----

def page_paths():
    """Every built page, as a site path -> file path map."""
    out = {}
    for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        rel = os.path.relpath(f, ROOT)
        path = "/" if rel == "index.html" else "/" + rel[: -len("index.html")]
        out[path] = f
    return out


def attr(tag, name):
    m = re.search(r'%s="([^"]*)"' % name, tag)
    return m.group(1) if m else None


def parse(markup):
    head = markup.split("</head>", 1)[0]
    links = re.findall(r"<link [^>]*>", head)
    metas = re.findall(r"<meta [^>]*>", head)
    return {
        "lang": attr(re.search(r"<html [^>]*>", markup).group(0), "lang"),
        "title": (re.search(r"<title>(.*?)</title>", head, re.S) or [None, ""])[1],
        "desc": next((attr(m, "content") for m in metas
                      if attr(m, "name") == "description"), None),
        "canonical": next((attr(l, "href") for l in links
                           if attr(l, "rel") == "canonical"), None),
        "alts": {attr(l, "hreflang"): attr(l, "href") for l in links
                 if attr(l, "rel") == "alternate"},
        "og": {attr(m, "property"): attr(m, "content") for m in metas
               if (attr(m, "property") or "").startswith("og:")},
        "h1": re.findall(r"<h1[^>]*>(.*?)</h1>", markup, re.S),
        "jsonld": re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                             markup, re.S),
        "hrefs": re.findall(r'<a [^>]*href="([^"]+)"', markup),
        "imgs": re.findall(r"<img [^>]*>", markup),
        "text": re.sub(r"<[^>]+>", " ", markup.split("<main", 1)[-1]),
    }


def expected_alternates(path):
    """The full alternate set a page must carry, derived from content.py."""
    for lang in LANGS:
        base = "/" if not lang["base"] else "/%s/" % lang["base"]
        if path == base:
            return {l["code"]: ("/" if not l["base"] else "/%s/" % l["base"])
                    for l in LANGS}
    for key in TOPICS:
        urls = {}
        for l in LANGS:
            prefix = "/%s" % l["base"] if l["base"] else ""
            urls[l["code"]] = "%s/%s/%s/" % (prefix, l["topic_dir"],
                                             l["topics"][key]["slug"])
        if path in urls.values():
            return urls
    return None  # privacy/terms: single-language, no alternate set expected


# ----------------------------------------------------------- static checks ----

def check_pages(pages):
    titles, descs = collections.defaultdict(list), collections.defaultdict(list)

    for path, f in sorted(pages.items()):
        with open(f, encoding="utf-8") as fh:
            p = parse(fh.read())

        if not p["title"]:
            fail(path, "no <title>")
        elif len(p["title"]) > TITLE_MAX:
            warn(path, "title %d chars, truncated in results around %d"
                 % (len(p["title"]), TITLE_MAX))
        if not p["desc"]:
            fail(path, "no meta description")
        elif not DESC_MIN <= len(p["desc"]) <= DESC_MAX:
            warn(path, "meta description %d chars, aim for %d-%d"
                 % (len(p["desc"]), DESC_MIN, DESC_MAX))
        titles[p["title"]].append(path)
        descs[p["desc"]].append(path)

        if len(p["h1"]) != 1:
            fail(path, "%d <h1> elements, expected exactly 1" % len(p["h1"]))

        want = ORIGIN + path
        if p["canonical"] != want:
            fail(path, "canonical is %r, expected %r" % (p["canonical"], want))

        exp = expected_alternates(path)
        if exp is not None:
            for code, target in exp.items():
                got = p["alts"].get(code)
                if got != ORIGIN + target:
                    fail(path, "hreflang %s is %r, expected %r"
                         % (code, got, ORIGIN + target))
            if "x-default" not in p["alts"]:
                fail(path, "no x-default alternate")
            if p["lang"] not in exp:
                fail(path, "html lang=%r is not one of %s" % (p["lang"], sorted(exp)))
            # Reciprocity: Google ignores a one-way alternate set entirely.
            for code, target in exp.items():
                other = pages.get(target)
                if not other:
                    fail(path, "hreflang %s points at %s, which is not built"
                         % (code, target))
                    continue
                with open(other, encoding="utf-8") as fh:
                    back = parse(fh.read())["alts"]
                if back.get(p["lang"]) != ORIGIN + path:
                    fail(path, "%s does not link back with hreflang %s"
                         % (target, p["lang"]))

        for key in ("og:title", "og:description", "og:url"):
            if not p["og"].get(key):
                warn(path, "no %s" % key)

        for block in p["jsonld"]:
            try:
                json.loads(block)
            except ValueError as exc:
                fail(path, "invalid JSON-LD: %s" % exc)

        for img in p["imgs"]:
            if not attr(img, "alt"):
                fail(path, "<img> without alt: %s" % img[:60])

        for href in p["hrefs"]:
            if href.startswith(("http", "mailto:", "#")):
                continue
            if href.endswith("/"):
                if href not in pages:
                    fail(path, "internal link to %s, which is not built" % href)
            elif not os.path.exists(os.path.join(ROOT, href.lstrip("/"))):
                fail(path, "internal link to %s, which does not exist" % href)

        # Policy and terms are legal pages, not landing pages; length is not a virtue there.
        if path not in ("/privacy/", "/terms/"):
            words = len(p["text"].split())
            if words < THIN_CONTENT_WORDS:
                warn(path, "%d words, thin for a page meant to rank" % words)

    for value, paths in titles.items():
        if len(paths) > 1:
            fail(paths[1], "title duplicated with %s" % paths[0])
    for value, paths in descs.items():
        if len(paths) > 1:
            fail(paths[1], "meta description duplicated with %s" % paths[0])


def check_sitemap(pages):
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        fail("/sitemap.xml", "missing")
        return
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = {el.text for el in ET.parse(path).getroot().iter("{%s}loc" % ns["s"])}
    for page in pages:
        if ORIGIN + page not in locs:
            fail("/sitemap.xml", "does not list %s" % page)
    for loc in locs:
        if loc.replace(ORIGIN, "") not in pages:
            fail("/sitemap.xml", "lists %s, which is not built" % loc)

    robots = os.path.join(ROOT, "robots.txt")
    if not os.path.exists(robots):
        fail("/robots.txt", "missing")
    else:
        body = open(robots, encoding="utf-8").read()
        if "Sitemap:" not in body:
            fail("/robots.txt", "does not point at the sitemap")
        if re.search(r"^Disallow: /\s*$", body, re.M):
            fail("/robots.txt", "disallows the whole site")


# ------------------------------------------------------------- lighthouse ----

CATEGORIES = ["performance", "accessibility", "best-practices", "seo"]


def lighthouse(url, tmpdir):
    out = os.path.join(tmpdir, "lh.json")
    cmd = [
        "npx", "--yes", "lighthouse@12", url,
        "--quiet", "--output=json", "--output-path=" + out,
        "--only-categories=" + ",".join(CATEGORIES),
        "--chrome-flags=--headless --no-sandbox --disable-gpu",
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        detail = getattr(exc, "stderr", b"") or b""
        return None, detail.decode("utf-8", "replace").strip().splitlines()[-1:] or [str(exc)]
    with open(out, encoding="utf-8") as fh:
        report = json.load(fh)
    scores = {c: round((report["categories"][c]["score"] or 0) * 100)
              for c in CATEGORIES}
    audits = report["audits"]
    scores["lcp_s"] = round(audits["largest-contentful-paint"]["numericValue"] / 1000, 2)
    scores["cls"] = round(audits["cumulative-layout-shift"]["numericValue"], 3)
    failed = sorted(
        ref["id"] for ref in report["categories"]["seo"]["auditRefs"]
        if audits[ref["id"]].get("score") not in (None, 1)
    )
    return scores, failed


def run_lighthouse(base_url, paths):
    if not shutil.which("npx"):
        print("\nlighthouse: npx not found, skipping\n")
        return
    tmpdir = os.path.join(ROOT, ".lighthouse")
    os.makedirs(tmpdir, exist_ok=True)
    print("\nLighthouse (mobile emulation, %d pages)\n" % len(paths))
    print("  %-34s %5s %5s %5s %5s %7s %6s" %
          ("page", "perf", "a11y", "best", "seo", "LCP s", "CLS"))
    for path in paths:
        scores, failed = lighthouse(base_url + path, tmpdir)
        if scores is None:
            warn(path, "lighthouse failed: %s" % "; ".join(failed))
            print("  %-34s  failed" % path)
            continue
        print("  %-34s %5d %5d %5d %5d %7s %6s" % (
            path, scores["performance"], scores["accessibility"],
            scores["best-practices"], scores["seo"], scores["lcp_s"], scores["cls"]))
        for audit in failed:
            fail(path, "lighthouse seo audit failed: %s" % audit)
        if scores["performance"] < 90:
            warn(path, "performance %d" % scores["performance"])
        if scores["accessibility"] < 90:
            warn(path, "accessibility %d" % scores["accessibility"])
    shutil.rmtree(tmpdir, ignore_errors=True)


def sample_paths(pages):
    """Home plus the first topic in each language — enough to catch per-language
    regressions without paying for 25 Lighthouse runs."""
    out = []
    for lang in LANGS:
        base = "/" if not lang["base"] else "/%s/" % lang["base"]
        prefix = "/%s" % lang["base"] if lang["base"] else ""
        topic = "%s/%s/%s/" % (prefix, lang["topic_dir"],
                               lang["topics"][TOPICS[0]]["slug"])
        out += [p for p in (base, topic) if p in pages]
    return out


# ------------------------------------------------------------------- main ----

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lighthouse", action="store_true", help="also run Lighthouse")
    ap.add_argument("--all", action="store_true",
                    help="with --lighthouse, run every page instead of a sample")
    ap.add_argument("--live", action="store_true",
                    help="point Lighthouse at %s instead of the local build" % ORIGIN)
    args = ap.parse_args()

    pages = page_paths()
    print("%d pages built, %d languages\n" % (len(pages), len(LANGS)))

    check_pages(pages)
    check_sitemap(pages)

    if args.lighthouse:
        targets = sorted(pages) if args.all else sample_paths(pages)
        if args.live:
            run_lighthouse(ORIGIN, targets)
        else:
            httpd, base = serve(ROOT)
            try:
                run_lighthouse(base, targets)
            finally:
                httpd.shutdown()

    for label, items in (("FAIL", errors), ("warn", warnings)):
        if items:
            print("\n%s (%d)" % (label, len(items)))
            for page, msg in items:
                print("  %-34s %s" % (page, msg))

    print("\n%d failures, %d warnings" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

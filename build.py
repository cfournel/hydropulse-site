#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for gethydropulse.com.

    python3 build.py

Writes the whole site (home + topic pages per language, privacy policy, terms,
sitemap, robots.txt, 404) into this directory from the copy in `content.py`.
Generated files are committed — GitHub Pages serves them as-is, there is no
build step on the Pages side.

Everything cross-cutting that SEO depends on — canonical URLs, reciprocal
hreflang alternates, breadcrumbs, JSON-LD — is derived here rather than typed
per page, so adding a language or a topic cannot silently produce a half-linked
page. Rerun after any edit to `content.py`; `git status` shows what changed.
"""

import html
import json
import os
import shutil

from content import SITE, TOPICS, LANGS

ROOT = os.path.dirname(os.path.abspath(__file__))
ORIGIN = SITE["origin"]

# The HydroPulse mark: a droplet with a pulse trace through it — the two halves
# of the product in one glyph (water, and the heart rate that drives the model).
# Kept in step with the launcher icon in store-assets/icon-512.png.
DROPLET_PATH = "M12 3.2C12 3.2 5.8 10 5.8 14.1a6.2 6.2 0 0 0 12.4 0C18.2 10 12 3.2 12 3.2Z"
PULSE_PATH = "M8.4 14.4h2.1l1.1-2.4 1.4 4 1.1-1.6h1.5"

MARK_SHAPES = ('<path d="%s"/><path d="%s"/>' % (DROPLET_PATH, PULSE_PATH))

MARK = ('<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        + MARK_SHAPES + '</svg>')

# The droplet alone, on the app's near-black ground, for the browser tab.
#
# Two deliberate differences from the header mark. The droplet is *filled* rather
# than stroked, and the pulse trace inside it is dropped: at 16px a 1.4px stroke
# lands on roughly one pixel and the interior detail turns to noise, so what
# survives is the silhouette. And the shape is the only thing on the tile, which
# is what makes it identifiable in a strip of twenty tabs.
#
# The PNG and .ico fallbacks are rendered from this file rather than downscaled
# from the store icon, whose gradient turns to mud at 16px. Render them with a
# real SVG engine (see the note in README.md) — ImageMagick's built-in renderer
# silently drops these paths and leaves you a blank dark square.
FAVICON_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
               '<rect width="24" height="24" rx="5" fill="#0F191C"/>'
               '<path d="' + DROPLET_PATH + '" fill="#38B6E8"/></svg>')


# ------------------------------------------------------------------ paths ----

def home_url(lang):
    return "/" if not lang["base"] else "/%s/" % lang["base"]


def topic_url(lang, key):
    prefix = "/%s" % lang["base"] if lang["base"] else ""
    return "%s/%s/%s/" % (prefix, lang["topic_dir"], lang["topics"][key]["slug"])


def privacy_url(lang):
    # One policy document, in English, shared by every language — it is also the
    # URL declared in the Play Console, so it must never move.
    return "/privacy/"


def terms_url(lang):
    return "/terms/"


def out_path(url):
    """`/fr/hydratation/au-bureau/` -> `<repo>/fr/hydratation/au-bureau/index.html`"""
    rel = url.strip("/")
    return os.path.join(ROOT, rel, "index.html") if rel else os.path.join(ROOT, "index.html")


def esc(s):
    return html.escape(s, quote=False)


# --------------------------------------------------------------- template ----

def head(lang, title, desc, url, alternates, jsonld):
    """alternates: [(hreflang, path)], first entry also used for x-default."""
    links = "".join(
        '\n<link rel="alternate" hreflang="%s" href="%s%s">' % (code, ORIGIN, path)
        for code, path in alternates
    )
    links += '\n<link rel="alternate" hreflang="x-default" href="%s%s">' % (ORIGIN, alternates[0][1])
    blocks = "".join(
        '\n<script type="application/ld+json">%s</script>' % json.dumps(b, ensure_ascii=False)
        for b in jsonld
    )
    if SITE.get("search_console"):
        blocks = ('\n<meta name="google-site-verification" content="%s">'
                  % esc(SITE["search_console"])) + blocks
    return """<!doctype html>
<html lang="%(code)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(origin)s%(url)s">%(links)s
<meta property="og:type" content="website">
<meta property="og:site_name" content="HydroPulse">
<meta property="og:locale" content="%(code)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(origin)s%(url)s">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#0F191C">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">%(blocks)s
</head>
<body>
""" % {
        "code": lang["code"], "title": esc(title), "desc": esc(desc),
        "origin": ORIGIN, "url": url, "links": links, "blocks": blocks,
    }


def header(lang, alternates, title):
    """The wordmark spells out the page's own <title>, not just "HydroPulse"."""
    langs = "".join(
        '<a href="%s" hreflang="%s" %s>%s</a>' % (
            path, code,
            'aria-current="true"' if code == lang["code"] else "",
            next(l["label"] for l in LANGS if l["code"] == code),
        )
        for code, path in alternates
    )
    return """<header class="site-head"><div class="wrap">
  <a class="mark" href="%s">%s<span>%s</span></a>
  <nav class="langs" aria-label="%s">%s</nav>
</div></header>
<main class="wrap">
""" % (home_url(lang), MARK, esc(title), esc(lang["ui"]["langs_label"]), langs)


def footer(lang):
    ui = lang["ui"]
    items = "".join("<li>%s</li>" % i for i in [
        '<a href="%s">%s</a>' % (home_url(lang), esc(ui["home_crumb"])),
        '<a href="%s">%s</a>' % (privacy_url(lang), esc(ui["foot_privacy"])),
        '<a href="%s">%s</a>' % (terms_url(lang), esc(ui["foot_terms"])),
        '<a href="%s" rel="noopener">%s</a>' % (SITE["play"], esc(ui["foot_play"])),
    ])
    return """</main>
<footer class="site-foot"><div class="wrap">
  <ul>%s</ul>
  <p>%s</p>
</div></footer>
</body>
</html>
""" % (items, esc(lang["ui"]["foot_tag"]))


def cta(lang):
    """Official Google Play badge, localised, served from assets/badges/.

    Google's badge guidelines require the artwork unmodified, so it is an <img>
    rather than a redrawn button: no recolouring for dark mode, no cropping, and
    the width/height attributes match the file's own aspect ratio.
    """
    ui = lang["ui"]
    return ('<p><a class="cta" href="%s" rel="noopener">'
            '<img src="/assets/badges/%s.png" width="216" height="84" '
            'alt="%s" loading="lazy" decoding="async"></a></p>\n'
            '<p class="muted">%s %s</p>\n'
            % (SITE["play"], lang["code"], esc(ui["badge_alt"]),
               esc(ui["cta_note"]), esc(ui["app_lang_note"])))


def how_it_works(lang):
    ui = lang["ui"]
    steps = "".join("<li>%s</li>" % esc(s) for s in ui["how_steps"])
    return "<h2>%s</h2>\n<ol class=\"steps\">%s</ol>\n" % (esc(ui["how_title"]), steps)


def features(lang):
    ui = lang["ui"]
    items = "".join("<li>%s</li>" % esc(f) for f in ui["features"])
    return '<h2>%s</h2>\n<ul class="checks">%s</ul>\n' % (esc(ui["features_title"]), items)


def sources(lang):
    """Naming the methodology sources is the trust signal that separates an
    estimate from a guess — and the disclaimer beside it is what keeps a
    health-adjacent page honest, and Play-policy-safe."""
    ui = lang["ui"]
    return ("<h2>%s</h2>\n<p>%s</p>\n"
            "<h2>%s</h2>\n<div class=\"callout\"><p>%s</p></div>\n" % (
                esc(ui["sources_title"]), esc(ui["sources_body"]),
                esc(ui["safety_title"]), esc(ui["safety_body"])))


def privacy_block(lang):
    ui = lang["ui"]
    return ("<h2>%s</h2>\n<p>%s</p>\n<p><a href=\"%s\">%s</a></p>\n" % (
        esc(ui["privacy_title"]), esc(ui["privacy_body"]),
        privacy_url(lang), esc(ui["privacy_link"])))


def screens(lang, only=None):
    """Watch captures, 480x480 downscaled to 400. Every image is lazy-loaded and
    carries its intrinsic width/height, which is what keeps CLS at 0 and keeps
    them out of the LCP measurement.

    The app's UI is English-only, so one set of files is shared across languages;
    alt text and captions are localised, the pixels are not.
    """
    items = [i for i in lang["ui"]["screens"] if only is None or i[0] in only]
    figures = []
    for key, alt, caption in items:
        figures.append(
            '<li><figure>'
            '<img src="/assets/screens/%s.webp" width="400" height="400" '
            'loading="lazy" decoding="async" alt="%s">'
            '<figcaption>%s</figcaption></figure></li>'
            % (key, esc(alt), esc(caption)))
    return '<ul class="shots">%s</ul>\n' % "".join(figures)


def topic_cards(lang, exclude=None):
    lis = []
    for key in TOPICS:
        if key == exclude:
            continue
        t = lang["topics"][key]
        lis.append('<li><a href="%s"><strong>%s</strong><span>%s</span></a></li>'
                   % (topic_url(lang, key), esc(t["nav"]), esc(t["card"])))
    return '<ul class="cards">%s</ul>\n' % "".join(lis)


def write(url, markup):
    path = out_path(url)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markup)
    return path


# ------------------------------------------------------------------ pages ----

def alternates_home():
    return [(l["code"], home_url(l)) for l in LANGS]


def alternates_topic(key):
    return [(l["code"], topic_url(l, key)) for l in LANGS]


def app_jsonld(lang, url, desc):
    return {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "HydroPulse",
        "operatingSystem": "Wear OS 3.0+",
        "applicationCategory": "HealthApplication",
        "description": desc,
        "url": ORIGIN + url,
        "inLanguage": lang["code"],
        "installUrl": SITE["play"],
        "offers": {"@type": "Offer", "price": "2.59", "priceCurrency": "USD"},
    }


def build_home(lang):
    h = lang["home"]
    ui = lang["ui"]
    url = home_url(lang)
    alts = alternates_home()
    site_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "HydroPulse",
        "url": ORIGIN + "/",
        "inLanguage": [l["code"] for l in LANGS],
    }
    body = ["<h1>%s</h1>\n" % esc(h["h1"]), '<p class="lede">%s</p>\n' % esc(h["lede"])]
    body.append(cta(lang))
    body += ["<p>%s</p>\n" % esc(p) for p in h["intro"]]
    body.append(how_it_works(lang))
    body.append(features(lang))
    body.append("<h2>%s</h2>\n" % esc(ui["screens_title"]))
    body.append(screens(lang))
    body.append("<h2>%s</h2>\n" % esc(ui["topics_title"]))
    body.append(topic_cards(lang))
    body.append(sources(lang))
    body.append(privacy_block(lang))
    markup = (head(lang, h["title"], h["desc"], url, alts,
                   [site_ld, app_jsonld(lang, url, h["desc"])])
              + header(lang, alts, h["title"]) + "".join(body) + footer(lang))
    return write(url, markup)


def build_topic(lang, key):
    t = lang["topics"][key]
    ui = lang["ui"]
    url = topic_url(lang, key)
    alts = alternates_topic(key)

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": lang["code"],
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in t["faq"]
        ],
    }
    crumbs_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": ui["home_crumb"],
             "item": ORIGIN + home_url(lang)},
            {"@type": "ListItem", "position": 2, "name": t["nav"],
             "item": ORIGIN + url},
        ],
    }

    body = ['<p class="crumbs"><a href="%s">%s</a> &rsaquo; %s</p>\n'
            % (home_url(lang), esc(ui["home_crumb"]), esc(t["nav"]))]
    body.append("<h1>%s</h1>\n" % esc(t["h1"]))
    body.append('<p class="lede">%s</p>\n' % esc(t["lede"]))
    body.append("<h2>%s</h2>\n" % esc(t["why_title"]))
    body += ["<p>%s</p>\n" % esc(p) for p in t["why"]]
    body.append('<h2>%s</h2>\n<ul class="checks">%s</ul>\n' % (
        esc(ui["works_title"]), "".join("<li>%s</li>" % esc(w) for w in t["works_on"])))
    body.append(how_it_works(lang))
    body.append("<h2>%s</h2>\n<p>%s</p>\n" % (esc(ui["expect_title"]), esc(t["expect"])))
    body.append(screens(lang, only={"home", "notification"}))
    body.append(cta(lang))
    body.append('<h2>%s</h2>\n<div class="faq">%s</div>\n' % (
        esc(ui["faq_title"]),
        "".join("<h3>%s</h3><p>%s</p>" % (esc(q), esc(a)) for q, a in t["faq"])))
    body.append(sources(lang))
    body.append(privacy_block(lang))
    body.append("<h2>%s</h2>\n%s" % (esc(ui["related_title"]), topic_cards(lang, exclude=key)))

    markup = (head(lang, t["title"], t["desc"], url, alts,
                   [crumbs_ld, faq_ld, app_jsonld(lang, url, t["desc"])])
              + header(lang, alts, t["title"]) + "".join(body) + footer(lang))
    return write(url, markup)


# The policy text below is the published form of docs/PRIVACY_POLICY.md in this
# repo. It is the URL declared in the Play Console, so keep the two in sync and
# never move the path.
PRIVACY_BODY = """<h1>Privacy Policy</h1>
<p class="muted">Last updated: %(updated)s</p>

<p class="lede">HydroPulse estimates your hydration needs from data that stays on
your watch. There is no account, no advertising SDK and no product analytics.</p>

<h2>Summary</h2>
<div class="callout">
  <p>We do not sell data, run ads, or track what you do in the app. Two things
  leave the device, and neither carries your health data: an anonymous weather
  lookup (coordinates only, no account or device identifier), and a crash report
  if the app fails.</p>
</div>

<h2>Data we process</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Data</th><th>Purpose</th><th>Where it is stored</th><th>Sent off-device?</th></tr></thead>
  <tbody>
    <tr><td>Heart rate (watch sensor)</td><td>Estimate exertion for the hydration model</td>
        <td>On-device memory only, not persisted long-term</td><td>No</td></tr>
    <tr><td>Steps, active calories, exercise state</td><td>Distinguish activity from rest</td>
        <td>On-device memory only</td><td>No</td></tr>
    <tr><td>Approximate (coarse) location</td><td>Look up local temperature and humidity</td>
        <td>Not stored; used transiently for the weather call</td>
        <td>Yes — coordinates only, to Open-Meteo (open-meteo.com), with no account or device identifier</td></tr>
    <tr><td>Weight, age, biological sex, resting and maximum heart rate, sweat profile, pregnancy or nursing status</td>
        <td>Personalise the hydration model</td><td>Locally on-device (Android DataStore)</td><td>No</td></tr>
    <tr><td>Water intake log (amount and timestamp)</td><td>Show history and feed the hydration ledger</td>
        <td>Locally on-device (Room database)</td><td>No</td></tr>
    <tr><td>Crash reports: stack trace, device model, OS version, app version, and a Firebase installation identifier</td>
        <td>Diagnose and fix crashes</td><td>Sent on next launch after a crash; not stored in the app</td>
        <td>Yes — to Firebase Crashlytics (Google). Contains no heart rate, no activity, no water log and no location</td></tr>
  </tbody>
</table>
</div>

<h2>Crash reporting</h2>
<p>HydroPulse uses <strong>Firebase Crashlytics</strong> (Google) so that a crash
can be diagnosed and fixed. When the app fails, it sends a stack trace along with
the device model, OS version, app version and a Firebase installation identifier
&mdash; an identifier for the app install, not for you.</p>
<div class="callout">
  <p>A crash report never contains your heart rate, your activity, your water log,
  your profile or your location. It describes the failure, not the user.</p>
</div>
<p>Crashlytics is governed by
<a href="https://firebase.google.com/support/privacy" rel="noopener">Google&rsquo;s
Firebase privacy documentation</a>. Reports are retained for a limited period and
then deleted.</p>

<h2>What we do not do</h2>
<ul>
  <li>No account creation, no login, no advertising identifiers.</li>
  <li>No advertising SDKs, and no product or usage analytics &mdash; nothing records
    which screens you open or how often you use the app.</li>
  <li>No backend of ours &mdash; the only network calls are the weather lookup and,
    after a failure, a crash report.</li>
  <li>No sale or sharing of personal data with third parties.</li>
</ul>

<h2>Health data</h2>
<p>Heart rate and activity data are sensitive under Google Play&rsquo;s health and
fitness data policies. HydroPulse uses this data solely to compute the in-app
hydration estimate, does not transmit raw heart-rate or activity data anywhere
&mdash; crash reports included &mdash; and does not use it for advertising or
profiling.</p>

<h2>Permissions requested, and why</h2>
<ul>
  <li><strong>BODY_SENSORS</strong> — read heart rate for the exertion component of the model.</li>
  <li><strong>ACTIVITY_RECOGNITION</strong> — detect steps and exercise sessions.</li>
  <li><strong>ACCESS_COARSE_LOCATION</strong> — look up local weather. Precise location is never requested.</li>
  <li><strong>POST_NOTIFICATIONS</strong> — deliver hydration reminders.</li>
</ul>
<p>All four are optional. Declined, the app keeps working with sensible defaults
for the components it can no longer sense.</p>

<h2>Data retention and deletion</h2>
<p>All personal data &mdash; profile, water log, ledger &mdash; lives in local app
storage on your watch. Uninstalling the app deletes it. There is no server-side
account or profile to delete, because none exists. The one exception is crash
reports, which sit with Firebase Crashlytics under Google&rsquo;s own retention
period; write to the address below to have any relating to your installation
removed.</p>

<h2>Children&rsquo;s privacy</h2>
<p>HydroPulse is not directed at children under 13 (or the relevant age of digital
consent in your jurisdiction) and does not knowingly collect data from them.</p>

<h2>Changes to this policy</h2>
<p>Material changes are reflected here with an updated date above, and shipped
alongside an app release note.</p>

<h2>Contact</h2>
<p>Questions about this policy can be sent to
<a href="mailto:%(email)s">%(email)s</a>.</p>
""" % {"email": SITE["email"], "updated": "30 August 2026"}


TERMS_BODY = """<h1>Terms of Service</h1>
<p class="muted">Last updated: %(updated)s</p>

<p class="lede">HydroPulse is a wellness tool sold as a one-time purchase on Google
Play. These terms cover what it is, what it is not, and what you can expect.</p>

<h2>The licence</h2>
<p>Purchasing HydroPulse grants you a personal, non-exclusive, non-transferable
licence to use the app on devices associated with your Google account, under the
Google Play Terms of Service. You may not redistribute, resell or reverse-engineer
the app except where that right cannot be excluded by law.</p>

<h2>Not medical advice</h2>
<div class="callout">
  <p>HydroPulse produces an <strong>estimate</strong> of fluid balance, not a
  measurement of your hydration state. It is not a medical device. It does not
  diagnose, treat, cure, monitor or prevent dehydration or any other condition,
  and it must not be used as a substitute for professional medical advice.</p>
</div>
<p>If you take diuretics, have a fluid restriction, or live with a kidney, heart
or endocrine condition, follow your clinician&rsquo;s guidance on fluid intake
rather than this app&rsquo;s. Seek urgent care for confusion, fainting, or signs of
heat illness. Drinking very large volumes of plain water in a short time can be
dangerous; the app is not designed to encourage it.</p>

<h2>Accuracy</h2>
<p>The model depends on sensor readings, on the profile you enter and on public
weather data. Optical wrist heart-rate sensors are imperfect, weather is regional
rather than local to you, and a profile that is out of date will produce estimates
that are out of date. The app is provided &ldquo;as is&rdquo;, without warranty that
its estimates are accurate for any particular person or situation.</p>

<h2>Third-party services</h2>
<p>Weather data comes from Open-Meteo (open-meteo.com), crash reporting from
Firebase Crashlytics (Google), and distribution and billing from Google Play. None
of them receives personal data from HydroPulse beyond what is described in the
<a href="/privacy/">privacy policy</a>.</p>

<h2>Refunds</h2>
<p>Refunds are handled by Google Play under its own refund policy. We have no
separate billing relationship with you and cannot process a payment or a refund
directly.</p>

<h2>Liability</h2>
<p>To the maximum extent permitted by law, liability arising from use of the app is
limited to the amount you paid for it. Nothing in these terms limits liability that
cannot be limited by law, including your statutory consumer rights.</p>

<h2>Changes</h2>
<p>These terms may change alongside app updates. The date above records the current
version.</p>

<h2>Contact</h2>
<p><a href="mailto:%(email)s">%(email)s</a></p>
""" % {"email": SITE["email"], "updated": "30 August 2026"}


def build_doc(url, title, desc, body):
    """The policy and terms exist once, in English, shared by every language."""
    en = LANGS[0]
    markup = (head(en, title, desc, url, [(en["code"], url)], [])
              + header(en, alternates_home(), title) + body + footer(en))
    return write(url, markup)


def build_404():
    en = LANGS[0]
    body = ("<h1>Page not found</h1>\n"
            '<p class="lede">That page does not exist. Start from the home page, or pick a '
            "topic below.</p>\n" + topic_cards(en))
    title = "Page not found — HydroPulse"
    markup = (head(en, title, "This page does not exist.",
                   "/404.html", [(en["code"], "/")], [])
              + header(en, alternates_home(), title) + body + footer(en))
    path = os.path.join(ROOT, "404.html")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(markup)
    return path


def build_sitemap():
    entries = []
    for lang in LANGS:
        entries.append((home_url(lang), alternates_home(), "1.0"))
    for key in TOPICS:
        for lang in LANGS:
            entries.append((topic_url(lang, key), alternates_topic(key), "0.8"))
    entries.append(("/privacy/", [("en", "/privacy/")], "0.3"))
    entries.append(("/terms/", [("en", "/terms/")], "0.3"))

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, alts, priority in entries:
        out.append("  <url>")
        out.append("    <loc>%s%s</loc>" % (ORIGIN, url))
        for code, path in alts:
            out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>'
                       % (code, ORIGIN, path))
        out.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>'
                   % (ORIGIN, alts[0][1]))
        out.append("    <lastmod>%s</lastmod>" % SITE["updated"])
        out.append("    <priority>%s</priority>" % priority)
        out.append("  </url>")
    out.append("</urlset>")
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    return path


def build_robots():
    path = os.path.join(ROOT, "robots.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % ORIGIN)
    return path


def clean():
    """Drop generated language/topic trees so renamed slugs don't leave orphans."""
    for lang in LANGS:
        d = lang["base"] or lang["topic_dir"]
        target = os.path.join(ROOT, d)
        if os.path.isdir(target):
            shutil.rmtree(target)
    for d in ("privacy", "terms"):
        target = os.path.join(ROOT, d)
        if os.path.isdir(target):
            shutil.rmtree(target)


def build_favicon_svg():
    path = os.path.join(ROOT, "assets", "favicon.svg")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FAVICON_SVG + "\n")
    return path


def main():
    clean()
    written = [build_favicon_svg()]
    for lang in LANGS:
        written.append(build_home(lang))
        for key in TOPICS:
            written.append(build_topic(lang, key))
    written.append(build_doc(
        "/privacy/", "Privacy Policy — HydroPulse",
        "HydroPulse keeps your heart rate, activity and drink log on the watch. This policy "
        "explains exactly what is processed and what leaves the device.",
        PRIVACY_BODY))
    written.append(build_doc(
        "/terms/", "Terms of Service — HydroPulse",
        "The terms covering the HydroPulse app: licence, accuracy, refunds, and why an "
        "estimate is not a medical assessment.",
        TERMS_BODY))
    written.append(build_404())
    written.append(build_sitemap())
    written.append(build_robots())
    for path in written:
        print(os.path.relpath(path, ROOT))
    print("\n%d files written" % len(written))


if __name__ == "__main__":
    main()

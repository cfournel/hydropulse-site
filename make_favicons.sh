#!/usr/bin/env bash
# Rasterise assets/favicon.svg into the PNG and .ico fallbacks.
#
#     python3 build.py && ./make_favicons.sh
#
# Run this whenever FAVICON_SVG changes in build.py. The outputs are committed,
# like every other generated file here.
#
# Why Chromium and not ImageMagick: `convert favicon.svg out.png` looks like it
# works and silently produces a blank dark square. ImageMagick delegates SVG to
# rsvg-convert, and when that is not installed it falls back to its own renderer,
# which drops the paths without an error. Chromium is the engine the icon will
# actually be displayed by, so it is also the one that should rasterise it.
set -euo pipefail

cd "$(dirname "$0")"
# Scratch space inside the repo, not /tmp: Chromium is commonly installed as a
# confined snap, which cannot read files under /tmp and fails with nothing but a
# missing output file. Gitignored.
tmp=.favicon-build
rm -rf "$tmp"; mkdir -p "$tmp"
trap 'rm -rf "$tmp"' EXIT

svg=$(cat assets/favicon.svg)

render() {  # render <size> <destination>
  local size=$1 dest=$2
  cat > "$tmp/page.html" <<HTML
<style>html,body{margin:0;padding:0;background:transparent}
svg{display:block;width:${size}px;height:${size}px}</style>
$svg
HTML
  # A page, not a data: URL — Chromium blocks file:// subresources from data:.
  chromium --headless --disable-gpu --no-sandbox \
    --default-background-color=00000000 \
    --window-size="$size,$size" --hide-scrollbars \
    --screenshot="$dest" "file://$PWD/$tmp/page.html" >/dev/null 2>&1
}

render 16 "$tmp/16.png"
render 32 "$tmp/32.png"
render 48 "$tmp/48.png"
render 180 "$tmp/180.png"

cp "$tmp/16.png" assets/favicon-16.png
cp "$tmp/32.png" assets/favicon-32.png

# iOS composites the home-screen icon on its own background and applies its own
# corner mask, so this one is flattened opaque rather than left with alpha corners.
convert "$tmp/180.png" -background "#0F191C" -alpha remove -alpha off assets/apple-touch-icon.png

convert "$tmp/16.png" "$tmp/32.png" "$tmp/48.png" favicon.ico

identify assets/favicon-16.png assets/favicon-32.png assets/apple-touch-icon.png favicon.ico

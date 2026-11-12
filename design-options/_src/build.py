"""Generate /design-options/ for the timgutowski.com redesign review.
Run: python3 build.py <output dir>   (writes <out>/design-options/...)"""
import os, sys
from shared import *
from options import OPTIONS
from palettes import PALETTES

out = os.path.join(sys.argv[1] if len(sys.argv) > 1 else "out", "design-options")
os.makedirs(os.path.join(out, "assets"), exist_ok=True)


def w(path, text):
    p = os.path.join(out, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)


w("assets/palettes.css", "/* Color palettes for the design options. Edit or add a block to try new colors.\n   Every text/background pair is checked for WCAG 2.2 AA contrast (4.5:1). */\n" + palettes_css())
w("assets/base.css", BASE_CSS)
w("assets/switcher.js", switcher_js())

for folder, key, name, fn, blurb in OPTIONS:
    css, home, work = fn()
    home = home.replace("<blockquote>", '<p class="bq">').replace("</blockquote>", "</p>")
    css = css.replace(".outcome blockquote", ".outcome .bq")
    w(f"{folder}/style.css", f"/* Design option: {name} */\n" + css.strip() + "\n")
    w(f"{folder}/index.html", page(key, f"{name} · Design option · Tim Gutowski", home, "style.css"))
    w(f"{folder}/work.html", page(key, f"Work · {name} · Design option · Tim Gutowski", work, "style.css"))

# Review index
cards = ""
for i, (folder, key, name, fn, blurb) in enumerate(OPTIONS):
    cards += f'''<li class="opt"><a class="shot" href="{folder}/index.html" data-keep tabindex="-1" aria-hidden="true"><img src="shots/{folder}.png" alt="" width="1200" height="760" loading="lazy"></a>
<div class="tx"><p class="num">Option {folder.split("-")[0]}</p><h2><a href="{folder}/index.html" data-keep>{e(name)}</a></h2><p>{e(blurb)}</p>
<ul class="lk"><li><a href="{folder}/index.html" data-keep>Home</a></li><li><a href="{folder}/work.html" data-keep>Work</a></li><li><a href="preview.html?src={folder}/index.html" data-keep>Phone view</a></li></ul></div></li>'''
pal_list = "".join(f'<li><span class="sw" style="background:linear-gradient(135deg,{p["primary"]} 0 50%,{p["accent"]} 50%)"></span>{e(p["label"])}</li>' for p in PALETTES.values())
index = f'''<!doctype html><html lang="en" data-palette="classic" data-home="index.html"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>Design options · timgutowski.com redesign</title><link rel="icon" href="../img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/palettes.css"><link rel="stylesheet" href="assets/base.css">
<style>
body{{font:400 17px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif;background:#F4F3EF;color:#16181D}}
.wrap{{max-width:1180px;margin:0 auto;padding:56px 32px 120px}}
h1{{font-size:clamp(34px,4vw,48px);line-height:1.1;margin:0 0 16px;letter-spacing:-.02em}}
.intro{{max-width:46em;color:#3f4450}}.intro p{{margin:0 0 12px}}
.how{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:32px 0 48px}}
.how div{{background:#fff;border-radius:14px;padding:22px 24px;border:1px solid #E3E1DA}}.how h2{{font-size:18px;margin:0 0 8px}}.how ul{{margin:0;padding-left:20px}}
.pl{{list-style:none;padding:0;margin:8px 0 0;display:flex;flex-wrap:wrap;gap:8px 20px}}.pl li{{display:flex;align-items:center;gap:8px}}
.sw{{width:20px;height:20px;border-radius:50%;display:inline-block;border:1px solid rgba(0,0,0,.15)}}
.opts{{list-style:none;margin:0;padding:0;display:grid;gap:28px}}
.opt{{display:grid;grid-template-columns:1.2fr 1fr;gap:32px;background:#fff;border-radius:18px;padding:20px;border:1px solid #E3E1DA;align-items:center}}
.shot img{{border-radius:10px;border:1px solid #E3E1DA}}
.num{{font:600 13px/1 system-ui;text-transform:uppercase;letter-spacing:.12em;color:#3B5BA9;margin:0 0 8px}}
.opt h2{{font-size:30px;margin:0 0 10px;letter-spacing:-.01em}}.opt h2 a{{text-decoration:none}}.opt h2 a:hover{{text-decoration:underline}}
.opt p{{margin:0 0 16px;color:#3f4450}}
.lk{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:10px}}
.lk a{{display:inline-block;padding:9px 16px;border-radius:999px;border:1.5px solid #16181D;text-decoration:none;font-weight:600;font-size:15px}}
.lk li:first-child a{{background:#16181D;color:#fff}}
#pal-slot{{margin:0 0 28px}}#pal-slot .pal{{position:static;display:inline-block;box-shadow:none}}
:focus-visible{{outline:3px solid #3B5BA9;outline-offset:3px}}
@media (max-width:820px){{.how,.opt{{grid-template-columns:1fr}}.wrap{{padding:32px 16px 120px}}}}
</style><script src="assets/switcher.js"></script></head><body>
<main id="main" class="wrap">
<h1>Three design directions for timgutowski.com</h1>
<div class="intro"><p>Each option uses the same real content (homepage and Work page) so you can compare the look and feel, not the words. Nothing here is final: type, layout, and color can be mixed across options.</p>
<p>Pick a palette with the color control just above the options (it also sits in the lower-left corner of every option page). Your choice follows you from page to page.</p></div>
<div class="how"><div><h2>What to look for</h2><ul><li>Which one feels most like a consultant you&rsquo;d hire?</li><li>Which homepage tells you fastest what Tim does?</li><li>Anything you&rsquo;d steal from one option for another?</li></ul></div>
<div><h2>Palettes to try</h2><ul class="pl">{pal_list}</ul><p style="margin:12px 0 0;font-size:15px;color:#3f4450">Every palette passes WCAG 2.2 AA contrast for text.</p></div></div>
<div id="pal-slot"></div>
<ol class="opts">{cards}</ol>
</main></body></html>
'''
w("index.html", index)

preview = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><title>Phone view · Design options</title>
<style>body{margin:0;background:#2b2d33;font:500 15px system-ui,sans-serif;color:#fff;min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:24px 16px}
.bar{display:flex;gap:16px;margin-bottom:18px;flex-wrap:wrap;justify-content:center}.bar a{color:#fff}
.phone{width:390px;height:844px;max-width:100%;border-radius:48px;border:12px solid #0d0e11;overflow:hidden;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.5)}
iframe{width:100%;height:100%;border:0}.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}:focus-visible{outline:3px solid #FFD95A;outline-offset:3px}</style></head><body>
<nav class="bar" aria-label="Preview"><a href="index.html" id="back">All options</a><a id="desk" href="#">Open at full size</a></nav>
<main class="phone"><h1 class="sr-only">Phone-size preview</h1><iframe id="f" title="Phone-size preview of the design option"></iframe></main>
<script>var q=new URLSearchParams(location.search),s=q.get('src')||'1-editorial/index.html',p=q.get('palette');
if(!/^[0-9]-[a-z]+\\/(index|work)\\.html$/.test(s))s='1-editorial/index.html';
var u=s+(p?'?palette='+encodeURIComponent(p):'');document.getElementById('f').src=u;document.getElementById('desk').href=u;
if(p)document.getElementById('back').href='index.html?palette='+encodeURIComponent(p);</script></body></html>
'''
w("preview.html", preview)
print("wrote", out)

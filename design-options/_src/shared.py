"""Shared pieces: palette CSS, base accessibility CSS, palette switcher, page shell."""
from palettes import PALETTES
from content import *
import html as H

FONTS = {
    "editorial": "family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500",
    "studio": "family=Archivo:wght@400;500;600;800;900&family=Inter:wght@400;500;600",
    "swiss": "family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500",
    "warm": "family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Source+Sans+3:wght@400;600",
    "consult": "family=DM+Serif+Display&family=Plus+Jakarta+Sans:wght@400;500;600;700",
}


def palettes_css():
    out = []
    for i, (k, p) in enumerate(PALETTES.items()):
        sel = f':root[data-palette="{k}"]' if i else f':root, :root[data-palette="{k}"]'
        out.append(sel + "{" + ";".join(f"--{n}:{v}" for n, v in p.items() if n != "label") + "}")
    return "\n".join(out) + "\n"


BASE_CSS = """/* Shared accessibility and reset rules for every design option. */
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink)}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
.skip{position:absolute;left:12px;top:-60px;z-index:100;background:var(--ink);color:var(--bg);padding:10px 14px;border-radius:6px;text-decoration:none;font-weight:600}
.skip:focus{top:12px}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
:focus-visible{outline:3px solid var(--primary);outline-offset:3px;border-radius:4px}
.on-deep :focus-visible,.on-primary :focus-visible{outline-color:var(--accent)}
a,button{min-height:24px}
.wwk,.wwk p{color:var(--ondeep)!important}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
/* Palette switcher (review only) */
.pal{position:fixed;left:12px;bottom:12px;z-index:90;background:#111;color:#fff;border-radius:12px;padding:10px 12px;font:500 13px/1.3 system-ui,sans-serif;box-shadow:0 6px 24px rgba(0,0,0,.25);max-width:calc(100vw - 24px)}
.pal p{margin:0 0 8px;display:flex;justify-content:space-between;gap:12px;align-items:center}
.pal a{color:#fff}
.pal .sw{display:flex;gap:8px;flex-wrap:wrap}
.pal button{width:32px;height:32px;border-radius:50%;border:2px solid #fff;cursor:pointer;padding:0;background:linear-gradient(135deg,var(--a) 0 50%,var(--b) 50% 100%)}
.pal button[aria-pressed=true]{box-shadow:0 0 0 3px #111,0 0 0 5px #fff}
.pal button:focus-visible{outline:3px solid #FFD95A;outline-offset:3px}
.pal .hide{background:none;border:0;color:#bbb;width:auto;height:auto;font:inherit;text-decoration:underline;cursor:pointer}
@media print{.pal{display:none}}
"""


def switcher_js():
    items = ",".join(f'["{k}","{p["label"]}","{p["primary"]}","{p["accent"]}"]' for k, p in PALETTES.items())
    return """/* Palette switcher for the design review pages. Not for production. */
(function(){
  var P=[%s];
  var root=document.documentElement;
  function get(){var q=new URLSearchParams(location.search).get('palette');if(q)return q;try{return localStorage.getItem('tg-palette')}catch(e){return null}}
  function set(k){root.setAttribute('data-palette',k);try{localStorage.setItem('tg-palette',k)}catch(e){}
    document.querySelectorAll('.pal button[data-k]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.k===k)});
    document.querySelectorAll('a[data-keep]').forEach(function(a){var u=new URL(a.href,location.href);u.searchParams.set('palette',k);a.href=u.pathname+u.search+u.hash})}
  var cur=get()||'classic';root.setAttribute('data-palette',cur);
  document.addEventListener('DOMContentLoaded',function(){
    if(window.self!==window.top && !/[?&]panel=1/.test(location.search)){set(cur);return}
    var d=document.createElement('div');d.className='pal';d.setAttribute('role','region');d.setAttribute('aria-label','Design review controls');
    var home=root.getAttribute('data-home')||'../index.html';d.innerHTML='<p><span>Color palette</span><a href="'+home+'" data-keep>All options</a></p><div class="sw" role="group" aria-label="Color palette"></div><p style="margin:8px 0 0"><button type="button" class="hide">Hide controls</button></p>';
    var g=d.querySelector('.sw');
    P.forEach(function(p){var b=document.createElement('button');b.type='button';b.dataset.k=p[0];b.title=p[1];b.setAttribute('aria-label',p[1]);b.style.setProperty('--a',p[2]);b.style.setProperty('--b',p[3]);b.addEventListener('click',function(){set(p[0])});g.appendChild(b)});
    d.querySelector('.hide').addEventListener('click',function(){d.remove()});
    var slot=document.getElementById('pal-slot');(slot||document.body).appendChild(d);if(slot)d.querySelector('.hide').parentNode.remove();set(cur);
  });
})();
""" % items


def page(opt, title, body, css, depth="../", desc=""):
    return f"""<!doctype html>
<html lang="en" data-palette="classic">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc or H1)}">
<link rel="icon" href="{depth}../img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[opt]}&display=swap">
<link rel="stylesheet" href="{depth}assets/palettes.css">
<link rel="stylesheet" href="{depth}assets/base.css">
<link rel="stylesheet" href="{css}">
<script src="{depth}assets/switcher.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
</body>
</html>
"""


def e(s):
    return H.escape(s, quote=False).replace("'", "&rsquo;")


def nav_links(active):
    items = [("Home", "index.html"), ("Work", "work.html"), ("Services", "../../consulting.html"), ("About", "../../about.html")]
    return "".join(f'<li><a href="{h}"{" aria-current=page" if n == active else ""}{" data-keep" if not h.startswith("..") else ""}>{n}</a></li>' for n, h in items)


ICONS = {  # simple inline SVG line icons, decorative
    "wp": '<path d="M4 6h16M4 12h10M4 18h16" />',
    "data": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2" />',
    "app": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>',
    "a11y": '<circle cx="12" cy="5" r="2"/><path d="M5 9l7 1 7-1M12 10v5l-3 6M12 15l3 6"/>',
    "api": '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
    "cloud": '<path d="M7 18h10a4 4 0 0 0 0-8 6 6 0 0 0-11.6 1.5A3.5 3.5 0 0 0 7 18z"/>',
}


def icon(k, size=28):
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[k]}</svg>'


def img(p, cls=""):
    return f'<img src="../../img/{p["img"]}" alt="{e(p["alt"])}" width="1571" height="1206" loading="lazy"{f" class={cls!r}" if cls else ""}>'


def wwk_panel(cls="wwk"):
    return f'<div class="{cls}" role="img" aria-label="Illustration: Wendy\'s Wonderful Kids"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg><p>Helping children in foster care find permanent families.</p></div>'


def clients_html(hcls="cg"):
    return "".join(f'<div class="{hcls}"><h3>{e(g)}</h3><ul>' + "".join(f"<li>{e(n)}</li>" for n in names) + "</ul></div>" for g, names in CLIENTS)

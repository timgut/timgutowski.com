"""Five design directions. Each returns (css, home_body, work_body)."""
from shared import *

YEAR = "2026"


def footer(cls, extra=""):
    return f'''<footer class="{cls}"><div class="wrap ft">
<p class="ft-name">Tim Gutowski <span>Software &amp; Technology Consulting · Chicago, IL</span></p>
<ul class="ft-links"><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{LINKEDIN}">LinkedIn</a></li><li><a href="../../resume.html">Résumé</a></li></ul>
{extra}<p class="ft-small">© {YEAR} Tim Gutowski</p></div></footer>'''


UNION_ALT = "Workers on a picket line in 1941, holding signs that read Unionism is Americanism and We want a contract"
CREDIT_CODE = 'Code photo: <a href="https://unsplash.com/@juanjodev02">Juanjo Jaramillo</a> on Unsplash.'
CREDIT_UNION = 'Picket line photo: <a href="https://unsplash.com/@nypl">The New York Public Library</a> on Unsplash.'
CREDIT_DESK = ''


def credits(*c):
    c = [x for x in c if x]
    return f'<p class="ft-small ft-credit">{" ".join(c)}</p>' if c else ""


def union_band(cls, eb, h, p):
    return f'''<section class="ub {cls}" aria-labelledby="ub-h"><div class="ub-img"><img src="../../img/union-picket-1941.jpg" alt="{UNION_ALT}" width="2000" height="1351" loading="lazy"></div>
<div class="ub-tx"><p class="ub-eb">{eb}</p><h2 id="ub-h">{h}</h2><p>{p}</p><p class="ub-cr">Photo: The New York Public Library on Unsplash</p></div></section>'''


def header(cls, active, brand):
    return f'''<header class="{cls}"><div class="wrap hd">
<a class="brand" href="index.html" data-keep>{brand}</a>
<nav aria-label="Main"><ul class="nav">{nav_links(active)}</ul></nav>
<a class="hd-cta" href="../../contact.html">Start a project</a>
</div></header>'''


# ---------------------------------------------------------------- 1. Refined editorial
def editorial():
    css = """
body{font:400 18px/1.65 Inter,system-ui,sans-serif}
.wrap{max-width:1160px;margin:0 auto;padding:0 32px}
h1,h2,h3,.serif{font-family:Lora,Georgia,serif;font-weight:600;letter-spacing:-.01em;color:var(--ink)}
.mono{font:500 13px/1.4 'Fira Code',monospace;letter-spacing:.02em;color:var(--muted)}
header.ed{border-bottom:1px solid var(--line);background:var(--bg)}
.hd{display:flex;align-items:center;gap:32px;min-height:84px}
.brand{font-family:Lora,serif;font-weight:700;font-size:22px;text-decoration:none;color:var(--ink);margin-right:auto}
.brand small{display:block;font:500 12px/1.2 Inter,sans-serif;color:var(--muted);letter-spacing:.04em;text-transform:uppercase;margin-top:2px}
.nav{display:flex;gap:28px;list-style:none;margin:0;padding:0}
.nav a{text-decoration:none;font-size:16px;color:var(--ink);padding:6px 0}
.nav a[aria-current]{box-shadow:inset 0 -2px var(--primary)}
.hd-cta{font-weight:600;font-size:16px;color:var(--primary);text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:6px;text-decoration-color:var(--accent)}
.hero{display:grid;grid-template-columns:1.6fr 1fr;gap:72px;padding:96px 0 72px}
.hero h1{font-size:clamp(42px,6vw,76px);line-height:1.04;margin:18px 0 28px}
.hero h1 em{font-style:italic;color:var(--primary);background:linear-gradient(transparent 62%,var(--accent) 62% 92%,transparent 92%)}
.lede{font-size:21px;color:var(--ink);max-width:36em}
.lede+p{color:var(--muted)}
.aside{border-left:1px solid var(--line);padding-left:32px;align-self:end}
.aside h2{font:600 13px/1.4 Inter,sans-serif;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:0 0 14px}
.aside ul{list-style:none;margin:0 0 28px;padding:0}
.aside li{font-family:Lora,serif;font-size:20px;padding:8px 0;border-bottom:1px solid var(--line)}
.btn{display:inline-block;background:var(--primary);color:var(--onprimary);padding:14px 22px;border-radius:2px;text-decoration:none;font-weight:600;font-size:16px}
.link{font-weight:600;color:var(--primary);text-underline-offset:5px}
.ctas{display:flex;gap:28px;align-items:center;margin-top:32px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--ink);border-bottom:1px solid var(--line);margin-bottom:96px}
.stats div{padding:28px 28px 28px 0}.stats div+div{padding-left:28px;border-left:1px solid var(--line)}
.stats b{display:block;font:600 52px/1 Lora,serif;color:var(--primary)}
.stats span{display:block;color:var(--muted);font-size:16px;margin-top:10px}
.sec{padding:0 0 104px}
.sec-h{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding-bottom:16px;margin-bottom:8px}
.sec-h h2{font-size:40px;margin:0}
.svc{display:grid;grid-template-columns:1fr 1fr;column-gap:72px;list-style:none;margin:0;padding:0;counter-reset:s}
.svc li{counter-increment:s;padding:28px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:56px 1fr}
.svc li::before{content:counter(s,decimal-leading-zero);font:500 14px/2 'Fira Code',monospace;color:var(--primary)}
.svc h3{font-size:24px;margin:0 0 6px}.svc p{margin:0;color:var(--muted)}
.spread{display:grid;grid-template-columns:1.25fr 1fr;gap:64px;align-items:center;padding:56px 0;border-bottom:1px solid var(--line)}
.spread:nth-child(even) .fig{order:2}
.fig img{border:1px solid var(--line);box-shadow:0 30px 60px -30px rgba(0,0,0,.25)}
.spread h3{font-size:36px;line-height:1.1;margin:10px 0 16px}
.spread p{color:var(--muted)}
.tags{font:500 13px/1.6 'Fira Code',monospace;color:var(--muted)}
.wwk{background:var(--deep);color:var(--ondeep);aspect-ratio:4/3;display:flex;flex-direction:column;justify-content:flex-end;padding:40px}
.wwk p{font:500 30px/1.2 Lora,serif;margin:16px 0 0;max-width:14em}
.proc{display:grid;grid-template-columns:repeat(3,1fr);gap:48px;list-style:none;padding:0;margin:40px 0 0}
.proc b{display:block;font:italic 500 64px/1 Lora,serif;color:var(--primary);margin-bottom:12px}
.proc h3{font-size:26px;margin:0 0 8px}.proc p{color:var(--muted);margin:0}
.cta{background:var(--tint);padding:96px 0;text-align:center}
.cta h2{font-size:clamp(36px,5vw,60px);margin:0 0 20px}
.cta p{max-width:34em;margin:0 auto 32px;font-size:20px}
footer.ed{border-top:1px solid var(--line);padding:40px 0 120px;font-size:15px;color:var(--muted)}
.ft{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:baseline}
.ft-name{margin:0 auto 0 0;color:var(--ink);font-family:Lora,serif;font-weight:600;font-size:18px}.ft-name span{display:block;font:400 14px Inter,sans-serif;color:var(--muted)}
.ft-links{display:flex;gap:24px;list-style:none;margin:0;padding:0}.ft-small{width:100%;margin:8px 0 0}
.pagehead{padding:88px 0 48px;border-bottom:1px solid var(--line);margin-bottom:24px}
.pagehead h1{font-size:clamp(44px,6vw,80px);margin:12px 0 20px}
.caps{display:grid;grid-template-columns:1fr 1fr;column-gap:72px}
.caps div{padding:24px 0;border-bottom:1px solid var(--line)}.caps h3{font-size:22px;margin:0 0 6px}.caps p{margin:0 0 8px;color:var(--muted)}
.clients{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 56px;margin-top:32px}
.cg h3{font:600 13px/1.4 Inter,sans-serif;text-transform:uppercase;letter-spacing:.08em;color:var(--primary);border-top:2px solid var(--ink);padding-top:12px;margin:0 0 10px}
.cg ul{list-style:none;margin:0;padding:0}.cg li{font-size:16px;padding:3px 0}
@media (max-width:820px){.wrap{padding:0 20px}.hd{flex-wrap:wrap;gap:8px 20px;padding:14px 0}.nav{order:3;width:100%;gap:20px}.hero,.spread,.svc,.caps{grid-template-columns:1fr}.hero{gap:40px;padding:56px 0}.aside{border-left:0;padding-left:0}.stats{grid-template-columns:1fr}.stats div+div{border-left:0;padding-left:0;border-top:1px solid var(--line)}.spread{gap:28px}.spread:nth-child(even) .fig{order:0}.proc,.clients{grid-template-columns:1fr;gap:32px}.svc{column-gap:0}.sec-h h2{font-size:32px}}
"""
    brand = 'Tim Gutowski<small>Software &amp; Technology Consulting</small>'
    svc = "".join(f"<li><div></div><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>" for t, d, _ in SERVICES).replace("<div></div>", "", 0)
    svc = "".join(f"<li><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>" for t, d, _ in SERVICES)
    def spread(p, long=False):
        fig = img(p) if p["img"] else wwk_panel()
        return f'''<article class="spread"><div class="fig">{fig}</div><div><p class="mono">{e(p["client"])}{" · " + p["url"] if p["url"] else ""}</p>
<h3>{e(p["title"])}</h3><p>{e(p["long"] if long else p["short"])}</p><p class="tags">{e(p["tags"])}</p></div></article>'''
    home = header("ed", "Home", brand) + f'''
<main id="main"><div class="wrap">
<section class="hero"><div><p class="mono">{e(EYEBROW)}</p>
<h1><em>Right-sized</em> technology solutions for organizations big and small.</h1>
<p class="lede">{e(LEDE)}</p><p>{e(LEDE2)}</p>
<div class="ctas"><a class="btn" href="../../contact.html">Start a project</a><a class="link" href="work.html" data-keep>See recent work</a></div></div>
<div class="aside"><h2>Built for</h2><ul>{"".join(f"<li>{e(b)}</li>" for b in BUILT_FOR)}</ul></div></section>
<div class="stats">{"".join(f"<div><b>{n}</b><span>{e(t)}</span></div>" for n, t in STATS)}</div>
<section class="sec" aria-labelledby="s1"><div class="sec-h"><h2 id="s1">What I do</h2><a class="link" href="../../consulting.html">Services &amp; engagements</a></div><ol class="svc">{svc}</ol></section>
<section class="sec" aria-labelledby="s2"><div class="sec-h"><h2 id="s2">Recent projects</h2><a class="link" href="work.html" data-keep>All work</a></div>{spread(PROJECTS[0])}{spread(PROJECTS[1])}</section>
<section class="sec" aria-labelledby="s3"><div class="sec-h"><h2 id="s3">How we work together</h2></div>
<ol class="proc">{"".join(f"<li><b>0{i+1}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(PROCESS))}</ol></section>
</div>
<section class="cta" aria-labelledby="s4"><div class="wrap"><h2 id="s4">{e(CTA_H)}</h2><p>{e(CTA_P)}</p><div class="ctas" style="justify-content:center"><a class="btn" href="../../contact.html">Start a project</a><a class="link" href="mailto:{EMAIL}">Email me</a></div></div></section>
</main>''' + footer("ed")
    work = header("ed", "Work", brand) + f'''
<main id="main"><div class="wrap">
<section class="pagehead"><p class="mono">Selected work</p><h1>Work</h1><p class="lede">{e(WORK_INTRO)}</p></section>
<section class="sec" aria-labelledby="fp"><h2 id="fp" class="sr-only">Featured projects</h2>{"".join(spread(p, True) for p in PROJECTS)}</section>
<section class="sec" aria-labelledby="w2"><div class="sec-h"><h2 id="w2">More of what I build</h2></div>
<div class="caps">{"".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p><p class='tags'>{e(s)}</p></div>" for t, d, s in CAPABILITIES)}</div></section>
<section class="sec" aria-labelledby="w3"><div class="sec-h"><h2 id="w3">Organizations I've built for</h2></div><div class="clients">{clients_html()}</div></section>
</div>
<section class="cta" aria-labelledby="w4"><div class="wrap"><h2 id="w4">Want something like this?</h2><div class="ctas" style="justify-content:center"><a class="btn" href="../../contact.html">Start the conversation</a></div></div></section>
</main>''' + footer("ed")
    return css, home, work


# ---------------------------------------------------------------- 2. Bold studio
def studio():
    css = """
body{font:400 18px/1.6 Inter,system-ui,sans-serif}
.wrap{max-width:1240px;margin:0 auto;padding:0 32px}
h1,h2,h3{font-family:Archivo,Inter,sans-serif;font-weight:800;letter-spacing:-.02em;line-height:.98;margin:0}
header.st{background:var(--primary);color:var(--onprimary)}
.hd{display:flex;align-items:center;gap:28px;min-height:84px}
.brand{font:900 26px/1 Archivo,sans-serif;color:var(--onprimary);text-decoration:none;margin-right:auto;letter-spacing:-.02em}
.brand span{color:var(--accent)}
.nav{display:flex;gap:6px;list-style:none;margin:0;padding:0}
.nav a{color:var(--onprimary);text-decoration:none;font-weight:600;font-size:16px;padding:10px 14px;border-radius:999px}
.nav a[aria-current]{box-shadow:inset 0 0 0 2px var(--onprimary)}
.hd-cta{background:var(--accent);color:var(--onaccent);font-weight:700;text-decoration:none;padding:12px 20px;border-radius:999px;font-size:16px}
.hero{position:relative;background:var(--primary);color:var(--onprimary);padding:112px 0 0;overflow:hidden;min-height:760px}
.hero .wrap,.pagehead .wrap{position:relative;z-index:2}
.bg{position:absolute;inset:0;background:var(--primary)}
.bg img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1);opacity:.55}
.bg::after{content:"";position:absolute;inset:0;background:var(--primary);mix-blend-mode:multiply;opacity:.9}
.bg::before{content:"";position:absolute;right:-90px;top:120px;width:300px;height:300px;border-radius:50%;background:var(--accent);z-index:1;opacity:.95}
.hero .eb{font-weight:600;font-size:15px;letter-spacing:.12em;text-transform:uppercase;color:var(--onprimary);opacity:.9;margin:0 0 24px}
.hero h1{color:var(--onprimary);font-size:clamp(52px,9vw,128px);max-width:11ch}
.hero h1 mark{background:var(--accent);color:var(--onaccent);padding:0 .12em;border-radius:.08em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hero-row{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:end;padding:48px 0 88px}
.hero-row p{font-size:20px;margin:0;max-width:30em}
.btns{display:flex;gap:12px;flex-wrap:wrap;justify-content:flex-end}
.btn{display:inline-block;padding:16px 26px;border-radius:999px;font-weight:700;text-decoration:none;font-size:17px}
.btn.y{background:var(--accent);color:var(--onaccent)}.btn.o{border:2px solid currentColor;color:inherit}
.btn.p{background:var(--primary);color:var(--onprimary)}
.band{background:var(--accent);color:var(--onaccent);padding:20px 0;font:800 22px/1.2 Archivo,sans-serif;letter-spacing:-.01em}
.band ul{display:flex;flex-wrap:wrap;gap:8px 28px;list-style:none;margin:0;padding:0}
.band li::after{content:"✦";margin-left:28px;font-size:16px;vertical-align:middle}.band li:last-child::after{content:none}
.sec{padding:110px 0}
.sec-h{display:flex;justify-content:space-between;align-items:end;gap:24px;margin-bottom:48px}
.sec-h h2{font-size:clamp(44px,6vw,84px)}
.more{font-weight:700;color:var(--primary);text-underline-offset:6px;text-decoration-thickness:2px}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;list-style:none;margin:0;padding:0}
.tiles li{background:var(--surface);border:2px solid var(--ink);border-radius:20px;padding:28px;transition:transform .2s,box-shadow .2s}
.tiles li:hover{transform:translate(-4px,-4px);box-shadow:8px 8px 0 var(--ink)}
.tiles .ic{width:56px;height:56px;border-radius:16px;background:var(--tint);color:var(--primary);display:grid;place-items:center;margin-bottom:22px}
.tiles h3{font-size:28px;margin-bottom:10px}.tiles p{margin:0;color:var(--muted)}
.proj{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.card{border-radius:24px;overflow:hidden;background:var(--tint);display:flex;flex-direction:column}
.card .fig{padding:36px 36px 0}.card .fig img{border-radius:12px 12px 0 0}
.card .tx{background:var(--surface);padding:28px 32px 32px;border-top:2px solid var(--ink);flex:1}
.card .cl{font-weight:700;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:var(--primary);margin:0 0 10px}
.card h3{font-size:36px;margin-bottom:12px}.card p{margin:0 0 12px;color:var(--muted)}
.tags{font-size:14px;font-weight:600;color:var(--ink)!important}
.wwk{background:var(--deep);color:var(--ondeep);min-height:280px;border-radius:12px 12px 0 0;padding:32px;display:flex;flex-direction:column;justify-content:flex-end}
.wwk p{font:800 30px/1.05 Archivo,sans-serif;margin:16px 0 0}
.deep{background:var(--deep);color:var(--ondeep)}
.deep h2{color:var(--ondeep)}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;list-style:none;margin:0;padding:0}
.steps b{display:block;font:900 120px/.8 Archivo,sans-serif;color:var(--accent);margin-bottom:20px}
.steps h3{font-size:34px;color:var(--ondeep);margin-bottom:10px}.steps p{color:var(--deepmuted);margin:0}
.cta{padding:96px 0}
.cta-box{background:var(--accent);color:var(--onaccent);border-radius:32px;padding:72px;display:grid;grid-template-columns:1.4fr 1fr;gap:40px;align-items:end}
.cta-box h2{font-size:clamp(44px,6vw,88px)}.cta-box p{margin:0 0 24px;font-size:19px}
footer.st{background:var(--ink);color:var(--bg);padding:48px 0 120px;font-size:15px}
.ft{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:baseline}
.ft-name{margin:0 auto 0 0;font:800 22px Archivo,sans-serif}.ft-name span{display:block;font:400 14px Inter,sans-serif;opacity:.85;margin-top:6px}
.ft-links{display:flex;gap:24px;list-style:none;margin:0;padding:0}.ft-small{width:100%;margin:8px 0 0;opacity:.8}
footer.st :focus-visible{outline-color:var(--accent)}
.pagehead{position:relative;overflow:hidden;background:var(--primary);color:var(--onprimary);padding:120px 0 120px}
.ub{position:relative;min-height:520px;display:flex;align-items:flex-end;background:var(--deep);overflow:hidden}
.ub-img{position:absolute;inset:0}.ub-img img{width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:grayscale(1) contrast(1.05)}
.ub-tx{position:relative;z-index:2;background:var(--accent);color:var(--onaccent);max-width:560px;margin:0 0 56px 32px;padding:32px 36px;border-radius:24px}
.ub-tx h2{font-size:clamp(32px,4vw,52px);color:var(--onaccent);margin-bottom:14px}.ub-tx p{margin:0 0 10px}.ub-eb{font-weight:700;font-size:14px;letter-spacing:.12em;text-transform:uppercase}
.ub-cr{font-size:13px}
.ub :focus-visible{outline-color:var(--onaccent)}
.ft-credit a{color:inherit}
.pagehead h1{color:var(--onprimary);font-size:clamp(64px,11vw,160px)}
.pagehead p{font-size:21px;max-width:34em;margin:28px 0 0}
.capg{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.capg div{border-top:4px solid var(--primary);padding-top:16px}.capg h3{font-size:22px;margin-bottom:8px}.capg p{font-size:16px;color:var(--muted);margin:0 0 8px}
.clients{columns:3;column-gap:48px}
.cg{break-inside:avoid;margin-bottom:32px}.cg h3{font-size:24px;margin-bottom:10px}
.cg ul{list-style:none;margin:0;padding:0}.cg li{padding:6px 0;border-bottom:1px solid var(--line);font-weight:500}
@media (max-width:860px){.wrap{padding:0 20px}.hd{flex-wrap:wrap;gap:10px;padding:14px 0}.nav{order:3;width:100%;overflow-x:auto}.hero-row,.proj,.cta-box{grid-template-columns:1fr}.hero{min-height:0}.bg::before{display:none}.ub-tx{margin:0 16px 24px}.btns{justify-content:flex-start}.tiles,.steps,.capg{grid-template-columns:1fr}.clients{columns:1}.sec{padding:72px 0}.cta-box{padding:40px 28px}.steps b{font-size:84px}.card .fig{padding:20px 20px 0}}
"""
    brand = 'TG<span>.</span>'
    tiles = "".join(f'<li><div class="ic">{icon(k)}</div><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d, k in SERVICES)
    def card(p, long=False):
        fig = img(p) if p["img"] else wwk_panel()
        return f'<article class="card"><div class="fig">{fig}</div><div class="tx"><p class="cl">{e(p["client"])}</p><h3>{e(p["title"])}</h3><p>{e(p["long"] if long else p["short"])}</p><p class="tags">{e(p["tags"])}</p></div></article>'
    home = header("st on-primary", "Home", brand) + f'''
<main id="main">
<section class="hero on-primary"><div class="bg"><img src="../../img/code-editor.jpg" alt="" width="2000" height="1333"></div><div class="wrap"><p class="eb">{e(EYEBROW)}</p>
<h1><mark>Right-sized</mark> tech for orgs big &amp; small.</h1>
<div class="hero-row"><p>{e(LEDE)} {e(LEDE2)}</p><div class="btns"><a class="btn y" href="../../contact.html">Start a project</a><a class="btn o" href="work.html" data-keep>See the work</a></div></div></div></section>
<div class="band" aria-label="Built for"><div class="wrap"><ul>{"".join(f"<li>{e(b)}</li>" for b in BUILT_FOR)}</ul></div></div>
<section class="sec" aria-labelledby="s1"><div class="wrap"><div class="sec-h"><h2 id="s1">What I do</h2><a class="more" href="../../consulting.html">Services &amp; engagements</a></div><ul class="tiles">{tiles}</ul></div></section>
<section class="sec" style="padding-top:0" aria-labelledby="s2"><div class="wrap"><div class="sec-h"><h2 id="s2">Recent work</h2><a class="more" href="work.html" data-keep>All work</a></div><div class="proj">{card(PROJECTS[0])}{card(PROJECTS[1])}</div></div></section>
<section class="sec deep on-deep" aria-labelledby="s3"><div class="wrap"><div class="sec-h"><h2 id="s3">How we work</h2></div>
<ol class="steps">{"".join(f"<li><b>0{i+1}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(PROCESS))}</ol></div></section>
<section class="cta" aria-labelledby="s4"><div class="wrap"><div class="cta-box"><h2 id="s4">Let&rsquo;s build something that fits.</h2><div><p>{e(CTA_P)}</p><div class="btns" style="justify-content:flex-start"><a class="btn p" href="../../contact.html">Start a project</a><a class="btn o" href="mailto:{EMAIL}">Email me</a></div></div></div></div></section>
</main>''' + footer("st", credits(CREDIT_CODE))
    work = header("st on-primary", "Work", brand) + f'''
<main id="main">
<section class="pagehead on-primary"><div class="bg"><img src="../../img/portfolio-hero.jpg" alt="" width="1788" height="775"></div><div class="wrap"><h1>Work.</h1><p>{e(WORK_INTRO)}</p></div></section>
<section class="sec" aria-labelledby="fp"><h2 id="fp" class="sr-only">Featured projects</h2><div class="wrap"><div class="proj">{card(PROJECTS[0], True)}{card(PROJECTS[1], True)}</div><div class="proj" style="margin-top:24px;grid-template-columns:1fr">{card(PROJECTS[2], True)}</div></div></section>
<section class="sec" style="padding-top:0" aria-labelledby="w2"><div class="wrap"><div class="sec-h"><h2 id="w2">More of what I build</h2></div>
<div class="capg">{"".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p><p class='tags'>{e(s)}</p></div>" for t, d, s in CAPABILITIES)}</div></div></section>
{union_band("on-deep","Who I build for","Built for people who do the work.","Labor unions, worker-safety researchers, advocacy groups, and public agencies: most of my clients exist to serve working people, and their websites have to work for them.")}
<section class="sec deep on-deep" aria-labelledby="w3"><div class="wrap"><div class="sec-h"><h2 id="w3">Who I&rsquo;ve built for</h2></div><div class="clients">{clients_html()}</div></div></section>
<section class="cta" aria-labelledby="w4"><div class="wrap"><div class="cta-box"><h2 id="w4">Want something like this?</h2><div><a class="btn p" href="../../contact.html">Start the conversation</a></div></div></div></section>
</main>''' + footer("st", credits(CREDIT_UNION))
    css += ".deep .cg li{border-color:rgba(255,255,255,.18)}.deep .cg h3{color:var(--accent)}"
    return css, home, work


# ---------------------------------------------------------------- 3. Technical / Swiss grid
def swiss():
    css = """
body{font:400 17px/1.6 'IBM Plex Sans',system-ui,sans-serif}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
.mono{font-family:'IBM Plex Mono',monospace}
h1,h2,h3{font-weight:600;letter-spacing:-.015em;margin:0;color:var(--ink);line-height:1.15}
header.sw{border-bottom:1px solid var(--ink);background:var(--bg)}
.hd{display:grid;grid-template-columns:3fr 6fr 3fr;align-items:center;min-height:72px}
.brand{font:600 15px 'IBM Plex Mono',monospace;color:var(--ink);text-decoration:none}
.brand b{background:var(--primary);color:var(--onprimary);padding:4px 7px;margin-right:8px}
.nav{display:flex;gap:28px;list-style:none;margin:0;padding:0}
.nav a{text-decoration:none;font-size:15px;color:var(--ink);padding:6px 0}
.nav a[aria-current]::before{content:"→ ";color:var(--primary)}
.hd-cta{justify-self:end;font:500 14px 'IBM Plex Mono',monospace;color:var(--onprimary);background:var(--primary);padding:10px 14px;text-decoration:none}
.grid{display:grid;grid-template-columns:repeat(12,1fr);border-left:1px solid var(--line)}
.grid>*{border-right:1px solid var(--line)}
.lbl{font:500 13px/1.4 'IBM Plex Mono',monospace;color:var(--primary);text-transform:uppercase;letter-spacing:.06em}
.hero{border-bottom:1px solid var(--ink)}
.hero .a{grid-column:span 8;padding:72px 40px 64px 0}.hero .b{grid-column:span 4;padding:72px 0 64px 32px;display:flex;flex-direction:column;justify-content:space-between}
.hero h1{font-size:clamp(40px,5.4vw,70px);line-height:1.04;margin:20px 0 28px}
.hero h1 span{color:var(--primary)}
.hero p{margin:0 0 16px;max-width:34em;color:var(--muted)}.hero p.big{font-size:20px;color:var(--ink)}
dl.meta{margin:0;font:400 14px/1.5 'IBM Plex Mono',monospace}
dl.meta div{display:grid;grid-template-columns:110px 1fr;padding:10px 0;border-top:1px solid var(--line)}
dl.meta dt{color:var(--muted)}dl.meta dd{margin:0}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.btn{font:500 15px 'IBM Plex Mono',monospace;padding:14px 18px;text-decoration:none;border:1px solid var(--ink);color:var(--ink)}
.btn.p{background:var(--ink);color:var(--bg)}
.stats{border-bottom:1px solid var(--ink)}
.stats>div{grid-column:span 4;padding:32px 24px 32px 0}.stats>div+div{padding-left:24px}
.stats b{display:block;font:500 56px/1 'IBM Plex Mono',monospace;color:var(--ink)}
.stats b::after{content:"";display:block;width:32px;height:4px;background:var(--accent);margin-top:14px}
.stats span{display:block;margin-top:12px;color:var(--muted);font-size:15px}
.sec{padding:88px 0 0}
.sec-h{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--ink);padding-bottom:14px}
.sec-h h2{font-size:34px}.sec-h a{font:500 14px 'IBM Plex Mono',monospace;color:var(--primary)}
.rows{list-style:none;margin:0;padding:0;counter-reset:r}
.rows li{display:grid;grid-template-columns:80px 1fr 1.6fr;gap:24px;padding:22px 0;border-bottom:1px solid var(--line);counter-increment:r;align-items:baseline}
.rows li::before{content:"[" counter(r,decimal-leading-zero) "]";font:500 14px 'IBM Plex Mono',monospace;color:var(--primary)}
.rows h3{font-size:21px}.rows p{margin:0;color:var(--muted)}
.specs{display:grid;grid-template-columns:1fr 1fr;gap:0;border-left:1px solid var(--line)}
.spec{border-right:1px solid var(--line);border-bottom:1px solid var(--line);padding:28px}
.spec img{border:1px solid var(--line);margin-bottom:22px}
.spec h3{font-size:26px;margin:8px 0 10px}.spec p{color:var(--muted);margin:0 0 16px}
.spec dl{margin:0;font:400 13px/1.5 'IBM Plex Mono',monospace}.spec dl div{display:grid;grid-template-columns:80px 1fr;border-top:1px solid var(--line);padding:8px 0}.spec dt{color:var(--muted)}.spec dd{margin:0}
.wwk{background:var(--deep);color:var(--ondeep);aspect-ratio:4/3;padding:28px;display:flex;flex-direction:column;justify-content:flex-end;margin-bottom:22px}
.wwk p{font:500 24px/1.25 'IBM Plex Sans',sans-serif;margin:14px 0 0}
.tl{display:grid;grid-template-columns:repeat(3,1fr);list-style:none;margin:0;padding:0}
.tl li{border-top:4px solid var(--primary);padding:20px 24px 0 0;margin-right:24px}
.tl .lbl{display:block;margin-bottom:12px}.tl h3{font-size:24px;margin-bottom:8px}.tl p{color:var(--muted);margin:0}
.a11y{display:flex;gap:16px;align-items:center;margin:72px 0 0;padding:20px 24px;border:1px solid var(--ink);font:400 14px/1.5 'IBM Plex Mono',monospace}
.a11y b{background:var(--accent);color:var(--onaccent);padding:4px 8px;white-space:nowrap}
.cta{margin-top:88px;background:var(--deep);color:var(--ondeep);padding:88px 0}
.cta h2{color:var(--ondeep);font-size:clamp(36px,5vw,64px);max-width:14ch}
.cta p{color:var(--deepmuted);max-width:34em;margin:20px 0 28px}
.cta .btn{border-color:var(--ondeep);color:var(--ondeep)}.cta .btn.p{background:var(--accent);color:var(--onaccent);border-color:var(--accent)}
footer.sw{padding:40px 0 120px;font:400 14px/1.6 'IBM Plex Mono',monospace;color:var(--muted)}
.ft{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:baseline}
.ft-name{margin:0 auto 0 0;color:var(--ink)}.ft-name span{display:block;color:var(--muted)}
.ft-links{display:flex;gap:24px;list-style:none;margin:0;padding:0}.ft-small{width:100%;margin:6px 0 0}
.pagehead{border-bottom:1px solid var(--ink);padding:72px 0 48px}
.pagehead h1{font-size:clamp(48px,7vw,96px);margin:16px 0 20px}.pagehead p{font-size:20px;max-width:36em;margin:0;color:var(--muted)}
.capt{width:100%;border-collapse:collapse;margin-top:0}
.capt th,.capt td{text-align:left;vertical-align:top;padding:16px 16px 16px 0;border-bottom:1px solid var(--line)}
.capt th{font-weight:600;font-size:18px;width:26%}.capt td{color:var(--muted)}.capt td.m{font:400 13px 'IBM Plex Mono',monospace;color:var(--ink);width:28%}
.clients{display:grid;grid-template-columns:repeat(3,1fr);border-left:1px solid var(--line)}
.cg{border-right:1px solid var(--line);border-bottom:1px solid var(--line);padding:24px}
.cg h3{font:500 13px 'IBM Plex Mono',monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--primary);margin-bottom:12px}
.cg ul{list-style:none;margin:0;padding:0;font-size:15px}.cg li{padding:3px 0}
@media (max-width:860px){.wrap{padding:0 20px}.hd{grid-template-columns:1fr auto;gap:10px;padding:12px 0}.hd nav{grid-column:1/-1;order:3}.nav{gap:18px}.hero .a,.hero .b,.stats>div{grid-column:1/-1;padding:32px 0}.grid{border-left:0}.grid>*{border-right:0}.stats>div+div{padding-left:0;border-top:1px solid var(--line)}.rows li{grid-template-columns:56px 1fr;}.rows li p{grid-column:2}.specs,.tl,.clients{grid-template-columns:1fr}.tl li{margin:0 0 28px}.capt th,.capt td{display:block;width:auto!important;padding:4px 0}.capt tr{display:block;padding:12px 0;border-bottom:1px solid var(--line)}.capt th,.capt td{border:0}}
"""
    brand = '<b>TG/</b>Tim Gutowski'
    rows = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d, _ in SERVICES)
    def spec(p, long=False):
        fig = img(p) if p["img"] else wwk_panel()
        return f'''<article class="spec">{fig}<p class="lbl">{e(p["client"])}</p><h3>{e(p["title"])}</h3><p>{e(p["long"] if long else p["short"])}</p>
<dl>{f"<div><dt>URL</dt><dd>{p['url']}</dd></div>" if p["url"] else ""}<div><dt>Stack</dt><dd>{e(p["tags"])}</dd></div></dl></article>'''
    home = header("sw", "Home", brand) + f'''
<main id="main"><div class="wrap">
<section class="hero grid"><div class="a"><p class="lbl">{e(EYEBROW)}</p><h1>Right-sized technology <span>for organizations big and small.</span></h1><p class="big">{e(LEDE)}</p><p>{e(LEDE2)}</p>
<div class="btns"><a class="btn p" href="../../contact.html">Start a project →</a><a class="btn" href="work.html" data-keep>Recent work</a></div></div>
<div class="b"><dl class="meta"><div><dt>Based</dt><dd>Chicago, IL</dd></div><div><dt>Focus</dt><dd>Software, web &amp; data</dd></div><div><dt>Clients</dt><dd>Unions, nonprofits, campaigns, agencies</dd></div><div><dt>Standard</dt><dd>WCAG 2.2 AA</dd></div><div><dt>Engage</dt><dd>Projects, ongoing, team extension</dd></div></dl></div></section>
<div class="stats grid">{"".join(f"<div><b>{n}</b><span>{e(t)}</span></div>" for n, t in STATS)}</div>
<section class="sec" aria-labelledby="s1"><div class="sec-h"><h2 id="s1">Services</h2><a href="../../consulting.html">Engagement details →</a></div><ol class="rows">{rows}</ol></section>
<section class="sec" aria-labelledby="s2"><div class="sec-h"><h2 id="s2">Selected work</h2><a href="work.html" data-keep>All work →</a></div><div class="specs">{spec(PROJECTS[0])}{spec(PROJECTS[1])}</div></section>
<section class="sec" aria-labelledby="s3"><div class="sec-h" style="margin-bottom:32px"><h2 id="s3">Process</h2></div>
<ol class="tl">{"".join(f"<li><span class='lbl'>Step 0{i+1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(PROCESS))}</ol>
<p class="a11y"><b>WCAG 2.2 AA</b> This site is built to the same accessibility standard I deliver for clients: keyboard and screen reader tested, with sufficient contrast in every color palette.</p></section>
</div>
<section class="cta on-deep" aria-labelledby="s4"><div class="wrap"><p class="lbl" style="color:var(--accent)">Next step</p><h2 id="s4">{e(CTA_H)}</h2><p>{e(CTA_P)}</p><div class="btns"><a class="btn p" href="../../contact.html">Start a project →</a><a class="btn" href="mailto:{EMAIL}">{EMAIL}</a></div></div></section>
</main>''' + footer("sw")
    work = header("sw", "Work", brand) + f'''
<main id="main"><div class="wrap">
<section class="pagehead"><p class="lbl">Index of work</p><h1>Work</h1><p>{e(WORK_INTRO)}</p></section>
<section class="sec" style="padding-top:48px" aria-labelledby="fp"><h2 id="fp" class="sr-only">Featured projects</h2><div class="specs">{"".join(spec(p, True) for p in PROJECTS)}</div></section>
<section class="sec" aria-labelledby="w2"><div class="sec-h"><h2 id="w2">Capabilities</h2></div>
<table class="capt"><caption class="sr-only">Capabilities, with description and typical stack</caption><tbody>{"".join(f"<tr><th scope='row'>{e(t)}</th><td>{e(d)}</td><td class='m'>{e(s)}</td></tr>" for t, d, s in CAPABILITIES)}</tbody></table></section>
<section class="sec" aria-labelledby="w3"><div class="sec-h" style="margin-bottom:0"><h2 id="w3">Clients &amp; partners</h2></div><div class="clients">{clients_html()}</div></section>
</div>
<section class="cta on-deep" aria-labelledby="w4"><div class="wrap"><h2 id="w4">Want something like this?</h2><div class="btns"><a class="btn p" href="../../contact.html">Start the conversation →</a></div></div></section>
</main>''' + footer("sw")
    return css, home, work


# ---------------------------------------------------------------- 4. Warm and human
def warm():
    css = """
body{font:400 19px/1.65 'Source Sans 3',system-ui,sans-serif}
.wrap{max-width:1140px;margin:0 auto;padding:0 32px}
h1,h2,h3{font-family:Fraunces,Georgia,serif;font-weight:600;letter-spacing:-.01em;color:var(--ink);margin:0;line-height:1.12;font-variation-settings:"SOFT" 100}
header.wm{padding:20px 0}
.hd{display:flex;align-items:center;gap:24px;background:var(--surface);border-radius:999px;padding:10px 10px 10px 24px;box-shadow:0 1px 0 var(--line),0 10px 30px -20px rgba(0,0,0,.25)}
.brand{font:600 22px Fraunces,serif;color:var(--ink);text-decoration:none;margin-right:auto;display:flex;align-items:center;gap:12px}
.brand i{width:36px;height:36px;border-radius:50%;background:var(--primary);color:var(--onprimary);display:grid;place-items:center;font:600 14px 'Source Sans 3',sans-serif;font-style:normal}
.nav{display:flex;gap:4px;list-style:none;margin:0;padding:0}
.nav a{text-decoration:none;color:var(--ink);font-weight:600;font-size:17px;padding:10px 14px;border-radius:999px}
.nav a[aria-current]{background:var(--tint)}
.hd-cta{background:var(--primary);color:var(--onprimary);padding:12px 20px;border-radius:999px;font-weight:600;text-decoration:none;font-size:17px}
.hero{display:grid;grid-template-columns:1.3fr 1fr;gap:64px;align-items:center;padding:64px 0 80px}
.hi{font:italic 600 26px Fraunces,serif;color:var(--primary);margin:0 0 12px}
.hero h1{font-size:clamp(40px,5.2vw,66px);line-height:1.08;margin-bottom:24px}
.hero p{margin:0 0 16px;max-width:32em}.hero p.m{color:var(--muted)}
.btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:28px;align-items:center}
.btn{display:inline-block;background:var(--primary);color:var(--onprimary);padding:15px 26px;border-radius:999px;text-decoration:none;font-weight:600}
.btn.s{background:transparent;color:var(--primary);text-decoration:underline;text-underline-offset:5px;padding:15px 8px}
.portrait{position:relative}
.ph{aspect-ratio:4/5;border-radius:200px 200px 32px 32px;background:var(--tint);display:grid;place-items:center;text-align:center;color:var(--muted);font-size:16px;border:2px dashed var(--line);padding:24px}
.ph b{display:block;font:600 64px Fraunces,serif;color:var(--primary);margin-bottom:8px}
.sticker{position:absolute;left:-28px;bottom:36px;background:var(--accent);color:var(--onaccent);border-radius:20px;padding:16px 20px;font-weight:600;font-size:16px;line-height:1.35;max-width:220px;transform:rotate(-3deg)}
.strip{background:var(--surface);border-radius:28px;padding:28px 36px;display:flex;flex-wrap:wrap;gap:12px 28px;align-items:center;margin-bottom:96px}
.strip h2{font:600 15px 'Source Sans 3',sans-serif;text-transform:uppercase;letter-spacing:.1em;color:var(--muted)}
.strip ul{display:flex;flex-wrap:wrap;gap:10px;list-style:none;margin:0;padding:0}
.strip li{background:var(--tint);border-radius:999px;padding:6px 14px;font-weight:600;font-size:16px}
.sec{padding:0 0 104px}
.sec-h{max-width:40em;margin-bottom:40px}.sec-h h2{font-size:clamp(34px,4vw,48px);margin-bottom:12px}.sec-h p{color:var(--muted);margin:0}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;list-style:none;margin:0;padding:0}
.cards li{background:var(--surface);border-radius:24px;padding:28px;border:1px solid var(--line)}
.cards .ic{width:52px;height:52px;border-radius:50%;background:var(--accent);color:var(--onaccent);display:grid;place-items:center;margin-bottom:18px}
.cards h3{font-size:23px;margin-bottom:8px}.cards p{margin:0;color:var(--muted);font-size:17px}
.stories{display:grid;gap:28px}
.story{display:grid;grid-template-columns:1fr 1.1fr;gap:48px;align-items:center;background:var(--surface);border-radius:32px;padding:28px;border:1px solid var(--line)}
.story img{border-radius:20px}
.story .cl{font-weight:600;color:var(--primary);margin:0 0 6px}
.story h3{font-size:34px;margin-bottom:12px}.story p{color:var(--muted);margin:0 0 12px}
.tags{font-size:15px;color:var(--ink)!important}
.wwk{background:var(--deep);color:var(--ondeep);border-radius:20px;aspect-ratio:4/3;padding:32px;display:flex;flex-direction:column;justify-content:flex-end}
.wwk p{font:600 28px/1.2 Fraunces,serif;margin:14px 0 0}
.together{background:var(--deep);color:var(--ondeep);border-radius:40px;padding:72px 56px}
.together h2{color:var(--ondeep);font-size:clamp(34px,4vw,48px);margin-bottom:40px}
.together ol{display:grid;grid-template-columns:repeat(3,1fr);gap:36px;list-style:none;margin:0;padding:0}
.together b{display:inline-grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--accent);color:var(--onaccent);font-weight:700;margin-bottom:16px}
.together h3{color:var(--ondeep);font-size:26px;margin-bottom:8px}.together p{color:var(--deepmuted);margin:0}
.cta{text-align:center;padding:24px 0 112px}
.cta h2{font-size:clamp(38px,5vw,60px);margin-bottom:18px}.cta p{max-width:32em;margin:0 auto;color:var(--muted)}
.cta .btns{justify-content:center}
footer.wm{background:var(--surface);border-top:1px solid var(--line);padding:48px 0 120px;font-size:16px;color:var(--muted)}
.ft{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:baseline}
.ft-name{margin:0 auto 0 0;color:var(--ink);font:600 20px Fraunces,serif}.ft-name span{display:block;font:400 15px 'Source Sans 3',sans-serif;color:var(--muted)}
.ft-links{display:flex;gap:24px;list-style:none;margin:0;padding:0}.ft-small{width:100%;margin:6px 0 0}
.hero-full{position:relative;min-height:680px;display:flex;align-items:center;margin-top:-84px;padding:120px 0 64px;overflow:hidden;background:var(--deep)}
.hero-full.short{min-height:520px}
.hero-full>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.9) sepia(.15)}
.hero-full::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(20,18,16,.72) 0%,rgba(20,18,16,.35) 55%,transparent 100%)}
.hero-full.short::after{background:linear-gradient(90deg,rgba(20,18,16,.86) 0%,rgba(20,18,16,.6) 55%,rgba(20,18,16,.2) 100%)}
.hero-full .wrap{position:relative;z-index:2;width:100%}
.hcard{max-width:620px;color:#fff}
.hcard h1{color:#fff;font-size:clamp(40px,5.2vw,64px);line-height:1.08;margin-bottom:20px}.hcard p{color:#f3efe9;margin:0 0 12px;font-size:20px}
.hcard .hi{color:var(--accent)}
.hcard .btn.s{color:#fff}
.hcard :focus-visible{outline-color:var(--accent)}
header.wm{position:relative;z-index:10}
.meet{display:grid;grid-template-columns:.8fr 1.2fr;gap:64px;align-items:center;padding:88px 0}
.meet h2{font-size:clamp(32px,4vw,46px);margin-bottom:16px}.meet p{margin:0 0 14px}.meet p.m{color:var(--muted)}
.meet .ph{aspect-ratio:4/5}
.ub{display:grid;grid-template-columns:1.3fr 1fr;align-items:stretch;background:var(--tint);margin:0 0 96px}
.ub-img img{width:100%;height:100%;object-fit:cover;min-height:440px;filter:sepia(.25)}
.ub-tx{padding:56px 48px;align-self:center;max-width:560px}
.ub-tx h2{font-size:clamp(30px,3.6vw,44px);margin-bottom:14px}.ub-tx p{margin:0 0 12px;color:var(--muted)}
.ub-eb{font:italic 600 22px Fraunces,serif;color:var(--primary)!important}.ub-cr{font-size:14px}
.ft-credit a{color:inherit}
.pagehead{padding:56px 0 48px;max-width:44em}.pagehead h1{font-size:clamp(44px,6vw,72px);line-height:1.08;margin:8px 0 20px}.pagehead p{color:var(--muted);font-size:21px;margin:0}
.capw{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.capw div{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:24px}.capw h3{font-size:22px;margin-bottom:6px}.capw p{margin:0 0 8px;color:var(--muted);font-size:17px}
.clients{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.cg{background:var(--surface);border-radius:24px;padding:24px;border:1px solid var(--line)}.cg h3{font-size:21px;margin-bottom:10px;color:var(--primary)}
.cg ul{list-style:none;margin:0;padding:0;font-size:17px}.cg li{padding:3px 0}
@media (max-width:860px){.wrap{padding:0 16px}.hd{flex-wrap:wrap;border-radius:24px;padding:14px}.nav{order:3;width:100%;overflow-x:auto}.hero,.story,.meet,.ub{grid-template-columns:1fr}.hero{gap:36px;padding:40px 0 64px}.meet{gap:32px;padding:56px 0}.hero-full{min-height:620px;margin-top:-150px;padding-top:180px}.hero-full::after{background:linear-gradient(180deg,rgba(20,18,16,.5),rgba(20,18,16,.82))}.hero-full.short::after{background:rgba(20,18,16,.82)}.ub-tx{padding:32px 20px}.ub-img img{min-height:280px}.sticker{left:12px}.cards,.together ol,.capw,.clients{grid-template-columns:1fr}.together{padding:48px 24px;border-radius:28px}.story{padding:16px;gap:20px}}
"""
    brand = '<i>TG</i>Tim Gutowski'
    cards = "".join(f'<li><div class="ic">{icon(k, 24)}</div><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d, k in SERVICES)
    def story(p, long=False):
        fig = img(p) if p["img"] else wwk_panel()
        return f'<article class="story"><div>{fig}</div><div><p class="cl">{e(p["client"])}</p><h3>{e(p["title"])}</h3><p>{e(p["long"] if long else p["short"])}</p><p class="tags">{e(p["tags"])}</p></div></article>'
    home = header("wm", "Home", brand) + f'''
<main id="main">
<section class="hero-full"><img src="../../img/portfolio-hero.jpg" alt="" width="1788" height="775"><div class="wrap"><div class="hcard"><p class="hi">Hi, I&rsquo;m Tim.</p><h1>I build right-sized technology for organizations big and small.</h1><p>{e(LEDE)}</p>
<div class="btns"><a class="btn" href="../../contact.html">Tell me about your project</a><a class="btn s" href="work.html" data-keep>See my work</a></div></div></div></section>
<div class="wrap">
<section class="meet" aria-labelledby="meet-h"><div class="portrait"><div class="ph"><div><b>TG</b>Portrait of Tim goes here<br>(a warm, natural-light photo)</div></div><p class="sticker">Chicago-based. Working with clients across the country.</p></div>
<div><h2 id="meet-h">A developer who listens first.</h2><p>{e(LEDE2)}</p><p class="m">I came to technology as a writer, so I explain the why, not just the how, to your board as clearly as to your developers.</p></div></section>
<section class="strip" aria-labelledby="bf"><h2 id="bf">Built for</h2><ul>{"".join(f"<li>{e(b)}</li>" for b in BUILT_FOR)}</ul></section>
<section class="sec" aria-labelledby="s1"><div class="sec-h"><h2 id="s1">How I can help</h2><p>Most projects start with one of these. If yours doesn&rsquo;t fit neatly, that&rsquo;s fine too.</p></div><ul class="cards">{cards}</ul></section>
<section class="sec" aria-labelledby="s2"><div class="sec-h"><h2 id="s2">A couple of recent projects</h2></div><div class="stories">{story(PROJECTS[0])}{story(PROJECTS[1])}</div></section>
<section class="sec" aria-labelledby="s3"><div class="together on-deep"><h2 id="s3">What working together looks like</h2><ol>{"".join(f"<li><b>{i+1}</b><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(PROCESS))}</ol></div></section>
<section class="cta" aria-labelledby="s4"><h2 id="s4">Let&rsquo;s talk it through.</h2><p>{e(CTA_P)}</p><div class="btns"><a class="btn" href="../../contact.html">Start a project</a><a class="btn s" href="mailto:{EMAIL}">Or just email me</a></div></section>
</div></main>''' + footer("wm")
    work = header("wm", "Work", brand) + f'''
<main id="main"><div class="wrap">
</div><section class="hero-full short"><img src="../../img/code-editor.jpg" alt="" width="2000" height="1333"><div class="wrap"><div class="hcard"><p class="hi">The work</p><h1>Things I&rsquo;ve built, and who for.</h1><p>{e(WORK_INTRO)}</p></div></div></section><div class="wrap">
<section class="sec" aria-labelledby="fp"><h2 id="fp" class="sr-only">Featured projects</h2><div class="stories">{"".join(story(p, True) for p in PROJECTS)}</div></section>
<section class="sec" aria-labelledby="w2"><div class="sec-h"><h2 id="w2">More of what I build</h2></div><div class="capw">{"".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p><p class='tags'>{e(s)}</p></div>" for t, d, s in CAPABILITIES)}</div></section>
</div>{union_band("","Who I build for","Built for the people who do the work.","Labor unions, worker-safety researchers, advocacy groups, and public agencies: most of my clients exist to serve working people, and their websites have to work for them.")}<div class="wrap">
<section class="sec" aria-labelledby="w3"><div class="sec-h"><h2 id="w3">Organizations I&rsquo;ve built for</h2><p>Directly and through agency partners.</p></div><div class="clients">{clients_html()}</div></section>
<section class="cta" aria-labelledby="w4"><h2 id="w4">Want something like this?</h2><div class="btns"><a class="btn" href="../../contact.html">Start the conversation</a></div></section>
</div></main>''' + footer("wm", credits(CREDIT_CODE, CREDIT_UNION))
    return css, home, work


# ---------------------------------------------------------------- 5. Consultancy (inspired by MLA Strategies)
def consult():
    css = """
body{font:400 18px/1.7 'Plus Jakarta Sans',system-ui,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 32px}
h1,h2,h3{font-family:'DM Serif Display',Georgia,serif;font-weight:400;letter-spacing:-.005em;color:var(--ink);margin:0;line-height:1.1}
.eb{font:700 13px/1.4 'Plus Jakarta Sans',sans-serif;text-transform:uppercase;letter-spacing:.16em;color:var(--primary);margin:0 0 16px}
header.cs{position:absolute;left:0;right:0;top:0;z-index:5}
.hd{display:flex;align-items:center;gap:32px;min-height:96px;color:var(--ondeep)}
.brand{font:400 26px 'DM Serif Display',serif;color:var(--ondeep);text-decoration:none;margin-right:auto}
.nav{display:flex;gap:28px;list-style:none;margin:0;padding:0}
.nav a{color:var(--ondeep);text-decoration:none;font-weight:500;font-size:16px;padding:6px 0}
.nav a[aria-current]{box-shadow:inset 0 -2px var(--accent)}
.hd-cta{border:1.5px solid var(--ondeep);color:var(--ondeep);padding:11px 20px;text-decoration:none;font-weight:600;font-size:15px;border-radius:2px}
.hero{position:relative;min-height:640px;display:flex;align-items:flex-end;background:var(--deep);color:var(--ondeep);overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.3;filter:grayscale(.5)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,var(--deep) 100%);opacity:.9}
.hero .wrap{position:relative;z-index:2;padding-top:180px;padding-bottom:88px;width:100%}
.hero .eb{color:var(--accent)}
.hero h1{color:var(--ondeep);font-size:clamp(44px,6vw,80px);max-width:15ch;margin-bottom:28px}
.hero p{color:var(--deepmuted);max-width:34em;margin:0 0 32px;font-size:20px}
.btn{display:inline-block;background:var(--accent);color:var(--onaccent);padding:15px 26px;text-decoration:none;font-weight:700;border-radius:2px;font-size:16px}
.btn.d{background:var(--primary);color:var(--onprimary)}
.tl{color:var(--primary);font-weight:600;text-underline-offset:5px}
.intro{display:grid;grid-template-columns:1fr 1fr;gap:80px;padding:112px 0;align-items:start}
.intro h2{font-size:clamp(32px,3.6vw,46px)}
.intro p{margin:0 0 18px;color:var(--muted)}
.intro .links{display:flex;gap:28px;margin-top:8px}
.how{background:var(--surface);padding:104px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.how h2{font-size:clamp(34px,4vw,52px);max-width:16ch;margin-bottom:56px}
.how ol{display:grid;grid-template-columns:repeat(3,1fr);gap:56px;list-style:none;margin:0;padding:0}
.how li{border-top:1px solid var(--ink);padding-top:22px}
.how .n{font:700 14px 'Plus Jakarta Sans',sans-serif;letter-spacing:.12em;color:var(--primary)}
.how h3{font-size:30px;margin:12px 0 12px}.how p{color:var(--muted);margin:0}
.svc{padding:104px 0}
.svc-g{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);margin-top:40px}
.svc-g div{padding:32px 32px 32px 0;border-bottom:1px solid var(--line)}
.svc-g div:not(:nth-child(3n)){border-right:1px solid var(--line)}.svc-g div:not(:nth-child(3n+1)){padding-left:32px}
.svc-g h3{font-size:26px;margin-bottom:10px}.svc-g p{color:var(--muted);margin:0;font-size:17px}
.outcome{background:var(--tint);padding:96px 0}
.outcome blockquote{margin:0;font:400 clamp(28px,3.4vw,44px)/1.25 'DM Serif Display',serif;color:var(--ink);max-width:24em}
.outcome strong{font-weight:400;background:linear-gradient(transparent 70%,var(--accent) 70%)}
.case{padding:112px 0}
.case-g{display:grid;grid-template-columns:1.15fr 1fr;gap:72px;align-items:center}
.case img{box-shadow:0 30px 60px -30px rgba(0,0,0,.35)}
.case h2{font-size:clamp(34px,4vw,50px);margin-bottom:20px}.case p{color:var(--muted);margin:0 0 18px}
.second{display:grid;grid-template-columns:1fr 1.15fr;gap:72px;align-items:center;margin-top:96px}
.final{background:var(--deep);color:var(--ondeep);padding:112px 0;text-align:center}
.final h2{color:var(--ondeep);font-size:clamp(38px,5vw,64px);margin-bottom:22px}
.final p{color:var(--deepmuted);max-width:32em;margin:0 auto 32px}
footer.cs{background:var(--deep);color:var(--deepmuted);border-top:1px solid rgba(255,255,255,.15);padding:48px 0 120px;font-size:15px}
footer.cs a{color:var(--ondeep)}
.ft{display:flex;flex-wrap:wrap;gap:16px 40px;align-items:baseline}
.ft-name{margin:0 auto 0 0;color:var(--ondeep);font:400 24px 'DM Serif Display',serif}.ft-name span{display:block;font:400 14px 'Plus Jakarta Sans',sans-serif;color:var(--deepmuted)}
.ft-links{display:flex;gap:24px;list-style:none;margin:0;padding:0}.ft-small{width:100%;margin:6px 0 0}
footer.cs :focus-visible{outline-color:var(--accent)}
.wwk{background:var(--deep);color:var(--ondeep);aspect-ratio:4/3;padding:40px;display:flex;flex-direction:column;justify-content:flex-end}
.wwk p{font:400 32px/1.15 'DM Serif Display',serif;margin:16px 0 0}
.ub{display:grid;grid-template-columns:1.25fr 1fr;background:var(--deep);color:var(--ondeep)}
.ub-img img{width:100%;height:100%;min-height:520px;object-fit:cover;object-position:center 30%;filter:grayscale(1)}
.ub-tx{padding:72px 56px;align-self:center;max-width:560px}
.ub-tx h2{color:var(--ondeep);font-size:clamp(32px,3.8vw,48px);margin-bottom:18px}.ub-tx p{color:var(--deepmuted);margin:0 0 14px}
.ub-eb{font:700 13px/1.4 'Plus Jakarta Sans',sans-serif;text-transform:uppercase;letter-spacing:.16em;color:var(--accent)!important}.ub-cr{font-size:13px}
.ft-credit a{color:var(--ondeep)}
.pagehead{position:relative;overflow:hidden;background:var(--deep);color:var(--ondeep);padding:200px 0 88px}
.pagehead img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.22;filter:grayscale(1);object-position:center 35%}
.pagehead::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 20%,var(--deep) 100%);opacity:.9}
.pagehead .wrap{position:relative;z-index:2}
.pagehead .eb{color:var(--accent)}.pagehead h1{color:var(--ondeep);font-size:clamp(48px,7vw,88px);margin-bottom:24px}.pagehead p{color:var(--deepmuted);max-width:36em;font-size:20px;margin:0}
.cases{padding:96px 0 0}
.cases article{display:grid;grid-template-columns:1.1fr 1fr;gap:64px;align-items:center;padding-bottom:88px}
.cases article:nth-child(even) > :first-child{order:2}
.cases h2{font-size:clamp(32px,3.6vw,46px);margin-bottom:16px}.cases p{color:var(--muted);margin:0 0 14px}
.tags{font-size:14px;font-weight:600;color:var(--ink)!important;letter-spacing:.02em}
.clients{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 56px;margin-top:40px}
.cg h3{font-size:24px;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:10px}
.cg ul{list-style:none;margin:0;padding:0;font-size:16px;color:var(--muted)}.cg li{padding:3px 0}
@media (max-width:860px){.wrap{padding:0 20px}.hd{flex-wrap:wrap;gap:10px 20px;padding:16px 0}.nav{order:3;width:100%;gap:20px}.hero{min-height:560px}.intro,.case-g,.second,.cases article{grid-template-columns:1fr;gap:32px}.cases article:nth-child(even) > :first-child{order:0}.how ol,.svc-g,.clients,.ub{grid-template-columns:1fr}.ub-img img{min-height:300px}.ub-tx{padding:40px 20px}.svc-g div{padding:24px 0!important;border-right:0!important}.intro{padding:72px 0}}
"""
    brand = "Tim Gutowski"
    svc = "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d, _ in SERVICES)
    p0, p1, p2 = PROJECTS
    home = header("cs on-deep", "Home", brand) + f'''
<main id="main">
<section class="hero on-deep"><img src="../../img/code-editor.jpg" alt="" width="2000" height="1333"><div class="wrap"><p class="eb">Software &amp; technology consulting · Chicago</p>
<h1>Right-sized technology for organizations big and small.</h1><p>{e(LEDE)}</p><a class="btn" href="../../contact.html">Get started</a></div></section>
<div class="wrap"><section class="intro" aria-labelledby="s1"><h2 id="s1">Built for the people who rely on it, and the staff who keep it running.</h2>
<div><p>{e(LEDE2)}</p><p>Clients work with me directly, from the first call through launch and support. When a project needs a designer or writer, I bring in partners I&rsquo;ve worked with for years.</p>
<div class="links"><a class="tl" href="../../contact.html">Contact me</a><a class="tl" href="work.html" data-keep>See the work</a></div></div></section></div>
<section class="how" aria-labelledby="s2"><div class="wrap"><p class="eb">How it works</p><h2 id="s2">A clear path from first call to handoff.</h2>
<ol>{"".join(f"<li><span class='n'>0{i+1}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>" for i, (t, d) in enumerate(PROCESS))}</ol></div></section>
<section class="svc" aria-labelledby="s3"><div class="wrap"><p class="eb">What I do</p><h2 id="s3" style="font-size:clamp(34px,4vw,52px)">Services</h2><div class="svc-g">{svc}</div></div></section>
<section class="outcome" aria-label="Outcomes"><div class="wrap"><p class="eb">The result</p><blockquote>Technology that helps you <strong>reach the people you serve</strong>, <strong>save staff time</strong>, and <strong>make better decisions</strong>, without paying for more than you need.</blockquote></div></section>
<section class="case" aria-labelledby="s4"><div class="wrap"><div class="case-g"><div>{img(p0)}</div><div><p class="eb">Case study</p><h2 id="s4">{e(p0["title"])} for {e(p0["client"])}</h2><p>{e(p0["long"])}</p><a class="tl" href="work.html" data-keep>See more work</a></div></div>
<div class="second"><div><p class="eb">Case study</p><h2>{e(p1["title"])} for {e(p1["client"])}</h2><p>{e(p1["short"])}</p></div><div>{img(p1)}</div></div></div></section>
<section class="final on-deep" aria-labelledby="s5"><div class="wrap"><h2 id="s5">Ready to build something<br>that fits?</h2><p>{e(CTA_P)}</p><a class="btn" href="../../contact.html">Get started</a></div></section>
</main>''' + footer("cs on-deep", credits(CREDIT_CODE))
    def case(p):
        fig = img(p) if p["img"] else wwk_panel()
        return f'<article><div>{fig}</div><div><p class="eb">{e(p["client"])}</p><h2>{e(p["title"])}</h2><p>{e(p["long"])}</p><p class="tags">{e(p["tags"])}</p></div></article>'
    work = header("cs on-deep", "Work", brand) + f'''
<main id="main">
<section class="pagehead on-deep"><img src="../../img/portfolio-hero.jpg" alt="" width="1788" height="775"><div class="wrap"><p class="eb">Case studies</p><h1>Work</h1><p>{e(WORK_INTRO)}</p></div></section>
<div class="wrap"><section class="cases" aria-labelledby="fp"><h2 id="fp" class="sr-only">Featured projects</h2>{"".join(case(p) for p in PROJECTS)}</section></div>
<section class="how" aria-labelledby="w2"><div class="wrap"><p class="eb">Capabilities</p><h2 id="w2">More of what I build</h2><div class="svc-g" style="margin-top:0">{"".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d, s in CAPABILITIES[:6])}</div></div></section>
{union_band("on-deep","Who I build for","Built for the people who do the work.","Labor unions, worker-safety researchers, advocacy groups, and public agencies: most of my clients exist to serve working people, and their websites have to work for them.")}
<section class="svc" aria-labelledby="w3"><div class="wrap"><p class="eb">Clients &amp; partners</p><h2 id="w3" style="font-size:clamp(34px,4vw,52px)">Organizations I&rsquo;ve built for</h2><div class="clients">{clients_html()}</div></div></section>
<section class="final on-deep" aria-labelledby="w4"><div class="wrap"><h2 id="w4">Want something like this?</h2><a class="btn" href="../../contact.html">Get started</a></div></section>
</main>''' + footer("cs on-deep", credits(CREDIT_UNION))
    return css, home, work


OPTIONS = [
    ("2-studio", "studio", "Bold studio", studio,
     "Big type over a full-width, color-tinted photo, strong color blocks, and punchy project tiles. Reads like a design studio."),
    ("4-warm", "warm", "Warm and human", warm,
     "A full-width photo hero, rounded shapes, a soft serif, and a first-person welcome with a portrait. Approachable and personal."),
    ("5-consultancy", "consult", "Consultancy", consult,
     "A dark full-bleed hero, eyebrow labels, a numbered process, an outcomes statement, and case studies. Modeled on the overall direction of mlastrategies.com."),
]

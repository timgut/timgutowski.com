/* Palette switcher for the design review pages. Not for production. */
(function(){
  var P=[["classic","Blue & yellow (current)","#3B5BA9","#FFD95A"],["navy","Navy & ivory","#1F3A68","#E9B949"],["forest","Forest & gold","#2F6B4F","#E7B53C"],["coral","Ink & coral","#B23E2B","#FF8A6B"],["teal","Slate & teal","#0F6E73","#7FD1C7"]];
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

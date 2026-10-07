#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera el CURSO INTENSIVO de normativa de FP (curso/index.html) a partir del
contenido definido en build/curso_data.py y de los datos oficiales de
build/normdata.json (para estadísticas y enlaces a la fuente).

Uso:  python3 build/build_curso.py

El resultado es un archivo autónomo (sin dependencias) que se puede abrir con
doble clic. Metodología: lecciones, fichas con repetición espaciada (SRS),
tests por módulo, examen final y taller de números.
"""
import datetime
import json
import os

from curso_data import MODULES, NUMBERS, PLAN, INTRO

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
OUT_DIR = os.path.join(ROOT, "curso")
OUT = os.path.join(OUT_DIR, "index.html")

DOCS = {}
try:
    with open(os.path.join(BASE, "normdata.json"), encoding="utf-8") as fh:
        _nd = json.load(fh)
    DOCS = _nd.get("docs", {})
except Exception:
    DOCS = {}


def stats():
    ncards = sum(len(m.get("cards", [])) for m in MODULES)
    nquiz = sum(len(m.get("quiz", [])) for m in MODULES)
    nnum = len(NUMBERS)
    return ncards, nquiz, nnum


TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Curso intensivo · Normativa de FP (Comunitat Valenciana)</title>
<meta name="description" content="Curso interactivo e intensivo para aprender y memorizar la normativa de Formación Profesional de la Comunitat Valenciana: lecciones, fichas SRS, tests y examen final.">
<style>
  :root{
    --bg:#f4f6f9; --surface:#fff; --surface-2:#eef3f8; --text:#182430; --muted:#5a6b7b;
    --primary:#0d5c8c; --primary-2:#0a4a72; --accent:#d98a2b; --border:#dde5ee;
    --ok:#1e7a4b; --warn:#a86300; --danger:#b3261e; --purple:#6c3483;
    --radius:14px; --shadow:0 1px 2px rgba(16,32,48,.06),0 10px 28px rgba(16,32,48,.07);
    --maxw:1180px;
  }
  html[data-theme="dark"]{
    --bg:#0e1620; --surface:#152230; --surface-2:#1b2b3c; --text:#e8eef5; --muted:#9fb1c2;
    --primary:#5aa9dd; --primary-2:#84c4f2; --accent:#f0b45a; --border:#26384a;
    --ok:#5ec98d; --warn:#e2a94f; --danger:#ff8a80; --purple:#c39bd3;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px rgba(0,0,0,.35);
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--text);
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    -webkit-font-smoothing:antialiased}
  a{color:var(--primary);text-decoration:none}
  a:hover{text-decoration:underline}
  h1,h2,h3,h4{line-height:1.25;margin:0 0 .4em}
  code{background:var(--surface-2);padding:.1em .4em;border-radius:6px;font-size:.9em}
  b,strong{color:var(--text)}

  .topbar{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--surface) 90%,transparent);
    backdrop-filter:saturate(1.4) blur(8px);border-bottom:1px solid var(--border)}
  .topbar .inner{max-width:var(--maxw);margin:0 auto;padding:.55rem 1rem;display:flex;gap:.6rem;align-items:center;flex-wrap:wrap}
  .brand{display:flex;align-items:center;gap:.6rem;font-weight:700}
  .brand .dot{width:32px;height:32px;border-radius:9px;background:linear-gradient(135deg,var(--primary),var(--accent));
    display:grid;place-items:center;color:#fff;font-size:.8rem;font-weight:800}
  .brand small{display:block;font-weight:500;color:var(--muted);font-size:.72rem}
  .grow{flex:1}
  .iconbtn{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:10px;
    padding:.4rem .65rem;cursor:pointer;font-size:.85rem;display:inline-flex;gap:.4rem;align-items:center}
  .iconbtn:hover{background:var(--surface-2)}

  nav.tabs{max-width:var(--maxw);margin:.9rem auto 0;padding:0 1rem;display:flex;gap:.4rem;flex-wrap:wrap}
  nav.tabs button{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:999px;
    padding:.45rem .9rem;cursor:pointer;font-size:.9rem;font-weight:600}
  nav.tabs button.active{background:var(--primary);color:#fff;border-color:var(--primary)}
  main{max-width:var(--maxw);margin:1.1rem auto 4rem;padding:0 1rem}
  .view{display:none}
  .view.active{display:block}

  .card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
    padding:1rem 1.1rem;box-shadow:var(--shadow);margin-bottom:1rem}
  .grid{display:grid;gap:.9rem}
  .g2{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
  .g3{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
  .muted{color:var(--muted)}
  .small{font-size:.86rem}
  .pill{display:inline-block;font-size:.72rem;font-weight:700;background:var(--surface-2);border:1px solid var(--border);
    color:var(--muted);border-radius:999px;padding:.12rem .55rem}
  .pill.ok{color:var(--ok);border-color:color-mix(in srgb,var(--ok) 45%,var(--border))}
  .pill.warn{color:var(--warn);border-color:color-mix(in srgb,var(--warn) 45%,var(--border))}
  .pill.bad{color:var(--danger);border-color:color-mix(in srgb,var(--danger) 45%,var(--border))}

  .btn{background:var(--primary);color:#fff;border:none;border-radius:10px;padding:.55rem .95rem;cursor:pointer;
    font-size:.92rem;font-weight:600}
  .btn:hover{background:var(--primary-2)}
  .btn.ghost{background:transparent;color:var(--primary);border:1px solid var(--border)}
  .btn.ghost:hover{background:var(--surface-2)}
  .btn.ok{background:var(--ok)}
  .btn.warn{background:var(--warn)}
  .btn.bad{background:var(--danger)}
  .btn:disabled{opacity:.45;cursor:not-allowed}
  .btns{display:flex;gap:.5rem;flex-wrap:wrap}

  /* plan / progreso */
  .hero{background:linear-gradient(135deg,color-mix(in srgb,var(--primary) 12%,var(--surface)),var(--surface));
    border:1px solid var(--border);border-radius:16px;padding:1.2rem 1.3rem;box-shadow:var(--shadow)}
  .hero h2{margin-bottom:.2rem}
  .kpi{display:flex;gap:1rem;flex-wrap:wrap;margin-top:.6rem}
  .kpi div{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:.55rem .8rem;min-width:110px}
  .kpi b{font-size:1.35rem;display:block;line-height:1.1}
  .kpi span{font-size:.76rem;color:var(--muted)}
  .bar{height:9px;background:var(--surface-2);border-radius:999px;overflow:hidden;border:1px solid var(--border)}
  .bar>i{display:block;height:100%;background:linear-gradient(90deg,var(--primary),var(--accent));width:0}
  .modrow{display:flex;gap:.8rem;align-items:center;padding:.7rem .8rem;border:1px solid var(--border);
    border-radius:12px;background:var(--surface);margin-bottom:.55rem;cursor:pointer}
  .modrow:hover{border-color:var(--primary)}
  .modrow .n{width:30px;height:30px;border-radius:9px;background:var(--primary);color:#fff;display:grid;place-items:center;
    font-weight:800;font-size:.85rem;flex:none}
  .modrow .t{flex:1;min-width:0}
  .modrow .t b{display:block}
  .modrow .meta{font-size:.78rem;color:var(--muted)}
  .modrow .mini{width:110px;flex:none}
  .mastery{font-size:.8rem;font-weight:700;text-align:right;flex:none;width:56px}

  /* plan checklist */
  .day{border:1px solid var(--border);border-radius:12px;background:var(--surface);padding:.7rem .85rem;margin-bottom:.55rem}
  .day h4{margin:0 0 .3rem;font-size:.95rem}
  .task{display:flex;gap:.5rem;align-items:flex-start;font-size:.9rem;padding:.18rem 0;cursor:pointer}
  .task input{margin-top:.25rem}
  .task.done span{text-decoration:line-through;color:var(--muted)}

  /* lecciones */
  .lesson{line-height:1.72}
  .lesson h3{margin-top:1.2rem;color:var(--primary);font-size:1.12rem}
  .lesson h4{margin-top:1rem;color:var(--text);font-size:1rem}
  .lesson ul,.lesson ol{padding-left:1.25rem}
  .lesson li{margin:.3rem 0}
  .lesson table,.tbl{width:100%;border-collapse:collapse;background:var(--surface);border-radius:12px;overflow:hidden;
    box-shadow:var(--shadow);font-size:.92rem;margin:.7rem 0}
  .lesson th,.lesson td,.tbl th,.tbl td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--border);vertical-align:top}
  .lesson th,.tbl th{background:var(--surface-2);font-size:.78rem;text-transform:uppercase;letter-spacing:.03em;color:var(--muted)}
  .callout{border-radius:12px;padding:.75rem .9rem;margin:.7rem 0;border:1px solid var(--border);font-size:.93rem}
  .callout.tip{background:color-mix(in srgb,var(--ok) 10%,var(--surface));border-left:4px solid var(--ok)}
  .callout.warn{background:color-mix(in srgb,var(--warn) 12%,var(--surface));border-left:4px solid var(--warn)}
  .callout.trap{background:color-mix(in srgb,var(--danger) 10%,var(--surface));border-left:4px solid var(--danger)}
  .callout.info{background:color-mix(in srgb,var(--primary) 8%,var(--surface));border-left:4px solid var(--primary)}
  .ref{font-size:.76rem;font-weight:600;background:var(--surface-2);border:1px solid var(--border);color:var(--muted);
    border-radius:6px;padding:.12rem .45rem;display:inline-block;margin:.1rem .25rem .1rem 0}
  kbd{font-family:inherit;background:var(--surface-2);border:1px solid var(--border);border-bottom-width:2px;border-radius:6px;
    padding:.02em .4em;font-size:.9em}
  .big{font-size:1.05rem;font-weight:700;color:var(--accent)}

  /* fichas */
  .flash{perspective:1400px;margin-top:.5rem}
  .flip{position:relative;min-height:260px;transition:transform .5s;transform-style:preserve-3d;cursor:pointer}
  .flip.on{transform:rotateY(180deg)}
  .face{position:absolute;inset:0;backface-visibility:hidden;border:1px solid var(--border);border-radius:16px;
    background:var(--surface);box-shadow:var(--shadow);padding:1.3rem 1.4rem;overflow:auto}
  .face.front{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;font-size:1.15rem;font-weight:600}
  .face.back{transform:rotateY(180deg);font-size:1rem;line-height:1.6}
  .face .qtag{position:absolute;top:.7rem;left:.9rem;font-size:.72rem;color:var(--muted);font-weight:700;letter-spacing:.04em}
  .face .qref{position:absolute;bottom:.7rem;left:.9rem;font-size:.74rem;color:var(--muted)}
  .grade{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.9rem}
  .grade .btn{flex:1;min-width:120px}

  /* test */
  .opt{display:block;width:100%;text-align:left;border:1px solid var(--border);background:var(--surface);color:var(--text);
    border-radius:12px;padding:.7rem .85rem;margin:.4rem 0;cursor:pointer;font-size:.95rem}
  .opt:hover{border-color:var(--primary)}
  .opt.sel{border-color:var(--primary);background:color-mix(in srgb,var(--primary) 8%,var(--surface))}
  .opt.ok{border-color:var(--ok);background:color-mix(in srgb,var(--ok) 13%,var(--surface))}
  .opt.bad{border-color:var(--danger);background:color-mix(in srgb,var(--danger) 11%,var(--surface))}
  .opt .mk{font-weight:800;margin-right:.4rem}
  .qtext{font-size:1.08rem;font-weight:600;margin:.2rem 0 .6rem}
  .progressline{display:flex;gap:.6rem;align-items:center;flex-wrap:wrap;margin-bottom:.4rem}

  .score{font-size:2.6rem;font-weight:800;line-height:1}
  .center{text-align:center}

  /* numeros */
  .numrow{display:flex;gap:.7rem;align-items:center;border:1px solid var(--border);border-radius:12px;background:var(--surface);
    padding:.6rem .8rem;margin-bottom:.5rem}
  .numrow .q{flex:1}
  .numrow .a{font-weight:800;color:var(--accent);min-width:110px;text-align:right}
  .numrow.hide .a{color:transparent;background:var(--surface-2);border-radius:8px;padding:0 .5rem}
  .flashnum{font-size:2rem;font-weight:800;text-align:center;margin:.6rem 0}

  footer{max-width:var(--maxw);margin:0 auto;padding:1.4rem 1rem 3rem;color:var(--muted);font-size:.84rem;border-top:1px solid var(--border)}
  @media (max-width:640px){ .modrow .mini{display:none} }
</style>
</head>
<body>

<div class="topbar">
  <div class="inner">
    <div class="brand">
      <span class="dot">FP</span>
      <span>Curso intensivo de normativa<small>Formación Profesional · Comunitat Valenciana</small></span>
    </div>
    <span class="grow"></span>
    <button class="iconbtn" id="resumeBtn" title="Repasar lo pendiente de hoy">🔥 Repaso de hoy <b id="dueN">0</b></button>
    <button class="iconbtn" id="themeBtn" title="Cambiar tema">◐ Tema</button>
  </div>
</div>

<nav class="tabs" id="tabs"></nav>

<main>
  <section class="view" id="v-plan"></section>
  <section class="view" id="v-lesson"></section>
  <section class="view" id="v-cards"></section>
  <section class="view" id="v-quiz"></section>
  <section class="view" id="v-exam"></section>
  <section class="view" id="v-numbers"></section>
</main>

<footer>
  <p><b>Curso intensivo de normativa de FP</b> — material didáctico no oficial elaborado a partir de las fuentes del DOGV/BOE.
  En caso de duda prevalece el texto publicado en el diario oficial. Curso 2026-27.</p>
  <p class="small">Tu progreso se guarda en este navegador (localStorage). Generado el __GENERATED__.</p>
</footer>

<script>
window.CURSO = __CURSO_DATA__;
</script>
<script>
(function(){
  "use strict";
  var C = window.CURSO || {modules:[],numbers:[]};
  var MODS = C.modules || [];
  var NUMBERS = C.numbers || [];
  var PLAN = C.plan || [];
  var LS = "curso-fp-v1";
  var today = function(){ var d=new Date(); return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0"); };
  var DAY = 86400000;
  var BOX = [0,1,2,4,8,16]; // días por caja

  var state = load();
  function load(){
    try{ var s=JSON.parse(localStorage.getItem(LS)); if(s&&typeof s==="object") return s; }catch(e){}
    return {cards:{},quiz:{},exam:{best:0,tries:0},checks:{},numbers:{right:0,total:0}};
  }
  function save(){ try{ localStorage.setItem(LS, JSON.stringify(state)); }catch(e){} }

  /* ---------- tema ---------- */
  var root=document.documentElement;
  try{ var th=localStorage.getItem(LS+"-theme"); if(th) root.setAttribute("data-theme",th); }catch(e){}
  document.getElementById("themeBtn").addEventListener("click",function(){
    var t=root.getAttribute("data-theme")==="dark"?"light":"dark";
    root.setAttribute("data-theme",t); try{ localStorage.setItem(LS+"-theme",t);}catch(e){}
  });

  function esc(s){ return String(s==null?"":s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;"}[c];}); }
  function el(id){ return document.getElementById(id); }
  function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)); var t=a[i];a[i]=a[j];a[j]=t;} return a; }

  function cardId(mi,ci){ return MODS[mi].id+":"+ci; }
  function cardState(id){
    if(!state.cards[id]) state.cards[id]={box:0,due:today(),seen:0,right:0};
    return state.cards[id];
  }
  function isDue(id){ var c=state.cards[id]; if(!c) return true; return c.due<=today(); }
  function moduleStats(mi){
    var m=MODS[mi], total=m.cards.length, learned=0, due=0;
    for(var i=0;i<m.cards.length;i++){ var id=cardId(mi,i), c=state.cards[id];
      if(c&&c.box>=3) learned++; if(isDue(id)) due++; }
    var quiz=state.quiz[m.id]||0;
    var cardPct= total? learned/total : 1;
    var mastery=Math.round((cardPct*100*0.5)+(quiz*0.5));
    return {total:total,learned:learned,due:due,quiz:quiz,mastery:mastery};
  }
  function globalStats(){
    var learned=0,total=0,due=0,msum=0;
    for(var i=0;i<MODS.length;i++){ var s=moduleStats(i); learned+=s.learned; total+=s.total; due+=s.due; msum+=s.mastery; }
    var overall=MODS.length?Math.round(msum/MODS.length):0;
    return {learned:learned,total:total,due:due,overall:overall};
  }

  /* ---------- pestañas ---------- */
  var TABS=[["plan","Plan y progreso"],["lesson","Lecciones"],["cards","Fichas SRS"],["quiz","Tests"],["exam","Examen final"],["numbers","Números clave"]];
  var tabs=el("tabs");
  TABS.forEach(function(t,i){
    var b=document.createElement("button"); b.textContent=t[1]; b.dataset.v=t[0];
    b.addEventListener("click",function(){ go(t[0]); });
    tabs.appendChild(b);
  });
  function go(v){
    Array.prototype.forEach.call(tabs.children,function(b){ b.classList.toggle("active", b.dataset.v===v); });
    ["plan","lesson","cards","quiz","exam","numbers"].forEach(function(x){ el("v-"+x).classList.toggle("active",x===v); });
    window.scrollTo({top:0,behavior:"smooth"});
    if(v==="plan") renderPlan();
    if(v==="lesson") renderLessonIndex();
    if(v==="cards"){ if(session) renderCard(); else renderCardsHome(); }
    if(v==="quiz"){ if(quizSession && quizSession.pos<quizSession.qs.length) renderQuiz(); else renderQuizIndex(); }
    if(v==="exam") renderExam();
    if(v==="numbers") renderNumbers();
    updateDue();
  }
  function updateDue(){ document.getElementById("dueN").textContent=globalStats().due; }
  document.getElementById("resumeBtn").addEventListener("click",function(){ startCards("due"); go("cards"); });

  /* ---------- PLAN ---------- */
  function renderPlan(){
    var g=globalStats();
    var h='<div class="hero"><h2>Tu ruta para sabértela de verdad</h2>'+
      '<p class="muted" style="margin:.2rem 0 .2rem">'+esc(INTRO)+'</p>'+
      '<div class="kpi">'+
        '<div><b>'+g.overall+'%</b><span>dominio global</span></div>'+
        '<div><b>'+g.learned+'/'+g.total+'</b><span>fichas aprendidas</span></div>'+
        '<div><b>'+g.due+'</b><span>repasos pendientes</span></div>'+
        '<div><b>'+(state.exam.best||0)+'%</b><span>mejor examen final</span></div>'+
      '</div>'+
      '<div style="margin-top:.8rem" class="bar"><i style="width:'+g.overall+'%"></i></div>'+
    '</div>';

    h+='<div class="card"><h3 style="margin-bottom:.2rem">Módulos del curso</h3>'+
       '<p class="muted small">Pulsa un módulo para estudiar la lección, sus fichas y su test. El dominio combina fichas aprendidas (50%) y mejor test (50%).</p>';
    MODS.forEach(function(m,mi){
      var s=moduleStats(mi);
      var cls=s.mastery>=80?"ok":(s.mastery>0?"warn":"");
      h+='<div class="modrow" data-mod="'+mi+'">'+
           '<div class="n">'+(mi+1)+'</div>'+
           '<div class="t"><b>'+esc(m.title)+'</b><div class="meta">'+esc(m.tagline)+'</div></div>'+
           '<div class="mini"><div class="bar"><i style="width:'+s.mastery+'%"></i></div><div class="meta">'+s.learned+'/'+s.total+' fichas · test '+(s.quiz||0)+'%</div></div>'+
           '<div class="mastery"><span class="pill '+cls+'">'+s.mastery+'%</span></div>'+
         '</div>';
    });
    h+='</div>';

    if(PLAN.length){
      h+='<div class="card"><h3 style="margin-bottom:.2rem">Plan intensivo ('+PLAN.length+' días)</h3>'+
         '<p class="muted small">Idea: 1 sesión de estudio + 1 repaso por día. Marca las tareas hechas.</p>';
      PLAN.forEach(function(d,di){
        h+='<div class="day"><h4>Día '+(di+1)+' · '+esc(d.title)+'</h4>';
        d.tasks.forEach(function(t,ti){
          var key="p"+di+"-"+ti;
          h+='<label class="task'+(state.checks[key]?" done":"")+'"><input type="checkbox" data-check="'+key+'"'+(state.checks[key]?" checked":"")+'><span>'+t+'</span></label>';
        });
        h+='</div>';
      });
      h+='</div>';
    }
    el("v-plan").innerHTML=h;
    Array.prototype.forEach.call(el("v-plan").querySelectorAll("[data-mod]"),function(r){
      r.addEventListener("click",function(){ openLesson(+r.dataset.mod); });
    });
    Array.prototype.forEach.call(el("v-plan").querySelectorAll("[data-check]"),function(cb){
      cb.addEventListener("change",function(){ state.checks[cb.dataset.check]=cb.checked; save(); cb.closest(".task").classList.toggle("done",cb.checked); });
    });
  }

  /* ---------- LECCIONES ---------- */
  function renderLessonIndex(){
    var h='<div class="card"><h2>Lecciones</h2><p class="muted">Lee cada módulo, fíjate en los números y en las trampas, y pásate a las fichas.</p></div>';
    h+='<div class="grid g2">';
    MODS.forEach(function(m,mi){
      var s=moduleStats(mi);
      h+='<div class="card" style="margin-bottom:0"><div class="pill">Módulo '+(mi+1)+'</div>'+
         '<h3 style="margin:.4rem 0 .2rem">'+esc(m.title)+'</h3>'+
         '<p class="muted small">'+esc(m.tagline)+'</p>'+
         '<div class="btns"><button class="btn" data-open="'+mi+'">Estudiar lección</button>'+
         '<button class="btn ghost" data-cards="'+mi+'">Fichas ('+s.total+')</button>'+
         '<button class="btn ghost" data-quiz="'+mi+'">Test</button></div></div>';
    });
    h+='</div>';
    el("v-lesson").innerHTML=h;
    bind(el("v-lesson"));
  }
  function bind(scope){
    Array.prototype.forEach.call(scope.querySelectorAll("[data-open]"),function(b){ b.addEventListener("click",function(){ openLesson(+b.dataset.open); }); });
    Array.prototype.forEach.call(scope.querySelectorAll("[data-cards]"),function(b){ b.addEventListener("click",function(){ startCards(+b.dataset.cards); go("cards"); }); });
    Array.prototype.forEach.call(scope.querySelectorAll("[data-quiz]"),function(b){ b.addEventListener("click",function(){ go("quiz"); startQuiz(+b.dataset.quiz); }); });
  }
  function openLesson(mi){
    var m=MODS[mi], s=moduleStats(mi);
    var h='<div class="btns" style="margin-bottom:.6rem"><button class="btn ghost" id="backL">← Todas las lecciones</button>'+
      '<button class="btn" data-cards="'+mi+'">Fichas ('+s.total+')</button><button class="btn ghost" data-quiz="'+mi+'">Test</button></div>';
    h+='<div class="card"><div class="pill">Módulo '+(mi+1)+'</div><h2 style="margin:.4rem 0 .1rem">'+esc(m.title)+'</h2>'+
       '<p class="muted">'+esc(m.tagline)+'</p>';
    if(m.objetivos&&m.objetivos.length){
      h+='<div class="callout info"><b>Al terminar sabrás…</b><ul style="margin:.4rem 0 0">';
      m.objetivos.forEach(function(o){ h+='<li>'+o+'</li>'; });
      h+='</ul></div>';
    }
    h+='<div class="lesson">'+m.lesson+'</div>';
    if(m.trucos&&m.trucos.length){
      h+='<h3 style="color:var(--primary);margin-top:1.2rem">🧠 Cómo memorizarlo</h3>';
      m.trucos.forEach(function(t){ h+='<div class="callout tip">'+t+'</div>'; });
    }
    if(m.trampas&&m.trampas.length){
      h+='<h3 style="color:var(--danger);margin-top:1.2rem">⚠️ Trampas típicas</h3><ul>';
      m.trampas.forEach(function(t){ h+='<li>'+t+'</li>'; });
      h+='</ul>';
    }
    if(m.normas&&m.normas.length){
      h+='<p style="margin-top:1rem">';
      m.normas.forEach(function(n){ h+='<a class="ref" href="'+esc(n.u)+'" target="_blank" rel="noopener">'+esc(n.t)+' ↗</a>'; });
      h+='</p>';
    }
    h+='</div>';
    el("v-lesson").innerHTML=h;
    document.getElementById("backL").addEventListener("click",renderLessonIndex);
    bind(el("v-lesson"));
  }

  /* ---------- FICHAS (SRS) ---------- */
  var session=null; // {queue:[{mi,ci}], pos, showBack}
  function allCardsDue(){
    var q=[]; MODS.forEach(function(m,mi){ m.cards.forEach(function(c,ci){ if(isDue(cardId(mi,ci))) q.push({mi:mi,ci:ci}); }); });
    return q;
  }
  function renderCardsHome(){
    var due=allCardsDue().length, g=globalStats();
    var h='<div class="card"><h2>Fichas con repetición espaciada</h2>'+
      '<p class="muted">Cada ficha vuelve justo antes de que se te olvide (cajas 0→16 días). Valora con sinceridad: si dudas, pulsa «Otra vez».</p>'+
      '<div class="kpi" style="margin:.6rem 0"><div><b>'+due+'</b><span>para repasar hoy</span></div>'+
      '<div><b>'+g.learned+'/'+g.total+'</b><span>aprendidas (caja ≥3)</span></div></div>'+
      '<div class="btns"><button class="btn" id="startDue"'+(due?"":" disabled")+'>Repasar las pendientes ('+due+')</button>'+
      '<button class="btn ghost" id="startAll">Practicar todas ('+g.total+')</button>'+
      '<button class="btn ghost" id="resetCards">Reiniciar progreso de fichas</button></div></div>';
    h+='<div class="card"><h3>Elige un módulo</h3><div class="grid g2">';
    MODS.forEach(function(m,mi){ var s=moduleStats(mi);
      h+='<button class="opt" data-cards="'+mi+'"><b>'+(mi+1)+'. '+esc(m.title)+'</b><div class="muted small">'+s.learned+'/'+s.total+' aprendidas · '+s.due+' pendientes</div></button>';
    });
    h+='</div></div>';
    el("v-cards").innerHTML=h;
    document.getElementById("startDue").addEventListener("click",function(){ startCards("due"); });
    document.getElementById("startAll").addEventListener("click",function(){ startCards("all"); });
    document.getElementById("resetCards").addEventListener("click",function(){
      if(confirm("¿Reiniciar el progreso de todas las fichas?")){ state.cards={}; save(); renderCardsHome(); updateDue(); }
    });
    bind(el("v-cards"));
  }
  function startCards(scope){
    var queue;
    if(scope==="due") queue=shuffle(allCardsDue());
    else if(scope==="all"){ queue=[]; MODS.forEach(function(m,mi){ m.cards.forEach(function(c,ci){ queue.push({mi:mi,ci:ci}); }); }); queue=shuffle(queue); }
    else { var mi=+scope; queue=MODS[mi].cards.map(function(c,ci){ return {mi:mi,ci:ci}; }); }
    session={queue:queue,pos:0,showBack:false,scope:scope};
    renderCard();
  }
  function renderCard(){
    if(!session){ renderCardsHome(); return; }
    if(session.pos>=session.queue.length){
      var g=globalStats(), nDone=session.queue.length; session=null;
      el("v-cards").innerHTML='<div class="card center"><h2>¡Sesión completada! 🎉</h2>'+
        '<p class="muted">Has repasado '+nDone+' fichas. Aprendidas: '+g.learned+'/'+g.total+'.</p>'+
        '<div class="btns" style="justify-content:center"><button class="btn" id="again">Otro repaso</button>'+
        '<button class="btn ghost" id="home">Volver</button></div></div>';
      document.getElementById("again").addEventListener("click",renderCardsHome);
      document.getElementById("home").addEventListener("click",renderCardsHome);
      updateDue(); return;
    }
    var it=session.queue[session.pos], m=MODS[it.mi], c=m.cards[it.ci];
    var h='<div class="progressline"><button class="btn ghost" id="quit">← Salir</button>'+
      '<div class="grow" style="max-width:340px"><div class="bar"><i style="width:'+Math.round(session.pos/session.queue.length*100)+'%"></i></div></div>'+
      '<span class="muted small">'+(session.pos+1)+' / '+session.queue.length+'</span></div>';
    h+='<div class="flash"><div class="flip'+(session.showBack?" on":"")+'" id="flip">'+
      '<div class="face front"><span class="qtag">MÓDULO '+(it.mi+1)+'</span><div>'+esc(c.q)+'</div>'+
        '<span class="qref">'+(session.showBack?"":"(pulsa para ver)")+'</span></div>'+
      '<div class="face back"><span class="qtag">RESPUESTA</span><div>'+esc(c.a)+'</div>'+
        (c.ref?'<span class="qref">'+esc(c.ref)+'</span>':'')+'</div></div></div>';
    if(session.showBack){
      h+='<div class="grade"><button class="btn bad" data-g="0">Otra vez</button>'+
         '<button class="btn ok" data-g="1">Bien</button><button class="btn warn" data-g="2">Fácil</button></div>';
    }else{
      h+='<div class="grade"><button class="btn" id="reveal">Mostrar respuesta</button></div>';
    }
    el("v-cards").innerHTML=h;
    document.getElementById("quit").addEventListener("click",renderCardsHome);
    var flip=document.getElementById("flip");
    flip.addEventListener("click",function(){ if(!session.showBack){ session.showBack=true; renderCard(); } });
    var rev=document.getElementById("reveal"); if(rev) rev.addEventListener("click",function(){ session.showBack=true; renderCard(); });
    Array.prototype.forEach.call(document.querySelectorAll("[data-g]"),function(b){
      b.addEventListener("click",function(){ grade(it,+b.dataset.g); });
    });
  }
  function grade(it,g){
    var id=cardId(it.mi,it.ci), c=cardState(id);
    c.seen++; c.right += (g>=1?1:0);
    if(g===0) c.box=0; else if(g===1) c.box=Math.min(5,c.box+1); else c.box=Math.min(5,c.box+2);
    var days=BOX[c.box];
    c.due = new Date(Date.now()+days*DAY).toISOString().slice(0,10);
    save();
    session.pos++; session.showBack=false; renderCard(); updateDue();
  }

  /* ---------- TESTS ---------- */
  var quizSession=null;
  function renderQuizIndex(){
    var h='<div class="card"><h2>Tests por módulo</h2><p class="muted">Preguntas tipo test con corrección y explicación. Tu mejor nota se guarda.</p></div><div class="grid g2">';
    MODS.forEach(function(m,mi){
      var s=moduleStats(mi), cls=(s.quiz||0)>=80?"ok":(s.quiz?"warn":"");
      h+='<div class="card" style="margin-bottom:0"><h3 style="margin:.2rem 0">'+(mi+1)+'. '+esc(m.title)+'</h3>'+
         '<p class="muted small">'+m.quiz.length+' preguntas · '+s.total+' fichas</p>'+
         (s.quiz?'<p><span class="pill '+cls+'">Mejor: '+s.quiz+'%</span></p>':'')+
         '<button class="btn" data-quiz="'+mi+'">Empezar test</button></div>';
    });
    h+='</div>';
    el("v-quiz").innerHTML=h;
    Array.prototype.forEach.call(el("v-quiz").querySelectorAll("[data-quiz]"),function(b){ b.addEventListener("click",function(){ startQuiz(+b.dataset.quiz); }); });
  }
  function prepare(questions){
    return shuffle(questions.map(function(q){
      var idx=q.opts.map(function(o,i){return i;});
      var correct=q.ok;
      var pairs=shuffle(idx.map(function(i){ return {o:q.opts[i],ok:i===correct}; }));
      return {q:q.q, opts:pairs.map(function(p){return p.o;}), ok:pairs.findIndex(function(p){return p.ok;}), why:q.why, ref:q.ref};
    }));
  }
  function startQuiz(mi){
    var qs=prepare(MODS[mi].quiz);
    quizSession={mi:mi,qs:qs,pos:0,answers:[],sel:null,done:false};
    renderQuiz();
  }
  function renderQuiz(){
    var s=quizSession;
    if(s.pos>=s.qs.length){ return quizResult(); }
    var q=s.qs[s.pos];
    var h='<div class="progressline"><button class="btn ghost" id="qquit">← Salir</button>'+
      '<div class="grow" style="max-width:340px"><div class="bar"><i style="width:'+Math.round(s.pos/s.qs.length*100)+'%"></i></div></div>'+
      '<span class="muted small">'+(s.pos+1)+' / '+s.qs.length+'</span></div>';
    h+='<div class="card"><div class="pill">Módulo '+(s.mi+1)+' · '+esc(MODS[s.mi].title)+'</div>'+
      '<div class="qtext">'+esc(q.q)+'</div>';
    q.opts.forEach(function(o,i){ h+='<button class="opt" data-o="'+i+'"><span class="mk">'+String.fromCharCode(65+i)+'.</span>'+esc(o)+'</button>'; });
    if(s.sel!=null){
      var ok=s.sel===q.ok;
      h+='<div class="callout '+(ok?"tip":"trap")+'"><b>'+(ok?"✅ Correcto":"❌ Incorrecto")+'.</b> '+esc(q.why||"")+(q.ref?' <span class="ref">'+esc(q.ref)+'</span>':'')+'</div>';
      h+='<div class="btns"><button class="btn" id="next">'+(s.pos===s.qs.length-1?"Ver resultado":"Siguiente")+'</button></div>';
    }
    h+='</div>';
    el("v-quiz").innerHTML=h;
    document.getElementById("qquit").addEventListener("click",function(){ quizSession=null; renderQuizIndex(); });
    Array.prototype.forEach.call(el("v-quiz").querySelectorAll("[data-o]"),function(b){
      b.addEventListener("click",function(){ if(s.sel!=null) return; s.sel=+b.dataset.o; s.answers.push(s.sel===q.ok); renderQuiz(); });
    });
    var nx=document.getElementById("next"); if(nx) nx.addEventListener("click",function(){ s.pos++; s.sel=null; renderQuiz(); });
  }
  function quizResult(){
    var s=quizSession, right=s.answers.filter(Boolean).length, pct=Math.round(right/s.qs.length*100);
    var prev=state.quiz[MODS[s.mi].id]||0; state.quiz[MODS[s.mi].id]=Math.max(prev,pct); save();
    el("v-quiz").innerHTML='<div class="card center"><h2>Resultado del test</h2>'+
      '<div class="score">'+pct+'%</div><p class="muted">'+right+' de '+s.qs.length+' correctas'+(pct>prev?' · ¡nuevo récord!':'')+'</p>'+
      '<p><span class="pill '+(pct>=80?"ok":"warn")+'">'+verdict(pct)+'</span></p>'+
      '<div class="btns" style="justify-content:center"><button class="btn" id="retry">Repetir test</button>'+
      '<button class="btn ghost" id="toCards">Repasar fichas del módulo</button>'+
      '<button class="btn ghost" id="toIndex">Otros tests</button></div>'+
      (pct<80?'<p class="muted small" style="margin-top:.6rem">Vuelve a la lección, repasa las fichas y repite el test en un rato.</p>':'')+'</div>';
    document.getElementById("retry").addEventListener("click",function(){ startQuiz(s.mi); });
    document.getElementById("toCards").addEventListener("click",function(){ startCards(s.mi); go("cards"); });
    document.getElementById("toIndex").addEventListener("click",function(){ quizSession=null; renderQuizIndex(); });
    updateDue();
  }
  function verdict(p){ return p>=90?"Dominado":(p>=80?"Aprobado":(p>=60?"Vas bien, repasa":"Necesitas repasar")); }

  /* ---------- EXAMEN FINAL ---------- */
  var exam=null, examTimer=null;
  function allQuestions(){ var a=[]; MODS.forEach(function(m,mi){ m.quiz.forEach(function(q){ a.push({q:q.q,opts:q.opts,ok:q.ok,why:q.why,ref:q.ref,mi:mi}); }); }); return a; }
  function renderExam(){
    if(exam&&!exam.finished) return renderExamRun();
    var total=allQuestions().length;
    el("v-exam").innerHTML='<div class="card center"><h2>Examen final</h2>'+
      '<p class="muted">30 preguntas aleatorias de todo el curso · 25 minutos · se aprueba con <b>80%</b>.</p>'+
      '<p><span class="pill">Mejor nota: '+(state.exam.best||0)+'%</span> <span class="pill">Intentos: '+(state.exam.tries||0)+'</span></p>'+
      '<p class="muted small">Banco disponible: '+total+' preguntas.</p>'+
      '<button class="btn" id="examStart">Empezar examen</button></div>';
    document.getElementById("examStart").addEventListener("click",startExam);
  }
  function startExam(){
    exam={qs:prepare(shuffle(allQuestions()).slice(0,30)),pos:0,answers:[],sel:null,finished:false,seconds:25*60};
    examTimer=null;
    renderExamRun();
  }
  function fmt(s){ var m=Math.floor(s/60), x=s%60; return m+":"+String(x).padStart(2,"0"); }
  function renderExamRun(){
    var q=exam.qs[exam.pos];
    var h='<div class="progressline"><span class="pill">Pregunta '+(exam.pos+1)+'/'+exam.qs.length+'</span>'+
      '<span class="grow"></span><span class="pill">⏱ <b id="examClock">'+fmt(exam.seconds)+'</b></span></div>';
    h+='<div class="card"><div class="qtext">'+esc(q.q)+'</div>';
    q.opts.forEach(function(o,i){ h+='<button class="opt'+(exam.answers[exam.pos]===i?" sel":"")+'" data-o="'+i+'"><span class="mk">'+String.fromCharCode(65+i)+'.</span>'+esc(o)+'</button>'; });
    h+='<div class="btns" style="margin-top:.5rem"><button class="btn ghost" id="prev"'+(exam.pos===0?" disabled":"")+'>← Anterior</button>'+
       '<button class="btn" id="nextE">'+(exam.pos===exam.qs.length-1?"Terminar":"Siguiente →")+'</button>'+
       '<span class="grow"></span><button class="btn ghost" id="giveup">Entregar ya</button></div></div>';
    el("v-exam").innerHTML=h;
    Array.prototype.forEach.call(el("v-exam").querySelectorAll("[data-o]"),function(b){ b.addEventListener("click",function(){ exam.answers[exam.pos]=+b.dataset.o; renderExamRun(); }); });
    document.getElementById("prev").addEventListener("click",function(){ if(exam.pos>0){exam.pos--; renderExamRun();} });
    document.getElementById("nextE").addEventListener("click",function(){ if(exam.pos<exam.qs.length-1){ exam.pos++; renderExamRun(); } else submitExam(); });
    document.getElementById("giveup").addEventListener("click",submitExam);
    ensureClock();
  }
  function ensureClock(){
    if(examTimer) return;
    examTimer=setInterval(function(){
      if(!exam||exam.finished){ clearInterval(examTimer); examTimer=null; return; }
      exam.seconds--; var t=el("examClock"); if(t){ t.textContent=fmt(exam.seconds); if(exam.seconds<=0) submitExam(); }
    },1000);
  }
  function submitExam(){
    if(!exam||exam.finished) return;
    exam.finished=true; if(examTimer){ clearInterval(examTimer); examTimer=null; }
    var right=0; exam.qs.forEach(function(q,i){ if(exam.answers[i]===q.ok) right++; });
    var pct=Math.round(right/exam.qs.length*100);
    state.exam.tries=(state.exam.tries||0)+1; state.exam.best=Math.max(state.exam.best||0,pct); save();
    var h='<div class="card center"><h2>Examen final</h2><div class="score">'+pct+'%</div>'+
      '<p class="muted">'+right+'/'+exam.qs.length+' correctas · '+(pct>=80?"✅ APTO":"❌ No apto")+'</p>'+
      '<div class="bar" style="margin:.6rem auto;max-width:420px"><i style="width:'+pct+'%"></i></div>'+
      '<button class="btn" id="againE">Repetir</button></div>';
    h+='<div class="card"><h3>Revisión</h3>';
    exam.qs.forEach(function(q,i){
      var mine=exam.answers[i], ok=mine===q.ok;
      if(ok) return;
      h+='<div style="border-left:3px solid var(--danger);padding-left:.7rem;margin:.7rem 0"><b>'+esc(q.q)+'</b>'+
         '<div class="small">Tu respuesta: <span style="color:var(--danger)">'+esc(mine==null?"(sin responder)":q.opts[mine])+'</span></div>'+
         '<div class="small">Correcta: <span style="color:var(--ok)">'+esc(q.opts[q.ok])+'</span></div>'+
         '<div class="muted small">'+esc(q.why||"")+(q.ref?' · <span class="ref">'+esc(q.ref)+'</span>':'')+'</div></div>';
    });
    h+='<button class="btn ghost" id="backHome">Volver al inicio del examen</button></div>';
    el("v-exam").innerHTML=h;
    document.getElementById("againE").addEventListener("click",function(){ exam=null; startExam(); });
    document.getElementById("backHome").addEventListener("click",function(){ exam=null; renderExam(); });
  }

  /* ---------- NÚMEROS CLAVE ---------- */
  function renderNumbers(){
    var h='<div class="card"><h2>Taller de números clave</h2>'+
      '<p class="muted">Casi todos los errores son de cifras. Oculta las respuestas y recítalas; luego pásalas a un test.</p>'+
      '<div class="btns"><button class="btn" id="hideAll">Ocultar todas</button><button class="btn ghost" id="showAll">Mostrar todas</button>'+
      '<button class="btn ghost" id="drill">Modo interrogatorio 🔥</button></div></div>';
    h+='<div class="card" id="numList"><table class="tbl"><tr><th>Pregunta</th><th style="width:150px;text-align:right">Respuesta</th></tr>';
    NUMBERS.forEach(function(n,i){ h+='<tr class="numrow" style="border:none"><td class="q">'+n.q+'</td><td class="a">'+n.a+'</td></tr>'; });
    h+='</table></div>';
    el("v-numbers").innerHTML=h;
    document.getElementById("hideAll").addEventListener("click",function(){ Array.prototype.forEach.call(document.querySelectorAll(".numrow"),function(r){ r.classList.add("hide"); }); });
    document.getElementById("showAll").addEventListener("click",function(){ Array.prototype.forEach.call(document.querySelectorAll(".numrow"),function(r){ r.classList.remove("hide"); }); });
    document.getElementById("drill").addEventListener("click",renderDrill);
  }
  var drill=null;
  function renderDrill(){
    if(!drill||drill.pos>=drill.qs.length){ drill={qs:shuffle(NUMBERS),pos:0,shown:false,right:0,wrong:0}; }
    var q=drill.qs[drill.pos];
    var h='<div class="progressline"><button class="btn ghost" id="dquit">← Salir</button><span class="grow"></span>'+
      '<span class="pill ok">✔ '+drill.right+'</span> <span class="pill bad">✘ '+drill.wrong+'</span> <span class="muted small">'+(drill.pos+1)+'/'+drill.qs.length+'</span></div>';
    h+='<div class="card center"><div class="pill">Números clave</div><div class="flashnum">'+esc(q.q)+'</div>';
    if(drill.shown){
      h+='<div class="callout tip center" style="font-size:1.15rem"><b>'+esc(q.a)+'</b></div>'+
         '<div class="btns" style="justify-content:center"><button class="btn ok" id="dok">Lo sabía</button><button class="btn bad" id="dno">Fallo</button></div>';
    }else{
      h+='<button class="btn" id="dshow">Ver respuesta</button>';
    }
    h+='</div>';
    el("v-numbers").innerHTML=h;
    document.getElementById("dquit").addEventListener("click",renderNumbers);
    var s=document.getElementById("dshow"); if(s) s.addEventListener("click",function(){ drill.shown=true; renderDrill(); });
    var ok=document.getElementById("dok"); if(ok) ok.addEventListener("click",function(){ drill.right++; state.numbers.right++; state.numbers.total++; save(); drill.pos++; drill.shown=false; renderDrill(); });
    var no=document.getElementById("dno"); if(no) no.addEventListener("click",function(){ drill.wrong++; state.numbers.total++; save(); drill.pos++; drill.shown=false; renderDrill(); });
  }

  /* ---------- init ---------- */
  function init(){ renderPlan(); go("plan"); }
  init();
})();
</script>
</body>
</html>
"""


def normalize(mods):
    """Convierte las tuplas de curso_data.py en objetos que espera el motor."""
    out = []
    for m in mods:
        m = dict(m)
        m["cards"] = [
            {"q": c[0], "a": c[1], "ref": (c[2] if len(c) > 2 else "")}
            for c in m.get("cards", [])
        ]
        m["quiz"] = [
            {
                "q": z[0], "opts": list(z[1]), "ok": z[2],
                "why": (z[3] if len(z) > 3 else ""),
                "ref": (z[4] if len(z) > 4 else ""),
            }
            for z in m.get("quiz", [])
        ]
        m["normas"] = [{"t": n[0], "u": n[1]} for n in m.get("normas", [])]
        out.append(m)
    return out


def main():
    data = {
        "modules": normalize(MODULES),
        "numbers": NUMBERS,
        "plan": PLAN,
    }
    js = json.dumps(data, ensure_ascii=False)
    js = js.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = TEMPLATE.replace("__CURSO_DATA__", js)
    html = html.replace("__GENERATED__", datetime.date.today().isoformat())
    # INTRO se inserta vía JS esc() (texto plano) para evitar problemas de comillas.
    html = html.replace('var C = window.CURSO || {modules:[],numbers:[]};',
                        'var C = window.CURSO || {modules:[],numbers:[]};\n  var INTRO = ' + json.dumps(INTRO, ensure_ascii=False) + ";")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    nc, nq, nn = stats()
    print(f"curso/index.html generado · {len(MODULES)} módulos · "
          f"{nc} fichas · {nq} preguntas · {nn} números clave · {len(html)} bytes")


if __name__ == "__main__":
    main()

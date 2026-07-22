#!/usr/bin/env python3
"""Build Aviation Maintenance Academy - single-file offline HTML app."""
import json
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
from academy_data import MODULES, TRACKS, RANKS, XP, ACHIEVEMENTS, FLASHCARDS, GLOSSARY
from sims_ref_data import SIMS, REFERENCE
from academy_ext2 import EXT2_QUIZ, EXT2_FLASHCARDS, EXT2_GLOSSARY, EXT2_SIMS, EXT2_REFERENCE
from academy_ext4 import EXT4_SIMS, EXT4_REFERENCE
from academy_ext6 import EXT6_SIMS, EXT6_REFERENCE
from academy_ext8 import EXT8_SIMS, EXT8_REFERENCE
from academy_ext10 import EXT10_SIMS, EXT10_REFERENCE
from academy_ext12 import EXT12_SIMS, EXT12_REFERENCE
from academy_ext14 import EXT14_SIMS, EXT14_REFERENCE
from academy_ext16 import EXT16_SIMS, EXT16_REFERENCE
from academy_ext18 import EXT18_SIMS, EXT18_REFERENCE
from academy_ext20 import EXT20_SIMS, EXT20_REFERENCE
from academy_ext22 import EXT22_SIMS, EXT22_REFERENCE
from academy_ext23 import EXT23_REFERENCE, EXT23_ORAL, EXT23_PRACTICAL

# Safety net: guarantee every module has a non-empty icon (prevents literal
# 'undefined' from rendering in the Modules list if a future module dict omits it)
for _m in MODULES:
    if not _m.get('icon'):
        _m['icon'] = '&#x2708;'

# Merge content expansion pack 2
for _m in MODULES:
    _m['quiz'] = _m['quiz'] + EXT2_QUIZ.get(_m['id'], [])
FLASHCARDS = FLASHCARDS + EXT2_FLASHCARDS
GLOSSARY = GLOSSARY + EXT2_GLOSSARY

# Safety net: normalize any flashcards authored with q/a keys instead of front/back
# so they display correctly in the flip-card UI (front/back is the canonical schema).
for _fc in FLASHCARDS:
    if "front" not in _fc and "q" in _fc:
        _fc["front"] = _fc.pop("q")
    if "back" not in _fc and "a" in _fc:
        _fc["back"] = _fc.pop("a")

# Safety net: backfill any quiz question missing an "explain" field (would otherwise
# render the literal text "null"/"undefined" in the reveal box after answering).
for _m in MODULES:
    for _q in _m["quiz"]:
        if not _q.get("explain"):
            _q["explain"] = "Correct answer: " + _q["choices"][_q["answer"]] + "."

# Safety net: dedupe flashcards by front text (case-insensitive), keep first occurrence,
# merge the longer/more-detailed back text if a later duplicate has one.
_seen_fronts_build = {}
_deduped_flashcards_build = []
for _fc in FLASHCARDS:
    _key = _fc["front"].strip().lower()
    if _key not in _seen_fronts_build:
        _seen_fronts_build[_key] = _fc
        _deduped_flashcards_build.append(_fc)
    else:
        _existing = _seen_fronts_build[_key]
        if len(_fc.get("back", "")) > len(_existing.get("back", "")):
            _existing["back"] = _fc["back"]
FLASHCARDS = _deduped_flashcards_build

# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
_seen_terms_build = set()
_deduped_glossary_build = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms_build:
        _seen_terms_build.add(_key)
        _deduped_glossary_build.append(_g)
GLOSSARY = _deduped_glossary_build
SIMS = SIMS + EXT2_SIMS
REFERENCE = REFERENCE + EXT2_REFERENCE

# Merge content expansion pack 4 (Wave 2 sims/reference)
SIMS = SIMS + EXT4_SIMS
REFERENCE = REFERENCE + EXT4_REFERENCE

# Merge content expansion pack 6 (Wave 3 sims/reference)
SIMS = SIMS + EXT6_SIMS
REFERENCE = REFERENCE + EXT6_REFERENCE

# Merge content expansion pack 8 (Wave 4 sims/reference)
SIMS = SIMS + EXT8_SIMS
REFERENCE = REFERENCE + EXT8_REFERENCE

# Merge content expansion pack 10 (Wave 5 sims/reference)
SIMS = SIMS + EXT10_SIMS
REFERENCE = REFERENCE + EXT10_REFERENCE

# Merge content expansion pack 12 (Wave 6 sims/reference)
SIMS = SIMS + EXT12_SIMS
REFERENCE = REFERENCE + EXT12_REFERENCE

# Merge content expansion pack 14 (Wave 7 sims/reference)
SIMS = SIMS + EXT14_SIMS
REFERENCE = REFERENCE + EXT14_REFERENCE

# Merge content expansion pack 16 (Wave 8 sims/reference)
SIMS = SIMS + EXT16_SIMS
REFERENCE = REFERENCE + EXT16_REFERENCE

# Merge content expansion pack 18 (Wave 9 sims/reference)
SIMS = SIMS + EXT18_SIMS
REFERENCE = REFERENCE + EXT18_REFERENCE

# Merge content expansion pack 20 (Wave 10 sims/reference)
SIMS = SIMS + EXT20_SIMS
REFERENCE = REFERENCE + EXT20_REFERENCE

# Merge content expansion pack 22 (Wave 11 sims/reference)
SIMS = SIMS + EXT22_SIMS
REFERENCE = REFERENCE + EXT22_REFERENCE

# Merge content expansion pack 23 (Wave 12: Oral & Practical exam prep cards)
REFERENCE = REFERENCE + EXT23_REFERENCE
ORAL_QUESTIONS = list(EXT23_ORAL)
PRACTICAL_TASKS = list(EXT23_PRACTICAL)

with open(os.path.join(DIR, 'avia_features.js'), encoding='utf-8') as _ff:
    FEATURES_JS = _ff.read()

with open(os.path.join(DIR, 'avia_auth.js'), encoding='utf-8') as _af:
    AUTH_JS = _af.read()

with open(os.path.join(DIR, 'avia_instructor.js'), encoding='utf-8') as _if:
    INSTRUCTOR_JS = _if.read()

OUT = os.path.join(DIR, "Aviation_Maintenance_Academy.html")

CSS = """
:root{--bg:#0f172a;--bg2:#1e293b;--bg3:#334155;--txt:#e2e8f0;--txt2:#94a3b8;--accent:#3b82f6;--accent2:#60a5fa;--ok:#10b981;--warn:#f59e0b;--fail:#ef4444;--rad:12px}
[data-theme=light]{--bg:#f8fafc;--bg2:#e2e8f0;--bg3:#cbd5e1;--txt:#1e293b;--txt2:#475569}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--txt);min-height:100vh;display:flex;flex-direction:column}
.container{max-width:900px;margin:0 auto;padding:1.5rem;width:100%}
header{background:var(--bg2);padding:1rem 1.5rem;border-bottom:2px solid var(--accent);display:flex;align-items:center;gap:1rem;flex-wrap:wrap}
header h1{font-size:1.4rem;flex:1}
.nav-btn{background:var(--bg3);border:none;color:var(--txt);padding:0.4rem 0.8rem;border-radius:6px;cursor:pointer;font-size:0.85rem}
.nav-btn:hover,.nav-btn.active{background:var(--accent);color:#fff}
.card{background:var(--bg2);border-radius:var(--rad);padding:1.5rem;margin-bottom:1rem;border:1px solid var(--bg3)}
.card h2{margin-bottom:0.8rem;color:var(--accent2)}
.card h3{margin:1rem 0 0.5rem;color:var(--warn)}
.progress-bar{height:8px;background:var(--bg3);border-radius:4px;overflow:hidden;margin:0.5rem 0}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--ok));transition:width 0.5s}
.xp-ring{width:100px;height:100px;border-radius:50%;border:6px solid var(--bg3);display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:bold;margin:0 auto 0.5rem;position:relative}
.track-chip{display:inline-block;padding:0.2rem 0.6rem;border-radius:12px;font-size:0.75rem;font-weight:600;margin:0.2rem}
.module-card{cursor:pointer;transition:transform 0.2s,box-shadow 0.2s}
.module-card:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,0.3)}
.module-card .icon{font-size:2rem}
.quiz-opt{display:block;width:100%;text-align:left;padding:0.8rem 1rem;margin:0.4rem 0;border:2px solid var(--bg3);border-radius:8px;background:var(--bg);color:var(--txt);cursor:pointer;font-size:0.95rem}
.quiz-opt:hover{border-color:var(--accent)}
.quiz-opt.correct{border-color:var(--ok);background:rgba(16,185,129,0.1)}
.quiz-opt.wrong{border-color:var(--fail);background:rgba(239,68,68,0.1)}
.explain{background:var(--bg3);padding:0.8rem;border-radius:8px;margin:0.5rem 0;font-size:0.9rem;display:none}
.flashcard{width:100%;min-height:200px;perspective:1000px;cursor:pointer;margin:1rem 0}
.flashcard-inner{position:relative;width:100%;min-height:200px;transition:transform 0.5s;transform-style:preserve-3d}
.flashcard.flipped .flashcard-inner{transform:rotateY(180deg)}
.flashcard-face{position:absolute;width:100%;min-height:200px;backface-visibility:hidden;display:flex;align-items:center;justify-content:center;padding:2rem;text-align:center;border-radius:var(--rad);font-size:1.2rem}
.flashcard-front{background:var(--bg2);border:2px solid var(--accent)}
.flashcard-back{background:var(--bg2);border:2px solid var(--ok);transform:rotateY(180deg)}
.gloss-item{padding:0.5rem 0;border-bottom:1px solid var(--bg3)}
.gloss-item b{color:var(--accent2)}
.badge{display:inline-flex;align-items:center;gap:0.3rem;padding:0.3rem 0.6rem;background:var(--bg3);border-radius:8px;margin:0.2rem;font-size:0.8rem}
.badge.earned{background:var(--accent);color:#fff}
input[type=text],input[type=search]{background:var(--bg);border:1px solid var(--bg3);color:var(--txt);padding:0.5rem;border-radius:6px;width:100%;margin:0.5rem 0}
.btn{background:var(--accent);color:#fff;border:none;padding:0.6rem 1.2rem;border-radius:8px;cursor:pointer;font-size:0.9rem;font-weight:600}
.btn:hover{opacity:0.9}
.btn-sec{background:var(--bg3);color:var(--txt)}
.hidden{display:none!important}
.grid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem}
.streak{font-size:1.5rem;text-align:center;margin:0.5rem 0}
.section-body{line-height:1.7;margin:0.5rem 0}
.section-body ul,.section-body ol{margin-left:1.5rem}
.section-body b{color:var(--accent2)}
.cert-box{text-align:center;border:3px double var(--warn);padding:2rem;border-radius:var(--rad);margin:1rem 0}
.cert-box h2{color:var(--warn);font-size:1.8rem}
@media(max-width:600px){.grid2{grid-template-columns:1fr}header{flex-direction:column;align-items:flex-start}}
@media print{body{background:#fff;color:#000}.card{border:1px solid #ccc}header,.nav-btn{display:none}}
.sr-only-focusable{position:absolute;left:-9999px;top:0;background:var(--accent);color:#fff;padding:0.5rem 1rem;border-radius:0 0 8px 0;z-index:10000}
.sr-only-focusable:focus{left:0}
"""

def build_js():
    return f"""
const MODS={json.dumps(MODULES)};
const TRACKS={json.dumps(TRACKS)};
const RANKS={json.dumps(RANKS)};
const XP_TABLE={json.dumps(XP)};
const ACHIEVEMENTS={json.dumps(ACHIEVEMENTS)};
const FLASHCARDS={json.dumps(FLASHCARDS)};
const GLOSSARY={json.dumps(GLOSSARY)};
const SIMS={json.dumps(SIMS)};
const REFERENCE={json.dumps(REFERENCE)};
const ORAL_QUESTIONS={json.dumps(ORAL_QUESTIONS)};
    const PRACTICAL_TASKS={json.dumps(PRACTICAL_TASKS)};
const DEF={{xp:0,done:[],quizScores:{{}},flashReviewed:0,srCards:{{}},streak:0,lastVisit:null,visitLog:[],achievements:[],examPassed:false,examScore:0,missed:{{}},notes:{{}},bookmarks:[],lastChallenge:null,challengeDate:null,examDate:null,practicalLog:{{}},scoreHistory:[],lastExportAt:null,flashMissed:{{}},challengeStreak:0,readinessHistory:[],focusSessions:0}};
let S;
let ACCT={{users:[],current:null}};
function acctKey(){{return 'avia_academy_'+(ACCT.current||'guest')}}
function persist(){{localStorage.setItem(acctKey(),JSON.stringify(S))}}
function load(){{try{{S=JSON.parse(localStorage.getItem(acctKey()))||structuredClone(DEF)}}catch{{S=structuredClone(DEF)}}_lastGrade=null;updateStreak()}}
function updateStreak(){{const today=new Date().toDateString();if(!S.visitLog)S.visitLog=[];if(!S.visitLog.includes(today)){{S.visitLog.push(today);if(S.visitLog.length>60)S.visitLog=S.visitLog.slice(-60);}}if(S.lastVisit===today)return;if(S.lastVisit){{const d=new Date(S.lastVisit);d.setDate(d.getDate()+1);if(d.toDateString()===today)S.streak++;else S.streak=1}}else S.streak=1;if(!S.bestStreak||S.streak>S.bestStreak)S.bestStreak=S.streak;S.lastVisit=today;persist()}}
function addXP(n){{S.xp+=n;persist()}}
function getRank(){{let r=RANKS[0];for(const rk of RANKS)if(S.xp>=rk.xp)r=rk;return r}}
function pct(){{return Math.round(S.done.length/MODS.length*100)}}
function logScoreHistory(label,pct){{
  if(!S.scoreHistory)S.scoreHistory=[];
  S.scoreHistory.push({{date:new Date().toISOString(),label:label,pct:pct}});
  if(S.scoreHistory.length>40)S.scoreHistory=S.scoreHistory.slice(-40);
  persist();
}}
function checkAch(id){{if(!S.achievements.includes(id)){{S.achievements.push(id);if(!S.achDates)S.achDates={{}};S.achDates[id]=new Date().toISOString();persist();toast(ACHIEVEMENTS.find(a=>a.id===id))}}}}
function toast(ach){{if(!ach)return;const stack=document.getElementById('toast-stack');if(!stack)return;const d=document.createElement('div');d.setAttribute('role','status');d.setAttribute('aria-live','polite');d.style.cssText='background:var(--warn);color:#000;padding:1rem;border-radius:8px;font-weight:600;animation:fadeIn 0.3s;box-shadow:0 4px 12px rgba(0,0,0,.3)';d.textContent=ach.icon+' '+ach.name+'!';stack.appendChild(d);setTimeout(()=>d.remove(),3000)}}
function show(id){{document.querySelectorAll('.view').forEach(v=>v.classList.add('hidden'));document.getElementById(id).classList.remove('hidden')}}
function readinessScore(){{
  const modPct=MODS.length?S.done.length/MODS.length*100:0;
  const scores=Object.values(S.quizScores||{{}});
  const quizAvg=scores.length?scores.reduce((a,b)=>a+b,0)/scores.length:0;
  const sp=S.subjectPassed||{{}};
  const subjPct=['general','airframe','powerplant'].filter(id=>sp[id]).length/3*100;
  const oralPct=S.oralBest||0;
  const practicalPct=(typeof PRACTICAL_TASKS!=='undefined'&&PRACTICAL_TASKS.length)?Object.keys(S.practicalLog||{{}}).length/PRACTICAL_TASKS.length*100:0;
  const examPct=S.examPassed?100:(S.examScore||0);
  const total=Math.round(modPct*0.30+quizAvg*0.15+subjPct*0.15+oralPct*0.1+practicalPct*0.15+examPct*0.15);
  let label='Just Starting';
  if(total>=90)label='Exam Ready';else if(total>=70)label='Nearly There';else if(total>=40)label='Building Momentum';
  const finalTotal=Math.min(100,total);
  if(finalTotal>=90)checkAch('exam_ready');
  const todayKey=new Date().toDateString();
  S.readinessHistory=S.readinessHistory||[];
  const lastEntry=S.readinessHistory[S.readinessHistory.length-1];
  if(lastEntry&&lastEntry.date===todayKey){{lastEntry.total=finalTotal;}}
  else{{S.readinessHistory.push({{date:todayKey,total:finalTotal}});if(S.readinessHistory.length>40)S.readinessHistory.shift();}}
  return {{total:finalTotal,label,modPct:Math.round(modPct),quizAvg:Math.round(quizAvg),subjPct:Math.round(subjPct),oralPct:Math.round(oralPct),practicalPct:Math.round(practicalPct),examPct:Math.round(examPct)}};
}}
function weekDigestCard(){{
  const now=Date.now();const weekMs=7*86400000;
  const hist=(S.scoreHistory||[]).filter(h=>now-new Date(h.date).getTime()<=weekMs);
  const recentVisits=(S.visitLog||[]).filter(d=>now-new Date(d).getTime()<=weekMs).length;
  if(!hist.length&&!recentVisits)return '';
  const avgPct=hist.length?Math.round(hist.reduce((a,h)=>a+h.pct,0)/hist.length):0;
  const passCt=hist.filter(h=>h.pct>=70).length;
  let h='<div class="card"><h3>&#x1F4C5; This Week</h3>';
  h+='<div class="lm-stats" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(90px,1fr));gap:0.6rem">';
  h+='<div class="lm-stat" style="background:var(--bg2);border-radius:8px;padding:0.6rem;text-align:center"><b style="font-size:1.3rem;color:var(--accent2);display:block">'+recentVisits+'</b>day'+(recentVisits===1?'':'s')+' active</div>';
  h+='<div class="lm-stat" style="background:var(--bg2);border-radius:8px;padding:0.6rem;text-align:center"><b style="font-size:1.3rem;color:var(--accent2);display:block">'+hist.length+'</b>quiz'+(hist.length===1?'':'zes')+' taken</div>';
  h+='<div class="lm-stat" style="background:var(--bg2);border-radius:8px;padding:0.6rem;text-align:center"><b style="font-size:1.3rem;color:var(--accent2);display:block">'+avgPct+'%</b>avg score</div>';
  h+='<div class="lm-stat" style="background:var(--bg2);border-radius:8px;padding:0.6rem;text-align:center"><b style="font-size:1.3rem;color:var(--accent2);display:block">'+passCt+'/'+hist.length+'</b>passed (70%+)</div>';
  h+='</div>';
  const rh=(S.readinessHistory||[]).filter(p=>now-new Date(p.date).getTime()<=weekMs);
  if(rh.length>=2){{
    const delta=rh[rh.length-1].total-rh[0].total;
    const sign=delta>0?'+':'';
    const clr=delta>0?'var(--ok)':delta<0?'var(--fail)':'var(--txt2)';
    h+='<p style="margin-top:0.5rem;font-size:0.85rem">Readiness: <b>'+rh[rh.length-1].total+'%</b> <span style="color:'+clr+'">('+sign+delta+'% this week)</span></p>';
  }}
  h+='</div>';
  return h;
}}
function trendCard(){{
  const hist=(S.scoreHistory||[]).slice(-15);
  if(hist.length<2)return '';
  const w=560,ht=140,pad=24;
  const stepX=hist.length>1?(w-pad*2)/(hist.length-1):0;
  const pts=hist.map(function(pt,i){{
    const x=pad+i*stepX;
    const y=pad+ (100-pt.pct)/100*(ht-pad*1.5);
    return {{x:x,y:y,pt:pt}};
  }});
  const line=pts.map(function(p){{return p.x.toFixed(1)+','+p.y.toFixed(1);}}).join(' ');
  const dots=pts.map(function(p){{
    const title=esc(p.pt.label)+': '+p.pt.pct+'%';
    return '<circle cx="'+p.x.toFixed(1)+'" cy="'+p.y.toFixed(1)+'" r="4" fill="var(--accent)"><title>'+title+'</title></circle>';
  }}).join('');
  const passLine=pad+(100-70)/100*(ht-pad*1.5);
  let h='<div class="card"><h3>&#x1F4C8; Score Trend (last '+hist.length+' attempts)</h3>';
  h+='<svg viewBox="0 0 '+w+' '+ht+'" style="width:100%;height:150px" preserveAspectRatio="none">';
  h+='<line x1="'+pad+'" y1="'+passLine.toFixed(1)+'" x2="'+(w-pad)+'" y2="'+passLine.toFixed(1)+'" stroke="var(--warn)" stroke-dasharray="4,3" stroke-width="1"/>';
  h+='<polyline points="'+line+'" fill="none" stroke="var(--accent)" stroke-width="2.5"/>';
  h+=dots;
  h+='</svg>';
  h+='<p style="color:var(--txt2);font-size:.8rem">Dashed line = 70% pass bar. Hover a dot for details. Tracks Practice Quizzes, Cram Quizzes, Subject Tests, Mock Oral, and the Final Exam.</p></div>';
  return h;
}}
function teamCompareCard(){{
  if(typeof ACCT==='undefined'||!ACCT.users||ACCT.users.length<2||typeof userProgress!=='function')return '';
  const me=(typeof curUser==='function')?curUser():null;if(!me)return '';
  const others=ACCT.users.filter(u=>u.id!==me.id);
  if(!others.length)return '';
  const otherReadiness=others.map(u=>userProgress(u).readiness||0);
  const teamAvg=Math.round(otherReadiness.reduce((a,b)=>a+b,0)/otherReadiness.length);
  const myReadiness=readinessScore().total;
  const diff=myReadiness-teamAvg;
  const col=diff>=0?'var(--ok)':'var(--warn)';
  const verb=diff>=0?'ahead of':'behind';
  return '<div class="card" style="text-align:center"><h3>&#x1F465; How You Compare</h3><p>Your readiness: <b>'+myReadiness+'%</b> &middot; Team average: <b>'+teamAvg+'%</b></p><p style="color:'+col+';font-weight:600">'+(diff===0?'You are right at the team average.':('You are '+Math.abs(diff)+'% '+verb+' the rest of the team.'))+'</p></div>';
}}
function readinessCard(){{
  const r=readinessScore();
  let h='<div class="card"><h3>&#x1F6E9; Exam Readiness: <span style="color:'+(r.total>=90?'var(--ok)':r.total>=70?'var(--accent2)':r.total>=40?'var(--warn)':'var(--fail)')+'">'+r.total+'% &mdash; '+r.label+'</span></h3>';
  h+='<div class="progress-bar"><div class="progress-fill" style="width:'+r.total+'%"></div></div>';
  h+='<div style="display:grid;grid-template-columns:1fr 1fr;gap:0.3rem;font-size:0.8rem;color:var(--txt2);margin-top:0.6rem">';
  h+='<div>Modules: '+r.modPct+'%</div><div>Quiz avg: '+r.quizAvg+'%</div>';
  h+='<div>Subject tests: '+r.subjPct+'%</div><div>Mock Oral best: '+r.oralPct+'%</div>';
  h+='<div>Practical tasks: '+r.practicalPct+'%</div><div>Final Exam: '+r.examPct+'%</div></div>';
  h+='<div style="text-align:center;margin-top:0.6rem;display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap"><button class="btn btn-sec" onclick="printReadinessReport()">&#x1F5A8; Print Full Readiness Report</button>';
  if(r.modPct>=100)h+='<button class="btn btn-sec" onclick="printCertificate()">&#x1F393; Print Certificate of Completion</button>';
  h+='</div></div>';
  return h;
}}
function nextStepCard(){{
  const r=readinessScore();
  if(r.modPct<100){{
    const nextMod=MODS.find(m=>!S.done.includes(m.id));
    if(nextMod)return '<div class="card" style="border:1px solid var(--accent)"><h3>&#x1F449; Next Best Step</h3><p>Finish your remaining modules first &mdash; they unlock Subject Tests and feed everything else. Next up: <b>'+nextMod.title+'</b>.</p><button class="btn" onclick="openModule(\\''+nextMod.id+'\\')">Continue: '+nextMod.title+'</button></div>';
  }}
  const pillars=[
    {{key:'quizAvg',val:r.quizAvg,label:'Quiz average',action:'startCramQuiz()',cta:'&#x1F525; Cram Weak Areas Quiz'}},
    {{key:'subjPct',val:r.subjPct,label:'Subject tests',action:'renderSubTests()',cta:'&#x23F1; Take a Subject Test'}},
    {{key:'oralPct',val:r.oralPct,label:'Mock Oral',action:'renderOral()',cta:'&#x1F3A4; Practice Mock Oral'}},
    {{key:'practicalPct',val:r.practicalPct,label:'Practical tasks',action:'renderPractical()',cta:'&#x1F527; Log a Practical Task'}},
    {{key:'examPct',val:r.examPct,label:'Final Exam',action:'renderExam()',cta:'&#x1F4DD; Take the Final Exam'}}
  ];
  pillars.sort((a,b)=>a.val-b.val);
  const worst=pillars[0];
  if(worst.val>=90)return '<div class="card" style="border:1px solid var(--ok)"><h3>&#x1F680; Next Best Step</h3><p style="color:var(--ok)">&#x2705; Every readiness pillar is 90%+. You are exam ready &mdash; keep sharp with a Random Practice Quiz or review your weakest flashcard deck.</p></div>';
  return '<div class="card" style="border:1px solid var(--warn)"><h3>&#x1F449; Next Best Step</h3><p>Your lowest readiness pillar is <b>'+worst.label+'</b> at <b>'+worst.val+'%</b>. Focus here for the biggest readiness gain.</p><button class="btn" onclick="'+worst.action+'">'+worst.cta+'</button></div>';
}}
function studyPlanCard(){{
  if(!S.examDate)return '';
  const remainMods=MODS.length-S.done.length;
  const today=new Date();today.setHours(0,0,0,0);
  const target=new Date(S.examDate);target.setHours(0,0,0,0);
  const daysLeft=Math.ceil((target-today)/86400000);
  let h='<div class="card" style="border:1px solid var(--accent)"><h3>&#x1F5D3; Study Plan</h3>';
  if(daysLeft<0){{h+='<p style="color:var(--fail)">Your target exam date has passed. Update it in your Profile.</p></div>';return h;}}
  const remainPractical=(typeof PRACTICAL_TASKS!=='undefined')?PRACTICAL_TASKS.length-Object.keys(S.practicalLog||{{}}).length:0;
  if(remainMods===0){{
    let tail='Focus on Subject Tests, the Final Exam, and Mock Oral before '+target.toLocaleDateString()+'.';
    if(remainPractical>0)tail+=' You also have <b>'+remainPractical+'</b> Practical Task'+(remainPractical===1?'':'s')+' left to log.';
    h+='<p style="color:var(--ok)">&#x2705; All modules complete. '+tail+'</p></div>';return h;
  }}
  const perDay=daysLeft>0?Math.ceil(remainMods/daysLeft):remainMods;
  h+='<p><b>'+daysLeft+'</b> day'+(daysLeft===1?'':'s')+' until your target exam date ('+target.toLocaleDateString()+'). You have <b>'+remainMods+'</b> module'+(remainMods===1?'':'s')+' left.</p>';
  h+='<p style="color:var(--txt2)">Recommended pace: <b>'+perDay+' module'+(perDay===1?'':'s')+'/day</b> to finish with time to spare for review.</p>';
  const estMinPerDay=perDay*8;
  const estLabel=estMinPerDay>=60?(Math.round(estMinPerDay/60*10)/10)+' hour'+(Math.round(estMinPerDay/60*10)/10===1?'':'s'):estMinPerDay+' minutes';
  h+='<p style="color:var(--txt2);font-size:0.85rem">&#x23F1; Estimated daily study time at this pace: <b>~'+estLabel+'/day</b> (~8 min/module).</p>';
  const rReady=readinessScore();
  if(daysLeft<=14&&rReady.total<70){{
    h+='<p style="color:var(--fail);margin-top:0.6rem">&#x26A0; Only '+daysLeft+' day'+(daysLeft===1?'':'s')+' left and your overall Exam Readiness is just <b>'+rReady.total+'%</b>. At this pace, consider intensifying your study time or discussing a later date with your instructor/DME.</p>';
  }}else if(perDay>3){{
    h+='<p style="color:var(--warn);margin-top:0.6rem">&#x26A0; '+perDay+' modules/day is an aggressive pace. If that is not realistic, consider moving your target exam date back in your Profile.</p>';
  }}
  h+='</div>';
  return h;
}}
function renderDash(){{
  const r=getRank();
  let h='<div class="card"><div class="xp-ring">'+r.level+'</div><div style="text-align:center"><b>'+r.name+'</b><br>'+S.xp+' XP</div>';
  h+='<div class="progress-bar"><div class="progress-fill" style="width:'+pct()+'%"></div></div><div style="text-align:center;font-size:0.85rem">'+pct()+'% complete ('+S.done.length+'/'+MODS.length+' modules)</div>';
  h+='<div class="streak">'+S.streak+' day streak &#x1F525;'+(S.bestStreak&&S.bestStreak>S.streak?' <span style="font-size:0.7rem;color:var(--txt2)">(best: '+S.bestStreak+')</span>':'')+'</div></div>';
  h+=renderStreakCal();
  h+=readinessCard();
  h+=teamCompareCard();
  h+=nextStepCard();
  h+=studyPlanCard();
  h+=weekDigestCard();
  h+=trendCard();
  const dueN=(typeof srDueIdx==="function")?srDueIdx().length:0;
  if(dueN>0)h+=\'<div class="card" style="text-align:center;cursor:pointer" onclick="renderFlash()">&#x1F501; <b>\'+dueN+\'</b> flashcard\'+(dueN===1?"":"s")+\' due for review &#x2192;</div>\';
  h+=(typeof missedPreviewCard==='function'?missedPreviewCard():'');

  const _wk=weakestModule();
  if(_wk)h+='<div class="card" style="text-align:center;cursor:pointer;border:1px solid var(--warn)" onclick="openModule(\\''+_wk.id+'\\')">&#x1F3AF; Lowest quiz score: <b>'+_wk.title+'</b> ('+_wk.score+'%) &mdash; tap to review &#x2192;</div>';
  h+=\'<div style="text-align:center;margin:0.5rem 0;display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap"><button class="btn btn-sec" onclick="printStudyGuide()">&#x1F5A8; Export Study Guide</button><button class="btn btn-sec" onclick="printNotes()">&#x1F4DD; Export My Notes</button></div>\';
  h+=(typeof challengeCard==='function'?challengeCard():'');
  h+=almostThereCard();
  h+=(typeof focusTimerCard==='function'?focusTimerCard():'');
  h+='<div style="text-align:center;margin:0.5rem 0;display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap"><button class="btn btn-sec" onclick="startPracticeQuiz()">&#x1F3B2; Random Practice Quiz</button><button class="btn btn-sec" onclick="renderMastery()">&#x1F4CA; Mastery Report</button></div>';
  h+=(typeof dashAssignedCard==='function'?dashAssignedCard():'');
  h+=(typeof termOfDayCard==='function'?termOfDayCard():'');
  h+=(typeof refCardOfDayCard==='function'?refCardOfDayCard():'');
  h+=(typeof flashOfDayCard==='function'?flashOfDayCard():'');
  const _remainMods=MODS.length-S.done.length;
  if(_remainMods>0){{
    const _estMin=_remainMods*8;
    const _estLabel=_estMin>=60?(Math.round(_estMin/60*10)/10)+' hours':_estMin+' minutes';
    h+='<div class="card" style="text-align:center"><p style="color:var(--txt2)">&#x23F1; Estimated time to finish remaining '+_remainMods+' module'+(_remainMods===1?'':'s')+': <b>'+_estLabel+'</b> <span style="font-size:0.7rem">(~8 min/module)</span></p></div>';
  }}
  h+=(typeof notesOverviewCard==='function'?notesOverviewCard():'');
  h+=(typeof renderRecent==='function'?renderRecent():'');
  h+='<h2 style="margin:1rem 0">Tracks</h2><div class="grid2">';
  for(const t of TRACKS){{
    const mods=t.modules.map(id=>MODS.find(m=>m.id===id));
    const done=mods.filter(m=>S.done.includes(m.id)).length;
    const complete=done===mods.length;
    h+='<div class="card"><h3 style="color:'+t.color+'">'+t.name+' ('+done+'/'+mods.length+')'+(complete?' <span style="font-size:0.75rem;background:var(--ok);color:#fff;border-radius:6px;padding:0.1rem 0.5rem;vertical-align:middle">&#x1F3C6; COMPLETE</span>':'')+'</h3>';
    h+='<div class="progress-bar"><div class="progress-fill" style="width:'+(done/mods.length*100)+'%;background:'+t.color+'"></div></div>';
    for(const m of mods){{
      const dn=S.done.includes(m.id)?'&#x2705;':'&#x25CB;';
      const best=(S.quizBest&&S.quizBest[m.id]!=null)?' <span style="font-size:0.7rem;color:var(--txt2)">('+S.quizBest[m.id]+'%)</span>':'';
      h+='<div class="module-card card" onclick="openModule(\\''+m.id+'\\')"><span class="icon">'+m.icon+'</span> '+dn+' '+m.title+best+'</div>';
    }}
    h+='</div>';
  }}
  h+='</div>';
  document.getElementById('dash-content').innerHTML=h;
}}
let curModId=null;
function nextIncompleteModule(afterId){{
  const i=MODS.findIndex(m=>m.id===afterId);
  if(i<0)return null;
  for(let k=i+1;k<MODS.length;k++){{if(!S.done.includes(MODS[k].id))return MODS[k];}}
  for(let k=0;k<i;k++){{if(!S.done.includes(MODS[k].id))return MODS[k];}}
  return null;
}}
function openModule(id){{
  curModId=id;
  const m=MODS.find(x=>x.id===id);if(!m)return;
  if(!S.recentModules)S.recentModules=[];
  S.recentModules=S.recentModules.filter(rid=>rid!==id);
  S.recentModules.unshift(id);
  if(S.recentModules.length>5)S.recentModules=S.recentModules.slice(0,5);
  persist();
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>'+m.icon+' '+m.title+'</h2>';
  h+='<span class="track-chip" style="background:'+TRACKS.find(t=>t.modules.includes(id)).color+'">'+TRACKS.find(t=>t.modules.includes(id)).name+'</span>';
  h+='<span class="track-chip" style="background:var(--bg3);color:var(--txt2);margin-left:0.4rem">&#x1F4D6; '+esc(m.faa_ref||'')+'</span>';
  h+=\'<button class="btn btn-sec" style="margin-top:0.6rem" onclick="printModule(\\\'\'+id+\'\\\')">&#x1F5A8; Print / Save as PDF</button>\';
  h+=\'<button class="btn btn-sec" style="margin-top:0.6rem" onclick="readAloud(\\\'\'+id+\'\\\')">&#x1F50A; Read Aloud</button> <button class="btn btn-sec" style="margin-top:0.6rem" onclick="stopReadAloud()">&#x23F9; Stop Reading</button>\';
  h+='</div>';
  for(const sec of m.sections){{
    h+='<div class="card"><h3>'+sec.heading+'</h3><div class="section-body">'+sec.body+'</div></div>';
  }}
  if(!S.done.includes(id)){{
    h+='<div style="text-align:center;margin:1rem"><button class="btn" onclick="markRead(\\''+id+'\\')">&#x2705; Mark Lessons Read</button></div>';
  }}else{{
    h+='<div class="card" style="text-align:center;color:var(--ok)">&#x2705; Lessons completed</div>';
    const _nm=nextIncompleteModule(id);
    if(_nm)h+='<div style="text-align:center;margin:0.5rem 0"><button class="btn" onclick="openModule(\\''+_nm.id+'\\')">Next Module: '+_nm.icon+' '+_nm.title+' &#x2192;</button></div>';
  }}
  h+='<div class="card"><h2>&#x1F4DD; My Notes</h2><textarea id="note-'+id+'" placeholder="Jot down anything worth remembering..." style="width:100%;min-height:90px;background:var(--bg);color:var(--txt);border:1px solid var(--bg3);border-radius:8px;padding:0.6rem;font-family:inherit" onchange="saveNote(\\\'\'+id+\'\\\',this.value)">'+esc(S.notes[id]||'')+'</textarea></div>';
  h+='<div class="card"><h2>&#x1F4DD; Quiz</h2><div id="quiz-area"></div></div>';
  document.getElementById('mod-content').innerHTML=h;
  renderQuiz(m);
  show('v-module');
}}
function saveNote(id,val){{S.notes[id]=val;persist();}}
function markRead(id){{
  if(!S.done.includes(id)){{S.done.push(id);addXP(XP_TABLE.lesson*5)}}
  if(typeof logActivity==='function')logActivity('complete',ACCT.current,id,ACCT.current);
  if(S.done.length===1)checkAch('first_lesson');
  const genMods=TRACKS.find(t=>t.id==='general').modules;
  if(genMods.every(mid=>S.done.includes(mid)))checkAch('all_general');
  const afMods=TRACKS.find(t=>t.id==='airframe').modules;
  if(afMods.every(mid=>S.done.includes(mid)))checkAch('all_airframe');
  const ppMods=TRACKS.find(t=>t.id==='powerplant').modules;
  if(ppMods.every(mid=>S.done.includes(mid)))checkAch('all_powerplant');
  if(genMods.every(mid=>S.done.includes(mid))&&afMods.every(mid=>S.done.includes(mid))&&ppMods.every(mid=>S.done.includes(mid)))checkAch('triple_crown');
  if(S.done.length===MODS.length)checkAch('full_ap');
  if(S.streak>=7)checkAch('streak_7');
  persist();openModule(id);
}}
let quizStart=0;
function renderQuiz(m){{
  quizStart=Date.now();
  quizAnswers={{}};
  const area=document.getElementById('quiz-area');if(!area)return;
  let h='';
  m.quiz.forEach((q,i)=>{{
    h+='<div class="card" id="q'+i+'"><p><b>'+(i+1)+'. '+q.q+'</b></p>';
    q.choices.forEach((c,ci)=>{{
      h+='<button class="quiz-opt" onclick="answer('+i+','+ci+','+q.answer+')">'+c+'</button>';
    }});
    h+='<div class="explain" id="ex'+i+'">'+q.explain+'</div></div>';
  }});
  h+='<div id="quiz-result"></div>';
  area.innerHTML=h;
}}
let quizAnswers={{}};
function answer(qi,ci,correct){{
  if(quizAnswers[qi]!==undefined)return;
  quizAnswers[qi]=ci;
  const opts=document.querySelectorAll('#q'+qi+' .quiz-opt');
  if(opts[ci])opts[ci].classList.add(ci===correct?'correct':'wrong');
  if(ci!==correct&&opts[correct])opts[correct].classList.add('correct');
  const exEl=document.getElementById('ex'+qi);if(exEl)exEl.style.display='block';
  trackMissed(curModId,qi,ci===correct);
  const total=document.querySelectorAll('[id^=q]').length;
  const answered=Object.keys(quizAnswers).length;
  if(answered===total){{
    const score=Object.entries(quizAnswers).filter(([k,v])=>v===MODS.flatMap(m=>m.quiz)[parseInt(k)]?.answer).length;
    // recalculate from current module
    const modQuiz=document.getElementById('quiz-area');
    let correct_count=0;
    for(let i=0;i<total;i++)if(quizAnswers[i]===parseInt(document.querySelectorAll('#q'+i+' .quiz-opt.correct')[0]?.dataset?.ci||quizAnswers[i]))correct_count++;
    // simpler: count .correct that also have the user selection
    correct_count=0;
    for(let i=0;i<total;i++){{const opts2=document.querySelectorAll('#q'+i+' .quiz-opt');let ca=-1;opts2.forEach((o,idx)=>{{if(o.classList.contains('correct'))ca=idx}});if(quizAnswers[i]===ca)correct_count++}}
    const pctScore=Math.round(correct_count/total*100);
    if(curModId){{
      S.quizScores[curModId]=pctScore;
      if(!S.quizBest)S.quizBest={{}};
      if(!S.quizBest[curModId]||pctScore>S.quizBest[curModId])S.quizBest[curModId]=pctScore;
      const _modForHist=MODS.find(mm=>mm.id===curModId);
      logScoreHistory((_modForHist?_modForHist.title:curModId)+' Quiz',pctScore);
      persist();
    }}
    let msg='<div class="card"><h3>Score: '+correct_count+'/'+total+' ('+pctScore+'%)</h3>';
    if(pctScore===100){{msg+='<p style="color:var(--ok)">&#x1F4AF; Perfect!</p>';addXP(XP_TABLE.quiz_perfect);checkAch('perfect_quiz');const elapsed=(Date.now()-quizStart)/1000;if(elapsed<60)checkAch('speed_demon')}}
    else if(pctScore>=70){{msg+='<p style="color:var(--warn)">Good - review missed items.</p>';addXP(XP_TABLE.quiz_pass)}}
    else{{msg+='<p style="color:var(--fail)">Below 70% - restudy this module.</p>'}}
    msg+='</div>';
    document.getElementById('quiz-result').innerHTML=msg;
    quizAnswers={{}};
  }}
}}
function trackMissed(modId,qIndex,wasCorrect){{
  if(!modId)return;
  if(!S.missed[modId])S.missed[modId]={{}};
  if(wasCorrect){{delete S.missed[modId][qIndex];if(Object.keys(S.missed[modId]).length===0)delete S.missed[modId];}}
  else{{S.missed[modId][qIndex]=true;}}
  persist();
}}
function missedList(){{
  const out=[];
  for(const modId in S.missed){{
    const m=MODS.find(x=>x.id===modId);if(!m)continue;
    for(const qi in S.missed[modId]){{
      const q=m.quiz[parseInt(qi)];if(!q)continue;
      out.push({{modId,modTitle:m.title,qi:parseInt(qi),q}});
    }}
  }}
  return out;
}}
function missedPreviewCard(){{
  const items=missedList();
  if(!items.length)return '';
  const preview=items.slice(0,3);
  let h='<div class="card" style="cursor:pointer" onclick="renderReview()"><h3 style="margin-top:0">&#x1F3AF; <b>'+items.length+'</b> missed question'+(items.length===1?'':'s')+' to review</h3>';
  preview.forEach(it=>{{
    const snippet=it.q.q.length>80?it.q.q.slice(0,80)+'\u2026':it.q.q;
    h+='<p style="margin:0.3rem 0;font-size:0.85rem;color:var(--txt2)"><span style="color:var(--txt1)">'+it.modTitle+':</span> '+snippet+'</p>';
  }});
  if(items.length>preview.length)h+='<p style="font-size:0.8rem;color:var(--txt2)">+'+(items.length-preview.length)+' more &#x2192;</p>';
  h+='</div>';
  return h;
}}
function renderReview(){{
  const items=missedList();
  let h='<div class="card"><h2>&#x1F3AF; Review Missed Questions</h2><p style="color:var(--txt2)">Questions you answered incorrectly, across all modules. Answer correctly to clear them from this list.</p>';
  if(items.length>0)h+='<button class="btn btn-sec" onclick="printMissedReview()">&#x1F5A8; Print Missed Questions</button>';
  h+='</div>';
  if(items.length===0){{h+='<div class="card" style="text-align:center;color:var(--ok)">&#x2705; No missed questions right now - nice work!</div>';}}
  items.forEach((it,idx)=>{{
    h+='<div class="card" id="rv'+idx+'"><p style="color:var(--txt2);font-size:0.85rem">'+it.modTitle+'</p><p><b>'+it.q.q+'</b></p>';
    it.q.choices.forEach((c,ci)=>{{
      h+='<button class="quiz-opt" onclick="reviewAnswer(\\\'\'+it.modId+\'\\\','+it.qi+','+ci+','+it.q.answer+',\\\'\'+'rv'+idx+\'\\\')">'+c+'</button>';
    }});
    h+='<div class="explain" id="rvex'+idx+'">'+it.q.explain+'</div></div>';
  }});
  document.getElementById('review-content').innerHTML=h;
  show('v-review');
}}
function reviewAnswer(modId,qi,ci,correct,cardId){{
  const card=document.getElementById(cardId);if(!card)return;
  const opts=card.querySelectorAll('.quiz-opt');
  opts.forEach(o=>o.disabled=true);
  opts[ci].classList.add(ci===correct?'correct':'wrong');
  if(ci!==correct)opts[correct].classList.add('correct');
  const ex=document.getElementById(cardId.replace('rv','rvex'));if(ex)ex.style.display='block';
  trackMissed(modId,qi,ci===correct);
  if(ci===correct)setTimeout(renderReview,900);
}}
function srCard(idx){{
  if(!S.srCards)S.srCards={{}};
  if(!S.srCards[idx])S.srCards[idx]={{due:0,ivl:0,ef:2.5,reps:0}};
  return S.srCards[idx];
}}
function srDueIdx(){{
  const now=Date.now();const due=[];
  for(let i=0;i<FLASHCARDS.length;i++){{if(srCard(i).due<=now)due.push(i);}}
  return due;
}}
function srPickIdx(){{
  const due=srDueIdx();
  if(due.length){{due.sort((a,b)=>srCard(a).due-srCard(b).due);return due[0];}}
  return Math.floor(Math.random()*FLASHCARDS.length);
}}
let _flashIdx=null;
let _flashBookmarkMode=false;
let _flashCramMode=false;
function toggleBookmark(idx){{
  if(!S.bookmarks)S.bookmarks=[];
  const i=S.bookmarks.indexOf(idx);
  if(i>=0)S.bookmarks.splice(i,1);else S.bookmarks.push(idx);
  persist();renderFlash();
}}
function toggleBookmarkMode(){{
  _flashBookmarkMode=!_flashBookmarkMode;
  renderFlash();
}}
function toggleFlashCramMode(){{
  _flashCramMode=!_flashCramMode;
  renderFlash();
}}
function renderFlash(keepIdx){{
  if(_flashBookmarkMode&&(!S.bookmarks||S.bookmarks.length===0)){{_flashBookmarkMode=false;}}
  const weakIdx=Object.keys(S.flashMissed||{{}}).map(Number);
  if(_flashCramMode&&weakIdx.length===0){{_flashCramMode=false;}}
  if(!keepIdx){{
    if(_flashCramMode){{
      _flashIdx=weakIdx[Math.floor(Math.random()*weakIdx.length)];
    }}else if(_flashBookmarkMode){{
      const bm=S.bookmarks;
      _flashIdx=bm[Math.floor(Math.random()*bm.length)];
    }}else{{
      _flashIdx=srPickIdx();
    }}
  }}
  const fc=FLASHCARDS[_flashIdx];
  const dueCount=srDueIdx().length;
  const isBm=(S.bookmarks||[]).includes(_flashIdx);
  const bmCount=(S.bookmarks||[]).length;
  const seenCount=S.srCards?Object.keys(S.srCards).filter(k=>S.srCards[k].reps>0).length:0;
  const deckPct=FLASHCARDS.length?Math.round(seenCount/FLASHCARDS.length*100):0;
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x1F0CF; Flashcards</h2><p>'+FLASHCARDS.length+' cards total &middot; Due now: <b>'+dueCount+'</b> &middot; Reviewed: '+S.flashReviewed+' &middot; Bookmarked: <b>'+bmCount+'</b></p>';
  h+='<div class="progress-bar"><div class="progress-fill" style="width:'+deckPct+'%"></div></div><p style="text-align:center;font-size:0.8rem;color:var(--txt2)">Deck mastery: '+deckPct+'% of cards seen at least once ('+seenCount+'/'+FLASHCARDS.length+')</p>';
  h+='<p style="color:var(--txt2);font-size:0.85rem">Click the card to flip, then grade how well you knew it. Spaced repetition schedules harder cards more often. <span style="opacity:0.7">Keyboard: Space to flip, 1-4 to grade.</span></p>';
  const weakCount=Object.keys(S.flashMissed||{{}}).length;
  h+='<button class="btn btn-sec" onclick="toggleBookmarkMode()">'+(_flashBookmarkMode?'&#x1F501; Back to Normal Deck':'&#x2B50; Study Bookmarked Only ('+bmCount+')')+'</button>';
  if(weakCount>0||_flashCramMode)h+=' <button class="btn btn-sec" onclick="toggleFlashCramMode()">'+(_flashCramMode?'&#x1F501; Back to Normal Deck':'&#x1F9E0; Cram Weak Cards ('+weakCount+')')+'</button>';
  if(bmCount>0)h+=' <button class="btn btn-sec" onclick="printBookmarks()">&#x1F5A8; Print Bookmarked Cards</button>';
  h+=' <button class="btn btn-sec" onclick="exportFlashcardsCSV()">&#x2B07; Export Deck (Anki CSV)</button>';
  h+='</div>';
  h+='<div class="flashcard" id="flashcard-el" onclick="this.classList.toggle(\\'flipped\\');document.getElementById(\\'fc-grades\\').classList.remove(\\'hidden\\')"><div class="flashcard-inner"><div class="flashcard-face flashcard-front"><b>'+fc.front+'</b></div><div class="flashcard-face flashcard-back">'+fc.back+'</div></div></div>';
  h+='<div style="text-align:center;margin-top:0.6rem"><button class="btn btn-sec" onclick="event.stopPropagation();toggleBookmark('+_flashIdx+')">'+(isBm?'&#x2B50; Bookmarked (click to remove)':'&#x2606; Bookmark this card')+'</button></div>';
  h+='<div class="hidden" id="fc-grades" style="display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap;margin-top:1rem">';
  h+='<button class="btn" style="background:var(--fail)" onclick="srGrade(0)">&#x1F614; Again</button>';
  h+='<button class="btn" style="background:var(--warn);color:#000" onclick="srGrade(1)">&#x1F615; Hard</button>';
  h+='<button class="btn" style="background:var(--ok)" onclick="srGrade(2)">&#x1F642; Good</button>';
  h+='<button class="btn" style="background:var(--accent)" onclick="srGrade(3)">&#x1F60E; Easy</button>';
  h+='</div>';
  if(_lastGrade)h+='<div style="text-align:center;margin-top:0.6rem"><button class="btn btn-sec" onclick="undoLastGrade()">&#x21A9; Undo Last Grade</button></div>';
  document.getElementById('flash-content').innerHTML=h;
  show('v-flash');
}}
let _lastGrade=null;
function srGrade(grade){{
  const idx=_flashIdx;if(idx===null)return;
  const c=srCard(idx);const day=86400000;
  _lastGrade={{idx:idx,prev:Object.assign({{}},c),wasMissed:!!(S.flashMissed&&S.flashMissed[idx]),reviewed:S.flashReviewed,xp:S.xp}};
  if(!S.flashMissed)S.flashMissed={{}};
  if(grade===0){{c.reps=0;c.ivl=0;c.ef=Math.max(1.3,c.ef-0.2);c.due=Date.now()+5*60000;S.flashMissed[idx]=true;}}
  else if(grade===1){{c.ivl=c.reps>0?Math.max(1,Math.round(c.ivl*1.2)):1;c.ef=Math.max(1.3,c.ef-0.15);c.reps++;c.due=Date.now()+c.ivl*day;}}
  else if(grade===2){{c.reps++;c.ivl=c.reps===1?1:(c.reps===2?6:Math.round(c.ivl*c.ef));c.due=Date.now()+c.ivl*day;delete S.flashMissed[idx];}}
  else{{c.reps++;c.ivl=c.reps===1?4:Math.round(c.ivl*c.ef*1.3);c.ef+=0.15;c.due=Date.now()+c.ivl*day;delete S.flashMissed[idx];}}
  S.flashReviewed++;if(S.flashReviewed>=50)checkAch('flash_50');addXP(XP_TABLE.flashcard);persist();
  renderFlash();
}}
function undoLastGrade(){{
  if(!_lastGrade)return;
  const g=_lastGrade;
  S.srCards[g.idx]=g.prev;
  if(!S.flashMissed)S.flashMissed={{}};
  if(g.wasMissed)S.flashMissed[g.idx]=true;else delete S.flashMissed[g.idx];
  S.flashReviewed=g.reviewed;
  S.xp=g.xp;
  _lastGrade=null;
  _flashIdx=g.idx;
  persist();
  renderFlash(true);
}}
function renderGloss(){{
  let starCt=(S.glossStars||[]).length;
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>Glossary ('+GLOSSARY.length+' terms)</h2><input type="search" id="gloss-search" placeholder="Search..." oninput="filterGloss()"><button class="btn btn-sec" style="margin-top:0.5rem" onclick="printGlossary()">&#x1F5A8; Print / Save as PDF</button> ';
  h+='<button class="btn btn-sec" onclick="toggleGlossStarFilter()">'+(_glossStarOnly?'&#x1F501; Show All':'&#x2B50; Starred Only ('+starCt+')')+'</button></div>';
  h+='<div class="card" id="gloss-list">';
  GLOSSARY.forEach(function(g,idx){{
    if(_glossStarOnly&&(S.glossStars||[]).indexOf(idx)<0)return;
    const starred=(S.glossStars||[]).indexOf(idx)>=0;
    h+='<div class="gloss-item"><b>'+g.term+'</b> &mdash; '+g.def+' <span style="cursor:pointer" onclick="toggleGlossStar('+idx+')">'+(starred?'&#x2B50;':'&#x2606;')+'</span></div>';
  }});
  h+='</div>';
  document.getElementById('gloss-content').innerHTML=h;
  show('v-gloss');
}}
let _glossStarOnly=false;
function toggleGlossStarFilter(){{_glossStarOnly=!_glossStarOnly;renderGloss();}}
function toggleGlossStar(idx){{
  if(!S.glossStars)S.glossStars=[];
  const i=S.glossStars.indexOf(idx);
  if(i>=0)S.glossStars.splice(i,1);else S.glossStars.push(idx);
  if((S.glossStars.length+(S.refStars||[]).length)>=5&&typeof checkAch==='function')checkAch('curator');
  persist();
  renderGloss();
}}
function filterGloss(){{
  const q=document.getElementById('gloss-search').value.toLowerCase();
  const items=document.querySelectorAll('.gloss-item');
  items.forEach(el=>{{el.style.display=el.textContent.toLowerCase().includes(q)?'':'none'}});
}}
function achProgress(id){{
  const genMods=TRACKS.find(t=>t.id==='general').modules;
  const afMods=TRACKS.find(t=>t.id==='airframe').modules;
  const ppMods=TRACKS.find(t=>t.id==='powerplant').modules;
  switch(id){{
    case 'first_lesson': return {{cur:Math.min(S.done.length,1),tgt:1,label:'lessons completed'}};
    case 'all_general': return {{cur:genMods.filter(m=>S.done.includes(m)).length,tgt:genMods.length,label:'General modules done'}};
    case 'all_airframe': return {{cur:afMods.filter(m=>S.done.includes(m)).length,tgt:afMods.length,label:'Airframe modules done'}};
    case 'all_powerplant': return {{cur:ppMods.filter(m=>S.done.includes(m)).length,tgt:ppMods.length,label:'Powerplant modules done'}};
    case 'full_ap': return {{cur:S.done.length,tgt:MODS.length,label:'total modules done'}};
    case 'streak_7': return {{cur:Math.min(S.streak,7),tgt:7,label:'day streak'}};
    case 'flash_50': return {{cur:Math.min(S.flashReviewed,50),tgt:50,label:'flashcards reviewed'}};
    case 'sim_explorer': return {{cur:Math.min((S.simsUsed||[]).length,10),tgt:10,label:'simulators tried'}};
    case 'documentarian': {{
      const req=['glossary','studyguide','notes'];
      const have=S.exportsUsed||[];
      const cur=req.filter(r=>have.includes(r)).length;
      return {{cur,tgt:3,label:'exports used'}};
    }}
    case 'triple_crown': {{
      const doneCt=[genMods,afMods,ppMods].filter(mods=>mods.every(mid=>S.done.includes(mid))).length;
      return {{cur:doneCt,tgt:3,label:'tracks fully completed'}};
    }}
    case 'subject_master': {{
      const req=['general','airframe','powerplant'];
      const have=S.subjectPassed||{{}};
      const cur=req.filter(id=>have[id]).length;
      return {{cur,tgt:3,label:'subject tests passed'}};
    }}
    case 'oral_ready': return {{cur:Math.min(S.oralBest||0,80),tgt:80,label:'% best mock oral score'}};
    case 'practical_task_veteran': return {{cur:Math.min(Object.keys(S.practicalLog||{{}}).length,15),tgt:15,label:'practical tasks logged'}};
    case 'exam_ready': return {{cur:Math.min(readinessScore().total,90),tgt:90,label:'% overall exam readiness'}};
    case 'challenge_streak': return {{cur:Math.min(S.challengeStreak||0,7),tgt:7,label:'day Daily Challenge streak'}};
    case 'focus_5': return {{cur:Math.min(S.focusSessions||0,5),tgt:5,label:'Focus Timer sessions completed'}};
    case 'curator': return {{cur:Math.min(((S.refStars||[]).length+(S.glossStars||[]).length),5),tgt:5,label:'items starred'}};
    default: return null;
  }}
}}
function almostThereCard(){{
  const locked=ACHIEVEMENTS.filter(a=>!S.achievements.includes(a.id));
  const withProg=locked.map(a=>{{const p=achProgress(a.id);return p?{{a,p,pct:p.tgt?p.cur/p.tgt*100:0}}:null;}}).filter(Boolean).filter(x=>x.pct>0&&x.pct<100);
  if(!withProg.length)return '';
  withProg.sort((x,y)=>y.pct-x.pct);
  const top=withProg.slice(0,2);
  let h='<div class="card"><h3>&#x1F3C5; Almost There</h3>';
  top.forEach(x=>{{
    h+='<div style="margin-bottom:0.5rem"><div style="display:flex;justify-content:space-between;font-size:0.85rem"><span>'+x.a.icon+' '+esc(x.a.name)+'</span><span style="color:var(--txt2)">'+x.p.cur+'/'+x.p.tgt+' '+x.p.label+'</span></div>';
    h+='<div class="progress-bar"><div class="progress-fill" style="width:'+Math.round(x.pct)+'%"></div></div></div>';
  }});
  h+='</div>';
  return h;
}}
function startFocusTimer(){{
  window._focusEndsAt=Date.now()+25*60000;
  if(window._focusTimerHandle)clearInterval(window._focusTimerHandle);
  window._focusTimerHandle=setInterval(focusTimerTick,1000);
  renderDash();
}}
function cancelFocusTimer(){{
  window._focusEndsAt=null;
  if(window._focusTimerHandle)clearInterval(window._focusTimerHandle);
  renderDash();
}}
function focusTimerTick(){{
  const el=document.getElementById('focus-timer');
  if(!el){{clearInterval(window._focusTimerHandle);return;}}
  const remain=Math.max(0,Math.round((window._focusEndsAt-Date.now())/1000));
  const mm=Math.floor(remain/60),ss=remain%60;
  el.textContent=mm+':'+(ss<10?'0':'')+ss;
  if(remain<=0){{clearInterval(window._focusTimerHandle);finishFocusSession();}}
}}
function finishFocusSession(){{
  window._focusEndsAt=null;
  S.focusSessions=(S.focusSessions||0)+1;
  addXP(XP_TABLE.focus_session);
  if(S.focusSessions>=5)checkAch('focus_5');
  persist();
  renderDash();
}}
function focusTimerCard(){{
  const sessions=S.focusSessions||0;
  let h='<div class="card"><h3>&#x23F1; Focus Timer</h3><p style="color:var(--txt2);font-size:0.85rem">Distraction-free 25-minute study sessions, Pomodoro-style. Sessions completed: <b>'+sessions+'</b></p>';
  if(window._focusEndsAt){{
    h+='<p style="text-align:center;font-size:1.5rem"><b id="focus-timer">25:00</b></p>';
    h+='<div style="text-align:center"><button class="btn btn-sec" onclick="cancelFocusTimer()">Cancel Session</button></div>';
  }}else{{
    h+='<div style="text-align:center"><button class="btn" onclick="startFocusTimer()">&#x25B6; Start 25-min Focus Session</button></div>';
  }}
  h+='</div>';
  return h;
}}
const SUBTEST_MINUTES={{general:120,airframe:180,powerplant:180}};
const SUBTEST_TARGET_LEN={{general:60,airframe:100,powerplant:100}};
function renderSubTests(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x23F1; Subject Practice Tests</h2><p style="color:var(--txt2)">Timed practice tests modeled on the FAA Airman Knowledge Test format &mdash; one per subject (General / Airframe / Powerplant), 70%+ to pass. Complete every module in a subject to unlock its test.</p></div>';
  for(const t of TRACKS){{
    const mods=t.modules;
    const doneCt=mods.filter(mid=>S.done.includes(mid)).length;
    const unlocked=doneCt>=mods.length;
    const passed=(S.subjectPassed||{{}})[t.id];
    const qLen=Math.min(SUBTEST_TARGET_LEN[t.id]||mods.length,mods.reduce((a,mid)=>{{const m=MODS.find(x=>x.id===mid);return a+(m?m.quiz.length:0)}},0));
    h+='<div class="card"><h3 style="color:'+t.color+'">'+t.name+' Test</h3><p>'+qLen+' questions &middot; '+(SUBTEST_MINUTES[t.id]||30)+' min &middot; Progress: '+doneCt+'/'+mods.length+' modules</p>';
    if(passed)h+='<p style="color:var(--ok)">&#x2705; Passed ('+passed+'%)</p>';
    if(unlocked){{h+='<button class="btn" onclick="startSubTest(\\''+t.id+'\\')">'+(passed?'Retake Test':'Start Test')+'</button>';}}
    if(passed)h+=' <button class="btn btn-sec" onclick="renderSubjectCert(\\''+t.id+'\\')">&#x1F4DC; View Certificate</button>';
    else{{h+='<p style="color:var(--warn)">Complete all '+t.name+' modules to unlock.</p>';}}
    if(unlocked){{
      h+='<p style="color:var(--txt2);font-size:0.85rem;margin-top:0.5rem">Or focus on one module:</p><div style="display:flex;flex-wrap:wrap;gap:0.4rem">';
      mods.forEach(mid=>{{
        const m=MODS.find(x=>x.id===mid);if(!m)return;
        h+='<button class="btn btn-sec" style="font-size:0.8rem" onclick="startSubTest(&quot;'+t.id+'&quot;,&quot;'+m.id+'&quot;)">'+m.title+'</button>';
      }});
      h+='</div>';
    }}
    h+='</div>';
  }}
  document.getElementById('subtest-content').innerHTML=h;
  show('v-subtest');
}}
function startSubTest(trackId,focusModId){{
  const t=TRACKS.find(x=>x.id===trackId);if(!t)return;
  window._subFocusMod=focusModId||null;
  let questions,minutes;
  if(focusModId){{
    const fm=MODS.find(x=>x.id===focusModId);
    questions=fm?fm.quiz.map((q,idx)=>({{...q,mod:fm.title,modId:fm.id,qIdx:idx}})):[];
    for(let i=questions.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[questions[i],questions[j]]=[questions[j],questions[i]];}}
    minutes=Math.max(10,questions.length*2);
  }}else{{
    const target=SUBTEST_TARGET_LEN[trackId]||t.modules.length;
    const guaranteed=[];const rest=[];
    for(const mid of t.modules){{
      const m=MODS.find(x=>x.id===mid);if(!m)continue;
      const pool=[...m.quiz];
      if(!pool.length)continue;
      const gi=Math.floor(Math.random()*pool.length);
      guaranteed.push({{...pool[gi],mod:m.title,modId:m.id,qIdx:gi}});
      pool.forEach((q,idx)=>{{if(idx!==gi)rest.push({{...q,mod:m.title,modId:m.id,qIdx:idx}})}});
    }}
    for(let i=rest.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[rest[i],rest[j]]=[rest[j],rest[i]];}}
    const need=Math.max(0,target-guaranteed.length);
    questions=[...guaranteed,...rest.slice(0,need)];
    for(let i=questions.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[questions[i],questions[j]]=[questions[j],questions[i]];}}
    minutes=SUBTEST_MINUTES[trackId]||30;
  }}
  window._subTrack=trackId;window._subAnswers={{}};window._subTotal=questions.length;window._subQuestions=questions;
  window._subEndsAt=Date.now()+minutes*60000;
  const focusLabel=focusModId?(MODS.find(x=>x.id===focusModId)||{{}}).title:null;
  let h='<div class="card"><h2>'+t.name+' Test'+(focusLabel?' &mdash; Focus: '+focusLabel:'')+' ('+questions.length+' questions)</h2><p>Score 70%+ to pass. Time remaining: <b id="subtest-timer">'+minutes+':00</b></p></div>';
  questions.forEach((q,i)=>{{
    h+='<div class="card" id="sq'+i+'"><p style="font-size:0.8rem;color:var(--txt2)">'+q.mod+'</p><p><b>'+(i+1)+'. '+q.q+'</b></p>';
    q.choices.forEach((c,ci)=>{{
      h+='<button class="quiz-opt" data-ci="'+ci+'" onclick="subTestAnswer('+i+','+ci+','+q.answer+',\\''+q.modId+'\\','+q.qIdx+')">'+c+'</button>';
    }});
    h+='<div class="explain" id="sqex'+i+'">'+q.explain+'</div></div>';
  }});
  h+='<div id="subtest-result"></div>';
  document.getElementById('subtest-content').innerHTML=h;
  if(window._subTimerHandle)clearInterval(window._subTimerHandle);
  window._subTimerHandle=setInterval(subTestTick,1000);
  subTestTick();
  show('v-subtest');
}}
function subTestTick(){{
  const el=document.getElementById('subtest-timer');
  if(!el){{clearInterval(window._subTimerHandle);return;}}
  const remain=Math.max(0,Math.round((window._subEndsAt-Date.now())/1000));
  const mm=Math.floor(remain/60),ss=remain%60;
  el.textContent=mm+':'+(ss<10?'0':'')+ss;
  if(remain<=0){{clearInterval(window._subTimerHandle);finishSubTest(true);}}
}}
function subTestAnswer(qi,ci,correct,modId,modQIdx){{
  if(window._subAnswers[qi]!==undefined)return;
  window._subAnswers[qi]=ci===correct?1:0;
  const opts=document.querySelectorAll('#sq'+qi+' .quiz-opt');
  if(opts[ci])opts[ci].classList.add(ci===correct?'correct':'wrong');
  if(ci!==correct&&opts[correct])opts[correct].classList.add('correct');
  document.getElementById('sqex'+qi).style.display='block';
  if(modId!==undefined&&modQIdx!==undefined)trackMissed(modId,parseInt(modQIdx),ci===correct);
  if(Object.keys(window._subAnswers).length===window._subTotal)finishSubTest(false);
}}
function finishSubTest(timedOut){{
  if(window._subTimerHandle)clearInterval(window._subTimerHandle);
  const total=window._subTotal;
  const score=Object.values(window._subAnswers).reduce((a,b)=>a+b,0);
  const pct=total?Math.round(score/total*100):0;
  const t=TRACKS.find(x=>x.id===window._subTrack);
  const isFocus=!!window._subFocusMod;
  logScoreHistory(t.name+(isFocus?' Focus Practice':' Subject Test'),pct);
  if(!S.subjectPassed)S.subjectPassed={{}};
  let msg='<div class="card"><h2>'+(timedOut?'&#x23F0; Time is up! ':'')+'Result: '+score+'/'+total+' ('+pct+'%)</h2>';
  if(isFocus){{
    msg+='<p style="color:var(--txt2)">Focus practice on a single module &mdash; this does not count toward passing the full '+t.name+' Subject Test.</p>';
    msg+=pct>=70?'<p style="color:var(--ok);font-size:1.2rem">&#x2705; Nice work on this module!</p>':'<p style="color:var(--fail)">Below 70% on this module &mdash; keep reviewing.</p>';
  }}else if(pct>=70){{
    msg+='<p style="color:var(--ok);font-size:1.2rem">&#x2705; PASSED</p>';
    S.subjectPassed[t.id]=pct;
    addXP(XP_TABLE.exam_pass);
    if(['general','airframe','powerplant'].every(id=>(S.subjectPassed||{{}})[id]))checkAch('subject_master');
    persist();
  }}else{{
    msg+='<p style="color:var(--fail)">Below 70%. Review the '+t.name+' modules and retake when ready.</p>';
  }}
  const byMod={{}};
  window._subQuestions.forEach(function(q,i){{
    const ok=window._subAnswers[i]===1;
    if(!byMod[q.modId])byMod[q.modId]={{title:q.mod,correct:0,total:0}};
    byMod[q.modId].total++;
    if(ok)byMod[q.modId].correct++;
  }});
  const areaRows=Object.values(byMod).map(function(r){{r.pct=Math.round(r.correct/r.total*100);return r;}}).sort((a,b)=>a.pct-b.pct);
  const weakAreas=areaRows.filter(r=>r.pct<70);
  msg+='<div class="card"><h3>Score by Subject Area</h3><p style="color:var(--txt2);font-size:0.85rem">Weakest topics first, just like the FAA test report &mdash; focus remaining study time here.</p>'+areaRows.map(function(r){{
    const c=r.pct>=85?'var(--ok)':(r.pct>=70?'var(--warn)':'var(--fail)');
    return '<div style="margin:0.6rem 0"><div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>'+r.title+'</span><span style="color:'+c+';font-weight:600">'+r.correct+'/'+r.total+' ('+r.pct+'%)</span></div><div class="progress-bar"><div class="progress-fill" style="width:'+r.pct+'%;background:'+c+'"></div></div></div>';
  }}).join('')+(weakAreas.length?'<p style="margin-top:0.8rem;color:var(--fail)">&#x26A0; '+weakAreas.length+' area'+(weakAreas.length>1?'s':'')+' below 70% &mdash; these are your highest-value study targets before the real exam.</p><button class="btn" onclick="startCramQuiz()">&#x1F525; Cram These Weak Areas</button>':'<p style="margin-top:0.8rem;color:var(--ok)">&#x2705; Every subject area scored 70%+.</p>')+'</div>';
  window._subLastReport={{trackName:t.name,date:new Date().toLocaleDateString(),score:score,total:total,pct:pct,areaRows:areaRows}};
  msg+='<div style="text-align:center;margin-top:0.6rem"><button class="btn btn-sec" onclick="printSubTestReport()">&#x1F5A8; Print Score Report</button></div>';
  msg+='<button class="btn btn-sec" onclick="renderSubTests()">Back to Subject Tests</button></div>';
  document.getElementById('subtest-result').innerHTML=msg;
}}
function renderOral(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x1F3A4; Mock Oral Exam</h2><p style="color:var(--txt2)">Rapid-fire open-response prompts styled after what a Designated Mechanic Examiner (DME) actually asks. There\\'s no multiple choice here &mdash; say your answer out loud, then reveal and self-grade honestly. This drills the skill the Written test can\\'t: explaining your reasoning.</p>';
  h+='<button class="btn" onclick="startOral()">Start Mock Oral ('+ORAL_QUESTIONS.length+' prompts)</button>';
  const oralCats=[...new Set(ORAL_QUESTIONS.map(q=>q.cat||'General'))];
  h+='<div style="margin-top:0.8rem"><p style="color:var(--txt2);font-size:0.85rem;margin-bottom:0.4rem">Or focus on one topic area:</p>';
  h+=oralCats.map(cat=>{{const n=ORAL_QUESTIONS.filter(q=>(q.cat||'General')===cat).length;return '<button class="btn btn-sec" style="margin:0.2rem" onclick="startOral(&quot;'+cat+'&quot;)">'+cat+' ('+n+')</button>';}}).join('');
  h+='</div><button class="btn btn-sec" style="margin-top:0.6rem" onclick="printOralBank()">&#x1F5A8; Print Oral Study Sheet</button></div>';
  document.getElementById('oral-content').innerHTML=h;
  show('v-oral');
}}
function startOral(cat){{
  let qs=cat?ORAL_QUESTIONS.filter(q=>(q.cat||'General')===cat):[...ORAL_QUESTIONS];
  qs=[...qs];
  for(let i=qs.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[qs[i],qs[j]]=[qs[j],qs[i]];}}
  window._oralQs=qs;window._oralIdx=0;window._oralGood=0;window._oralBad=0;window._oralResults=[];
  renderOralPrompt();
  show('v-oral');
}}
function renderOralPrompt(){{
  const qs=window._oralQs;const i=window._oralIdx;
  if(i>=qs.length){{finishOral();return;}}
  const q=qs[i];
  let h='<div class="card"><p style="color:var(--txt2)">Prompt '+(i+1)+' of '+qs.length+'</p><h3>'+q.prompt+'</h3>';
  h+='<div id="oral-answer" style="display:none;margin-top:1rem;padding:0.8rem;background:var(--bg3);border-radius:8px"><b>Model answer:</b> '+q.answer+'</div>';
  h+='<div style="margin-top:1rem" id="oral-actions">';
  h+='<button class="btn btn-sec" onclick="revealOral()">&#x1F441; Reveal Answer</button>';
  h+='</div>';
  h+='<div style="margin-top:1rem;display:none" id="oral-rate">';
  h+='<button class="btn" onclick="rateOral(true)">&#x2705; I nailed it</button> ';
  h+='<button class="btn btn-sec" onclick="rateOral(false)">&#x274C; Need review</button>';
  h+='</div></div>';
  document.getElementById('oral-content').innerHTML=h;
}}
function revealOral(){{
  document.getElementById('oral-answer').style.display='block';
  document.getElementById('oral-rate').style.display='block';
}}
function rateOral(good){{
  if(good)window._oralGood++;else window._oralBad++;
  const q=window._oralQs[window._oralIdx];
  window._oralResults.push({{cat:q.cat||'General',good:good}});
  window._oralIdx++;
  renderOralPrompt();
}}
function finishOral(){{
  const total=window._oralGood+window._oralBad;
  const pct=total?Math.round(window._oralGood/total*100):0;
  logScoreHistory('Mock Oral',pct);
  if(!S.oralBest||pct>S.oralBest)S.oralBest=pct;
  addXP(XP_TABLE.quiz_pass);
  if(pct>=80)checkAch('oral_ready');
  persist();
  let h='<div class="card"><h2>Mock Oral Complete</h2><p style="font-size:1.2rem">Self-graded: '+window._oralGood+'/'+total+' ('+pct+'%)</p>';
  if(pct>=80){{h+='<p style="color:var(--ok)">&#x2705; Strong oral readiness. Keep this up close to your exam date.</p>';}}
  else{{h+='<p style="color:var(--warn)">Review the Oral & Practical reference cards for the topics you flagged, then try again.</p>';}}
  const byCat={{}};
  (window._oralResults||[]).forEach(function(r){{
    if(!byCat[r.cat])byCat[r.cat]={{good:0,total:0}};
    byCat[r.cat].total++;
    if(r.good)byCat[r.cat].good++;
  }});
  const catRows=Object.keys(byCat).map(function(k){{return {{cat:k,good:byCat[k].good,total:byCat[k].total,pct:Math.round(byCat[k].good/byCat[k].total*100)}};}}).sort((a,b)=>a.pct-b.pct);
  if(catRows.length){{
    h+='<div class="card"><h3>Score by Topic Area</h3>'+catRows.map(function(r){{
      const cc=r.pct>=80?'var(--ok)':(r.pct>=50?'var(--warn)':'var(--fail)');
      return '<div style="margin:0.5rem 0"><div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>'+r.cat+'</span><span style="color:'+cc+';font-weight:600">'+r.good+'/'+r.total+' ('+r.pct+'%)</span></div><div class="progress-bar"><div class="progress-fill" style="width:'+r.pct+'%;background:'+cc+'"></div></div></div>';
    }}).join('')+'</div>';
  }}
  h+='<button class="btn" onclick="startOral()">&#x1F504; New Round</button> <button class="btn btn-sec" onclick="renderOral()">Back</button></div>';
  document.getElementById('oral-content').innerHTML=h;
}}
function renderPractical(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  const ptTotal=PRACTICAL_TASKS.length;
  const ptDone=PRACTICAL_TASKS.filter(t=>S.practicalLog[t.id]).length;
  const ptPct=ptTotal?Math.round(ptDone/ptTotal*100):0;
  h+='<div class="card"><h2>&#x1F527; Practical Task Log</h2><p>Log completion of these ACS-style hands-on tasks as you go, mirroring a real training/experience record. This is a personal log for your own tracking &mdash; it is not an official FAA logbook or endorsement.</p>';
  h+='<p style="color:var(--txt2)">Overall progress: '+ptDone+'/'+ptTotal+' tasks logged ('+ptPct+'%)</p>';
  h+='<div class="progress-bar"><div class="progress-fill" style="width:'+ptPct+'%"></div></div>';
  h+='<button class="btn btn-sec" style="margin-top:0.5rem" onclick="printPracticalLog()">&#x1F5A8; Print / Export Log</button></div>';
  const cats=['General','Airframe','Powerplant'];
  cats.forEach(cat=>{{
    const items=PRACTICAL_TASKS.filter(t=>t.cat===cat);
    h+='<div class="card"><h3>'+cat+'</h3>';
    items.forEach(t=>{{
      const log=S.practicalLog[t.id];
      h+='<div style="border-top:1px solid var(--bg3);padding:0.7rem 0">';
      h+='<div style="display:flex;justify-content:space-between;gap:0.5rem;flex-wrap:wrap"><div><strong>'+t.title+'</strong><br><span style="color:var(--txt2);font-size:0.9rem">'+t.desc+'</span></div>';
      if(log){{h+='<span style="color:var(--ok);white-space:nowrap">&#x2705; Logged '+log.date+'</span>';}}
      else{{h+='<span style="color:var(--txt2);white-space:nowrap">Not logged</span>';}}
      h+='</div>';
      h+='<div style="margin-top:0.5rem;display:flex;gap:0.5rem;flex-wrap:wrap;align-items:center">';
      h+='<input type="date" id="pt-date-'+t.id+'" value="'+(log?log.date:'')+'" style="background:var(--bg);color:var(--txt);border:1px solid var(--bg3);border-radius:6px;padding:0.3rem">';
      h+='<input type="text" id="pt-notes-'+t.id+'" placeholder="Notes (optional)" value="'+esc(log&&log.notes?log.notes:'')+'" style="flex:1;min-width:150px;background:var(--bg);color:var(--txt);border:1px solid var(--bg3);border-radius:6px;padding:0.3rem">';
      h+='<button class="btn" style="padding:0.3rem 0.7rem" onclick="practicalSave(\\''+t.id+'\\')">Save</button>';
      if(log){{h+=' <button class="btn btn-sec" style="padding:0.3rem 0.7rem" onclick="practicalClear(\\''+t.id+'\\')">Clear</button>';}}
      h+='</div></div>';
    }});
    h+='</div>';
  }});
  document.getElementById('practical-content').innerHTML=h;
  show('v-practical');
}}
function practicalSave(id){{
  const dEl=document.getElementById('pt-date-'+id);
  const nEl=document.getElementById('pt-notes-'+id);
  const d=(dEl&&dEl.value)||new Date().toISOString().slice(0,10);
  const n=(nEl&&nEl.value)||'';
  const isNew=!S.practicalLog[id];
  S.practicalLog[id]={{date:d,notes:n}};
  if(isNew)addXP(XP_TABLE.practical_task);
  persist();
  if(typeof logActivity==='function'&&typeof ACCT!=='undefined'&&ACCT.current)logActivity('practical',ACCT.current,id,ACCT.current);
  if(Object.keys(S.practicalLog).length>=15)checkAch('practical_task_veteran');
  renderPractical();
}}
function practicalClear(id){{
  delete S.practicalLog[id];
  persist();
  renderPractical();
}}
function renderAch(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  const next=ACHIEVEMENTS.find(a=>!S.achievements.includes(a.id)&&achProgress(a.id));
  if(next){{
    const p=achProgress(next.id);const pct=Math.round(p.cur/p.tgt*100);
    h+='<div class="card"><h3>'+next.icon+' Next up: '+next.name+'</h3><p style="color:var(--txt2)">'+next.desc+'</p>';
    h+='<div class="progress-bar"><div class="progress-fill" style="width:'+pct+'%"></div></div>';
    h+='<p style="font-size:0.85rem;text-align:center">'+p.cur+' / '+p.tgt+' '+p.label+'</p></div>';
  }}
  const earnedCt=ACHIEVEMENTS.filter(a=>S.achievements.includes(a.id)).length;
  const earnedPct=ACHIEVEMENTS.length?Math.round(earnedCt/ACHIEVEMENTS.length*100):0;
  h+='<div class="card"><h2>&#x1F3C6; Achievements</h2><p style="color:var(--txt2)">'+earnedCt+' / '+ACHIEVEMENTS.length+' unlocked ('+earnedPct+'%)</p>';
  h+='<div class="progress-bar"><div class="progress-fill" style="width:'+earnedPct+'%"></div></div>';
  h+='<button class="btn btn-sec" style="margin-top:0.5rem" onclick="printAchievements()">&#x1F5A8; Print / Save as PDF</button></div><div class="card">';
  for(const a of ACHIEVEMENTS){{
    const earned=S.achievements.includes(a.id);
    const earnedDate=(S.achDates&&S.achDates[a.id])?new Date(S.achDates[a.id]).toLocaleDateString():null;
    h+='<div class="badge'+(earned?' earned':'')+'" title="'+a.desc.replace(/"/g,'&quot;')+'">'+a.icon+' '+a.name+(earned?' &#x2705;':' &#x1F512;')+'<div style="font-size:0.7rem;color:var(--txt2);margin-top:0.2rem">'+a.desc+(earnedDate?'<br>Unlocked '+earnedDate:'')+'</div></div>';
  }}
  h+='</div>';
  document.getElementById('ach-content').innerHTML=h;
  show('v-ach');
}}
function renderExam(){{
  if(S.done.length<MODS.length){{
    let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
    h+='<div class="card"><h2>&#x1F4D1; Final Exam</h2><p style="color:var(--warn)">Complete all '+MODS.length+' modules to unlock the Final Exam.</p><p>Progress: '+S.done.length+'/'+MODS.length+'</p></div>';
    document.getElementById('exam-content').innerHTML=h;
    show('v-exam');return;
  }}
  // Build exam: 1 random question per module, guaranteeing full-course coverage
  // while keeping the exam a reasonable length as the course has grown.
  const questions=[];
  for(const m of MODS){{const pool=[...m.quiz];if(pool.length){{const idx=Math.floor(Math.random()*pool.length);questions.push({{...pool[idx],mod:m.title,modId:m.id,qIdx:idx}})}}}}
  for(let i=questions.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[questions[i],questions[j]]=[questions[j],questions[i]];}}
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x1F4D1; Final Exam ('+questions.length+' questions)</h2><p>Score 80%+ to pass and earn your certificate.</p></div>';
  questions.forEach((q,i)=>{{
    h+='<div class="card" id="eq'+i+'"><p style="font-size:0.8rem;color:var(--txt2)">'+q.mod+'</p><p><b>'+(i+1)+'. '+q.q+'</b></p>';
    q.choices.forEach((c,ci)=>{{
      h+='<button class="quiz-opt" data-ci="'+ci+'" onclick="examAnswer('+i+','+ci+','+q.answer+','+questions.length+',\\''+q.modId+'\\','+q.qIdx+')">'+c+'</button>';
    }});
    h+='<div class="explain" id="eex'+i+'">'+q.explain+'</div></div>';
  }});
  h+='<div id="exam-result"></div>';
  document.getElementById('exam-content').innerHTML=h;
  show('v-exam');
  window._examAnswers={{}};window._examTotal=questions.length;window._examQuestions=questions;
}}
function examAnswer(qi,ci,correct,total,modId,modQIdx){{
  if(window._examAnswers[qi]!==undefined)return;
  window._examAnswers[qi]=ci===correct?1:0;
  const opts=document.querySelectorAll('#eq'+qi+' .quiz-opt');
  if(opts[ci])opts[ci].classList.add(ci===correct?'correct':'wrong');
  if(ci!==correct&&opts[correct])opts[correct].classList.add('correct');
  document.getElementById('eex'+qi).style.display='block';
  if(modId!==undefined&&modQIdx!==undefined)trackMissed(modId,parseInt(modQIdx),ci===correct);
  if(Object.keys(window._examAnswers).length===total){{
    const score=Object.values(window._examAnswers).reduce((a,b)=>a+b,0);
    const pctE=Math.round(score/total*100);
    logScoreHistory('Final Exam',pctE);
    let msg='<div class="card"><h2>Exam Result: '+score+'/'+total+' ('+pctE+'%)</h2>';
    if(pctE>=80){{msg+='<p style="color:var(--ok);font-size:1.2rem">&#x2705; PASSED! You earned your certificate.</p>';S.examPassed=true;S.examScore=pctE;addXP(XP_TABLE.exam_pass);checkAch('exam_pass');persist()}}
    else{{msg+='<p style="color:var(--fail)">Below 80%. Review and retake.</p>'}}
    msg+='</div>';
    const byTrack={{}};
    (window._examQuestions||[]).forEach(function(q,qi2){{
      const trk=TRACKS.find(t=>t.modules.includes(q.modId));
      const key=trk?trk.id:'other';
      if(!byTrack[key])byTrack[key]={{id:trk?trk.id:'', title:trk?trk.name:'Other',correct:0,total:0}};
      byTrack[key].total++;
      if(window._examAnswers[qi2]===1)byTrack[key].correct++;
    }});
    const trackRows=Object.values(byTrack).map(function(r){{r.pct=r.total?Math.round(r.correct/r.total*100):0;return r;}}).sort((a,b)=>a.pct-b.pct);
    if(trackRows.length){{
      msg+='<div class="card"><h3>Score by Subject Area</h3>'+trackRows.map(function(r){{
        const c2=r.pct>=85?'var(--ok)':(r.pct>=70?'var(--warn)':'var(--fail)');
        let row='<div style="margin:0.6rem 0"><div style="display:flex;justify-content:space-between;font-size:0.9rem"><span>'+r.title+'</span><span style="color:'+c2+';font-weight:600">'+r.correct+'/'+r.total+' ('+r.pct+'%)</span></div><div class="progress-bar"><div class="progress-fill" style="width:'+r.pct+'%;background:'+c2+'"></div></div>';
        if(r.pct<70&&r.id){{row+='<button class="btn btn-sec" style="margin-top:0.4rem;font-size:0.8rem" onclick="show(\\'v-subtests\\');startSubTest(\\''+r.id+'\\')">&#x1F3AF; Practice '+r.title+'</button>';}}
        row+='</div>';
        return row;
      }}).join('')+'</div>';
    }}
    window._examLastReport={{date:new Date().toLocaleDateString(),score:score,total:total,pct:pctE,areaRows:trackRows}};
    msg+='<div style="text-align:center;margin-top:0.6rem"><button class="btn btn-sec" onclick="printExamReport()">&#x1F5A8; Print Exam Score Report</button></div>';
    document.getElementById('exam-result').innerHTML=msg;
  }}
}}
function renderCert(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  if(!S.examPassed){{h+='<div class="card"><p>Pass the Final Exam to earn your certificate.</p></div>';document.getElementById('cert-content').innerHTML=h;show('v-cert');return}}
  const refs=[...new Set(MODS.map(m=>m.faa_ref).filter(Boolean))].sort();
  h+='<div class="cert-box"><p style="font-size:0.9rem">AVIATION MAINTENANCE ACADEMY</p><h2>Certificate of Completion</h2><p style="margin:1rem 0;font-size:1.2rem">This certifies that the holder has completed<br>all '+MODS.length+' modules and passed the Final Examination<br>with a score of <b>'+S.examScore+'%</b></p>';
  h+='<p style="margin-top:1rem;font-size:0.8rem;color:var(--txt2)">Curriculum aligned to:<br>'+refs.map(r=>esc(r)).join('<br>')+'</p>';
  h+='<p style="margin-top:2rem;color:var(--txt2)">'+new Date().toLocaleDateString()+'</p>';
  h+='<p style="margin-top:1rem"><button class="btn" onclick="window.print()">&#x1F5A8; Print Certificate</button></p></div>';
  document.getElementById('cert-content').innerHTML=h;
  show('v-cert');
}}
function renderSubjectCert(trackId){{
  const t=TRACKS.find(x=>x.id===trackId);if(!t)return;
  const score=(S.subjectPassed||{{}})[trackId];
  if(!score){{return}}
  const refs=[...new Set(t.modules.map(mid=>{{const m=MODS.find(x=>x.id===mid);return m&&m.faa_ref}}).filter(Boolean))].sort();
  let h='<button class="btn btn-sec" onclick="renderSubTests()">&#x2190; Back to Subject Tests</button>';
  h+='<div class="cert-box"><p style="font-size:0.9rem">AVIATION MAINTENANCE ACADEMY</p><h2>Certificate of Subject Completion</h2><p style="margin:1rem 0;font-size:1.2rem">This certifies that the holder has completed<br>the <b>'+t.name+'</b> curriculum ('+t.modules.length+' modules)<br>and passed the '+t.name+' Subject Practice Test<br>with a score of <b>'+score+'%</b></p>';
  h+='<p style="margin-top:1rem;font-size:0.8rem;color:var(--txt2)">Curriculum aligned to:<br>'+refs.map(r=>esc(r)).join('<br>')+'</p>';
  h+='<p style="margin-top:2rem;color:var(--txt2)">'+new Date().toLocaleDateString()+'</p>';
  h+='<p style="margin-top:1rem"><button class="btn" onclick="window.print()">&#x1F5A8; Print Certificate</button></p></div>';
  document.getElementById('cert-content').innerHTML=h;
  show('v-cert');
}}
function allQuizFlat(){{
  const out=[];
  for(const m of MODS){{m.quiz.forEach((q,qi)=>{{out.push({{q:q.q,choices:q.choices,answer:q.answer,explain:q.explain,modId:m.id,modTitle:m.title,qi:qi}});}});}}
  return out;
}}
function dailyChallengeQ(){{
  const all=allQuizFlat();if(all.length===0)return null;
  const today=new Date().toDateString();
  let seed=0;for(let i=0;i<today.length;i++)seed+=today.charCodeAt(i);
  return all[seed%all.length];
}}
function challengeCard(){{
  const q=dailyChallengeQ();if(!q)return '';
  const today=new Date().toDateString();
  const done=S.challengeDate===today;
  let h='<div class="card" id="challenge-card"><h3>&#x1F3AF; Daily Challenge <span style="font-size:0.75rem;color:var(--txt2)">('+q.modTitle+')</span></h3>';
  if(S.challengeStreak>1)h+='<p style="font-size:0.8rem;color:var(--accent2)">&#x1F4C6; '+S.challengeStreak+'-day streak</p>';
  if(done){{
    const wasCorrect=S.lastChallenge&&S.lastChallenge.correct;
    h+='<p style="color:'+(wasCorrect?'var(--ok)':'var(--txt2)')+'">'+(wasCorrect?'&#x2705; Nailed it! ':'Answered. ')+'Come back tomorrow for a new question.</p>';
  }}else{{
    h+='<p><b>'+q.q+'</b></p>';
    q.choices.forEach((c,ci)=>{{h+='<button class="quiz-opt" onclick="challengeAnswer('+ci+','+q.answer+',\\''+q.modId+'\\','+q.qi+')">'+c+'</button>';}});
    h+='<div class="explain" id="challenge-explain">'+q.explain+'</div>';
  }}
  h+='</div>';
  return h;
}}
function challengeAnswer(ci,correct,modId,qi){{
  const today=new Date().toDateString();
  if(S.challengeDate===today)return;
  const yesterday=new Date();yesterday.setDate(yesterday.getDate()-1);
  S.challengeStreak=(S.challengeDate===yesterday.toDateString())?(S.challengeStreak||0)+1:1;
  S.challengeDate=today;
  S.lastChallenge={{ci:ci,correct:ci===correct}};
  if(ci===correct)addXP(XP_TABLE.quiz_pass);
  if(modId!==undefined&&qi!==undefined)trackMissed(modId,parseInt(qi),ci===correct);
  if(S.challengeStreak>=7)checkAch('challenge_streak');
  persist();
  const ex=document.getElementById('challenge-explain');if(ex)ex.style.display='block';
  setTimeout(renderDash,900);
}}
function renderRecent(){{
  if(!S.recentModules||S.recentModules.length===0)return '';
  let h='<div class="card"><h3>&#x1F553; Recently Viewed</h3>';
  S.recentModules.forEach(id=>{{
    const m=MODS.find(x=>x.id===id);if(!m)return;
    h+='<div style="cursor:pointer;padding:0.35rem 0;border-bottom:1px solid var(--bg3)" onclick="openModule(\\''+id+'\\')">'+m.icon+' '+m.title+'</div>';
  }});
  h+='</div>';
  return h;
}}
function notesOverviewCard(){{
  const noted=Object.keys(S.notes||{{}}).filter(id=>(S.notes[id]||'').trim().length>0);
  if(!noted.length)return '';
  let h='<div class="card"><h3>&#x1F4DD; My Notes ('+noted.length+')</h3>';
  noted.forEach(id=>{{
    const m=MODS.find(x=>x.id===id);if(!m)return;
    const preview=(S.notes[id]||'').trim().slice(0,80);
    h+='<div style="cursor:pointer;padding:0.35rem 0;border-bottom:1px solid var(--bg3)" onclick="openModule(\\''+id+'\\')"><b>'+m.title+'</b><br><span style="color:var(--txt2);font-size:0.8rem">'+esc(preview)+(preview.length>=80?'&hellip;':'')+'</span></div>';
  }});
  h+='<button class="btn btn-sec" style="margin-top:0.5rem" onclick="printNotes()">&#x1F5A8; Print All Notes</button></div>';
  return h;
}}
function termOfDay(){{
  if(!GLOSSARY||GLOSSARY.length===0)return null;
  const today=new Date().toDateString();
  let seed=0;for(let i=0;i<today.length;i++)seed+=today.charCodeAt(i);
  return GLOSSARY[seed%GLOSSARY.length];
}}
function termOfDayCard(){{
  const g=termOfDay();if(!g)return '';
  return '<div class="card"><h3>&#x1F4D6; Term of the Day</h3><p><b>'+g.term+'</b></p><p style="color:var(--txt2)">'+g.def+'</p></div>';
}}
function refCardOfDay(){{
  if(!REFERENCE||REFERENCE.length===0)return null;
  const today=new Date().toDateString();
  let seed=0;for(let i=0;i<today.length;i++)seed+=today.charCodeAt(i)*3;
  return REFERENCE[seed%REFERENCE.length];
}}
function refCardOfDayCard(){{
  const r=refCardOfDay();if(!r)return '';
  return '<div class="card"><h3>&#x1F4DA; Reference Card of the Day</h3><p><b>'+r.title+'</b> <span class="track-chip" style="background:var(--bg3);font-size:.7rem">'+r.cat+'</span></p><p style="color:var(--txt2)">'+r.body+'</p></div>';
}}
function flashOfDay(){{
  if(!FLASHCARDS||FLASHCARDS.length===0)return null;
  const today=new Date().toDateString();
  let seed=0;for(let i=0;i<today.length;i++)seed+=today.charCodeAt(i)*7;
  return FLASHCARDS[seed%FLASHCARDS.length];
}}
function flashOfDayCard(){{
  const f=flashOfDay();if(!f)return '';
  return '<div class="card"><h3>&#x1F3B4; Flashcard of the Day</h3><p><b>'+esc(f.front)+'</b></p><p style="color:var(--txt2)">'+esc(f.back)+'</p></div>';
}}
function trackComplete(t){{
  return t.modules.length>0&&t.modules.every(id=>S.done.includes(id));
}}
function weakestModule(){{
  const scored=Object.keys(S.quizScores).map(id=>({{id,score:S.quizScores[id]}})).filter(x=>x.score<90);
  if(scored.length===0)return null;
  scored.sort((a,b)=>a.score-b.score);
  const worst=scored[0];
  const m=MODS.find(x=>x.id===worst.id);
  if(!m)return null;
  return {{id:m.id,title:m.title,score:worst.score}};
}}

function renderStreakCal(){{
  if(!S.visitLog)S.visitLog=[];
  const days=[];
  for(let i=13;i>=0;i--){{
    const d=new Date();d.setDate(d.getDate()-i);
    days.push({{label:d.toDateString().slice(0,3),active:S.visitLog.includes(d.toDateString())}});
  }}
  let h='<div class="card"><h3 style="font-size:0.9rem;color:var(--txt2)">Last 14 Days</h3><div style="display:flex;gap:0.3rem;justify-content:center;flex-wrap:wrap;margin-top:0.5rem">';
  days.forEach(dy=>{{
    h+='<div style="width:1.6rem;height:1.6rem;border-radius:4px;display:flex;align-items:center;justify-content:center;font-size:0.6rem;background:'+(dy.active?'var(--ok)':'var(--bg3)')+';color:'+(dy.active?'#fff':'var(--txt2)')+'" title="'+dy.label+'">'+dy.label[0]+'</div>';
  }});
  h+='</div></div>';
  return h;
}}
let _pq=[];let _pqScore=0;
function startPracticeQuiz(){{
  _pqCram=false;
  _pqAnswered={{}};
  const all=[];
  MODS.forEach(m=>{{m.quiz.forEach((q,qi)=>{{all.push({{modId:m.id,modTitle:m.title,qi,q}});}});}});
  for(let i=all.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[all[i],all[j]]=[all[j],all[i]];}}
  _pq=all.slice(0,10);
  _pqScore=0;
  renderPracticeQuiz();
  show('v-practice');
}}
function startCramQuiz(){{
  _pqCram=true;
  _pqAnswered={{}};
  const scored=MODS.map(m=>({{m,score:S.quizScores[m.id]!==undefined?S.quizScores[m.id]:40}}));
  scored.sort((a,b)=>a.score-b.score);
  const weakMods=scored.slice(0,Math.min(15,scored.length)).map(x=>x.m);
  const all=[];
  weakMods.forEach(m=>{{m.quiz.forEach((q,qi)=>{{all.push({{modId:m.id,modTitle:m.title,qi,q}});}});}});
  for(let i=all.length-1;i>0;i--){{const j=Math.floor(Math.random()*(i+1));[all[i],all[j]]=[all[j],all[i]];}}
  _pq=all.slice(0,15);
  _pqScore=0;
  renderPracticeQuiz();
  show('v-practice');
}}
function renderPracticeQuiz(){{
  let h=_pqCram
    ?'<div class="card"><h2>&#x1F525; Cram Weak Areas</h2><p style="color:var(--txt2)">'+_pq.length+' questions weighted toward your lowest-scoring modules.</p></div>'
    :'<div class="card"><h2>&#x1F3B2; Random Practice Quiz</h2><p style="color:var(--txt2)">'+_pq.length+' random questions pulled from across every module.</p></div>';
  _pq.forEach((it,idx)=>{{
    h+='<div class="card" id="pq'+idx+'"><p style="color:var(--txt2);font-size:0.85rem">'+it.modTitle+'</p><p><b>'+(idx+1)+'. '+it.q.q+'</b></p>';
    it.q.choices.forEach((c,ci)=>{{
      h+='<button class="quiz-opt" onclick="answerPractice('+idx+','+ci+','+it.q.answer+',\\\'\'+it.modId+\'\\\','+it.qi+')">'+c+'</button>';
    }});
    h+='<div class="explain" id="pqex'+idx+'">'+it.q.explain+'</div></div>';
  }});
  h+='<div id="pq-result"></div>';
  document.getElementById('practice-content').innerHTML=h;
}}
let _pqAnswered={{}};
let _pqCram=false;
function answerPractice(idx,ci,correct,modId,qi){{
  if(_pqAnswered[idx]!==undefined)return;
  _pqAnswered[idx]=ci;
  const card=document.getElementById('pq'+idx);if(!card)return;
  const opts=card.querySelectorAll('.quiz-opt');
  if(opts[ci])opts[ci].classList.add(ci===correct?'correct':'wrong');
  if(ci!==correct&&opts[correct])opts[correct].classList.add('correct');
  const ex=document.getElementById('pqex'+idx);if(ex)ex.style.display='block';
  if(ci===correct)_pqScore++;
  if(modId!==undefined&&qi!==undefined)trackMissed(modId,parseInt(qi),ci===correct);
  if(Object.keys(_pqAnswered).length===_pq.length){{
    const pctScore=Math.round(_pqScore/_pq.length*100);
    logScoreHistory(_pqCram?'Cram Quiz':'Practice Quiz',pctScore);
    let msg='<div class="card"><h3>Practice Score: '+_pqScore+'/'+_pq.length+' ('+pctScore+'%)</h3>';
    if(pctScore>=70){{msg+='<p style="color:var(--ok)">Nice work!</p>';addXP(XP_TABLE.quiz_pass);}}
    else{{msg+='<p style="color:var(--warn)">Keep practicing across modules.</p>';}}
    msg+='<button class="btn btn-sec" onclick="startPracticeQuiz()">&#x1F504; New Random Quiz</button></div>';
    document.getElementById('pq-result').innerHTML=msg;
    _pqAnswered={{}};
  }}
}}
function renderMastery(){{
  let h='<button class="btn btn-sec" onclick="show(\\'v-dash\\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x1F4CA; Mastery Report</h2><p style="color:var(--txt2)">Average quiz score per track, based on completed module quizzes.</p><button class="btn btn-sec" onclick="printMasteryReport()">&#x1F5A8; Print Mastery Report</button></div>';
  let weakest=null;
  TRACKS.forEach(t=>{{
    const modIds=t.modules;
    const scores=modIds.map(id=>S.quizScores[id]).filter(s=>s!==undefined);
    const avg=scores.length?Math.round(scores.reduce((a,b)=>a+b,0)/scores.length):null;
    if(avg!==null&&(weakest===null||avg<weakest.avg))weakest={{t,avg}};
    h+='<div class="card"><h3 style="color:'+t.color+'">'+t.name+'</h3>';
    if(avg===null){{h+='<p style="color:var(--txt2)">No quizzes completed yet in this track.</p>';}}
    else{{
      h+='<div class="progress-bar"><div class="progress-fill" style="width:'+avg+'%;background:'+t.color+'"></div></div>';
      h+='<p style="text-align:center">'+avg+'% average across '+scores.length+'/'+modIds.length+' quizzed modules</p>';
      const modRows=modIds.map(id=>{{const m=MODS.find(x=>x.id===id);return {{m,score:S.quizScores[id]}};}}).filter(r=>r.m&&r.score!==undefined).sort((a,b)=>a.score-b.score);
      if(modRows.length){{
        h+='<details style="margin-top:0.5rem"><summary style="cursor:pointer;color:var(--txt2);font-size:0.85rem">Per-module breakdown (weakest first)</summary>';
        modRows.forEach(row=>{{
          const c2=row.score>=85?'var(--ok)':(row.score>=70?'var(--warn)':'var(--fail)');
          h+='<div style="display:flex;justify-content:space-between;align-items:center;margin:0.4rem 0;font-size:0.85rem"><span style="cursor:pointer" onclick="openModule(\\''+row.m.id+'\\')">'+row.m.title+'</span><span style="color:'+c2+';font-weight:600">'+row.score+'%</span></div>';
        }});
        h+='</details>';
      }}
    }}
    h+='</div>';
  }});
  if(weakest&&weakest.avg<90){{
    h+='<div class="card" style="border:1px solid var(--warn)"><h3>&#x1F3AF; Focus Area</h3><p style="color:var(--txt2)">Your lowest average is in <b style="color:'+weakest.t.color+'">'+weakest.t.name+'</b> ('+weakest.avg+'%). Revisit those module quizzes or try the Practice Quiz to sharpen this area.</p><button class="btn" onclick="startCramQuiz()">&#x1F525; Cram Weak Areas</button></div>';
  }}
  document.getElementById('mastery-content').innerHTML=h;
  show('v-mastery');
}}
function toggleTheme(){{const b=document.body;b.dataset.theme=b.dataset.theme==='light'?'dark':'light';localStorage.setItem('avia_theme',b.dataset.theme)}}
function resetProgress(){{if(confirm('Reset YOUR progress? (account stays)')){{localStorage.removeItem(acctKey());load();renderDash();show('v-dash')}}}}
function flashKeyHandler(e){{
  const v=document.getElementById('v-flash');
  if(!v||v.classList.contains('hidden'))return;
  const tag=(document.activeElement&&document.activeElement.tagName)||'';
  if(tag==='INPUT'||tag==='TEXTAREA')return;
  const card=document.getElementById('flashcard-el');
  if(e.code==='Space'){{
    e.preventDefault();
    if(card){{card.classList.toggle('flipped');const g=document.getElementById('fc-grades');if(g)g.classList.remove('hidden');}}
    return;
  }}
  if(['1','2','3','4'].includes(e.key)){{
    const grades=document.getElementById('fc-grades');
    if(grades&&!grades.classList.contains('hidden')){{srGrade(parseInt(e.key,10)-1);}}
  }}
}}
document.addEventListener('keydown',flashKeyHandler);
function boot(){{
  const theme=localStorage.getItem('avia_theme')||'dark';document.body.dataset.theme=theme;
  loadAccounts();
  const u=ACCT.users.find(x=>x.id===ACCT.current);
  if(u){{enterApp();}}else{{showGate();}}
}}
function enterApp(){{load();renderNavForRole();hideGate();renderDash();show('v-dash');}}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Aviation Maintenance Academy</title>
<style>{CSS}</style>
</head>
<body data-theme="dark">
<div id="gate"></div>
<div id="lmodal-host"></div>
<div id="toast-stack" style="position:fixed;top:1rem;right:1rem;z-index:9999;display:flex;flex-direction:column;gap:0.5rem;max-width:min(90vw,320px)" aria-live="polite"></div>
<a href="#main-content" class="sr-only-focusable">Skip to main content</a>
<header>
<h1>&#x2708;&#xFE0F; Aviation Maintenance Academy</h1>
<nav role="navigation" aria-label="Main navigation">
<button class="nav-btn active" onclick="show('v-dash');renderDash()">Dashboard</button>
<button class="nav-btn" onclick="renderSims()">Sims</button>
<button class="nav-btn" onclick="renderReference()">Reference</button>
<button class="nav-btn" onclick="renderSearch()" aria-label="Search">&#x1F50D;</button>
<button class="nav-btn" onclick="toggleTheme()" aria-label="Toggle dark/light theme">&#x1F317;</button>
<button class="nav-btn" onclick="renderFlash()">Flashcards</button>
<button class="nav-btn" onclick="renderGloss()">Glossary</button>
<button class="nav-btn" onclick="renderAch()">Achievements</button>
<button class="nav-btn" onclick="renderExam()">Final Exam</button>
<button class="nav-btn" onclick="renderSubTests()">&#x23F1; Subject Tests</button>
<button class="nav-btn" onclick="renderOral()">&#x1F3A4; Mock Oral</button>
<button class="nav-btn" onclick="renderPractical()">&#x1F527; Practical Log</button>
<button class="nav-btn" onclick="renderReview()">&#x1F3AF; Review</button>
<button class="nav-btn" onclick="renderCert()">Certificate</button>
<button class="nav-btn" id="nav-roster" style="display:none" onclick="renderRoster()" aria-label="Roster">&#x1F465; Roster</button>
<button class="nav-btn" onclick="renderProfile()" id="nav-profile" aria-label="My profile">&#x1F464;</button>
<button class="nav-btn" onclick="cmdOpen()" title="Command palette (Ctrl+K)" aria-label="Open command palette">&#x2318;K</button>
<button class="nav-btn" onclick="resetProgress()" title="Reset" aria-label="Reset progress">&#x1F5D1;</button>
</nav>
</header>
<main class="container" id="main-content">
<div class="view" id="v-dash"><div id="dash-content"></div></div>
<div class="view hidden" id="v-module"><div id="mod-content"></div></div>
<div class="view hidden" id="v-flash"><div id="flash-content"></div></div>
<div class="view hidden" id="v-gloss"><div id="gloss-content"></div></div>
<div class="view hidden" id="v-ach"><div id="ach-content"></div></div>
<div class="view hidden" id="v-exam"><div id="exam-content"></div></div>
<div class="view hidden" id="v-subtest"><div id="subtest-content"></div></div>
<div class="view hidden" id="v-oral"><div id="oral-content"></div></div>
<div class="view hidden" id="v-practical"><div id="practical-content"></div></div>
<div class="view hidden" id="v-profile"><div id="profile-content"></div></div>
<div class="view hidden" id="v-roster"><div id="roster-content"></div></div>
<div class="view hidden" id="v-sims"><div id="sims-content"></div></div>
<div class="view hidden" id="v-reference"><div id="reference-content"></div></div>
<div class="view hidden" id="v-search"><div id="search-content"></div></div>
<div class="view hidden" id="v-cert"><div id="cert-content"></div></div>
<div class="view hidden" id="v-review"><div id="review-content"></div></div>
<div class="view hidden" id="v-practice"><div id="practice-content"></div></div>
<div class="view hidden" id="v-mastery"><div id="mastery-content"></div></div>
</main>
<div id="cmdp" onclick="if(event.target.id==='cmdp')cmdClose()"><div class="box"><input id="cmdp-input" placeholder="Type a command or module..." oninput="cmdFilter(this.value)"><div class="res" id="cmdp-res"></div></div></div>
<script>{build_js()}
{FEATURES_JS}
{AUTH_JS}
{INSTRUCTOR_JS}
boot();</script>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"Built: {OUT} ({os.path.getsize(OUT)//1024} KB)")

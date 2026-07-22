/* ===== Aviation Academy: multi-user kiosk (accounts, PIN, roles, roster) ===== */
(function(){
  var css=""
  +"#gate{position:fixed;inset:0;background:var(--bg);z-index:10000;display:none;align-items:flex-start;justify-content:center;overflow:auto;padding:3vh 1rem}"
  +"#gate.on{display:flex}"
  +".gate-wrap{max-width:640px;width:100%}"
  +".gate-h{text-align:center;margin-bottom:1.5rem}"
  +".gate-h h1{font-size:1.6rem}.gate-h p{color:var(--txt2)}"
  +".acct-tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:1rem;margin-bottom:1rem}"
  +".acct-tile{background:var(--bg2);border:1px solid var(--bg3);border-radius:12px;padding:1rem;text-align:center;cursor:pointer;transition:transform .15s,border-color .15s}"
  +".acct-tile:hover{transform:translateY(-3px);border-color:var(--accent)}"
  +".acct-tile .av{font-size:2.2rem}"
  +".acct-tile .nm{font-weight:600;margin-top:.3rem}"
  +".acct-tile .rl{font-size:.75rem;color:var(--txt2)}"
  +".acct-tile .lk{font-size:.8rem;color:var(--warn)}"
  +".av-pick{display:flex;flex-wrap:wrap;gap:.4rem;margin:.5rem 0}"
  +".av-opt{font-size:1.5rem;cursor:pointer;padding:.3rem;border-radius:8px;border:2px solid transparent}"
  +".av-opt.sel{border-color:var(--accent);background:var(--bg3)}"
  +".keypad{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;max-width:240px;margin:1rem auto}"
  +".kp{background:var(--bg3);border:none;color:var(--txt);font-size:1.3rem;padding:.9rem;border-radius:10px;cursor:pointer}"
  +".kp:hover{background:var(--accent);color:#fff}"
  +".pin-dots{text-align:center;font-size:1.6rem;letter-spacing:.4rem;height:1.8rem}"
  +".rost-table{width:100%;border-collapse:collapse;font-size:.9rem}"
  +".rost-table th,.rost-table td{padding:.5rem;border-bottom:1px solid var(--bg3);text-align:left}"
  +".rost-table th{color:var(--txt2);font-size:.8rem}"
  +".rost-table tr.click{cursor:pointer}.rost-table tr.click:hover{background:var(--bg3)}"
  +"#lmodal{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:9997;display:flex;align-items:flex-start;justify-content:center;overflow:auto;padding:4vh 1rem}"
  +"#lmodal .box{max-width:680px;width:100%;background:var(--bg2);border:1px solid var(--accent);border-radius:12px;padding:1.5rem}"
  +".lm-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(90px,1fr));gap:.6rem;margin:1rem 0}"
  +".lm-stat{background:var(--bg);border-radius:8px;padding:.6rem;text-align:center}"
  +".lm-stat b{font-size:1.3rem;color:var(--accent2);display:block}"
  +".lm-mod{display:flex;justify-content:space-between;padding:.35rem .5rem;border-bottom:1px solid var(--bg3)}";
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
})();

var AVATARS=["&#x2708;","&#x1F527;","&#x1F6E9;","&#x2699;","&#x1F9F0;","&#x26A1;","&#x1F6E0;","&#x1F468;","&#x1F469;","&#x1F9D1;","&#x1F680;","&#x1F4E1;"];
var ROLES=["Trainee","Technician","Lead"];

function loadAccounts(){
  try{ACCT=JSON.parse(localStorage.getItem('avia_accounts'))||{users:[],current:null};}
  catch(e){ACCT={users:[],current:null};}
  if(!ACCT.users)ACCT.users=[];
}
function saveAccounts(){localStorage.setItem('avia_accounts',JSON.stringify(ACCT));}
function hashPin(pin,salt){var h=5381;var str=(salt||'')+'|'+pin;for(var i=0;i<str.length;i++){h=((h<<5)+h)+str.charCodeAt(i);h=h&0xffffffff;}return (''+h);}
function esc(s){return (''+(s==null?'':s)).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;','\'':'&#39;'}[c];});}
function curUser(){return ACCT.users.find(function(u){return u.id===ACCT.current;});}
function uid(){return 'u'+Date.now().toString(36)+Math.floor(Math.random()*1e4).toString(36);}

/* ---- Gate render ---- */
var _newAv=AVATARS[0],_pinFor=null,_pinBuf='',_pinNew=false,_showCreate=false;
function hideGate(){var g=document.getElementById('gate');g.classList.remove('on');g.innerHTML='';}
function showGate(){
  _pinFor=null;_pinBuf='';
  var g=document.getElementById('gate');
  var h='<div class="gate-wrap"><div class="gate-h"><h1>&#x2708;&#xFE0F; Aviation Maintenance Academy</h1><p>Select your profile to continue</p></div>';
  if(ACCT.users.length){
    h+='<div class="acct-tiles">';
    ACCT.users.forEach(function(u){
      h+='<div class="acct-tile" onclick="selectAccount(\''+u.id+'\')"><div class="av">'+u.av+'</div><div class="nm">'+esc(u.name)+'</div><div class="rl">'+u.role+'</div>'+(u.pinHash?'<div class="lk">&#x1F512; PIN</div>':'')+'</div>';
    });
    h+='</div>';
  }
  h+='<div style="text-align:center"><button class="btn" onclick="toggleCreate()">'+(_showCreate?'Cancel':'+ New Account')+'</button></div>';
  if(_showCreate||!ACCT.users.length){
    h+='<div class="card" style="margin-top:1rem"><h3>Create Account</h3>';
    h+='<div class="sim-io"><label>Name</label><input id="na-name" placeholder="Your name"><label>Role</label><select id="na-role">';
    ROLES.forEach(function(r){h+='<option>'+r+'</option>';});
    h+='</select></div>';
    h+='<label style="font-size:.85rem;color:var(--txt2)">Avatar</label><div class="av-pick" id="na-av">';
    AVATARS.forEach(function(a){h+='<span class="av-opt'+(a===_newAv?' sel':'')+'" onclick="pickAv(\''+a+'\')">'+a+'</span>';});
    h+='</div>';
    h+='<div class="sim-io"><label>PIN (optional, 4 digits)</label><input id="na-pin" inputmode="numeric" maxlength="4" placeholder="e.g. 1234"></div>';
    h+='<button class="btn" onclick="createAccount()">Create &amp; Enter</button></div>';
  }
  h+='</div>';
  g.innerHTML=h;g.classList.add('on');
}
function toggleCreate(){_showCreate=!_showCreate;showGate();}
function pickAv(a){_newAv=a;
  var box=document.getElementById('na-av');
  if(box)Array.prototype.forEach.call(box.children,function(c){c.className='av-opt'+(c.textContent===a?' sel':'');});
}
function createAccount(){
  var name=(document.getElementById('na-name').value||'').trim();
  var role=document.getElementById('na-role').value;
  var pin=(document.getElementById('na-pin').value||'').trim();
  if(!name){alert('Enter a name');return;}
  var id=uid();
  var u={id:id,name:name,role:role,av:_newAv,created:new Date().toISOString(),pinHash:pin?hashPin(pin,id):null};
  ACCT.users.push(u);ACCT.current=id;saveAccounts();
  _showCreate=false;_newAv=AVATARS[0];
  enterApp();
}
/* ---- PIN login ---- */
function selectAccount(id){
  var u=ACCT.users.find(function(x){return x.id===id;});if(!u)return;
  if(!u.pinHash){ACCT.current=id;saveAccounts();enterApp();return;}
  _pinFor=id;_pinBuf='';renderPin(u);
}
function renderPin(u){
  var g=document.getElementById('gate');
  var h='<div class="gate-wrap"><div class="gate-h"><div style="font-size:2.5rem">'+u.av+'</div><h1>'+esc(u.name)+'</h1><p>Enter PIN</p></div>';
  h+='<div class="card"><div class="pin-dots" id="pin-dots"></div><div class="keypad">';
  ['1','2','3','4','5','6','7','8','9'].forEach(function(d){h+='<button class="kp" onclick="pinPush(\''+d+'\')">'+d+'</button>';});
  h+='<button class="kp" onclick="pinBack()">&#x232B;</button><button class="kp" onclick="pinPush(\'0\')">0</button><button class="kp" onclick="pinEnter()">&#x2714;</button>';
  h+='</div><div style="text-align:center"><button class="btn btn-sec" onclick="showGate()">&#x2190; Back</button></div></div></div>';
  g.innerHTML=h;paintPin();
}
function paintPin(){var d=document.getElementById('pin-dots');if(!d)return;var s='';for(var i=0;i<4;i++)s+=(i<_pinBuf.length?'\u25CF':'\u25CB')+' ';d.textContent=s;}
function pinPush(d){if(_pinBuf.length>=4)return;_pinBuf+=d;paintPin();if(_pinBuf.length===4)setTimeout(pinEnter,150);}
function pinBack(){_pinBuf=_pinBuf.slice(0,-1);paintPin();}
function pinEnter(){
  var u=ACCT.users.find(function(x){return x.id===_pinFor;});if(!u)return;
  if(hashPin(_pinBuf,u.id)===u.pinHash){ACCT.current=u.id;saveAccounts();_pinBuf='';enterApp();}
  else{_pinBuf='';paintPin();var d=document.getElementById('pin-dots');if(d){d.textContent='Wrong PIN';setTimeout(paintPin,900);}}
}
document.addEventListener('keydown',function(e){
  var g=document.getElementById('gate');if(!g||!g.classList.contains('on')||!_pinFor)return;
  if(e.key>='0'&&e.key<='9')pinPush(e.key);
  else if(e.key==='Backspace')pinBack();
  else if(e.key==='Enter')pinEnter();
});

/* ---- session ---- */
function signOut(){ACCT.current=null;saveAccounts();showGate();}
function switchUser(){signOut();}
function renderNavForRole(){
  var u=curUser();var r=document.getElementById('nav-roster');
  if(r)r.style.display=(u&&u.role==='Lead')?'inline-block':'none';
}

/* ---- profile view ---- */
function renderProfile(){
  var u=curUser();if(!u){showGate();return;}
  var h='<button class="btn btn-sec" onclick="show(\'v-dash\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>'+u.av+' '+esc(u.name)+'</h2><p style="color:var(--txt2)">Role: <b>'+u.role+'</b> &middot; Joined '+new Date(u.created).toLocaleDateString()+'</p></div>';
  var daysSinceExport = S.lastExportAt ? Math.floor((Date.now()-S.lastExportAt)/86400000) : null;
  var hasProgress = (S.done&&S.done.length) || S.xp;
  if(hasProgress && (daysSinceExport===null || daysSinceExport>=14)){
    h+='<div class="card" style="border:1px solid var(--warn)"><h3>&#x1F4BE; Back Up Your Progress</h3><p style="color:var(--txt2)">Your progress lives only in this browser\'s local storage &mdash; clearing browser data or switching devices will lose it. '+(daysSinceExport===null?'You have never exported a backup.':'It has been '+daysSinceExport+' days since your last backup.')+'</p><button class="btn" onclick="exportProgress()">&#x1F4E4; Export Backup Now</button></div>';
  }

  h+='<div class="card"><h3>Account</h3>';
  h+='<label style="font-size:.85rem;color:var(--txt2)">Avatar</label><div class="av-pick">';
  AVATARS.forEach(function(a){h+='<span class="av-opt'+(a===u.av?' sel':'')+'" onclick="pfAvatar(\''+a+'\')">'+a+'</span>';});
  h+='</div>';
  h+='<div class="sim-io"><label>Role</label><select id="pf-role" onchange="pfRole(this.value)">';
  ROLES.forEach(function(r){h+='<option'+(r===u.role?' selected':'')+'>'+r+'</option>';});
  h+='</select></div>';
  h+='<div class="sim-io"><label>'+(u.pinHash?'Change':'Set')+' PIN (4 digits)</label><input id="pf-pin" inputmode="numeric" maxlength="4" placeholder="4 digits"></div>';
  h+='<button class="btn" onclick="pfSetPin()">'+(u.pinHash?'Change':'Set')+' PIN</button> ';
  if(u.pinHash)h+='<button class="btn btn-sec" onclick="pfRemovePin()">Remove PIN</button>';
  h+='</div>';
  h+='<div class="card"><h3>&#x1F5D3; Target Exam Date</h3><p style="color:var(--txt2);font-size:.85rem">Set your planned exam date to get a personalized study pace on your Dashboard.</p><div class="sim-io"><label>Date</label><input type="date" id="pf-examdate" value="'+(S.examDate||'')+'" onchange="pfSetExamDate(this.value)"></div></div>';
  h+='<div class="card"><h3>Session</h3><button class="btn btn-sec" onclick="switchUser()">&#x1F504; Switch User</button> <button class="btn btn-sec" onclick="signOut()">&#x1F6AA; Sign Out</button> <button class="btn btn-sec" onclick="resetProgress()">&#x1F5D1; Reset My Progress</button><button class="btn btn-sec" onclick="exportProgress()">&#x1F4E4; Export My Progress</button> <label class="btn btn-sec" style="display:inline-block">&#x1F4E5; Import Progress<input type="file" accept="application/json" style="display:none" onchange="importProgress(this)"></label></div>';
  h+='<div class="card"><h3>&#x2708;&#xFE0F; Sources &amp; Methodology</h3>';
  h+='<p style="color:var(--txt2);font-size:.9rem">Lesson content in this Academy is written to align with the subject matter '+
     'covered in the FAA Aviation Maintenance Technician Handbook series (FAA-H-8083-30A General, FAA-H-8083-31 Airframe, '+
     'FAA-H-8083-32B Powerplant). Each module lists its source handbook under its title. '+
     'This app is an independent study companion built for exam readiness practice &mdash; it is <b>not</b> an FAA-licensed '+
     'test bank, does not guarantee verbatim alignment with the official FAA Knowledge Test question pool, and does not '+
     'replace an FAA-approved ground school or the official handbooks, which we encourage every student to read directly.</p>';
  h+='</div>';
  document.getElementById('profile-content').innerHTML=h;show('v-profile');
}
function pfAvatar(a){var u=curUser();u.av=a;saveAccounts();renderProfile();}
function pfRole(r){var u=curUser();u.role=r;saveAccounts();renderNavForRole();}
function pfSetPin(){var u=curUser();var pin=(document.getElementById('pf-pin').value||'').trim();if(pin.length<4){alert('PIN must be 4 digits');return;}u.pinHash=hashPin(pin,u.id);saveAccounts();alert('PIN saved');renderProfile();}
function pfSetExamDate(val){S.examDate=val||null;persist();renderProfile();}
function pfRemovePin(){var u=curUser();u.pinHash=null;saveAccounts();renderProfile();}
/* ---- Lead-only team roster ---- */
function rankFor(xp){var r=RANKS[0];RANKS.forEach(function(rk){if(xp>=rk.xp)r=rk;});return r;}
function userProgress(u){
  var st;try{st=JSON.parse(localStorage.getItem('avia_academy_'+u.id));}catch(e){st=null;}
  st=st||{xp:0,done:[],quizScores:{},flashReviewed:0,streak:0,lastVisit:null,achievements:[],examPassed:false,examScore:0};
  st.pct=Math.round((st.done||[]).length/MODS.length*100);
  st.rank=rankFor(st.xp||0);
  if(typeof readinessScore==='function'){
    var modPct=MODS.length?(st.done||[]).length/MODS.length*100:0;
    var scores=Object.values(st.quizScores||{});
    var quizAvg=scores.length?scores.reduce(function(a,b){return a+b;},0)/scores.length:0;
    var sp=st.subjectPassed||{};
    var subjPct=['general','airframe','powerplant'].filter(function(id){return sp[id];}).length/3*100;
    var oralPct=st.oralBest||0;
    var practicalPct=(typeof PRACTICAL_TASKS!=='undefined'&&PRACTICAL_TASKS.length)?Object.keys(st.practicalLog||{}).length/PRACTICAL_TASKS.length*100:0;
    var examPct=st.examPassed?100:(st.examScore||0);
    st.readiness=Math.round(modPct*0.30+quizAvg*0.15+subjPct*0.15+oralPct*0.1+practicalPct*0.15+examPct*0.15);
    st.pillars={modPct:Math.round(modPct),quizAvg:Math.round(quizAvg),subjPct:Math.round(subjPct),oralPct:Math.round(oralPct),practicalPct:Math.round(practicalPct),examPct:Math.round(examPct)};
  }else{st.readiness=st.pct;}
  st.practicalCount=Object.keys(st.practicalLog||{}).length;
  return st;
}
function renderRoster(){
  var me=curUser();if(!me||me.role!=='Lead'){renderDash();return;}
  var rows=ACCT.users.map(function(u){return {u:u,p:userProgress(u)};});
  rows.sort(function(a,b){return b.p.readiness-a.p.readiness;});
  var h='<button class="btn btn-sec" onclick="show(\'v-dash\');renderDash()">&#x2190; Back</button>';
  h+='<div class="card"><h2>&#x1F465; Team Roster</h2><p style="color:var(--txt2)">'+rows.length+' account(s). Click a row for details.</p>';
  var avgPct=rows.length?Math.round(rows.reduce(function(a,r){return a+r.p.pct;},0)/rows.length):0;
  var passed=rows.filter(function(r){return r.p.examPassed;}).length;
  var avgReadiness=rows.length?Math.round(rows.reduce(function(a,r){return a+r.p.readiness;},0)/rows.length):0;
  h+='<div class="lm-stats"><div class="lm-stat"><b>'+rows.length+'</b>accounts</div><div class="lm-stat"><b>'+avgReadiness+'%</b>avg readiness</div><div class="lm-stat"><b>'+avgPct+'%</b>avg complete</div><div class="lm-stat"><b>'+passed+'</b>exam passed</div></div>';
  var pillarKeys=[['modPct','Modules'],['quizAvg','Quiz avg'],['subjPct','Subject tests'],['oralPct','Mock Oral'],['practicalPct','Practical tasks'],['examPct','Final Exam']];
  var pillarsAvail=rows.filter(function(r){return r.p.pillars;});
  if(pillarsAvail.length){
    var teamPillars=pillarKeys.map(function(pk){
      var vals=pillarsAvail.map(function(r){return r.p.pillars[pk[0]]||0;});
      var avg=Math.round(vals.reduce(function(a,b){return a+b;},0)/vals.length);
      return {label:pk[1],avg:avg};
    });
    teamPillars.sort(function(a,b){return a.avg-b.avg;});
    h+='<h3 style="margin-top:1rem">&#x1F6E9; Team Readiness Pillars (weakest first)</h3>';
    teamPillars.forEach(function(row){
      var col=row.avg>=90?'var(--ok)':row.avg>=70?'var(--accent2)':row.avg>=40?'var(--warn)':'var(--fail)';
      h+='<div class="lm-mod"><span>'+row.label+'</span><span style="color:'+col+';font-weight:600">'+row.avg+'%</span></div>';
    });
  }
  var missAgg={};
  rows.forEach(function(r){
    var m=r.p.missed||{};
    for(var modId in m){
      for(var qi in m[modId]){
        var key=modId+'::'+qi;
        missAgg[key]=(missAgg[key]||0)+1;
      }
    }
  });
  var missTop=Object.keys(missAgg).map(function(key){
    var parts=key.split('::');
    var m=MODS.find(function(x){return x.id===parts[0];});
    var q=m?m.quiz[parseInt(parts[1])]:null;
    return {mod:m,q:q,count:missAgg[key]};
  }).filter(function(x){return x.mod&&x.q;}).sort(function(a,b){return b.count-a.count;}).slice(0,5);
  if(missTop.length){
    h+='<h3 style="margin-top:1rem">&#x1F3AF; Class-wide Missed Questions</h3>';
    missTop.forEach(function(x){
      h+='<div class="lm-mod"><span>'+esc(x.mod.title)+': '+esc(x.q.q.slice(0,70))+(x.q.q.length>70?'...':'')+'</span><span style="color:var(--fail);font-weight:600">'+x.count+' learner(s)</span></div>';
    });
  }
  h+='<button class="btn btn-sec" onclick="exportRoster()">&#x2B07; Export CSV</button> <button class="btn btn-sec" onclick="exportAllAccountsBackup()">&#x1F4E6; Backup All Accounts</button></div>';
  h+='<div class="card"><table class="rost-table"><tr><th>Name</th><th>Role</th><th>Readiness</th><th>Complete</th><th>Rank</th><th>Badges</th><th>Streak</th><th>Exam</th><th>Assigned</th><th>Last seen</th></tr>';
  rows.forEach(function(r){
    var ex=r.p.examPassed?(r.p.examScore+'%'):'-';
    var ls=r.p.lastVisit?new Date(r.p.lastVisit).toLocaleDateString():'never';
    var asg=(typeof assignedTo==='function')?assignedTo(r.u.id):[];
    var adone=asg.filter(function(mid){return (r.p.done||[]).indexOf(mid)>=0;}).length;
    var over=asg.filter(function(mid){return dueStatus(dueOf(r.u.id,mid),(r.p.done||[]).indexOf(mid)>=0).cls==='over';}).length;
    var acell=asg.length?(adone+'/'+asg.length+(over?' <span class="db dueover">'+over+' overdue</span>':'')):'<span style="color:var(--txt2)">-</span>';
    var rcolor=r.p.readiness>=90?'var(--ok)':r.p.readiness>=70?'var(--accent2)':r.p.readiness>=40?'var(--warn)':'var(--fail)';
    h+='<tr class="click" onclick="openLearner(\''+r.u.id+'\')"><td>'+r.u.av+' '+esc(r.u.name)+'</td><td>'+r.u.role+'</td><td><b style="color:'+rcolor+'">'+r.p.readiness+'%</b></td><td>'+r.p.pct+'%</td><td>'+r.p.rank.name+'</td><td>'+(r.p.achievements||[]).length+'</td><td>'+(r.p.streak||0)+'</td><td>'+ex+'</td><td>'+acell+'</td><td>'+ls+'</td></tr>';
  });
  h+='</table></div>';
  var teamOver=0;
  rows.forEach(function(r){
    var asg=(typeof assignedTo==='function')?assignedTo(r.u.id):[];
    if(asg.some(function(mid){return dueStatus(dueOf(r.u.id,mid),(r.p.done||[]).indexOf(mid)>=0).cls==='over';}))teamOver++;
  });
  var atRisk=0;
  rows.forEach(function(r){
    if(!r.p.examDate)return;
    var today=new Date();today.setHours(0,0,0,0);
    var target=new Date(r.p.examDate);target.setHours(0,0,0,0);
    var daysLeft=Math.ceil((target-today)/86400000);
    if(daysLeft>=0&&daysLeft<=14&&r.p.readiness<70)atRisk++;
  });
  var banner=teamOver?'<div class="ralert">&#x26A0; '+teamOver+' learner(s) have overdue assignments.</div>':'';
  if(atRisk)banner+='<div class="ralert">&#x1F6A8; '+atRisk+' learner(s) have an exam in 14 days or less with readiness below 70%.</div>';
  var modOpts=MODS.map(function(m){return '<option value="'+m.id+'">'+m.title+'</option>';}).join('');
  var roleOpts=ROLES.map(function(rr){return '<option value="'+rr+'">'+rr+'</option>';}).join('');
  var cohort='<div class="card cohort"><h3>&#x1F4CC; Assign a module to a whole role</h3><div class="cohrow"><select id="coh-mod">'+modOpts+'</select><select id="coh-role">'+roleOpts+'</select><button class="btn" onclick="cohortAssign()">Assign to all</button></div></div>';
  h=h.replace('<div class="card"><h2>&#x1F465; Team Roster</h2>', banner+'<div class="card"><h2>&#x1F465; Team Roster</h2>');
  h+=cohort;
  if(typeof renderActivityFeed==='function')h+=renderActivityFeed();
  document.getElementById('roster-content').innerHTML=h;show('v-roster');
}
function exportRoster(){
  var rows=[['Name','Role','Readiness%','Complete%','ModulesDone','XP','Rank','Badges','Streak','ExamPassed','ExamScore','PracticalTasksLogged','LastSeen','Pillar_Modules%','Pillar_QuizAvg%','Pillar_SubjectTests%','Pillar_MockOral%','Pillar_Practical%','Pillar_FinalExam%']];
  ACCT.users.forEach(function(u){var p=userProgress(u);var pl=p.pillars||{};
    rows.push([u.name,u.role,p.readiness||0,p.pct,(p.done||[]).length,p.xp||0,p.rank.name,(p.achievements||[]).length,p.streak||0,p.examPassed?'yes':'no',p.examScore||0,p.practicalCount||0,p.lastVisit||'never',pl.modPct||0,pl.quizAvg||0,pl.subjPct||0,pl.oralPct||0,pl.practicalPct||0,pl.examPct||0]);
  });
  var csv=rows.map(function(r){return r.map(function(c){return '"'+(''+c).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
  var a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(csv);a.download='aviation_roster.csv';a.click();
}
function exportAllAccountsBackup(){
  var bundle={exportedAt:new Date().toISOString(),accounts:[]};
  ACCT.users.forEach(function(u){
    var st;try{st=JSON.parse(localStorage.getItem('avia_academy_'+u.id));}catch(e){st=null;}
    bundle.accounts.push({id:u.id,name:u.name,role:u.role,progress:st});
  });
  var data=JSON.stringify(bundle,null,2);
  var a=document.createElement('a');a.href='data:application/json;charset=utf-8,'+encodeURIComponent(data);a.download='aviation_academy_all_accounts_backup.json';a.click();
}
function exportProgress(){
  var u=curUser();if(!u)return;
  var data=JSON.stringify({exportedAt:new Date().toISOString(),user:u.name,progress:S},null,2);
  var a=document.createElement('a');a.href='data:application/json;charset=utf-8,'+encodeURIComponent(data);a.download='aviation_academy_progress_'+u.id+'.json';a.click();
  S.lastExportAt=Date.now();persist();
}
function importProgress(input){
  var f=input.files&&input.files[0];if(!f)return;
  var reader=new FileReader();
  reader.onload=function(){
    try{
      var parsed=JSON.parse(reader.result);
      var prog=parsed.progress||parsed;
      if(!prog||typeof prog!=='object'||!('xp' in prog)){alert('Invalid progress file.');return;}
      if(!confirm('Import progress? This will overwrite your CURRENT progress on this device.'))return;
      S=Object.assign(structuredClone(DEF),prog);persist();renderProfile();alert('Progress imported.');
    }catch(e){alert('Could not read that file - is it a valid Aviation Academy progress export?');}
  };
  reader.readAsText(f);
  input.value='';
}
function openLearner(id){
  var u=ACCT.users.find(function(x){return x.id===id;});if(!u)return;
  var p=userProgress(u);
  var h='<div class="box"><button class="btn btn-sec" onclick="closeLearner()">&#x2715; Close</button>';
  h+='<h2 style="margin-top:.5rem">'+u.av+' '+esc(u.name)+' <span class="track-chip" style="background:var(--bg3)">'+u.role+'</span></h2>';
  h+='<div class="lm-stats"><div class="lm-stat"><b>'+p.pct+'%</b>complete</div><div class="lm-stat"><b>'+(p.xp||0)+'</b>XP</div><div class="lm-stat"><b>'+p.rank.name+'</b>rank</div><div class="lm-stat"><b>'+(p.achievements||[]).length+'</b>badges</div><div class="lm-stat"><b>'+(p.streak||0)+'</b>streak</div><div class="lm-stat"><b>'+(p.examPassed?p.examScore+'%':'-')+'</b>exam</div><div class="lm-stat"><b>'+(p.practicalCount||0)+'/'+(typeof PRACTICAL_TASKS!=='undefined'?PRACTICAL_TASKS.length:20)+'</b>practical</div></div>';
  if(p.pillars){
    var pillarRows=[
      {label:'Modules',pct:p.pillars.modPct},
      {label:'Quiz avg',pct:p.pillars.quizAvg},
      {label:'Subject tests',pct:p.pillars.subjPct},
      {label:'Mock Oral',pct:p.pillars.oralPct},
      {label:'Practical tasks',pct:p.pillars.practicalPct},
      {label:'Final Exam',pct:p.pillars.examPct}
    ];
    pillarRows.sort(function(a,b){return a.pct-b.pct;});
    h+='<h3 style="margin-top:1rem">&#x1F6E9; Readiness Pillars (weakest first)</h3>';
    pillarRows.forEach(function(row){
      var col=row.pct>=90?'var(--ok)':row.pct>=70?'var(--accent2)':row.pct>=40?'var(--warn)':'var(--fail)';
      h+='<div class="lm-mod"><span>'+row.label+'</span><span style="color:'+col+';font-weight:600">'+row.pct+'%</span></div>';
    });
  }
  TRACKS.forEach(function(t){
    var mods=t.modules.map(function(mid){return MODS.find(function(m){return m.id===mid;});});
    var done=mods.filter(function(m){return (p.done||[]).indexOf(m.id)>=0;}).length;
    h+='<h3 style="color:'+t.color+';margin-top:1rem">'+t.name+' ('+done+'/'+mods.length+')</h3>';
    mods.forEach(function(m){
      var dn=(p.done||[]).indexOf(m.id)>=0;
      var q=(p.quizScores||{})[m.id];
      var qs=(q!=null)?(' &middot; quiz '+q+'%'+(q===100?' &#x1F3AF;':'')):'';
      h+='<div class="lm-mod"><span>'+(dn?'&#x2705;':'&#x25CB;')+' '+m.title+'</span><span style="color:var(--txt2);font-size:.85rem">'+qs+'</span></div>';
    });
  });
  h+='<p style="color:var(--txt2);font-size:.8rem;margin-top:1rem">Flashcards reviewed: '+(p.flashReviewed||0)+' &middot; Last active: '+(p.lastVisit?new Date(p.lastVisit).toLocaleDateString():'never')+'</p>';
  h+='<p style="margin-top:1rem"><button class="btn btn-sec" onclick="printLearnerReport(\''+u.id+'\')">&#x1F5A8; Print Learner Report</button></p>';
  if(curUser()&&curUser().role==='Lead'&&typeof learnerAssignPanel==='function')h+=learnerAssignPanel(u);
  h+='</div>';
  var host=document.getElementById('lmodal-host');
  host.innerHTML='<div id="lmodal" onclick="if(event.target.id===\'lmodal\')closeLearner()">'+h+'</div>';
}
function printLearnerReport(id){
  var u=ACCT.users.find(function(x){return x.id===id;});if(!u)return;
  var p=userProgress(u);
  var h='<h1>Learner Report: '+esc(u.name)+'</h1>';
  h+='<p class="pf-meta">'+new Date().toLocaleDateString()+' &middot; Role: '+u.role+'</p>';
  h+='<div class="pf-mod"><h2>Summary</h2><p>Complete: '+p.pct+'% &middot; XP: '+(p.xp||0)+' &middot; Rank: '+p.rank.name+' &middot; Badges: '+(p.achievements||[]).length+' &middot; Streak: '+(p.streak||0)+' &middot; Exam: '+(p.examPassed?p.examScore+'%':'not passed')+'</p></div>';
  if(p.pillars){
    h+='<div class="pf-mod"><h2>Readiness Pillars</h2>';
    h+='<p>Modules: '+p.pillars.modPct+'% &middot; Quiz avg: '+p.pillars.quizAvg+'% &middot; Subject tests: '+p.pillars.subjPct+'% &middot; Mock Oral: '+p.pillars.oralPct+'% &middot; Practical: '+p.pillars.practicalPct+'% &middot; Final Exam: '+p.pillars.examPct+'%</p></div>';
  }
  TRACKS.forEach(function(t){
    var mods=t.modules.map(function(mid){return MODS.find(function(m){return m.id===mid;});});
    var done=mods.filter(function(m){return (p.done||[]).indexOf(m.id)>=0;}).length;
    h+='<div class="pf-mod"><h2>'+t.name+' ('+done+'/'+mods.length+')</h2>';
    mods.forEach(function(m){
      var dn=(p.done||[]).indexOf(m.id)>=0;
      var q=(p.quizScores||{})[m.id];
      h+='<p>'+(dn?'[done] ':'[pending] ')+m.title+(q!=null?(' - quiz '+q+'%'):'')+'</p>';
    });
    h+='</div>';
  });
  printDoc('Learner Report - '+u.name, h);
}
function closeLearner(){document.getElementById('lmodal-host').innerHTML='';}

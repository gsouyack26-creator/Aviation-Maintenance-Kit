/* ===== Aviation Academy: instructor mode (assignments, due dates, activity) ===== */
(function(){
  var css=""
  +".agrid{display:flex;flex-wrap:wrap;gap:.4rem;margin:.5rem 0}"
  +".achip{background:var(--bg3);border:1px solid transparent;color:var(--txt);padding:.35rem .7rem;border-radius:14px;cursor:pointer;font-size:.82rem;display:inline-flex;align-items:center;gap:.3rem}"
  +".achip:hover{border-color:var(--accent)}"
  +".achip.on{background:rgba(59,130,246,.18);border-color:var(--accent)}"
  +".achip.dn{opacity:.7}"
  +".db{font-size:.68rem;padding:.05rem .4rem;border-radius:8px;margin-left:.3rem}"
  +".dueover{background:var(--fail);color:#fff}"
  +".duesoon{background:var(--warn);color:#000}"
  +".dueok{background:var(--bg);color:var(--txt2);border:1px solid var(--bg3)}"
  +".duedone{background:var(--ok);color:#fff}"
  +".duenone{background:var(--bg);color:var(--txt2)}"
  +".cohort{display:flex;gap:.6rem;flex-wrap:wrap;align-items:end}"
  +".cohort .sim-io{margin:0;flex:1;min-width:150px}"
  +".lmdrow{display:flex;justify-content:space-between;align-items:center;gap:.6rem;padding:.3rem 0;border-bottom:1px solid var(--bg3)}"
  +".lmdrow input{background:var(--bg);border:1px solid var(--bg3);color:var(--txt);padding:.3rem;border-radius:6px}"
  +".ralert{background:rgba(239,68,68,.15);border:1px solid var(--fail);border-radius:8px;padding:.6rem 1rem;margin-bottom:1rem;color:var(--fail)}"
  +".afeed{display:flex;flex-direction:column;gap:.3rem}"
  +".afrow{display:flex;gap:.6rem;align-items:center;padding:.35rem .5rem;border-bottom:1px solid var(--bg3);font-size:.88rem}"
  +".afic{font-size:1rem}.aftxt{flex:1}.aftime{color:var(--txt2);font-size:.75rem;white-space:nowrap}";
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
})();

/* ---- assignment store ---- */
function loadAssign(){try{return JSON.parse(localStorage.getItem('avia_assignments'))||{};}catch(e){return {};}}
function saveAssign(a){localStorage.setItem('avia_assignments',JSON.stringify(a));}
function assignedTo(uid){return loadAssign()[uid]||[];}
function toggleAssign(uid,mid){
  var a=loadAssign();if(!a[uid])a[uid]=[];
  var i=a[uid].indexOf(mid);
  if(i>=0){a[uid].splice(i,1);var d=loadDue();if(d[uid]){delete d[uid][mid];saveDue(d);}logActivity('unassign',uid,mid,ACCT.current);}
  else{a[uid].push(mid);logActivity('assign',uid,mid,ACCT.current);}
  saveAssign(a);
}
function assignMod(uid,mid){toggleAssign(uid,mid);openLearner(uid);}

/* ---- due dates ---- */
function loadDue(){try{return JSON.parse(localStorage.getItem('avia_assign_due'))||{};}catch(e){return {};}}
function saveDue(d){localStorage.setItem('avia_assign_due',JSON.stringify(d));}
function dueOf(uid,mid){var d=loadDue();return (d[uid]&&d[uid][mid])||null;}
function setDue(uid,mid,iso){var d=loadDue();if(!d[uid])d[uid]={};if(iso)d[uid][mid]=iso;else delete d[uid][mid];saveDue(d);}
function setDueFor(uid,mid,val){setDue(uid,mid,val);openLearner(uid);}
function dueStatus(iso,done){
  if(done)return {cls:'done',label:'done'};
  if(!iso)return {cls:'none',label:''};
  var today=new Date();today.setHours(0,0,0,0);
  var due=new Date(iso+'T00:00:00');
  var days=Math.round((due-today)/86400000);
  if(days<0)return {cls:'over',label:'overdue '+(-days)+'d',days:days};
  if(days<=3)return {cls:'soon',label:days===0?'due today':'due in '+days+'d',days:days};
  return {cls:'ok',label:'due in '+days+'d',days:days};
}

/* ---- activity log ---- */
function loadActivity(){try{return JSON.parse(localStorage.getItem('avia_activity'))||[];}catch(e){return [];}}
function logActivity(type,uid,mid,actor){
  if(!uid||!mid)return;
  var log=loadActivity();
  log.unshift({ts:Date.now(),type:type,uid:uid,mid:mid,actor:actor});
  if(log.length>200)log=log.slice(0,200);
  localStorage.setItem('avia_activity',JSON.stringify(log));
}
function nameOf(uid){var u=ACCT.users.find(function(x){return x.id===uid;});return u?esc(u.name):'someone';}
function modTitle(mid){var m=MODS.find(function(x){return x.id===mid;});if(m)return m.title;if(typeof PRACTICAL_TASKS!=='undefined'){var t=PRACTICAL_TASKS.find(function(x){return x.id===mid;});if(t)return t.title;}return mid;}
function relTime(ts){var s=(Date.now()-ts)/1000;if(s<60)return 'just now';if(s<3600)return Math.floor(s/60)+'m ago';if(s<86400)return Math.floor(s/3600)+'h ago';var d=Math.floor(s/86400);if(d<7)return d+'d ago';return new Date(ts).toLocaleDateString();}
function renderActivityFeed(){
  var log=loadActivity().slice(0,25);
  if(!log.length)return '<div class="card"><h3>Team Activity</h3><p style="color:var(--txt2)">No activity yet.</p></div>';
  var verb={assign:'assigned',unassign:'unassigned',complete:'completed',practical:'logged'},ic={assign:'&#x1F4CC;',unassign:'&#x2716;',complete:'&#x2705;',practical:'&#x1F527;'};
  var h='<div class="card"><h3>Team Activity</h3><div class="afeed">';
  log.forEach(function(e){
    var txt;
    if(e.type==='complete')txt='<b>'+nameOf(e.uid)+'</b> completed <b>'+modTitle(e.mid)+'</b>';
    else if(e.type==='practical')txt='<b>'+nameOf(e.uid)+'</b> logged practical task <b>'+modTitle(e.mid)+'</b>';
    else txt='<b>'+nameOf(e.actor)+'</b> '+verb[e.type]+' <b>'+modTitle(e.mid)+'</b> '+(e.type==='assign'?'to':'from')+' <b>'+nameOf(e.uid)+'</b>';
    h+='<div class="afrow"><span class="afic">'+(ic[e.type]||'')+'</span><span class="aftxt">'+txt+'</span><span class="aftime">'+relTime(e.ts)+'</span></div>';
  });
  h+='</div></div>';return h;
}

/* ===== PART 2: UI hooks ===== */
function dashAssignedCard(){
  if(!ACCT.current)return '';
  var mine=assignedTo(ACCT.current);
  if(!mine.length)return '';
  var rank={over:0,soon:1,none:2,ok:2,done:3};
  var rows=mine.map(function(mid){
    var done=(S.done&&S.done.indexOf(mid)>=0);
    var iso=dueOf(ACCT.current,mid);
    var ds=dueStatus(iso,done);
    return {mid:mid,done:done,ds:ds};
  }).sort(function(a,b){return rank[a.ds.cls]-rank[b.ds.cls];});
  var todo=rows.filter(function(r){return !r.done;}).length;
  var chips=rows.map(function(r){
    var m=MODS.find(function(x){return x.id===r.mid;});
    var badge=r.ds.cls==='none'?'':'<span class="db due'+r.ds.cls+'">'+r.ds.label+'</span>';
    return '<a class="achip'+(r.done?' dn':'')+'" onclick="openModule(\''+r.mid+'\')">'+(m?m.title:r.mid)+badge+'</a>';
  }).join('');
  var seen=S.seenAsg||[];
  var fresh=mine.filter(function(m){return seen.indexOf(m)<0;});
  if(fresh.length){
    fresh.forEach(function(m){var mm=MODS.find(function(x){return x.id===m;});setTimeout(function(){toast('&#x1F4CC; New: '+(mm?mm.title:m));},300);});
    S.seenAsg=mine.slice();persist();
  }
  return '<div class="card" style="border-left:3px solid var(--accent)"><h3>&#x1F4CC; Assigned to you <span style="color:var(--txt2);font-weight:400;font-size:.85rem">('+todo+' to do)</span></h3><div class="agrid">'+chips+'</div></div>';
}
function learnerAssignPanel(u){
  var mine=assignedTo(u.id);
  var chips=MODS.map(function(m){
    var on=mine.indexOf(m.id)>=0;
    var done=false;try{var raw=localStorage.getItem('avia_academy_'+u.id);if(raw){var st=JSON.parse(raw);done=st.done&&st.done.indexOf(m.id)>=0;}}catch(e){}
    return '<span class="achip'+(on?' on':'')+(done?' dn':'')+'" onclick="toggleAssign(\''+u.id+'\',\''+m.id+'\');openLearner(\''+u.id+'\')">'+m.title+'</span>';
  }).join('');
  var due='';
  if(mine.length){
    due='<div style="margin-top:.8rem"><b style="font-size:.85rem;color:var(--txt2)">DUE DATES</b>';
    mine.forEach(function(mid){
      var m=MODS.find(function(x){return x.id===mid;});
      var iso=dueOf(u.id,mid)||'';
      due+='<div class="lmdrow"><span style="flex:1">'+(m?m.title:mid)+'</span><input type="date" value="'+iso+'" onchange="setDueFor(\''+u.id+'\',\''+mid+'\',this.value)"></div>';
    });
    due+='</div>';
  }
  return '<div class="card" style="margin-top:1rem"><h3>Assign modules</h3><div class="agrid">'+chips+'</div>'+due+'</div>';
}
function cohortAssign(){
  var mid=document.getElementById('coh-mod').value;
  var role=document.getElementById('coh-role').value;
  if(!mid||!role)return;
  var n=0;
  ACCT.users.forEach(function(u){
    if(u.role!==role)return;
    if(assignedTo(u.id).indexOf(mid)>=0)return;
    toggleAssign(u.id,mid);n++;
  });
  var m=MODS.find(function(x){return x.id===mid;});
  alert('Assigned "'+(m?m.title:mid)+'" to '+n+' '+role+(n===1?'':'s')+'.');
  if(typeof renderRoster==='function')renderRoster();
}

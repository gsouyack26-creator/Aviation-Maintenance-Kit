/* ===== Aviation Academy feature pack: sims, reference, search, command palette ===== */
(function(){
  var css = ""
  + ".sim-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem}"
  + ".sim-tile{cursor:pointer;transition:transform .15s,border-color .15s}"
  + ".sim-tile:hover{transform:translateY(-3px);border-color:var(--accent)}"
  + ".sim-tile .icon{font-size:1.8rem}"
  + ".sim-io{display:flex;flex-direction:column;gap:.6rem;margin:.8rem 0}"
  + ".sim-io label{font-size:.85rem;color:var(--txt2)}"
  + ".sim-io input,.sim-io select{background:var(--bg);border:1px solid var(--bg3);color:var(--txt);padding:.5rem;border-radius:6px;font-size:1rem;width:100%}"
  + ".sim-out{background:var(--bg);border:1px dashed var(--accent);border-radius:8px;padding:1rem;margin-top:.5rem;font-size:1.05rem}"
  + ".sim-out b{color:var(--accent2)}"
  + ".wb-row{display:grid;grid-template-columns:2fr 1fr 1fr auto;gap:.4rem;margin-bottom:.4rem;align-items:center}"
  + ".wb-row input{padding:.4rem}"
  + ".ref-cats{display:flex;gap:.4rem;flex-wrap:wrap;margin:.5rem 0 1rem}"
  + ".ref-cat{background:var(--bg3);border:none;color:var(--txt);padding:.35rem .8rem;border-radius:14px;cursor:pointer;font-size:.8rem}"
  + ".ref-cat.active{background:var(--accent);color:#fff}"
  + ".ref-card h3{margin-top:0}"
  + ".search-box{width:100%;padding:.7rem 1rem;font-size:1.05rem;background:var(--bg);border:1px solid var(--bg3);color:var(--txt);border-radius:8px}"
  + ".search-hit{padding:.6rem .8rem;border-bottom:1px solid var(--bg3);cursor:pointer}"
  + ".search-hit:hover{background:var(--bg3)}"
  + ".search-hit .tag{font-size:.7rem;background:var(--bg3);padding:.1rem .5rem;border-radius:8px;color:var(--txt2);margin-right:.5rem}"
  + ".search-hit mark{background:var(--warn);color:#000;border-radius:2px}"
  + "#cmdp{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:9998;display:none;padding-top:12vh}"
  + "#cmdp.on{display:block}"
  + "#cmdp .box{max-width:560px;margin:0 auto;background:var(--bg2);border:1px solid var(--accent);border-radius:12px;overflow:hidden}"
  + "#cmdp input{width:100%;padding:1rem;font-size:1.1rem;background:var(--bg2);border:none;border-bottom:1px solid var(--bg3);color:var(--txt);outline:none}"
  + "#cmdp input:focus-visible{outline:2px solid var(--accent2);outline-offset:-2px}"
  + "#cmdp .res{max-height:50vh;overflow:auto}"
  + "#cmdp .ci{padding:.7rem 1rem;cursor:pointer;display:flex;gap:.6rem;align-items:center}"
  + "#cmdp .ci.sel,#cmdp .ci:hover{background:var(--accent);color:#fff}";
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
})();

/* ---------- SIMS ---------- */
var _simCat='All';
function simCats(){var s={};SIMS.forEach(function(x){s[x.cat]=1;});return ['All'].concat(Object.keys(s));}
function setSimCat(c){_simCat=c;renderSims();}
function renderSims(){
  var h='<div class="card"><h2>&#x1F9EA; Lab Sims</h2><p style="color:var(--txt2)">Interactive calculators for the shop. Tap one to open.</p><div class="ref-cats">';
  simCats().forEach(function(c){h+='<button class="ref-cat'+(c===_simCat?' active':'')+'" onclick="setSimCat(\''+c+'\')">'+c+'</button>';});
  h+='</div></div>';
  if(S.simsRecent&&S.simsRecent.length){
    h+='<div class="card"><h3 style="font-size:0.95rem">Recently Used</h3><div class="sim-grid">';
    S.simsRecent.map(function(id){return SIMS.find(function(s){return s.id===id;});}).filter(Boolean).forEach(function(s){
      h+='<div class="card quicksim-card" onclick="openSim(\''+s.id+'\')"><div class="icon">'+s.icon+'</div><h3>'+s.title+'</h3></div>';
    });
    h+='</div></div>';
  }
  h+='<div class="sim-grid">';
  SIMS.filter(function(s){return _simCat==='All'||s.cat===_simCat;}).forEach(function(s){
    h+='<div class="card sim-tile" onclick="openSim(\''+s.id+'\')"><div class="icon">'+s.icon+'</div><h3>'+s.title+'</h3><p style="font-size:.85rem;color:var(--txt2)">'+s.desc+'</p><span class="track-chip" style="background:var(--bg3)">'+s.cat+'</span></div>';
  });
  h+='</div>';
  document.getElementById('sims-content').innerHTML=h;
  show('v-sims');
}
function simBack(){return '<button class="btn btn-sec" onclick="renderSims()">&#x2190; All Sims</button>';}
function num(id){var v=parseFloat(document.getElementById(id).value);return isNaN(v)?null:v;}
function openSim(id){
  var s=SIMS.find(function(x){return x.id===id;});if(!s)return;
  if(!S.simsRecent)S.simsRecent=[];
  S.simsRecent=S.simsRecent.filter(function(x){return x!==id;});
  S.simsRecent.unshift(id);
  if(S.simsRecent.length>5)S.simsRecent=S.simsRecent.slice(0,5);
  persist();
  var h=simBack()+'<div class="card"><h2>'+s.icon+' '+s.title+'</h2><p style="color:var(--txt2)">'+s.desc+'</p></div>';
  h+='<div class="card" id="sim-body"></div>';
  document.getElementById('sims-content').innerHTML=h;
  var b=document.getElementById('sim-body');
  ({wb:simWB,ohm:simOhm,disp:simDisp,cr:simCR,gas:simGas,bend:simBend,diffcomp:simDiff,torque:simTorque,densalt:simDensAlt,vdrop:simVDrop,fuelplan:simFuelPlan,rivspace:simRivSpace,battery:simBattery,stallv:simStallV,tas:simTAS,proprpm:simPropRPM,loadfactor:simLoadFactor,sfc:simSFC,hydforce:simHydForce,oilconsum:simOilConsum,cabindiff:simCabinDiff,wireamp:simWireAmp,battcap:simBattCap,mixlean:simMixLean,jackload:simJackLoad,egtmargin:simEGTMargin,bondres:simBondRes,fabtest:simFabTest,boostmargin:simBoostMargin,fueldensity:simFuelDensity}[id])(b);
  show('v-sims');
  if(!S.simsUsed)S.simsUsed=[];
  if(S.simsUsed.indexOf(id)<0){S.simsUsed.push(id);addXP(XP_TABLE.flashcard*3);if(S.simsUsed.length>=10&&typeof checkAch==='function')checkAch('sim_explorer');persist();}
}
/* Weight & Balance */
function simWB(b){
  if(!window._wb)window._wb=[{n:'Empty aircraft',w:1500,a:36},{n:'Pilot + pax',w:340,a:37},{n:'Fuel',w:180,a:48}];
  var h='<p>Enter each station (weight lb, arm in). CG = total moment / total weight.</p>';
  h+='<div class="wb-row"><b>Station</b><b>Weight</b><b>Arm</b><span></span></div><div id="wb-rows"></div>';
  h+='<button class="btn btn-sec" onclick="wbAdd()">+ Add station</button>';
  h+='<div class="sim-io" style="margin-top:1rem"><label>Fwd CG limit (in)</label><input id="wb-fwd" type="number" value="33"><label>Aft CG limit (in)</label><input id="wb-aft" type="number" value="46"></div>';
  h+='<button class="btn" onclick="wbCalc()">Compute CG</button><div id="wb-out"></div>';
  b.innerHTML=h;wbRows();
}
function wbRows(){
  var h='';
  window._wb.forEach(function(r,i){
    h+='<div class="wb-row"><input value="'+r.n+'" onchange="_wb['+i+'].n=this.value"><input type="number" value="'+r.w+'" onchange="_wb['+i+'].w=parseFloat(this.value)||0"><input type="number" value="'+r.a+'" onchange="_wb['+i+'].a=parseFloat(this.value)||0"><button class="btn btn-sec" onclick="wbDel('+i+')">&#x2715;</button></div>';
  });
  document.getElementById('wb-rows').innerHTML=h;
}
function wbAdd(){window._wb.push({n:'Station',w:0,a:0});wbRows();}
function wbDel(i){window._wb.splice(i,1);wbRows();}
function wbCalc(){
  var tw=0,tm=0;window._wb.forEach(function(r){tw+=r.w;tm+=r.w*r.a;});
  var cg=tw?tm/tw:0;var fwd=num('wb-fwd'),aft=num('wb-aft');
  var ok=(fwd==null||cg>=fwd)&&(aft==null||cg<=aft);
  var v=ok?'<b style="color:var(--ok)">WITHIN LIMITS</b>':'<b style="color:var(--fail)">OUT OF LIMITS</b>';
  document.getElementById('wb-out').innerHTML='<div class="sim-out">Total weight: <b>'+tw.toFixed(1)+' lb</b><br>Total moment: <b>'+tm.toFixed(1)+' in-lb</b><br>CG: <b>'+cg.toFixed(2)+' in</b><br>'+v+'</div>';
}
/* Ohm's law */
function simOhm(b){
  b.innerHTML='<p>Enter any two values; leave the others blank.</p><div class="sim-io"><label>Voltage E (volts)</label><input id="o-e" type="number"><label>Current I (amps)</label><input id="o-i" type="number"><label>Resistance R (ohms)</label><input id="o-r" type="number"></div><button class="btn" onclick="ohmCalc()">Solve</button><div id="o-out"></div>';
}
function ohmCalc(){
  var E=num('o-e'),I=num('o-i'),R=num('o-r'),msg='';
  if(E==null&&I!=null&&R!=null){E=I*R;msg='E = I x R';}
  else if(I==null&&E!=null&&R!=null){I=E/R;msg='I = E / R';}
  else if(R==null&&E!=null&&I!=null){R=E/I;msg='R = E / I';}
  else{document.getElementById('o-out').innerHTML='<div class="sim-out" style="border-color:var(--fail)">Enter exactly two values.</div>';return;}
  var P=E*I;
  document.getElementById('o-out').innerHTML='<div class="sim-out">'+msg+'<br>E = <b>'+E.toFixed(2)+' V</b><br>I = <b>'+I.toFixed(3)+' A</b><br>R = <b>'+R.toFixed(2)+' ohm</b><br>Power P = E x I = <b>'+P.toFixed(2)+' W</b></div>';
}
/* Displacement */
function simDisp(b){
  b.innerHTML='<p>Displacement = (pi/4) x bore&sup2; x stroke x #cylinders.</p><div class="sim-io"><label>Bore (in)</label><input id="d-b" type="number" value="5.125"><label>Stroke (in)</label><input id="d-s" type="number" value="4.375"><label>Cylinders</label><input id="d-c" type="number" value="4"></div><button class="btn" onclick="dispCalc()">Compute</button><div id="d-out"></div>';
}
function dispCalc(){
  var bo=num('d-b'),st=num('d-s'),cy=num('d-c');
  if(bo==null||st==null||cy==null){document.getElementById('d-out').innerHTML='<div class="sim-out" style="border-color:var(--fail)">Fill all fields.</div>';return;}
  var one=(Math.PI/4)*bo*bo*st;var tot=one*cy;
  document.getElementById('d-out').innerHTML='<div class="sim-out">Per cylinder: <b>'+one.toFixed(2)+' cu in</b><br>Total displacement: <b>'+tot.toFixed(1)+' cu in</b></div>';
}
/* Compression ratio */
function simCR(b){
  b.innerHTML='<p>CR = total volume (piston at BDC) / clearance volume (piston at TDC).</p><div class="sim-io"><label>Cylinder swept volume (cu in)</label><input id="c-sw" type="number" value="70"><label>Clearance volume (cu in)</label><input id="c-cl" type="number" value="10"></div><button class="btn" onclick="crCalc()">Compute</button><div id="c-out"></div>';
}
function crCalc(){
  var sw=num('c-sw'),cl=num('c-cl');
  if(sw==null||cl==null||cl<=0){document.getElementById('c-out').innerHTML='<div class="sim-out" style="border-color:var(--fail)">Enter valid volumes (clearance &gt; 0).</div>';return;}
  var cr=(sw+cl)/cl;
  document.getElementById('c-out').innerHTML='<div class="sim-out">Total volume: <b>'+(sw+cl).toFixed(1)+' cu in</b><br>Compression ratio: <b>'+cr.toFixed(2)+' : 1</b></div>';
}
/* Gas laws */
function simGas(b){
  b.innerHTML='<p>Combined gas law P1V1/T1 = P2V2/T2. Leave the unknown blank. Temps are absolute (add 460 to deg F for Rankine, or 273 to deg C for Kelvin).</p><div class="sim-io"><label>P1</label><input id="g-p1" type="number"><label>V1</label><input id="g-v1" type="number"><label>T1 (absolute)</label><input id="g-t1" type="number"><label>P2</label><input id="g-p2" type="number"><label>V2</label><input id="g-v2" type="number"><label>T2 (absolute)</label><input id="g-t2" type="number"></div><button class="btn" onclick="gasCalc()">Solve for blank</button><div id="g-out"></div>';
}
function gasCalc(){
  var v={p1:num('g-p1'),v1:num('g-v1'),t1:num('g-t1'),p2:num('g-p2'),v2:num('g-v2'),t2:num('g-t2')};
  var blanks=Object.keys(v).filter(function(k){return v[k]==null;});
  var out=document.getElementById('g-out');
  if(blanks.length!==1){out.innerHTML='<div class="sim-out" style="border-color:var(--fail)">Leave exactly one field blank.</div>';return;}
  var k=blanks[0],r;
  if(k==='p2')r=v.p1*v.v1*v.t2/(v.t1*v.v2);
  else if(k==='v2')r=v.p1*v.v1*v.t2/(v.t1*v.p2);
  else if(k==='t2')r=v.t1*v.p2*v.v2/(v.p1*v.v1);
  else if(k==='p1')r=v.p2*v.v2*v.t1/(v.t2*v.v1);
  else if(k==='v1')r=v.p2*v.v2*v.t1/(v.t2*v.p1);
  else r=v.t2*v.p1*v.v1/(v.p2*v.v2);
  out.innerHTML='<div class="sim-out">Solved <b>'+k.toUpperCase()+'</b> = <b>'+r.toFixed(3)+'</b></div>';
}
/* Sheet metal bend */
function simBend(b){
  b.innerHTML='<p>90-deg setback = radius + thickness. Bend allowance = (0.01743 x R + 0.0078 x T) x degrees.</p><div class="sim-io"><label>Bend radius R (in)</label><input id="b-r" type="number" value="0.16"><label>Material thickness T (in)</label><input id="b-t" type="number" value="0.04"><label>Bend angle (deg)</label><input id="b-a" type="number" value="90"></div><button class="btn" onclick="bendCalc()">Compute</button><div id="b-out"></div>';
}
function bendCalc(){
  var R=num('b-r'),T=num('b-t'),A=num('b-a');
  if(R==null||T==null||A==null){document.getElementById('b-out').innerHTML='<div class="sim-out" style="border-color:var(--fail)">Fill all fields.</div>';return;}
  var sb=(A===90)?(R+T):(Math.tan(A*Math.PI/360)*(R+T));
  var ba=(0.01743*R+0.0078*T)*A;
  document.getElementById('b-out').innerHTML='<div class="sim-out">Setback: <b>'+sb.toFixed(4)+' in</b><br>Bend allowance: <b>'+ba.toFixed(4)+' in</b><br>Bend deduction (2 x SB - BA): <b>'+(2*sb-ba).toFixed(4)+' in</b></div>';
}
/* Differential compression */
function simDiff(b){
  b.innerHTML='<p>Enter the leak-down reading and where you hear air escaping. Typical minimum is 60/80 (verify mfr limit).</p><div class="sim-io"><label>Cylinder pressure (of 80)</label><input id="dc-p" type="number" value="72"><label>Where is the air escaping?</label><select id="dc-w"><option value="none">No obvious leak</option><option value="exhaust">Exhaust pipe</option><option value="intake">Carburetor / intake</option><option value="breather">Oil filler / breather</option></select></div><button class="btn" onclick="diffCalc()">Diagnose</button><div id="dc-out"></div>';
}
function diffCalc(){
  var p=num('dc-p'),w=document.getElementById('dc-w').value;
  var verdicts={none:'Within tolerance if above the minimum. Air loss is normal ring seepage.',exhaust:'Leaking <b>exhaust valve</b> - burnt/warped valve or seat. Consider staking/borescope.',intake:'Leaking <b>intake valve</b> - valve or seat leak on the induction side.',breather:'Air past the <b>piston rings</b> (worn/broken rings or scored cylinder wall).'};
  var low=(p!=null&&p<60);
  var head=low?'<b style="color:var(--fail)">'+p+'/80 - BELOW 60/80 minimum</b>':'<b style="color:var(--ok)">'+p+'/80 - above minimum</b>';
  document.getElementById('dc-out').innerHTML='<div class="sim-out">'+head+'<br>'+verdicts[w]+'</div>';
}
/* Torque Wrench Extension */
function simTorque(b){
  b.innerHTML='<p>Using an extension/adapter changes the dial reading needed to achieve the true (target) torque at the fastener. TW = TE x (L / (L + A)).</p>'+
    '<div class="sim-io"><label>Target (true) torque at fastener (in-lb)</label><input id="tq-te" type="number" value="360">'+
    '<label>Wrench handle length L (pivot to grip, in)</label><input id="tq-l" type="number" value="10">'+
    '<label>Extension length A (beyond wrench drive, in)</label><input id="tq-a" type="number" value="3">'+
    '</div><button class="btn" onclick="torqueCalc()">Calculate Wrench Setting</button><div id="tq-out"></div>';
}
function torqueCalc(){
  var te=num('tq-te'),l=num('tq-l'),a=num('tq-a');
  var out=document.getElementById('tq-out');
  if(te===null||l===null||a===null||l<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid numbers (L must be greater than 0).</div>';return;}
  var tw=te*(l/(l+a));
  out.innerHTML='<div class="sim-out">Set the wrench to: <b>'+tw.toFixed(1)+' in-lb</b><br>'+
    '<span style="color:var(--txt2)">TW = '+te+' x ('+l+' / ('+l+' + '+a+')) = '+tw.toFixed(2)+' in-lb. This produces '+te+' in-lb of true torque at the fastener.</span></div>';
}
/* Density Altitude */
function simDensAlt(b){
  b.innerHTML='<p>Estimate density altitude from field elevation, altimeter setting, and outside air temperature.</p>'+
    '<div class="sim-io"><label>Field elevation (ft)</label><input id="da-elev" type="number" value="1200">'+
    '<label>Altimeter setting (inHg)</label><input id="da-alt" type="number" value="29.62" step="0.01">'+
    '<label>Outside air temp (&deg;C)</label><input id="da-oat" type="number" value="30">'+
    '</div><button class="btn" onclick="densAltCalc()">Calculate</button><div id="da-out"></div>';
}
function densAltCalc(){
  var elev=num('da-elev'),alt=num('da-alt'),oat=num('da-oat');
  var out=document.getElementById('da-out');
  if(elev===null||alt===null||oat===null){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid numbers.</div>';return;}
  var pa=elev+((29.92-alt)*1000);
  var isaTemp=15-(2*(pa/1000));
  var da=pa+(120*(oat-isaTemp));
  var warn=da-pa>=1500?'<p style="color:var(--warn)">Significant performance penalty - consult performance charts before flight/maintenance test runs.</p>':'';
  out.innerHTML='<div class="sim-out">Pressure Altitude: <b>'+Math.round(pa)+' ft</b><br>ISA temp at that altitude: '+isaTemp.toFixed(1)+'&deg;C<br>'+
    'Density Altitude: <b>'+Math.round(da)+' ft</b><br><span style="color:var(--txt2)">'+Math.round(da-elev)+' ft above field elevation.</span>'+warn+'</div>';
}
/* Wire Size & Voltage Drop */
function simVDrop(b){
  b.innerHTML='<p>Check the voltage drop for a wire run (out and back) and whether the gauge is adequate.</p>'+
    '<div class="sim-io"><label>Source voltage (V)</label><input id="vd-v" type="number" value="28">'+
    '<label>Current (A)</label><input id="vd-i" type="number" value="10">'+
    '<label>One-way wire length (ft)</label><input id="vd-len" type="number" value="15">'+
    '<label>Wire gauge (AWG)</label><select id="vd-awg">'+
      '<option value="22">22 AWG (~16.5 mOhm/ft)</option><option value="20">20 AWG (~10.4 mOhm/ft)</option>'+
      '<option value="18" selected>18 AWG (~6.5 mOhm/ft)</option><option value="16">16 AWG (~4.1 mOhm/ft)</option>'+
      '<option value="14">14 AWG (~2.6 mOhm/ft)</option><option value="12">12 AWG (~1.6 mOhm/ft)</option>'+
    '</select></div><button class="btn" onclick="vdropCalc()">Calculate</button><div id="vd-out"></div>';
}
function vdropCalc(){
  var v=num('vd-v'),i=num('vd-i'),len=num('vd-len');
  var awg=document.getElementById('vd-awg').value;
  var ohmPerFt={'22':0.0165,'20':0.0104,'18':0.0065,'16':0.0041,'14':0.0026,'12':0.0016}[awg];
  var out=document.getElementById('vd-out');
  if(v===null||i===null||len===null||v<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid numbers.</div>';return;}
  var totalR=ohmPerFt*len*2;
  var vdrop=i*totalR;
  var pct=(vdrop/v)*100;
  var ok=pct<=5;
  out.innerHTML='<div class="sim-out">Round-trip wire resistance: '+totalR.toFixed(3)+' &#x2126;<br>'+
    'Voltage drop: <b>'+vdrop.toFixed(2)+' V</b> ('+pct.toFixed(1)+'% of source)<br>'+
    '<b style="color:'+(ok?'var(--ok)':'var(--fail)')+'">'+(ok?'Within typical 5% guideline':'Exceeds typical 5% guideline - consider a larger gauge or shorter run')+'</b>'+
    '<br><span style="color:var(--txt2)">Rule of thumb only - confirm against AC 43.13-1B wire tables and equipment-specific limits (avionics often need &le;2%).</span></div>';
}
/* Fuel Endurance Planner */
function simFuelPlan(b){
  b.innerHTML='<p>Estimate flight endurance and range from usable fuel and burn rate. Always plan a reserve.</p>'+
    '<div class="sim-io"><label>Usable fuel (gal)</label><input id="fp-fuel" type="number" value="40">'+
    '<label>Burn rate (gal/hr)</label><input id="fp-burn" type="number" value="8">'+
    '<label>Groundspeed (kt)</label><input id="fp-gs" type="number" value="120">'+
    '<label>Reserve required (min)</label><input id="fp-res" type="number" value="45">'+
    '</div><button class="btn" onclick="fuelPlanCalc()">Calculate</button><div id="fp-out"></div>';
}
function fuelPlanCalc(){
  var fuel=num('fp-fuel'),burn=num('fp-burn'),gs=num('fp-gs'),res=num('fp-res');
  var out=document.getElementById('fp-out');
  if(fuel===null||burn===null||gs===null||res===null||burn<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid numbers (burn rate must be greater than 0).</div>';return;}
  var totalEnd=fuel/burn;
  var reserveGal=burn*(res/60);
  var usableEnd=totalEnd-(res/60);
  var range=usableEnd*gs;
  var ok=usableEnd>0;
  out.innerHTML='<div class="sim-out">Total endurance: <b>'+totalEnd.toFixed(2)+' hr</b><br>'+
    'Reserve needed: '+reserveGal.toFixed(1)+' gal ('+res+' min)<br>'+
    '<b style="color:'+(ok?'var(--ok)':'var(--fail)')+'">Usable endurance after reserve: '+usableEnd.toFixed(2)+' hr</b><br>'+
    'Estimated range: <b>'+Math.round(range)+' nm</b>'+
    (ok?'':'<p style="color:var(--fail)">Insufficient fuel to meet the reserve requirement!</p>')+
    '<br><span style="color:var(--txt2)">Planning estimate only - always use POH performance data and account for wind, climb/descent fuel, and taxi.</span></div>';
}
/* Rivet Spacing Checker */
function simRivSpace(b){
  b.innerHTML='<p>Check rivet edge distance and pitch (row spacing) against standard minimum guidelines for a given shank diameter.</p>'+
    '<div class="sim-io"><label>Rivet diameter (in, e.g. 0.125 for 1/8")</label><input id="rs-d" type="number" value="0.125" step="0.001">'+
    '<label>Actual edge distance (in)</label><input id="rs-edge" type="number" value="0.28" step="0.01">'+
    '<label>Actual pitch / row spacing (in)</label><input id="rs-pitch" type="number" value="0.5" step="0.01">'+
    '</div><button class="btn" onclick="rivSpaceCalc()">Check Spacing</button><div id="rs-out"></div>';
}
function rivSpaceCalc(){
  var d=num('rs-d'),edge=num('rs-edge'),pitch=num('rs-pitch');
  var out=document.getElementById('rs-out');
  if(d===null||edge===null||pitch===null||d<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid numbers (diameter must be greater than 0).</div>';return;}
  var minEdge=2*d, minPitch=3*d;
  var edgeOk=edge>=minEdge, pitchOk=pitch>=minPitch;
  out.innerHTML='<div class="sim-out">Minimum edge distance (2xD): <b>'+minEdge.toFixed(3)+' in</b> &mdash; Actual: '+edge.toFixed(3)+' in '+
    '<b style="color:'+(edgeOk?'var(--ok)':'var(--fail)')+'">'+(edgeOk?'OK':'TOO CLOSE')+'</b>'+
    '<br>Minimum pitch (3xD): <b>'+minPitch.toFixed(3)+' in</b> &mdash; Actual: '+pitch.toFixed(3)+' in '+
    '<b style="color:'+(pitchOk?'var(--ok)':'var(--fail)')+'">'+(pitchOk?'OK':'TOO CLOSE')+'</b>'+
    '<br><span style="color:var(--txt2)">General guidance only - always confirm against the specific SRM for the actual structure.</span></div>';
}
/* Battery Capacity & C-Rate */
function simBattery(b){
  b.innerHTML='<p>Estimate discharge current and run time from battery capacity and desired C-rate, or from a fixed load current.</p>'+
    '<div class="sim-io"><label>Battery capacity (Ah)</label><input id="bt-cap" type="number" value="40">'+
    '<label>C-Rate (leave blank if using load current)</label><input id="bt-c" type="number" value="1" step="0.1">'+
    '<label>Load current (A) (leave blank if using C-rate)</label><input id="bt-i" type="number">'+
    '<label>Usable capacity factor (0-1, derate for age/temp)</label><input id="bt-derate" type="number" value="0.8" step="0.05">'+
    '</div><button class="btn" onclick="batteryCalc()">Calculate</button><div id="bt-out"></div>';
}
function batteryCalc(){
  var cap=num('bt-cap'),c=num('bt-c'),i=num('bt-i'),derate=num('bt-derate');
  var out=document.getElementById('bt-out');
  if(cap===null||cap<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid battery capacity (Ah).</div>';return;}
  if(derate===null||derate<=0)derate=1;
  var current,crate;
  if(i!=null&&i>0){current=i;crate=current/cap;}
  else if(c!=null&&c>0){crate=c;current=c*cap;}
  else{out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter either a C-rate or a load current.</div>';return;}
  var usableAh=cap*derate;
  var runHr=usableAh/current;
  out.innerHTML='<div class="sim-out">Discharge current: <b>'+current.toFixed(2)+' A</b> (C-rate '+crate.toFixed(2)+'C)<br>'+
    'Usable capacity ('+(derate*100).toFixed(0)+'%): <b>'+usableAh.toFixed(1)+' Ah</b><br>'+
    '<b>Estimated run time: '+runHr.toFixed(2)+' hr</b> ('+Math.round(runHr*60)+' min)'+
    '<br><span style="color:var(--txt2)">Estimate only - verify against manufacturer discharge curves; high C-rates reduce effective capacity further.</span></div>';
}
/* Stall Speed & Load Factor */
function simStallV(b){
  b.innerHTML='<p>Compute load factor and stall speed increase for a coordinated level turn at a given bank angle, or enter load factor directly.</p>'+
    '<div class="sim-io"><label>1g stall speed Vs (kt)</label><input id="sv-vs" type="number" value="60">'+
    '<label>Bank angle (deg) (leave blank if using load factor)</label><input id="sv-bank" type="number" value="45">'+
    '<label>Load factor n (leave blank if using bank angle)</label><input id="sv-n" type="number" step="0.1">'+
    '</div><button class="btn" onclick="stallVCalc()">Calculate</button><div id="sv-out"></div>';
}
function stallVCalc(){
  var vs=num('sv-vs'),bank=num('sv-bank'),n=num('sv-n');
  var out=document.getElementById('sv-out');
  if(vs===null||vs<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid 1g stall speed.</div>';return;}
  if(n==null){
    if(bank==null||bank<0||bank>=90){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a bank angle (0-89 deg) or a load factor.</div>';return;}
    n=1/Math.cos(bank*Math.PI/180);
  }else{
    bank=Math.acos(1/n)*180/Math.PI;
  }
  var vsNew=vs*Math.sqrt(n);
  var pctInc=((vsNew/vs)-1)*100;
  var warn=n>=2?'<p style="color:var(--fail)">High load factor - stall margin significantly reduced.</p>':'';
  out.innerHTML='<div class="sim-out">Bank angle: <b>'+bank.toFixed(1)+' deg</b><br>'+
    'Load factor n: <b>'+n.toFixed(2)+'g</b><br>'+
    'New stall speed: <b>'+vsNew.toFixed(1)+' kt</b> (+'+pctInc.toFixed(1)+'%)'+
    warn+
    '<br><span style="color:var(--txt2)">Vs(new) = Vs x sqrt(n). Coordinated level turn assumed; accelerated/uncoordinated maneuvers can be worse.</span></div>';
}
/* True Airspeed Calculator */
function simTAS(b){
  b.innerHTML='<p>Rough-estimate true airspeed from calibrated airspeed and pressure altitude, with an optional temperature correction. For precise work use POH tables or a flight computer.</p>'+
    '<div class="sim-io"><label>Calibrated airspeed (kt)</label><input id="tas-cas" type="number" value="120">'+
    '<label>Pressure altitude (ft)</label><input id="tas-alt" type="number" value="8000">'+
    '<label>Outside air temp (deg C, optional)</label><input id="tas-oat" type="number">'+
    '<label>ISA temp at this altitude (deg C, optional)</label><input id="tas-isa" type="number">'+
    '</div><button class="btn" onclick="tasCalc()">Calculate</button><div id="tas-out"></div>';
}
function tasCalc(){
  var cas=num('tas-cas'),alt=num('tas-alt'),oat=num('tas-oat'),isa=num('tas-isa');
  var out=document.getElementById('tas-out');
  if(cas===null||alt===null||cas<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid CAS and pressure altitude.</div>';return;}
  var tas=cas*(1+0.02*(alt/1000));
  var note='';
  if(oat!=null&&isa!=null){
    var diff=oat-isa;
    tas=tas*(1+0.002*diff);
    note='<br>Adjusted for '+diff.toFixed(1)+' deg C from ISA.';
  }
  out.innerHTML='<div class="sim-out">Estimated TAS: <b>'+tas.toFixed(1)+' kt</b>'+note+
    '<br><span style="color:var(--txt2)">Rule-of-thumb estimate (~2% per 1,000 ft), most accurate below ~10,000 ft. Use POH performance data for flight planning.</span></div>';
}
/* Propeller Tip Speed & RPM Limit */
function simPropRPM(b){
  b.innerHTML='<p>Compute propeller blade tip speed and its Mach number to check against the transonic caution zone.</p>'+
    '<div class="sim-io"><label>Propeller diameter (ft)</label><input id="pr-d" type="number" value="6.5" step="0.1">'+
    '<label>Propeller RPM</label><input id="pr-rpm" type="number" value="2700">'+
    '<label>Forward airspeed (kt, optional - adds to resultant tip speed)</label><input id="pr-tas" type="number">'+
    '</div><button class="btn" onclick="propRPMCalc()">Calculate</button><div id="pr-out"></div>';
}
function propRPMCalc(){
  var d=num('pr-d'),rpm=num('pr-rpm'),tas=num('pr-tas');
  var out=document.getElementById('pr-out');
  if(d===null||rpm===null||d<=0||rpm<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid diameter and RPM.</div>';return;}
  var rotSpeedFtSec=Math.PI*d*(rpm/60);
  var tasFtSec=(tas!=null?tas*1.6878:0);
  var resultant=Math.sqrt(rotSpeedFtSec*rotSpeedFtSec+tasFtSec*tasFtSec);
  var mach=resultant/1116;
  var warn=mach>=0.85?'<p style="color:var(--fail)">Approaching transonic - expect sharp drag/noise rise and possible blade stress.</p>':(mach>=0.7?'<p style="color:var(--warn)">Getting close to the transonic caution zone.</p>':'');
  out.innerHTML='<div class="sim-out">Rotational tip speed: <b>'+rotSpeedFtSec.toFixed(0)+' ft/sec</b><br>'+
    'Resultant tip speed (with forward speed): <b>'+resultant.toFixed(0)+' ft/sec</b><br>'+
    'Approx. tip Mach number: <b>'+mach.toFixed(2)+'</b>'+
    warn+
    '<br><span style="color:var(--txt2)">Sea-level standard-day speed of sound (~1,116 ft/sec) assumed. Actual limits vary by propeller design and altitude.</span></div>';
}
/* Load Factor & Turn Stall Speed */
function simLoadFactor(b){
  b.innerHTML='<p>Compute load factor (G) in a level, coordinated turn and the resulting stall speed increase.</p>'+
    '<div class="sim-io"><label>Bank angle (degrees)</label><input id="lf-bank" type="number" value="45" step="1">'+
    '<label>1G stall speed, Vs1 (kt, optional)</label><input id="lf-vs1" type="number" value="60">'+
    '</div><button class="btn" onclick="loadFactorCalc()">Calculate</button><div id="lf-out"></div>';
}
function loadFactorCalc(){
  var bank=num('lf-bank'),vs1=num('lf-vs1');
  var out=document.getElementById('lf-out');
  if(bank===null||bank<0||bank>=90){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a bank angle between 0 and 89 degrees.</div>';return;}
  var rad=bank*Math.PI/180;
  var n=1/Math.cos(rad);
  var warn=n>=2?'<p style="color:var(--fail)">High load factor - approaching or exceeding typical utility-category limits.</p>':(n>=1.5?'<p style="color:var(--warn)">Moderate load factor increase.</p>':'');
  var out2='<div class="sim-out">Load factor: <b>'+n.toFixed(2)+' G</b>';
  if(vs1!=null&&vs1>0){
    var vsTurn=vs1*Math.sqrt(n);
    out2+='<br>Stall speed in this turn: <b>'+vsTurn.toFixed(1)+' kt</b> (up from '+vs1.toFixed(1)+' kt at 1G)';
  }
  out2+=warn+'<br><span style="color:var(--txt2)">n = 1/cos(bank). Stall speed scales with sqrt(n). Assumes a level, coordinated turn.</span></div>';
  out.innerHTML=out2;
}
/* Specific Fuel Consumption Estimator */
function simSFC(b){
  b.innerHTML='<p>Estimate specific fuel consumption from fuel flow and power (piston, BSFC) or thrust (turbine, TSFC).</p>'+
    '<div class="sim-io"><label>Engine type</label><select id="sfc-type"><option value="piston">Piston (BHP)</option><option value="turbine">Turbine (thrust, lb)</option></select>'+
    '<label>Fuel flow (lb/hr)</label><input id="sfc-ff" type="number" value="80">'+
    '<label id="sfc-plabel">Brake horsepower</label><input id="sfc-power" type="number" value="200">'+
    '</div><button class="btn" onclick="sfcCalc()">Calculate</button><div id="sfc-out"></div>';
}
function sfcCalc(){
  var type=document.getElementById('sfc-type').value;
  var ff=num('sfc-ff'),power=num('sfc-power');
  var out=document.getElementById('sfc-out');
  if(ff===null||power===null||ff<=0||power<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid fuel flow and power/thrust values.</div>';return;}
  var sfc=ff/power;
  var unit=type==='piston'?'lb/hp/hr (BSFC)':'lb/lb-thrust/hr (TSFC)';
  out.innerHTML='<div class="sim-out">Specific fuel consumption: <b>'+sfc.toFixed(3)+'</b> '+unit+
    '<br><span style="color:var(--txt2)">Lower SFC = more efficient for the power/thrust produced. This is a single-point estimate - use POH/AFM fuel-flow charts for real flight planning.</span></div>';
}
/* Hydraulic Force & Pressure (Pascal\'s Law) */
function simHydForce(b){
  b.innerHTML='<p>Compute output force, pressure, or piston area in a hydraulic system using Pascal\'s Law (P = F / A) and the mechanical advantage between two pistons.</p>'+
    '<div class="sim-io"><label>Input force, F1 (lb)</label><input id="hf-f1" type="number" value="50">'+
    '<label>Input piston area, A1 (sq in)</label><input id="hf-a1" type="number" value="2">'+
    '<label>Output piston area, A2 (sq in)</label><input id="hf-a2" type="number" value="10">'+
    '</div><button class="btn" onclick="hydForceCalc()">Calculate</button><div id="hf-out"></div>';
}
function hydForceCalc(){
  var f1=num('hf-f1'),a1=num('hf-a1'),a2=num('hf-a2');
  var out=document.getElementById('hf-out');
  if(f1===null||a1===null||a2===null||a1<=0||a2<=0||f1<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid force and area values (areas must be greater than zero).</div>';return;}
  var p=f1/a1;
  var f2=p*a2;
  var ma=a2/a1;
  out.innerHTML='<div class="sim-out">System pressure: <b>'+p.toFixed(1)+' psi</b>'+
    '<br>Output force, F2: <b>'+f2.toFixed(1)+' lb</b>'+
    '<br>Mechanical advantage (A2/A1): <b>'+ma.toFixed(2)+'x</b>'+
    '<br><span style="color:var(--txt2)">Pressure is transmitted equally throughout the fluid (Pascal\'s Law). A larger output piston multiplies force but moves a shorter distance for the same fluid volume.</span></div>';
}
/* Oil Consumption Rate Estimator */
function simOilConsum(b){
  b.innerHTML='<p>Estimate engine oil consumption rate in quarts per hour from oil added and elapsed operating time.</p>'+
    '<div class="sim-io"><label>Oil added (quarts)</label><input id="oc-qt" type="number" value="1" step="0.1">'+
    '<label>Hours of operation since last check</label><input id="oc-hrs" type="number" value="10" step="0.1">'+
    '<label>Manufacturer limit (qt/hr, optional)</label><input id="oc-limit" type="number" value="0.1" step="0.01">'+
    '</div><button class="btn" onclick="oilConsumCalc()">Calculate</button><div id="oc-out"></div>';
}
function oilConsumCalc(){
  var qt=num('oc-qt'),hrs=num('oc-hrs'),limit=num('oc-limit');
  var out=document.getElementById('oc-out');
  if(qt===null||hrs===null||qt<0||hrs<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid oil quantity and a positive number of hours.</div>';return;}
  var rate=qt/hrs;
  var warn='';
  if(limit!=null&&limit>0){
    warn=rate>limit?'<p style="color:var(--fail)">Rate exceeds the entered manufacturer limit - investigate for wear or leaks.</p>':'<p style="color:var(--ok)">Rate is within the entered manufacturer limit.</p>';
  }
  out.innerHTML='<div class="sim-out">Oil consumption rate: <b>'+rate.toFixed(3)+' qt/hr</b>'+warn+
    '<br><span style="color:var(--txt2)">Compare against the engine manufacturer\'s published limit. A rising trend across multiple checks is more significant than a single reading.</span></div>';
}
/* Cabin Differential Pressure */
function simCabinDiff(b){
  b.innerHTML='<p>Estimate cabin differential pressure from aircraft altitude and cabin altitude, using a simple standard-atmosphere approximation (about 1 inHg per 1,000 ft up to 10,000 ft).</p>'+
    '<div class="sim-io"><label>Aircraft altitude (ft)</label><input id="cd-alt" type="number" value="35000">'+
    '<label>Cabin altitude (ft)</label><input id="cd-cab" type="number" value="8000">'+
    '<label>Max structural differential (psi, optional)</label><input id="cd-max" type="number" value="8.6" step="0.1">'+
    '</div><button class="btn" onclick="cabinDiffCalc()">Calculate</button><div id="cd-out"></div>';
}
function cabinDiffCalc(){
  var alt=num('cd-alt'),cab=num('cd-cab'),maxd=num('cd-max');
  var out=document.getElementById('cd-out');
  if(alt===null||cab===null||alt<0||cab<0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid altitude values.</div>';return;}
  function pressAt(ft){
    var capped=Math.min(ft,10000);
    var p=29.92-(capped/1000)*1.0;
    if(ft>10000)p-=(ft-10000)/1000*0.83;
    return p;
  }
  var pAlt=pressAt(alt), pCab=pressAt(cab);
  var diffInHg=pCab-pAlt;
  var diffPsi=diffInHg*0.4912;
  var warn='';
  if(maxd!=null&&maxd>0){
    warn=diffPsi>maxd?'<p style="color:var(--fail)">Computed differential exceeds the entered structural limit.</p>':'<p style="color:var(--ok)">Computed differential is within the entered structural limit.</p>';
  }
  out.innerHTML='<div class="sim-out">Estimated cabin differential pressure: <b>'+diffPsi.toFixed(2)+' psi</b> ('+diffInHg.toFixed(2)+' inHg)'+warn+
    '<br><span style="color:var(--txt2)">Approximation only - real pressurization schedules and atmospheric models are more precise. Always use the AFM/POH pressurization schedule and manual for actual limits.</span></div>';
}
/* Wire Ampacity Check */
function simWireAmp(b){
  b.innerHTML='<p>Compare a circuit\'s expected current draw against the wire\'s rated ampacity to check for adequate sizing.</p>'+
    '<div class="sim-io"><label>Wire rated ampacity (A)</label><input id="wa-rated" type="number" value="15">'+
    '<label>Expected circuit current (A)</label><input id="wa-load" type="number" value="10">'+
    '</div><button class="btn" onclick="wireAmpCalc()">Calculate</button><div id="wa-out"></div>';
}
function wireAmpCalc(){
  var rated=num('wa-rated'),load=num('wa-load');
  var out=document.getElementById('wa-out');
  if(rated===null||load===null||rated<=0||load<0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid rated ampacity and circuit current.</div>';return;}
  var margin=rated-load;
  var pct=(margin/rated*100);
  var msg=margin<0?'<p style="color:var(--fail)">Wire appears undersized - expected current exceeds rated ampacity!</p>':(pct<20?'<p style="color:var(--warn)">Low margin - consider upsizing the wire.</p>':'<p style="color:var(--ok)">Adequate margin for this load.</p>');
  out.innerHTML='<div class="sim-out">Ampacity margin: <b>'+margin.toFixed(1)+' A</b> ('+pct.toFixed(0)+'% of rated capacity)'+msg+
    '<br><span style="color:var(--txt2)">Always verify against the manufacturer\'s wire chart for bundle size, insulation type, and installation altitude/temperature.</span></div>';
}
/* Battery Capacity Check */
function simBattCap(b){
  b.innerHTML='<p>Compute a battery\'s remaining capacity percentage from a discharge test and compare it against a serviceability threshold.</p>'+
    '<div class="sim-io"><label>Rated capacity (amp-hours)</label><input id="bc-rated" type="number" value="25">'+
    '<label>Measured discharge (amp-hours)</label><input id="bc-meas" type="number" value="21">'+
    '<label>Serviceability threshold (%)</label><input id="bc-thresh" type="number" value="80">'+
    '</div><button class="btn" onclick="battCapCalc()">Calculate</button><div id="bc-out"></div>';
}
function battCapCalc(){
  var rated=num('bc-rated'),meas=num('bc-meas'),thresh=num('bc-thresh');
  var out=document.getElementById('bc-out');
  if(rated===null||meas===null||rated<=0||meas<0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid rated and measured capacity values.</div>';return;}
  var pct=meas/rated*100;
  var t=(thresh!=null&&thresh>0)?thresh:80;
  var msg=pct>=t?'<p style="color:var(--ok)">Battery meets the serviceability threshold.</p>':'<p style="color:var(--fail)">Battery is below the serviceability threshold - consider replacement.</p>';
  out.innerHTML='<div class="sim-out">Capacity: <b>'+pct.toFixed(1)+'%</b> of rated'+msg+
    '<br><span style="color:var(--txt2)">Always confirm the applicable serviceability threshold in the maintenance manual for this battery type.</span></div>';
}
/* Mixture Leaning Estimator */
function simMixLean(b){
  b.innerHTML='<p>Estimate a rough mixture-leaning guideline based on density altitude. Always follow the POH/AFM procedure and monitor EGT/CHT rather than leaning by feel alone.</p>'+
    '<div class="sim-io"><label>Density altitude (ft)</label><input id="ml-alt" type="number" value="6000">'+
    '</div><button class="btn" onclick="mixLeanCalc()">Calculate</button><div id="ml-out"></div>';
}
function mixLeanCalc(){
  var alt=num('ml-alt');
  var out=document.getElementById('ml-out');
  if(alt===null||alt<0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid density altitude.</div>';return;}
  var msg;
  if(alt<3000){msg='Leaning is generally not needed below about 3,000 ft density altitude - use full rich per POH guidance for most normally-aspirated engines.';}
  else{
    var leanPct=Math.min(((alt-3000)/1000)*3,25);
    msg='Approximate lean guideline: about <b>'+leanPct.toFixed(0)+'%</b> lean of full rich, increasing roughly with altitude above 3,000 ft.';
  }
  out.innerHTML='<div class="sim-out">'+msg+
    '<br><span style="color:var(--txt2)">This is a rough estimate only - always use the POH/AFM leaning procedure and monitor EGT/CHT instruments.</span></div>';
}
/* Jack Load Distribution */
function simJackLoad(b){
  b.innerHTML='<p>Estimate load sharing across a simple 3-point jacking setup (nose + two main gear points) from aircraft weight and CG position. This is a simplified estimate - always follow the aircraft-specific jacking procedure.</p>'+
    '<div class="sim-io"><label>Aircraft weight (lb)</label><input id="jl-w" type="number" value="12000">'+
    '<label>CG position (in aft of nose jack point)</label><input id="jl-cg" type="number" value="180">'+
    '<label>Main jack points distance aft of nose jack point (in)</label><input id="jl-main" type="number" value="220">'+
    '</div><button class="btn" onclick="jackLoadCalc()">Calculate</button><div id="jl-out"></div>';
}
function jackLoadCalc(){
  var w=num('jl-w'),cg=num('jl-cg'),main=num('jl-main');
  var out=document.getElementById('jl-out');
  if(w===null||cg===null||main===null||w<=0||main<=0||cg<0||cg>=main){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid values (CG must be between the nose jack point and the main jack points).</div>';return;}
  var noseLoad=w*(main-cg)/main;
  var mainTotal=w-noseLoad;
  var mainEach=mainTotal/2;
  out.innerHTML='<div class="sim-out">Estimated nose jack load: <b>'+noseLoad.toFixed(0)+' lb</b>'+
    '<br>Estimated load per main jack point: <b>'+mainEach.toFixed(0)+' lb</b> (main total: '+mainTotal.toFixed(0)+' lb)'+
    '<br><span style="color:var(--txt2)">Simplified moment-based estimate assuming a symmetric 3-point setup. Always verify against the aircraft maintenance manual\'s jacking procedure and rated jack capacities.</span></div>';
}
/* Turbine EGT Margin Tracker */
function simEGTMargin(b){
  b.innerHTML='<p>Compute the margin between current EGT and the redline limit at a stabilized power setting, and flag a shrinking trend versus a prior reading.</p>'+
    '<div class="sim-io"><label>EGT redline limit ( C or F, consistent unit)</label><input id="eg-limit" type="number" value="950">'+
    '<label>Current EGT reading</label><input id="eg-cur" type="number" value="880">'+
    '<label>Previous EGT reading at same power (optional)</label><input id="eg-prev" type="number" value="860">'+
    '</div><button class="btn" onclick="egtMarginCalc()">Calculate</button><div id="eg-out"></div>';
}
function egtMarginCalc(){
  var limit=num('eg-limit'),cur=num('eg-cur'),prev=num('eg-prev');
  var out=document.getElementById('eg-out');
  if(limit===null||cur===null||limit<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid limit and current EGT values.</div>';return;}
  var margin=limit-cur;
  var warn=margin<=0?'<p style="color:var(--fail)">Current EGT meets or exceeds the redline limit!</p>':(margin<50?'<p style="color:var(--warn)">Margin is getting low - monitor closely.</p>':'<p style="color:var(--ok)">Margin looks healthy.</p>');
  var trend='';
  if(prev!=null){
    var prevMargin=limit-prev;
    if(margin<prevMargin){
      trend='<br><p style="color:var(--warn)">Margin has shrunk since the previous reading (was '+prevMargin.toFixed(0)+', now '+margin.toFixed(0)+') - consider borescope inspection and trend review.</p>';
    }else{
      trend='<br><p style="color:var(--ok)">Margin is stable or improved versus the previous reading.</p>';
    }
  }
  out.innerHTML='<div class="sim-out">EGT margin: <b>'+margin.toFixed(0)+'</b>'+warn+trend+
    '<br><span style="color:var(--txt2)">Compare readings only at comparable, stabilized power settings for a meaningful trend.</span></div>';
}
function simBondRes(b){
  b.innerHTML='<p>Enter a measured bonding resistance and the bonding type to check it against typical pass/fail thresholds. Always confirm against the aircraft-specific manual value.</p>'+
    '<div class="sim-io"><label>Measured resistance (ohms)</label><input id="bd-res" type="number" step="0.0001" value="0.002">'+
    '<label>Bonding type</label><select id="bd-type"><option value="fuel">Fuel-system bonding (strict)</option><option value="general">General structure bonding</option></select>'+
    '</div><button class="btn" onclick="bondResCalc()">Check</button><div id="bd-out"></div>';
}
function bondResCalc(){
  var res=num('bd-res');
  var type=document.getElementById('bd-type').value;
  var out=document.getElementById('bd-out');
  if(res===null||res<0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter a valid resistance value.</div>';return;}
  var limit=type==='fuel'?0.003:0.1;
  var pass=res<=limit;
  var msg=pass?'<p style="color:var(--ok)">PASS - within typical '+limit.toFixed(4)+' ohm threshold for this bonding type.</p>':'<p style="color:var(--fail)">FAIL - exceeds typical '+limit.toFixed(4)+' ohm threshold. Clean and re-torque the bonding attachment, then re-test.</p>';
  out.innerHTML='<div class="sim-out">Measured: <b>'+res.toFixed(4)+' ohms</b><br>'+msg+
    '<br><span style="color:var(--txt2)">Use the aircraft maintenance manual value when available - this is a general reference threshold only.</span></div>';
}
function simFabTest(b){
  b.innerHTML='<p>Compare a punch-tester fabric strength reading against the minimum required strength to estimate remaining margin.</p>'+
    '<div class="sim-io"><label>Punch tester reading (lbs)</label><input id="fb-read" type="number" value="60">'+
    '<label>Minimum required strength (lbs)</label><input id="fb-min" type="number" value="50">'+
    '</div><button class="btn" onclick="fabTestCalc()">Calculate</button><div id="fb-out"></div>';
}
function fabTestCalc(){
  var reading=num('fb-read'),minReq=num('fb-min');
  var out=document.getElementById('fb-out');
  if(reading===null||minReq===null||minReq<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid reading and minimum strength values.</div>';return;}
  var margin=reading-minReq;
  var msg=margin>0?'<p style="color:var(--ok)">Airworthy - fabric strength is above the minimum required.</p>':'<p style="color:var(--fail)">NOT airworthy - fabric strength is at or below the minimum required. The aircraft must be re-covered before further flight.</p>';
  out.innerHTML='<div class="sim-out">Margin: <b>'+margin.toFixed(0)+' lbs</b><br>'+msg+
    '<br><span style="color:var(--txt2)">A low or negative margin requires re-covering even if the fabric looks visually sound.</span></div>';
}
function simBoostMargin(b){
  b.innerHTML='<p>Compare current manifold pressure against the redline limit to estimate overboost margin at a given altitude/power condition.</p>'+
    '<div class="sim-io"><label>Manifold pressure redline limit (inHg)</label><input id="bm-limit" type="number" value="36">'+
    '<label>Current manifold pressure reading (inHg)</label><input id="bm-cur" type="number" value="33">'+
    '</div><button class="btn" onclick="boostMarginCalc()">Calculate</button><div id="bm-out"></div>';
}
function boostMarginCalc(){
  var limit=num('bm-limit'),cur=num('bm-cur');
  var out=document.getElementById('bm-out');
  if(limit===null||cur===null||limit<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid limit and current manifold pressure values.</div>';return;}
  var margin=limit-cur;
  var msg=margin<=0?'<p style="color:var(--fail)">Manifold pressure meets or exceeds the redline limit - overboost condition!</p>':(margin<2?'<p style="color:var(--warn)">Margin is low - check wastegate operation.</p>':'<p style="color:var(--ok)">Margin looks healthy.</p>');
  out.innerHTML='<div class="sim-out">Overboost margin: <b>'+margin.toFixed(1)+' inHg</b><br>'+msg+
    '<br><span style="color:var(--txt2)">Compare readings only at the same altitude and power condition for a meaningful trend.</span></div>';
}
function simFuelDensity(b){
  b.innerHTML='<p>Convert a fuel volume reading into weight using actual fuel density for accurate weight and balance cross-checks.</p>'+
    '<div class="sim-io"><label>Fuel volume (gallons)</label><input id="fd-vol" type="number" value="50">'+
    '<label>Fuel density (lbs/gallon)</label><input id="fd-density" type="number" step="0.1" value="6.0">'+
    '</div><button class="btn" onclick="fuelDensityCalc()">Calculate</button><div id="fd-out"></div>';
}
function fuelDensityCalc(){
  var vol=num('fd-vol'),density=num('fd-density');
  var out=document.getElementById('fd-out');
  if(vol===null||density===null||vol<0||density<=0){out.innerHTML='<div class="sim-out" style="color:var(--fail)">Enter valid volume and density values.</div>';return;}
  var weight=vol*density;
  out.innerHTML='<div class="sim-out">Fuel weight: <b>'+weight.toFixed(1)+' lbs</b>'+
    '<br><span style="color:var(--txt2)">Always use actual measured or provided density - it varies with temperature and fuel batch.</span></div>';
}
/* ---------- REFERENCE LIBRARY ---------- */
var _refCat='All';
function refCats(){var s={};REFERENCE.forEach(function(r){s[r.cat]=1;});return ['All'].concat(Object.keys(s));}
function setRefCat(c){_refCat=c;renderReference();}
function printReference(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf('reference')<0){S.exportsUsed.push('reference');if(typeof checkDocumentarian==='function')checkDocumentarian();persist();}
  var h='<h1>Aviation Reference Library</h1>';
  h+='<p class="pf-meta">'+REFERENCE.length+' cards &middot; '+new Date().toLocaleDateString()+'</p>';
  h+='<div>'+REFERENCE.map(function(r){return '<b>'+r.title+'</b> ('+r.cat+')<br>'+r.body;}).join('<br><br>')+'</div>';
  printDoc('Aviation Reference Library', h);
}
function renderReference(){
  var starCt=(S.refStars||[]).length;
  var h='<div class="card"><h2>&#x1F4DA; Reference Library</h2><p style="color:var(--txt2)">Quick shop cheat-sheets. Filter by category.</p><div class="ref-cats">';
  refCats().forEach(function(c){h+='<button class="ref-cat'+(c===_refCat?' active':'')+'" onclick="setRefCat(\''+c+'\')">'+c+'</button>';});
  h+='</div><button class="btn btn-sec" style="margin-top:0.5rem" onclick="printReference()">&#x1F5A8; Print / Save as PDF</button> ';
  h+='<button class="btn btn-sec" onclick="toggleRefStarFilter()">'+(_refStarOnly?'&#x1F501; Show All':'&#x2B50; Starred Only ('+starCt+')')+'</button></div>';
  REFERENCE.map(function(r,idx){return {r:r,idx:idx};}).filter(function(x){return (_refCat==='All'||x.r.cat===_refCat)&&(!_refStarOnly||(S.refStars||[]).indexOf(x.idx)>=0);}).forEach(function(x){
    var r=x.r,idx=x.idx;
    var starred=(S.refStars||[]).indexOf(idx)>=0;
    h+='<div class="card ref-card"><h3>'+r.title+' <span class="track-chip" style="background:var(--bg3);font-size:.7rem">'+r.cat+'</span> <span style="cursor:pointer" onclick="toggleRefStar('+idx+')">'+(starred?'&#x2B50;':'&#x2606;')+'</span></h3><div class="section-body">'+r.body+'</div></div>';
  });
  document.getElementById('reference-content').innerHTML=h;
  show('v-reference');
}
var _refStarOnly=false;
function toggleRefStarFilter(){_refStarOnly=!_refStarOnly;renderReference();}
function toggleRefStar(idx){
  if(!S.refStars)S.refStars=[];
  var i=S.refStars.indexOf(idx);
  if(i>=0)S.refStars.splice(i,1);else S.refStars.push(idx);
  if((S.refStars.length+(S.glossStars||[]).length)>=5&&typeof checkAch==='function')checkAch('curator');
  persist();
  renderReference();
}

/* ---------- GLOBAL SEARCH ---------- */
var _tagRe=new RegExp('[<][^>]+[>]','g');
function stripTags(s){return (s||'').replace(_tagRe,' ');}
function escRe(s){return s.replace(new RegExp('[.*+?^${}()|[\\]\\\\]','g'),'\\$&');}
function hl(text,q){if(!q)return text;try{return text.replace(new RegExp('('+escRe(q)+')','ig'),'<mark>$1</mark>');}catch(e){return text;}}
function snippet(text,q){var t=stripTags(text);var i=t.toLowerCase().indexOf(q.toLowerCase());if(i<0)return t.slice(0,120);var s=Math.max(0,i-40);return (s>0?'...':'')+t.slice(s,s+140)+'...';}
function buildSearchIndex(){
  var idx=[];
  MODS.forEach(function(m){
    var body=m.sections.map(function(s){return s.heading+' '+s.body;}).join(' ');
    idx.push({type:'Module',label:m.title,text:m.title+' '+body,go:'openModule(\''+m.id+'\')'});
  });
  GLOSSARY.forEach(function(g){idx.push({type:'Glossary',label:g.term,text:g.term+' '+g.def,inline:g.def,go:'renderGloss()'});});
  REFERENCE.forEach(function(r){idx.push({type:'Reference',label:r.title,text:r.title+' '+r.cat+' '+r.body,inline:r.body,go:'renderReference()'});});
  SIMS.forEach(function(s){idx.push({type:'Sim',label:s.title,text:s.title+' '+s.desc,go:'openSim(\''+s.id+'\')'});});
    (typeof ORAL_QUESTIONS!=='undefined'?ORAL_QUESTIONS:[]).forEach(function(o,i){idx.push({type:'Mock Oral',label:o.prompt.slice(0,60)+(o.prompt.length>60?'...':''),text:o.prompt+' '+o.answer,inline:o.answer,go:'renderOral()'});});
  (typeof PRACTICAL_TASKS!=='undefined'?PRACTICAL_TASKS:[]).forEach(function(t){idx.push({type:'Practical Task',label:t.title,text:t.title+' '+t.cat+' '+t.desc,inline:t.desc,go:'renderPractical()'});});
  (typeof FLASHCARDS!=='undefined'?FLASHCARDS:[]).forEach(function(f){idx.push({type:'Flashcard',label:f.front,text:f.front+' '+f.back,inline:f.back,go:'renderFlash()'});});
  return idx;
}
function runSearch(q){
  q=(q||'').trim();
  var out=document.getElementById('search-results');
  if(q.length<2){out.innerHTML='<p style="color:var(--txt2)">Type at least 2 characters...</p>';return;}
  var ql=q.toLowerCase();
  var hits=buildSearchIndex().filter(function(it){return it.text.toLowerCase().indexOf(ql)>=0;}).slice(0,40);
  if(!hits.length){out.innerHTML='<p style="color:var(--txt2)">No matches for "'+q+'".</p>';return;}
  var h='<p style="color:var(--txt2)">'+hits.length+' result(s)</p>';
  hits.forEach(function(it){
    var sn=it.inline?stripTags(it.inline):snippet(it.text,q);
    h+='<div class="search-hit" onclick="'+it.go.replace(/"/g,'&quot;')+'"><span class="tag">'+it.type+'</span><b>'+hl(it.label,q)+'</b><div style="font-size:.85rem;color:var(--txt2)">'+hl(sn,q)+'</div></div>';
  });
  out.innerHTML=h;
}
function renderSearch(){
  document.getElementById('search-content').innerHTML='<div class="card"><h2>&#x1F50D; Search</h2><input class="search-box" id="search-input" placeholder="Search modules, glossary, reference, sims..." oninput="runSearch(this.value)"><div id="search-results" style="margin-top:1rem"><p style="color:var(--txt2)">Type at least 2 characters...</p></div></div>';
  show('v-search');
  var el=document.getElementById('search-input');if(el)el.focus();
}

/* ---------- COMMAND PALETTE (Ctrl+K) ---------- */
var _cmds=[
  {n:'Dashboard',i:'&#x1F3E0;',go:function(){show('v-dash');renderDash();}},
  {n:'Lab Sims',i:'&#x1F9EA;',go:renderSims},
  {n:'Reference Library',i:'&#x1F4DA;',go:renderReference},
  {n:'Flashcards',i:'&#x1F0CF;',go:function(){renderFlash();}},
  {n:'Glossary',i:'&#x1F4D6;',go:function(){renderGloss();}},
  {n:'Achievements',i:'&#x1F3C5;',go:function(){renderAch();}},
  {n:'Final Exam',i:'&#x1F393;',go:function(){renderExam();}},
  {n:'Certificate',i:'&#x1F3C6;',go:function(){renderCert();}},
  {n:'Subject Practice Tests',i:'&#x23F1;',go:function(){renderSubTests();}},
  {n:'Mock Oral Exam',i:'&#x1F3A4;',go:function(){renderOral();}},
  {n:'Practical Task Log',i:'&#x1F527;',go:function(){renderPractical();}},
  {n:'Cram Weak Areas',i:'&#x1F525;',go:function(){startCramQuiz();}},
  {n:'Review Missed Questions',i:'&#x1F3AF;',go:function(){renderReview();}},
  {n:'My Profile',i:'&#x1F464;',go:function(){renderProfile();}},
  {n:'Team Roster',i:'&#x1F465;',go:function(){renderRoster();}},
  {n:'Search',i:'&#x1F50D;',go:renderSearch},
  {n:'Toggle theme',i:'&#x1F313;',go:function(){toggleTheme();}}
];
var _cmdSel=0,_cmdList=[];
function cmdOpen(){
  MODS.forEach(function(m){_cmds.push({n:'Open: '+m.title,i:m.icon,go:function(){openModule(m.id);}});});
  _cmds=_cmds.filter(function(c,i){return _cmds.findIndex(function(x){return x.n===c.n;})===i;});
  document.getElementById('cmdp').classList.add('on');
  var inp=document.getElementById('cmdp-input');inp.value='';inp.focus();cmdFilter('');
}
function cmdClose(){document.getElementById('cmdp').classList.remove('on');}
function cmdFilter(q){
  q=(q||'').toLowerCase();
  _cmdList=_cmds.filter(function(c){return c.n.toLowerCase().indexOf(q)>=0;}).slice(0,10);
  _cmdSel=0;cmdPaint();
}
function cmdPaint(){
  var h='';_cmdList.forEach(function(c,i){h+='<div class="ci'+(i===_cmdSel?' sel':'')+'" onclick="cmdRun('+i+')">'+c.i+' '+c.n+'</div>';});
  document.getElementById('cmdp-res').innerHTML=h||'<div class="ci">No commands</div>';
}
function cmdRun(i){var c=_cmdList[i];cmdClose();if(c)c.go();}
document.addEventListener('keydown',function(e){
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();cmdOpen();return;}
  var p=document.getElementById('cmdp');if(!p||!p.classList.contains('on'))return;
  if(e.key==='Escape')cmdClose();
  else if(e.key==='ArrowDown'){e.preventDefault();_cmdSel=Math.min(_cmdSel+1,_cmdList.length-1);cmdPaint();}
  else if(e.key==='ArrowUp'){e.preventDefault();_cmdSel=Math.max(_cmdSel-1,0);cmdPaint();}
  else if(e.key==='Enter')cmdRun(_cmdSel);
});

// ---- Print / PDF export ----
function printDoc(title, bodyHtml){
  var w=window.open('', '_blank');
  if(!w){alert('Please allow popups for this page to print/export a PDF.');return;}
  var css='body{font-family:system-ui,-apple-system,sans-serif;color:#111;background:#fff;max-width:800px;margin:0 auto;padding:2rem;line-height:1.65}'+
    'h1{border-bottom:3px solid #3b82f6;padding-bottom:0.5rem;margin-bottom:0.5rem}'+
    'h2{color:#1e40af;margin-top:1.6rem;margin-bottom:0.4rem}'+
    'h3{color:#b45309;margin-top:1rem;margin-bottom:0.3rem}'+
    'ul,ol{margin-left:1.5rem}p{margin:0.4rem 0}'+
    '.pf-mod{margin-bottom:2rem;page-break-inside:avoid}'+
    '.pf-meta{color:#555;font-size:0.9rem;margin-bottom:1rem}'+
    '.pf-foot{margin-top:2rem;font-size:0.75rem;color:#666;border-top:1px solid #ccc;padding-top:0.5rem}'+
    '@media print{a{color:#111;text-decoration:none}}';
  var html='<!DOCTYPE html><html><head><meta charset="UTF-8"><title>'+title+'</title><style>'+css+'</style></head><body>'+
    bodyHtml+
    '<div class="pf-foot">Generated by Aviation Maintenance Academy &middot; '+new Date().toLocaleDateString()+
    ' &middot; Educational use only &mdash; not a substitute for FAA-approved data or certification.</div>'+
    '<script>window.onload=function(){window.print();};<\/script>'+
    '</body></html>';
  w.document.open();
  w.document.write(html);
  w.document.close();
}
function printModule(id){
  var m=MODS.find(function(x){return x.id===id;});
  if(!m)return;
  var h='<h1>'+m.title+'</h1><p class="pf-meta">Aviation Maintenance Academy &mdash; Study Notes</p>';
  if(m.faa_ref)h+='<p class="pf-meta">Reference: '+esc(m.faa_ref)+'</p>';
  m.sections.forEach(function(sec){
    h+='<h2>'+sec.heading+'</h2><div>'+sec.body+'</div>';
  });
  printDoc(m.title+' - Study Notes', '<div class="pf-mod">'+h+'</div>');
}
function stripHtml(str){
  return (''+(str==null?'':str)).replace(/<[^>]*>/g,' ').replace(/&amp;/g,'&').replace(/&#x[0-9A-Fa-f]+;/g,' ').replace(/&[a-z]+;/g,' ').replace(/\s+/g,' ').trim();
}
function readAloud(id){
  if(typeof window==='undefined'||!window.speechSynthesis||typeof SpeechSynthesisUtterance==='undefined')return;
  var m=MODS.find(function(x){return x.id===id;});
  if(!m)return;
  window.speechSynthesis.cancel();
  var text=m.title+'. ';
  m.sections.forEach(function(sec){text+=stripHtml(sec.heading)+'. '+stripHtml(sec.body)+' ';});
  var u=new SpeechSynthesisUtterance(text);
  u.rate=0.98;
  window.speechSynthesis.speak(u);
}
function stopReadAloud(){
  if(typeof window!=='undefined'&&window.speechSynthesis)window.speechSynthesis.cancel();
}
function checkDocumentarian(){
  var req=['glossary','studyguide','notes'];
  var have=S.exportsUsed||[];
  if(req.every(function(r){return have.indexOf(r)>=0;})&&typeof checkAch==='function')checkAch('documentarian');
}
function printOralBank(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf("oral")<0){S.exportsUsed.push("oral");if(typeof checkDocumentarian==="function")checkDocumentarian();persist();}
  var cats=[...new Set(ORAL_QUESTIONS.map(function(q){return q.cat||"General";}))];
  var h="<h1>Mock Oral Exam Study Sheet</h1>";
  h+="<p class=\"pf-meta\">"+ORAL_QUESTIONS.length+" prompts &middot; "+new Date().toLocaleDateString()+"</p>";
  h+=cats.map(function(cat){
    var qs=ORAL_QUESTIONS.filter(function(q){return (q.cat||"General")===cat;});
    return "<h2>"+cat+"</h2>"+qs.map(function(q){return "<p><b>Q:</b> "+q.prompt+"<br><b>A:</b> "+(q.answer||"")+"</p>";}).join("");
  }).join("");
  printDoc("Mock Oral Exam Study Sheet", h);
}
function printGlossary(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf('glossary')<0){S.exportsUsed.push('glossary');checkDocumentarian();persist();}
  var h='<h1>Aviation Maintenance Glossary</h1>';
  h+='<p class="pf-meta">'+GLOSSARY.length+' terms &middot; '+new Date().toLocaleDateString()+'</p>';
  h+='<div>'+GLOSSARY.map(function(g){return '<b>'+g.term+'</b> &mdash; '+g.def;}).join('<br><br>')+'</div>';
  printDoc('Aviation Maintenance Glossary', h);
}
function printCertificate(){
  var r=(typeof readinessScore==='function')?readinessScore():{total:0};
  var allModsDone=MODS.length>0&&S.done.length>=MODS.length;
  var u=(typeof curUser==='function'&&curUser())?curUser().name:'Aviation Maintenance Student';
  var h='<div style="text-align:center;border:4px double #1e40af;padding:2.5rem 2rem;border-radius:12px">';
  h+='<h1 style="border:none;font-size:1.6rem;letter-spacing:2px">CERTIFICATE OF COMPLETION</h1>';
  h+='<p style="color:#555;margin-top:0.5rem">Aviation Maintenance Academy</p>';
  h+='<p style="margin:1.8rem 0 0.3rem;font-size:1.1rem">This certifies that</p>';
  h+='<p style="font-size:1.8rem;font-weight:700;color:#1e40af;margin:0.3rem 0">'+esc(u)+'</p>';
  h+='<p style="margin:0.3rem 0 1.8rem">has completed all '+MODS.length+' modules of the General, Airframe, and Powerplant curriculum';
  h+=(S.examPassed?' and passed the Final Exam with a score of '+S.examScore+'%':'')+'.</p>';
  h+='<p style="color:#555">Overall Exam Readiness at completion: <b>'+r.total+'%</b></p>';
  h+='<p style="margin-top:2rem;color:#555;font-size:0.9rem">Issued '+new Date().toLocaleDateString()+'</p>';
  h+='<p style="margin-top:1.5rem;font-size:0.75rem;color:#888">This certificate reflects self-paced study progress in the Aviation Maintenance Academy app and is not an FAA credential. FAA A&amp;P certification requires passing the official FAA Knowledge Tests and an Oral &amp; Practical exam with a Designated Mechanic Examiner (DME).</p>';
  h+='</div>';
  if(!allModsDone){
    h='<p style="color:#b91c1c">You have not yet completed all '+MODS.length+' modules ('+S.done.length+'/'+MODS.length+' done). Finish every module to unlock your full certificate.</p>'+h;
  }
  printDoc('Aviation Maintenance Academy Certificate of Completion', h);
}
function printAchievements(){
  var earned=ACHIEVEMENTS.filter(function(a){return S.achievements.includes(a.id);});
  var locked=ACHIEVEMENTS.filter(function(a){return !S.achievements.includes(a.id);});
  var h='<h1>Aviation Maintenance Academy &mdash; Achievements</h1>';
  h+='<p class="pf-meta">'+earned.length+' / '+ACHIEVEMENTS.length+' unlocked &middot; '+new Date().toLocaleDateString()+'</p>';
  h+='<h2>Unlocked</h2>';
  h+=earned.length?('<ul>'+earned.map(function(a){return '<li><b>'+a.name+'</b> &mdash; '+a.desc+'</li>';}).join('')+'</ul>'):'<p>None yet &mdash; keep studying!</p>';
  h+='<h2>Still Locked</h2>';
  h+=locked.length?('<ul>'+locked.map(function(a){return '<li><b>'+a.name+'</b> &mdash; '+a.desc+'</li>';}).join('')+'</ul>'):'<p>All achievements unlocked &mdash; nice work!</p>';
  printDoc('Aviation Maintenance Academy Achievements', h);
}
function printNotes(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf('notes')<0){S.exportsUsed.push('notes');checkDocumentarian();persist();}
  var noted=Object.keys(S.notes||{}).filter(function(id){return (S.notes[id]||'').trim().length>0;});
  var h='<h1>My Aviation Maintenance Notes</h1>';
  h+='<p class="pf-meta">'+noted.length+' module'+(noted.length===1?'':'s')+' with notes &middot; '+new Date().toLocaleDateString()+'</p>';
  if(!noted.length){
    h+='<p><i>No notes saved yet &mdash; add notes while studying a module to see them here.</i></p>';
  }
  noted.forEach(function(id){
    var m=MODS.find(function(x){return x.id===id;});
    var title=m?m.title:id;
    h+='<div class="pf-mod"><h2>'+title+'</h2><div>'+(S.notes[id]||'').replace(/\n/g,'<br>')+'</div></div>';
  });
  printDoc('My Aviation Maintenance Notes', h);
}
function printBookmarks(){
  var bm=S.bookmarks||[];
  var h='<h1>My Bookmarked Flashcards</h1>';
  h+='<p class="pf-meta">'+bm.length+' bookmarked card'+(bm.length===1?'':'s')+' &middot; '+new Date().toLocaleDateString()+'</p>';
  if(!bm.length){
    h+='<p><i>No bookmarked flashcards yet &mdash; star a card while studying to add it here.</i></p>';
  }
  bm.forEach(function(idx){
    var fc=FLASHCARDS[idx];if(!fc)return;
    h+='<div class="pf-mod"><h2>'+esc(fc.front)+'</h2><div>'+fc.back+'</div></div>';
  });
  printDoc('My Bookmarked Flashcards', h);
}
function printStudyGuide(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf('studyguide')<0){S.exportsUsed.push('studyguide');checkDocumentarian();persist();}
  var doneMods=MODS.filter(function(m){return S.done.includes(m.id);});
  var r=getRank();
  var h='<h1>My Aviation Maintenance Study Guide</h1>';
  h+='<p class="pf-meta">'+doneMods.length+' of '+MODS.length+' modules completed &middot; '+S.xp+' XP &middot; Rank: '+r.name+' &middot; '+new Date().toLocaleDateString()+'</p>';
  if(!doneMods.length){
    h+='<p><i>No modules completed yet &mdash; mark lessons read in a module to add it here.</i></p>';
  }
  doneMods.forEach(function(m){
    h+='<div class="pf-mod"><h2>'+m.title+'</h2>';
    if(m.faa_ref)h+='<p class="pf-meta">Reference: '+esc(m.faa_ref)+'</p>';
    m.sections.forEach(function(sec){
      h+='<h3>'+sec.heading+'</h3><div>'+sec.body+'</div>';
    });
    h+='</div>';
  });
  h+='<div class="pf-mod"><h2>Glossary</h2><div>'+GLOSSARY.map(function(g){return '<b>'+g.term+'</b> &mdash; '+g.def;}).join('<br>')+'</div></div>';
  printDoc('Aviation Maintenance Study Guide', h);
}

function printPracticalLog(){
  if(!S.exportsUsed)S.exportsUsed=[];
  if(S.exportsUsed.indexOf('practicallog')<0){S.exportsUsed.push('practicallog');checkDocumentarian();persist();}
  var log=S.practicalLog||{};
  var loggedCount=Object.keys(log).length;
  var h='<h1>Practical Task Log</h1>';
  h+='<p class="pf-meta">'+loggedCount+' of '+PRACTICAL_TASKS.length+' ACS-style tasks logged &middot; '+new Date().toLocaleDateString()+'</p>';
  h+='<p><i>This is a personal training/experience record for self-tracking purposes only &mdash; it is not an official FAA logbook entry, endorsement, or sign-off. Have a supervising mechanic/DME co-sign the notes column where applicable.</i></p>';
  ['General','Airframe','Powerplant'].forEach(function(cat){
    var items=PRACTICAL_TASKS.filter(function(t){return t.cat===cat;});
    h+='<div class="pf-mod"><h2>'+cat+'</h2>';
    items.forEach(function(t){
      var entry=log[t.id];
      h+='<div style="margin-bottom:0.8rem"><h3>'+(entry?'&#x2611;':'&#x2610;')+' '+esc(t.title)+'</h3>';
      h+='<p>'+esc(t.desc)+'</p>';
      if(entry){
        h+='<p class="pf-meta">Completed: '+esc(entry.date)+(entry.notes?' &middot; Notes: '+esc(entry.notes):'')+'</p>';
      }else{
        h+='<p class="pf-meta">Date completed: __________________&nbsp;&nbsp;&nbsp;&nbsp;Signature: __________________</p>';
      }
      h+='</div>';
    });
    h+='</div>';
  });
  printDoc('Practical Task Log', h);
}

function printSubTestReport(){
  var r=window._subLastReport;
  if(!r){alert('Complete a Subject Test first to generate a score report.');return;}
  var h='<h1>'+esc(r.trackName)+' Subject Test Score Report</h1>';
  h+='<p class="pf-meta">'+r.date+' &middot; Overall: '+r.score+'/'+r.total+' ('+r.pct+'%) &middot; '+(r.pct>=70?'PASSED':'Below 70% \u2014 not yet passing')+'</p>';
  h+='<div class="pf-mod"><h2>Score by Subject Area</h2>';
  r.areaRows.forEach(function(a){
    h+='<p>'+(a.pct>=70?'&#x2611;':'&#x2610;')+' <b>'+esc(a.title)+'</b> \u2014 '+a.correct+'/'+a.total+' ('+a.pct+'%)</p>';
  });
  h+='</div>';
  var weak=r.areaRows.filter(function(a){return a.pct<70;});
  if(weak.length){
    h+='<p><i>Recommended focus before your DME appointment: '+weak.map(function(a){return esc(a.title);}).join(', ')+'.</i></p>';
  }
  printDoc(r.trackName+' Subject Test Score Report', h);
}

function printExamReport(){
  var r=window._examLastReport;
  if(!r){alert('Complete the Final Exam first to generate a score report.');return;}
  var h='<h1>Final Exam Score Report</h1>';
  h+='<p class="pf-meta">'+r.date+' &middot; Overall: '+r.score+'/'+r.total+' ('+r.pct+'%) &middot; '+(r.pct>=80?'PASSED':'Below 80% \u2014 not yet passing')+'</p>';
  h+='<div class="pf-mod"><h2>Score by Subject Area</h2>';
  r.areaRows.forEach(function(a){
    h+='<p>'+(a.pct>=70?'&#x2611;':'&#x2610;')+' <b>'+esc(a.title)+'</b> \u2014 '+a.correct+'/'+a.total+' ('+a.pct+'%)</p>';
  });
  h+='</div>';
  var weak=r.areaRows.filter(function(a){return a.pct<70;});
  if(weak.length){
    h+='<p><i>Recommended focus for retake/continued study: '+weak.map(function(a){return esc(a.title);}).join(', ')+'.</i></p>';
  }
  printDoc('Final Exam Score Report', h);
}

function printReadinessReport(){
  var r=readinessScore();
  var doneMods=MODS.filter(function(m){return S.done.includes(m.id);});
  var h='<h1>Exam Readiness Report</h1>';
  h+='<p class="pf-meta">'+new Date().toLocaleDateString()+' &middot; Overall Readiness: '+r.total+'% ('+r.label+')</p>';
  h+='<div class="pf-mod"><h2>Readiness Pillars</h2>';
  h+='<p>Modules Completed: '+r.modPct+'% ('+doneMods.length+'/'+MODS.length+')</p>';
  h+='<p>Quiz Average: '+r.quizAvg+'%</p>';
  h+='<p>Subject Tests Passed: '+r.subjPct+'% ('+['general','airframe','powerplant'].filter(function(id){return (S.subjectPassed||{})[id];}).length+'/3)</p>';
  h+='<p>Mock Oral Best Score: '+r.oralPct+'%</p>';
  h+='<p>Practical Tasks Logged: '+r.practicalPct+'% ('+Object.keys(S.practicalLog||{}).length+'/'+(typeof PRACTICAL_TASKS!=='undefined'?PRACTICAL_TASKS.length:0)+')</p>';
  h+='<p>Final Exam: '+r.examPct+'%'+(S.examPassed?' (PASSED)':'')+'</p></div>';
  var sp=S.subjectPassed||{};
  var subjLines=['general','airframe','powerplant'].filter(function(id){return sp[id]!==undefined;});
  if(subjLines.length){
    h+='<div class="pf-mod"><h2>Subject Test Scores</h2>';
    subjLines.forEach(function(id){
      var t=TRACKS.find(function(x){return x.id===id;});
      h+='<p>'+(t?t.name:id)+': '+sp[id]+'%'+(sp[id]>=70?' ✅':'')+'</p>';
    });
    h+='</div>';
  }
  if(S.oralBest!==undefined&&S.oralBest>0){
    h+='<div class="pf-mod"><h2>Mock Oral</h2><p>Best self-graded score: '+S.oralBest+'%</p></div>';
  }
  var log=S.practicalLog||{};
  var loggedCount=Object.keys(log).length;
  if(typeof PRACTICAL_TASKS!=='undefined'&&loggedCount){
    h+='<div class="pf-mod"><h2>Practical Task Log</h2><p>'+loggedCount+' of '+PRACTICAL_TASKS.length+' ACS-style tasks logged.</p>';
    h+='<p class="pf-meta">See the full Practical Task Log export for task-by-task details and sign-off lines.</p></div>';
  }
  var weakestArea=[
    {label:'Modules',val:r.modPct},
    {label:'Quiz average',val:r.quizAvg},
    {label:'Subject tests',val:r.subjPct},
    {label:'Mock Oral',val:r.oralPct},
    {label:'Practical tasks',val:r.practicalPct},
    {label:'Final Exam',val:r.examPct}
  ].sort(function(a,b){return a.val-b.val;})[0];
  h+='<div class="pf-mod"><h2>Recommended Focus</h2><p>Your lowest readiness pillar is <b>'+weakestArea.label+'</b> at <b>'+weakestArea.val+'%</b>. Prioritize this area before your DME appointment.</p></div>';
  h+='<p class="pf-foot">This report is a personal training/self-assessment summary generated by the Aviation Maintenance Academy app. It is not an official FAA document, endorsement, or sign-off.</p>';
  printDoc('Exam Readiness Report', h);
}

function exportFlashcardsCSV(){
  var rows=[['Front','Back']];
  FLASHCARDS.forEach(function(c){rows.push([c.front,c.back]);});
  var csv=rows.map(function(r){return r.map(function(v){return '"'+(''+v).replace(/"/g,'""')+'"';}).join(',');}).join('\n');
  var a=document.createElement('a');a.href='data:text/csv;charset=utf-8,'+encodeURIComponent(csv);a.download='aviation_flashcards.csv';a.click();
}

function printMasteryReport(){
  var h='<h1>Mastery Report</h1>';
  h+='<p class="pf-meta">'+new Date().toLocaleDateString()+' &middot; Average quiz score per track, based on completed module quizzes.</p>';
  TRACKS.forEach(function(t){
    var modIds=t.modules;
    var scores=modIds.map(function(id){return S.quizScores[id];}).filter(function(s){return s!==undefined;});
    var avg=scores.length?Math.round(scores.reduce(function(a,b){return a+b;},0)/scores.length):null;
    h+='<div class="pf-mod"><h2>'+t.name+'</h2>';
    if(avg===null){h+='<p>No quizzes completed yet in this track.</p></div>';return;}
    h+='<p>'+avg+'% average across '+scores.length+'/'+modIds.length+' quizzed modules</p>';
    var modRows=modIds.map(function(id){var m=MODS.find(function(x){return x.id===id;});return {m:m,score:S.quizScores[id]};}).filter(function(r){return r.m&&r.score!==undefined;}).sort(function(a,b){return a.score-b.score;});
    if(modRows.length){
      h+='<p><b>Per-module breakdown (weakest first):</b></p>';
      modRows.forEach(function(row){h+='<p>'+row.m.title+': '+row.score+'%</p>';});
    }
    h+='</div>';
  });
  printDoc('Mastery Report', h);
}

function printMissedReview(){
  var items=(typeof missedList==='function')?missedList():[];
  var h='<h1>Review Missed Questions</h1>';
  h+='<p class="pf-meta">'+new Date().toLocaleDateString()+' &middot; '+items.length+' question(s) currently missed</p>';
  items.forEach(function(it){
    h+='<div class="pf-mod"><p class="pf-meta">'+it.modTitle+'</p><p><b>'+it.q.q+'</b></p>';
    h+='<p>Correct answer: '+it.q.choices[it.q.answer]+'</p>';
    if(it.q.explain)h+='<p>'+it.q.explain+'</p>';
    h+='</div>';
  });
  printDoc('Review Missed Questions', h);
}

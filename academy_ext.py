"""Aviation Maintenance Academy - Expansion Content Pack (modules, cards, glossary)"""

EXT_MODULES = [
  {
    "id": "ground_ops", "title": "Ground Operations & Servicing", "track": "general", "icon": "&#x1F6E0;",
    "sections": [
      {"heading": "Ramp Safety & Marshalling", "body": "Standard hand signals for taxi/tow. Wing-walkers for clearance. Keep clear of intake <b>hazard (suction)</b> and exhaust <b>blast</b> zones - a turbine intake can ingest a person. Chock wheels before any servicing. Never approach a turning prop or rotor."},
      {"heading": "Fueling & Defueling", "body": "<b>Bonding and grounding first</b> to dissipate static (fire risk). Jet-A vs Avgas - never mix; check color (Avgas 100LL = blue). Fuel-truck or single-point pressure fueling. Watch for water contamination - <b>sump drains</b> checked for water/sediment."},
      {"heading": "Servicing Fluids & Gases", "body": "Oil, hydraulic fluid (correct spec - never mix Skydrol with mineral!), oxygen (<b>NO petroleum near O2 - explosion</b>), nitrogen for tires/struts/accumulators. Servicing carts and correct fittings. Bleed air precautions."},
      {"heading": "Jacking, Hoisting, Towing", "body": "Use approved <b>jack points</b> only; stabilize with tail stand. Weight-on-wheels considerations. Tow bar rated for aircraft; do not exceed nosewheel steering limits (bypass pin). Never leave a jacked aircraft unattended."},
      {"heading": "Tie-down & Cold Weather", "body": "Secure into wind; control locks/gust locks installed. Ground de-icing: Type I (heated, deice) vs Type IV (anti-ice, holdover). Preheat engines in extreme cold. Remove all frost/snow/ice before flight - <b>clean aircraft concept</b>."}
    , {"heading": "Foreign Object Debris (FOD) Prevention", "body": "FOD on the ramp and in hangars can be ingested by engines or strike propellers, causing catastrophic damage, so ramp personnel conduct regular FOD walks to visually sweep for loose hardware, debris, and trash before aircraft movement. FOD prevention includes tool control programs that account for every tool used near open aircraft structure, covering or capping open lines and ports during maintenance, and designated FOD containers at workstations. A single dropped fastener left on a ramp or in an intake duct can result in an engine failure, making FOD awareness a continuous discipline rather than an occasional inspection task."}],
    "quiz": [ {"q": "What is the primary purpose of a FOD walk on the ramp?", "choices": ["To check weather conditions", "To visually sweep for loose hardware and debris that could be ingested or cause damage", "To count aircraft on the ramp", "To inspect tire pressure"], "answer": 1, "explain": "FOD walks locate and remove debris, hardware, and trash from ramp and hangar areas before it can be ingested by engines or cause other damage."},
      {"q": "Before fueling you must first:", "choices": ["Check oil","Bond and ground the aircraft","Remove chocks","Start APU"], "answer": 1, "explain": "Bonding/grounding dissipates static electricity - a spark near fuel vapor is catastrophic."},
      {"q": "Avgas 100LL is dyed what color?", "choices": ["Clear","Blue","Green","Red"], "answer": 1, "explain": "100LL avgas is blue. Jet-A is clear/straw. Color confirms correct fuel."},
      {"q": "Why keep petroleum away from oxygen systems?", "choices": ["It stains","Explosion/fire hazard","It clogs valves","No reason"], "answer": 1, "explain": "Petroleum products in the presence of high-pressure oxygen can ignite explosively."},
      {"q": "The turbine intake hazard is:", "choices": ["Noise only","Suction/ingestion","Heat only","Vibration"], "answer": 1, "explain": "Intake suction can ingest people, tools, and debris - a lethal FOD hazard."},
      {"q": "The clean aircraft concept requires:", "choices": ["A washed exterior","No frost/snow/ice before flight","Polished metal","Clean windows"], "answer": 1, "explain": "All frozen contamination must be removed - even light frost disrupts lift."},
      {"q": "Nitrogen (not air) is used in struts/tires because:", "choices": ["It is cheaper","Inert, no moisture, no combustion support","It is colored","It weighs less"], "answer": 1, "explain": "Dry nitrogen avoids moisture/corrosion and won't support combustion in a hot brake fire."}
    ]
  },
  {
    "id": "weight_balance", "title": "Weight & Balance", "track": "general", "icon": "&#x2696;",
    "sections": [
      {"heading": "Why It Matters", "body": "An aircraft loaded outside CG limits may be uncontrollable. The mechanic maintains the <b>weight and balance record</b> and reweighs after major repairs/alterations. Every equipment change updates the record."},
      {"heading": "Key Terms", "body": "<b>Datum</b> - reference plane. <b>Arm</b> - distance from datum. <b>Moment</b> = weight x arm. <b>CG</b> = total moment / total weight. <b>Empty weight</b>, <b>useful load</b>, <b>MTOW</b> (max takeoff weight). Forward/aft CG limits from TCDS."},
      {"heading": "Weighing Procedure", "body": "Level the aircraft, use calibrated scales at each wheel/jack point. Subtract tare. Drainable fuel out (or note), full oil. Compute empty weight and empty-weight CG. Record in the aircraft records."},
      {"heading": "Adverse Loading & Ballast", "body": "Check most-forward and most-aft load cases stay within envelope. <b>Ballast</b> (permanent or temporary) corrects out-of-limit CG - must be placarded and secured. Equipment removal can shift CG dangerously."}
    ,
      {"heading": "Worked CG Example", "body": "Empty weight 1400 lb at arm 40 in gives moment 56,000 lb-in. Add pilot 170 lb at arm 37 = 6,290 lb-in. Add fuel 180 lb at arm 48 = 8,640 lb-in. Total weight 1750 lb, total moment 70,930 lb-in. <b>CG = 70,930 / 1750 = 40.5 in</b> - compare against the TCDS forward/aft limits to confirm the loading is legal before flight."}, {"heading": "Empty Weight CG Range and Equipment Changes", "body": "Every aircraft has an approved empty weight center of gravity (CG) range specified in its weight and balance data, and any equipment addition, removal, or relocation (avionics upgrades, seat changes, interior modifications) requires a new weight and balance calculation to confirm the aircraft remains within approved limits. Cumulative minor equipment changes over an aircraft's life can gradually shift the empty weight CG outside the approved envelope even though no single change seemed significant, which is why a full reweigh is periodically required by many manufacturers and after any major alteration. Technicians must update the permanent weight and balance record with the new empty weight, CG location, and a list of installed equipment after every applicable change."}],
    "quiz": [ {"q": "Why might a full aircraft reweigh be required periodically even without a major single alteration?", "choices": ["Only pilots request it for fun", "Cumulative minor equipment changes can gradually shift the empty weight CG outside approved limits", "Weight and balance never changes", "Fuel weight fully compensates for any change"], "answer": 1, "explain": "Small equipment changes over time can accumulate and shift the empty weight CG outside the approved envelope, which is why periodic reweighs and updates to records are required."},
      {"q": "Moment equals:", "choices": ["Weight / arm","Weight x arm","Arm / weight","Weight + arm"], "answer": 1, "explain": "Moment = weight x arm (a torque about the datum)."},
      {"q": "CG is calculated as:", "choices": ["Total weight / total moment","Total moment / total weight","Arm x datum","Weight x MTOW"], "answer": 1, "explain": "CG = total moment divided by total weight."},
      {"q": "The datum is:", "choices": ["The heaviest point","A reference plane for measurements","The CG","The tail"], "answer": 1, "explain": "The datum is a reference plane from which all arms are measured."},
      {"q": "Ballast must be:", "choices": ["Loose in the cabin","Placarded and secured","Painted red","Removed for flight"], "answer": 1, "explain": "Permanent/temporary ballast must be secured and placarded per approved data."},
      {"q": "Empty weight is 1400 lb at arm 40 in. What is the moment?", "choices": ["35 lb-in","1440 lb-in","56,000 lb-in","1360 lb-in"], "answer": 2, "explain": "Moment = weight x arm = 1400 x 40 = 56,000 lb-in."},
      {"q": "When must W&B be redone?", "choices": ["Every flight","After major repair/alteration or equipment change","Only at annual","Never"], "answer": 1, "explain": "Reweigh or recompute after major repairs, alterations, or equipment changes."}
    ]
  }
,
  {
    "id": "corrosion", "title": "Corrosion Control", "track": "general", "icon": "&#x1F9EA;",
    "sections": [
      {"heading": "What Corrosion Is", "body": "Electrochemical deterioration of metal returning it toward its ore state. Needs an <b>anode, cathode, electrolyte, and path</b>. Aluminum forms a protective oxide; chlorides (salt) and moisture break it down. Costs airlines billions and grounds aircraft."},
      {"heading": "Types", "body": "<ul><li><b>Surface/uniform</b> - general etching</li><li><b>Pitting</b> - localized deep holes</li><li><b>Intergranular</b> - along grain boundaries (heat-treat related)</li><li><b>Exfoliation</b> - layers lift/flake</li><li><b>Galvanic</b> - dissimilar metals in contact</li><li><b>Stress corrosion cracking</b>, <b>filiform</b>, <b>fretting</b></li></ul>"},
      {"heading": "Prevention", "body": "Protective finishes: <b>alodine/chromate conversion</b>, primer, paint. <b>Anodizing</b> aluminum. Seal faying surfaces. Drainage/ventilation. Keep it clean and dry. Corrosion-preventive compounds (CPC/LPS). Dissimilar-metal isolation (barrier tape, sealant)."},
      {"heading": "Treatment", "body": "Remove all corrosion products (mechanical/chemical), assess to damage limits per SRM, neutralize, restore protective finish. Non-powered abrasives on aluminum (no steel wool - it embeds iron). Document; re-inspect on schedule."},
      {"heading": "Corrosion Inspection in Practice", "body": "During a scheduled inspection, look first at known trouble spots: battery compartments, lavatory/galley floor areas, wheel wells, exhaust trails, and skin lap joints where moisture pools. A bright white or gray powdery bloom on aluminum is a classic sign of corrosion starting under paint. Use a flashlight at a raking angle and a mirror to check blind areas; tap-test suspect skin for disbonding. Any find gets photographed, measured, and compared against SRM allowable damage limits before any blend-out or repair is approved."}
    , {"heading": "Corrosion in Composite-to-Metal Interfaces", "body": "Galvanic corrosion is a particular concern where carbon fiber composites contact aluminum structure, since carbon fiber is electrically conductive and more noble than aluminum, creating a strong galvanic couple in the presence of moisture. Isolation is achieved using fiberglass isolation plies, non-conductive fasteners or sleeves, and sealant barriers between the composite and metal structure. Any breach of this isolation layer during repair or drilling can introduce accelerated corrosion at the interface that may not be visible until significant material loss has occurred, making proper isolation restoration during composite repairs a critical inspection item."}],
    "quiz": [ {"q": "Why is carbon fiber composite in contact with aluminum a galvanic corrosion concern?", "choices": ["Carbon fiber is an insulator", "Carbon fiber is conductive and more noble than aluminum, creating a strong galvanic couple", "Aluminum is more noble than carbon fiber", "Composites never touch metal in aircraft"], "answer": 1, "explain": "Carbon fiber's conductivity and nobility relative to aluminum create a strong galvanic couple, requiring isolation plies or sealant barriers to prevent accelerated corrosion."},
      {"q": "During inspection, a raking-light/mirror technique is used mainly to:", "choices": ["Measure paint thickness", "Reveal corrosion bloom or disbonding in blind/shadowed areas", "Check fuel quantity", "Test bonding straps"], "answer": 1, "explain": "Raking light and mirrors reveal subtle surface irregularities like corrosion blooms or skin disbonding that are easy to miss under normal lighting."},
      {"q": "Corrosion requires an electrolyte plus:", "choices": ["Anode, cathode, and path","Only heat","Only oxygen","Sunlight"], "answer": 0, "explain": "An electrochemical cell needs anode, cathode, electrolyte, and a conductive path."},
      {"q": "Layers lifting/flaking describes:", "choices": ["Pitting","Exfoliation","Filiform","Fretting"], "answer": 1, "explain": "Exfoliation corrosion lifts material in layers, common in extrusions."},
      {"q": "Dissimilar metals in contact cause:", "choices": ["Galvanic corrosion","Fatigue","Creep","Annealing"], "answer": 0, "explain": "Galvanic corrosion occurs between dissimilar metals with an electrolyte present."},
      {"q": "Why avoid steel wool on aluminum?", "choices": ["Too soft","Embeds iron particles that promote corrosion","It's expensive","It scratches paint only"], "answer": 1, "explain": "Steel wool leaves iron particles that create galvanic cells and accelerate corrosion."},
      {"q": "Chromate conversion coating (alodine) provides:", "choices": ["Structural strength","Corrosion protection and paint adhesion","Fuel resistance","Fire protection"], "answer": 1, "explain": "It forms a corrosion-resistant film and improves paint/primer adhesion."}
    ]
  },
  {
    "id": "human_factors", "title": "Human Factors & Safety", "track": "general", "icon": "&#x1F9E0;",
    "sections": [
      {"heading": "The Dirty Dozen", "body": "The 12 human-factors precursors to maintenance error: <b>Lack of communication, complacency, lack of knowledge, distraction, lack of teamwork, fatigue, lack of resources, pressure, lack of assertiveness, stress, lack of awareness, norms.</b> Recognizing them is the first defense."},
      {"heading": "SHELL & Error Chains", "body": "The <b>SHELL model</b>: Software, Hardware, Environment, Liveware (people) - errors happen at interfaces. Most accidents are a <b>chain</b> of small failures; breaking one link prevents the event. Swiss-cheese model of layered defenses."},
      {"heading": "Safety Nets", "body": "<b>Checklists</b>, work-cards, and sign-offs. Independent inspection of critical items (flight controls). <b>Fatigue management</b> - shift limits. <b>Just culture</b> - report errors without blame to learn. Proper documentation prevents repeat mistakes."},
      {"heading": "Shop Safety & PPE", "body": "Eye/hearing/respiratory protection. <b>Lockout/tagout</b> for energized systems. SDS/HazMat handling. Compressed-gas and battery-acid precautions. Confined-space (fuel tank) entry procedures. Proper lifting and FOD discipline."}
    ,
      {"heading": "Applying Human Factors Day to Day", "body": "A short <b>pre-task risk brief</b> - reviewing the job, hazards, and required tools/parts before starting - catches many errors before they happen. <b>Independent inspection</b> on flight-critical items (like control cable rigging) adds a second set of eyes. When interrupted mid-task, always re-verify the last completed step before continuing rather than assuming where you left off - interruption-driven errors are one of the most common causes of maintenance mistakes."}, {"heading": "Fatigue Risk Management", "body": "Fatigue impairs judgment, reaction time, and attention to detail similarly to alcohol intoxication, and maintenance fatigue risk management systems address scheduling practices, rest requirements, and self-assessment tools to reduce fatigue-related errors. Circadian rhythm disruption from shift work, especially rotating shifts and night shifts, is a major contributor, and technicians should recognize warning signs such as microsleeps, repeated re-reading of instructions, and difficulty concentrating as cues to pause and seek relief rather than continuing to work through fatigue. Organizations with mature safety cultures build fatigue reporting into their non-punitive safety reporting systems alongside other human factors hazards."}],
    "quiz": [ {"q": "How does significant fatigue affect a technician's performance?", "choices": ["It has no measurable effect", "It impairs judgment and reaction time similarly to alcohol intoxication", "It only affects physical strength", "It improves attention to detail"], "answer": 1, "explain": "Research shows fatigue produces cognitive impairment comparable to alcohol intoxication, affecting judgment, reaction time, and attention to detail."},
      {"q": "How many items in the Dirty Dozen?", "choices": ["10","12","14","6"], "answer": 1, "explain": "The Dirty Dozen is 12 human-factors error precursors."},
      {"q": "The SHELL model's second L is:", "choices": ["Logic","Liveware (people)","Loading","Lift"], "answer": 1, "explain": "SHELL = Software, Hardware, Environment, Liveware - the human element."},
      {"q": "A just culture encourages:", "choices": ["Hiding mistakes","Reporting errors to learn without blame","Punishing all errors","Ignoring reports"], "answer": 1, "explain": "Just culture invites honest error reporting so the system can improve."},
      {"q": "The Swiss-cheese model describes:", "choices": ["Cheese storage","Layered defenses with holes that can align","Fuel filtering","A rivet pattern"], "answer": 1, "explain": "Accidents occur when holes in successive defensive layers align."},
      {"q": "After being interrupted in the middle of a task, a mechanic should:", "choices": ["Continue from memory","Re-verify the last completed step before continuing","Restart the whole job from scratch every time","Ask someone else to guess where they left off"], "answer": 1, "explain": "Interruptions are a leading cause of maintenance error; re-checking the last completed step before resuming prevents skipped or duplicated actions."},
      {"q": "Lockout/tagout is used to:", "choices": ["Label parts","Prevent accidental energizing of systems","Track tools","Log hours"], "answer": 1, "explain": "LOTO isolates and secures energy sources so a system can't be activated during work."}
    ]
  }
,
  {
    "id": "fluid_power", "title": "Hydraulics & Pneumatics", "track": "airframe", "icon": "&#x1F4A7;",
    "sections": [
      {"heading": "Hydraulic Principle", "body": "Based on <b>Pascal's Law</b> - confined fluid transmits pressure equally, multiplying force. Actuators convert pressure to motion (gear, flaps, brakes, steering). Nearly incompressible fluid gives precise, powerful control."},
      {"heading": "Fluids - NEVER MIX", "body": "<b>MIL-H-5606</b> (mineral, red), <b>MIL-H-83282</b> (fire-resistant mineral, red), <b>Skydrol/phosphate-ester</b> (purple, transport category). Mixing types destroys seals. Skydrol is corrosive to skin/paint - full PPE. Match seal material (Buna vs EPDM/butyl)."},
      {"heading": "Components", "body": "Reservoir, engine/electric <b>pump</b>, filters, <b>selector/control valves</b>, actuators, <b>accumulator</b> (stores pressure, dampens surges - precharged with nitrogen/air), pressure relief valve, gauges. Open-center vs closed-center systems."},
      {"heading": "Pneumatics & Servicing", "body": "Some aircraft use high-pressure air (backup gear/brakes) or engine <b>bleed air</b> (pressurization, anti-ice, start). Moisture removal is critical. Bleed air off before servicing. Depressurize and verify zero before opening any line."}
    ,
      {"heading": "Troubleshooting Hydraulic Faults", "body": "<b>Spongy or slow actuation</b> usually means air trapped in the system - bleed at the highest point. <b>Erratic pressure/noise</b> can indicate a failing pump or clogged filter. <b>Slow gear extension</b> may be low fluid, a restricted line, or a weak accumulator precharge. Always relieve pressure and verify zero before opening any line, and trace leaks to their source rather than just topping off fluid."}, {"heading": "Hydraulic Fluid Contamination Classification", "body": "Hydraulic fluid contamination is quantified using particle counting standards such as NAS 1638 or ISO 4406, which classify fluid cleanliness by counting particles of various size ranges per unit volume. Servicing equipment and sample bottles must themselves meet cleanliness standards, since introducing contamination during a fluid top-off can be worse than the contamination being corrected. Common contamination sources include worn seals shedding particles, ingested dirt through breather caps, and cross-contamination from using the wrong fluid type or dirty transfer equipment; particle counts exceeding specification require filtration or fluid replacement before the system can be returned to service."}],
    "quiz": [ {"q": "What do standards like NAS 1638 or ISO 4406 quantify in hydraulic systems?", "choices": ["Fluid color", "Fluid contamination by particle count per size range and volume", "Fluid viscosity only", "System pressure"], "answer": 1, "explain": "These standards classify hydraulic fluid cleanliness by counting particles across defined size ranges within a unit volume of fluid."},
      {"q": "Hydraulics rely on which principle?", "choices": ["Bernoulli's","Pascal's Law","Ohm's Law","Charles' Law"], "answer": 1, "explain": "Pascal's Law - confined fluid transmits pressure equally, enabling force multiplication."},
      {"q": "Skydrol is what fluid type?", "choices": ["Mineral","Vegetable","Phosphate-ester","Synthetic oil"], "answer": 2, "explain": "Skydrol is a phosphate-ester fluid used in transport aircraft - corrosive, needs PPE."},
      {"q": "An accumulator does what?", "choices": ["Filters fluid","Stores pressure and dampens surges","Cools the fluid","Measures flow"], "answer": 1, "explain": "The accumulator stores hydraulic pressure and absorbs pressure spikes; it's precharged with gas."},
      {"q": "Mixing hydraulic fluid types causes:", "choices": ["Better performance","Seal damage/system failure","Color change only","Nothing"], "answer": 1, "explain": "Incompatible fluids attack seals - never mix mineral and phosphate-ester types."},
      {"q": "A hydraulic system that feels spongy or slow to actuate most likely has:", "choices": ["Too much fluid","Air trapped in the system","Excess accumulator precharge","A stuck relief valve open"], "answer": 1, "explain": "Trapped air compresses under load, producing a soft/delayed response - bleed the system at its highest point to remove it."},
      {"q": "Bleed air is taken from:", "choices": ["The battery","The engine compressor","Tires","The reservoir"], "answer": 1, "explain": "Bleed air is high-pressure air tapped from the engine compressor section."}
    ]
  },
  {
    "id": "landing_gear", "title": "Landing Gear & Brakes", "track": "airframe", "icon": "&#x1F6DE;",
    "sections": [
      {"heading": "Gear Types & Shock Absorption", "body": "Fixed vs <b>retractable</b>; tricycle vs tailwheel. <b>Oleo strut</b> (air-oil) absorbs landing loads - serviced with nitrogen and hydraulic fluid to correct <b>strut extension</b>. Leaf-spring and bungee types on light aircraft."},
      {"heading": "Retraction Systems", "body": "Hydraulic (most), electric, or manual backup. <b>Downlocks/uplocks</b> and <b>WOW (squat) switches</b> prevent inadvertent retraction on the ground. Position indicators (3 green). Emergency free-fall extension. Sequencing of gear doors."},
      {"heading": "Wheels & Tires", "body": "Split rims - <b>deflate before removing bolts</b> (stored energy = deadly). Tire pressure per spec (temperature-corrected). Inspect for cuts, wear, flat spots. Fusible plugs release pressure in overheated wheels. Balance and creep marks."},
      {"heading": "Brakes", "body": "Disc brakes: single/dual/multi-disc; steel or <b>carbon</b>. Hydraulic actuation. <b>Anti-skid</b> systems modulate to prevent lockup. Bleed to remove air. Wear-pin indicators. <b>Hot brakes</b> - approach from fore/aft, not the side (wheel explosion risk)."}
    ,
      {"heading": "Rigging & Alignment Checks", "body": "After gear component replacement, verify <b>toe-in/toe-out</b> and gear leg alignment per the maintenance manual - misalignment causes uneven tire wear and shimmy. Check strut extension against the servicing chart (correlates to weight and pressure). Confirm door rigging and sequencing so gear doors do not interfere with wheels during retraction/extension."}, {"heading": "Landing Gear Shimmy and Nosewheel Steering", "body": "Nosewheel shimmy is an oscillation of the nose gear about its steering axis, often caused by worn shimmy dampers, loose torque link bolts, out-of-balance wheels, or incorrect tire pressure. Shimmy dampers, which may be hydraulic or friction-disc type, absorb these oscillations and must be checked for proper fluid level and damping resistance during inspection. Nosewheel steering systems, whether direct mechanical linkage or hydraulically boosted, require correct centering and travel limit adjustment, since incorrect rigging can cause both steering binding and shimmy tendencies that mimic other landing gear faults."}],
    "quiz": [ {"q": "What is a common cause of nosewheel shimmy?", "choices": ["Overinflated main tires", "Worn shimmy dampers, loose torque link bolts, or out-of-balance wheels", "Excessive fuel load", "Cabin door seal wear"], "answer": 1, "explain": "Shimmy is typically caused by worn dampers, loose torque links, wheel imbalance, or incorrect tire pressure, all of which allow oscillation about the steering axis."},
      {"q": "An oleo strut is serviced with:", "choices": ["Only air","Nitrogen/air and hydraulic fluid","Only fluid","Grease"], "answer": 1, "explain": "The air-oil oleo strut uses both a gas charge and hydraulic fluid for proper extension/damping."},
      {"q": "The WOW/squat switch prevents:", "choices": ["Overheating","Gear retraction on the ground","Brake fade","Tire wear"], "answer": 1, "explain": "The weight-on-wheels switch inhibits gear retraction while on the ground."},
      {"q": "Before removing split-rim wheel bolts you must:", "choices": ["Heat the tire","Fully deflate the tire","Add air","Spin the wheel"], "answer": 1, "explain": "Deflate first - a pressurized split rim can blow apart with lethal force."},
      {"q": "Anti-skid systems:", "choices": ["Increase speed","Prevent wheel lockup/skidding","Cool tires","Steer the nose"], "answer": 1, "explain": "Anti-skid modulates brake pressure to keep wheels from locking, maximizing braking."},
      {"q": "Uneven or rapid tire wear on one side of the tread often points to:", "choices": ["Normal wear","Misaligned toe-in/toe-out", "Overinflation only", "A fusible plug issue"], "answer": 1, "explain": "Improper wheel alignment (toe-in/out) scrubs the tire unevenly and should be checked/corrected per the maintenance manual."},
      {"q": "Approach hot brakes from:", "choices": ["The side","Fore or aft, never the side","Directly behind the tire","Any direction"], "answer": 1, "explain": "Overheated wheels can explode radially - stand fore/aft, never to the side."}
    ]
  }
,
  {
    "id": "avionics", "title": "Avionics & Instruments", "track": "airframe", "icon": "&#x1F4E1;",
    "sections": [
      {"heading": "Pitot-Static System", "body": "<b>Pitot</b> senses ram (total) pressure; <b>static</b> ports sense ambient. Drives <b>airspeed, altimeter, VSI</b>. Blockages cause dangerous errors. Leak-check per 91.411. Never blow into a pitot tube toward instruments. Alternate static source for blockage."},
      {"heading": "Gyroscopic & Modern Displays", "body": "Rigidity and precession drive attitude/heading/turn instruments (vacuum or electric). Modern <b>glass cockpits</b> use AHRS, ADC, and EFIS. <b>Static-sensitive</b> electronics - use ESD protection. Software/database currency (nav data cycles)."},
      {"heading": "Communication & Navigation", "body": "VHF comm, transponder (Mode C/S, <b>ADS-B Out</b> required), VOR/ILS/GPS/WAAS. Antenna bonding and placement. EMI/RFI shielding. Under Part 43 avionics installation often needs approved data and possibly a repair station/authorized person."},
      {"heading": "Wiring & Electrical Practices", "body": "Follow AC 43.13-1B ch.11: correct gauge, support every ~24 in, service loops, chafe protection, drip loops, proper terminations. <b>Bonding and grounding</b> for lightning/EMI. Circuit protection sized to wire. Label per diagrams."}
    ,
      {"heading": "Systematic Avionics Troubleshooting", "body": "Start with the <b>simplest, most likely cause</b>: power, circuit breakers, connectors, and grounds before suspecting an LRU. Use wiring diagrams to trace a signal path and isolate whether the fault is upstream (sensor/source) or downstream (indicator/display). Built-in test equipment (<b>BITE</b>) on modern systems can log fault codes - always cross-check BITE codes against the maintenance manual rather than swapping boxes blindly."}, {"heading": "ADS-B and Transponder Systems", "body": "Automatic Dependent Surveillance-Broadcast (ADS-B) systems broadcast an aircraft's GPS-derived position, altitude, velocity, and identification to ground stations and other aircraft, and ADS-B Out is mandatory in most controlled U.S. airspace. Transponder and ADS-B installations require careful antenna placement to avoid shadowing by the airframe, proper bonding for RF grounding, and periodic certification testing (24-month transponder checks per 91.413, and ADS-B performance verification) to confirm accuracy of broadcast position and altitude data. Technicians troubleshooting ADS-B faults must check GPS position source integrity, since a faulty GPS antenna or receiver upstream will cause ADS-B Out to fail even if the transponder itself tests good."}, {"heading": "Static Discharge and Bonding for Avionics Protection", "body": "Avionics equipment is protected from lightning-induced transients and static discharge through a combination of airframe bonding (providing a low-resistance path for current to flow around rather than through sensitive electronics), shielded wiring with proper shield termination at both ends, and surge suppression devices at critical interface points where external wiring (antennas, external lighting circuits) connects to avionics units. A bonding or shielding discontinuity introduced during unrelated maintenance work, such as removing and reinstalling an access panel without restoring its bonding jumper, can leave avionics vulnerable to damage from an event that the original bonding scheme was specifically designed to protect against. Technicians performing any work near avionics wiring or bonding points must verify bonding and shielding continuity is restored to original specification before closing up the aircraft, since this type of latent defect often is not detected until an actual lightning strike or EMI event reveals it through equipment damage."}],
    "quiz": [ {"q": "What risk is created if a bonding jumper is not restored after removing and reinstalling an access panel near avionics?", "choices": ["No risk, bonding jumpers are purely cosmetic", "Avionics can become vulnerable to damage from lightning or EMI events the bonding was designed to protect against", "The panel will not close properly", "Avionics will run at a different voltage"], "answer": 1, "explain": "Bonding jumpers provide a low-resistance path protecting avionics from lightning and EMI; failing to restore one after maintenance leaves that protection compromised, often undetected until an actual event occurs."}, {"q": "What data does ADS-B Out broadcast from an aircraft?", "choices": ["Only the pilot's name", "GPS-derived position, altitude, velocity, and identification", "Fuel quantity only", "Engine RPM only"], "answer": 1, "explain": "ADS-B Out continuously broadcasts the aircraft's GPS-derived position, altitude, velocity, and ID for surveillance by ATC and other aircraft."},
      {"q": "The pitot tube senses:", "choices": ["Static pressure","Ram (total) pressure","Temperature","Voltage"], "answer": 1, "explain": "Pitot senses ram/total pressure; static ports sense ambient. Together they drive the air data instruments."},
      {"q": "Which instruments use the static system?", "choices": ["Tachometer","Airspeed, altimeter, VSI","Oil pressure","Ammeter"], "answer": 1, "explain": "Airspeed, altimeter, and VSI all reference static (and pitot for airspeed) pressure."},
      {"q": "ADS-B Out primarily provides:", "choices": ["Engine data","Position/surveillance broadcast","Fuel flow","Cabin temp"], "answer": 1, "explain": "ADS-B Out broadcasts GPS-derived position for ATC surveillance - now required airspace."},
      {"q": "Gyro instruments rely on:", "choices": ["Rigidity and precession","Bernoulli","Combustion","Capacitance only"], "answer": 0, "explain": "Gyroscopic rigidity in space and precession drive attitude, heading, and turn indicators."},
      {"q": "When troubleshooting a suspected avionics fault, the first step should generally be to:", "choices": ["Replace the most expensive LRU", "Check power, breakers, connectors, and grounds", "Reload all software immediately", "Swap boxes with another aircraft"], "answer": 1, "explain": "Simple, common causes (power, breakers, connections, grounds) should be ruled out before condemning an expensive line-replaceable unit."},
      {"q": "Handling avionics boxes requires:", "choices": ["Wet hands","ESD (static) protection","Heating first","No precautions"], "answer": 1, "explain": "Electronics are static-sensitive; use ESD straps/mats to avoid latent damage."}
    ]
  },
  {
    "id": "fuel_systems", "title": "Fuel & Metering Systems", "track": "powerplant", "icon": "&#x26FD;",
    "sections": [
      {"heading": "Fuel System Basics", "body": "Tanks (integral wet-wing, bladder, rigid), <b>boost pumps</b>, selector valves, filters/strainers, firewall shutoff. <b>Sump drains</b> catch water/sediment - check before first flight. Fuel vents prevent tank collapse/pressurization. Cross-feed for balance."},
      {"heading": "Carburetors", "body": "<b>Float-type</b> meters fuel via venturi suction. Main hazard: <b>carburetor icing</b> (temperature drop from vaporization/pressure) - use <b>carb heat</b>. Mixture control for altitude. Idle cutoff for shutdown. Accelerator pump for throttle transients."},
      {"heading": "Fuel Injection", "body": "Continuous-flow (Bendix/Continental) meters fuel to each cylinder - no carb ice, better distribution. Turbine engines use <b>fuel control units / FADEC</b> scheduling fuel with rpm, temp, and air data. Fuel nozzles atomize into combustors."},
      {"heading": "Fuel Contamination & Safety", "body": "Water, microbial growth, wrong grade, particulates. <b>Bonding/grounding</b> when fueling. Fire/explosion hazards - tank entry is confined-space with vapor purge. Fuel-quantity systems (float or capacitance). Filter bypass warnings."}
    ,
      {"heading": "Fuel Starvation Troubleshooting", "body": "Common causes of fuel-flow problems include a clogged filter/strainer, a failed boost pump, a stuck selector valve, a vented cap causing siphoning, or <b>vapor lock</b> (fuel boiling in the line from heat, dropping flow). Cross-feed and selector positions must be verified after any fuel-system maintenance. Always check for water/contamination first - it is the most common and easiest-to-find cause of engine roughness or flow interruption."}, {"heading": "Fuel Vapor Lock and Vapor Elimination", "body": "Vapor lock occurs when fuel in the lines heats up enough to form vapor bubbles, which can interrupt fuel flow to the engine especially in gravity-feed or low-pressure fuel systems on hot days or at altitude. Fuel system design counters this through vapor return lines that route vapor and hot fuel back to the tank, cooling fins or shielding on fuel lines routed near engine heat sources, and adequate fuel pump boost pressure to keep fuel above its vapor pressure point. Technicians troubleshooting intermittent power loss or rough running on hot days should consider vapor lock as a possible cause, particularly on carbureted engines with fuel lines routed near exhaust components."}],
    "quiz": [ {"q": "What causes vapor lock in a fuel system?", "choices": ["Too much fuel pressure", "Fuel heating enough to form vapor bubbles that interrupt flow", "Cold ambient temperatures", "Excess fuel filter capacity"], "answer": 1, "explain": "Vapor lock results from fuel vaporizing due to heat, interrupting the fuel flow needed for engine operation, particularly in low-pressure gravity-feed systems."},
      {"q": "Carburetor icing is countered with:", "choices": ["Mixture rich","Carburetor heat","More RPM","Fuel additive"], "answer": 1, "explain": "Carb heat supplies warm air to melt/prevent ice from the temperature drop in the venturi."},
      {"q": "Sump drains are checked for:", "choices": ["Oil level","Water and sediment","Voltage","Tire pressure"], "answer": 1, "explain": "Draining sumps removes water and sediment that settle at the tank low point."},
      {"q": "Continuous-flow fuel injection advantage over carbs:", "choices": ["Cheaper","No carb ice, better fuel distribution","Lighter only","Louder"], "answer": 1, "explain": "Injection eliminates carburetor icing and distributes fuel more evenly to cylinders."},
      {"q": "Turbine fuel scheduling is managed by:", "choices": ["A carburetor","Fuel control unit / FADEC","The pilot manually only","A magneto"], "answer": 1, "explain": "The FCU or FADEC schedules fuel with rpm, temperature, and air data inputs."},
      {"q": "Vapor lock in a fuel system is best described as:", "choices": ["Water trapped in the tank", "Fuel boiling in the line, interrupting flow", "A stuck selector valve", "Microbial growth in the tank"], "answer": 1, "explain": "Vapor lock occurs when fuel in the line gets hot enough to boil, forming vapor bubbles that block liquid fuel flow to the engine."},
      {"q": "Fuel tank entry is:", "choices": ["Routine, no precautions","A confined space requiring vapor purge","Done while fueling","Never allowed"], "answer": 1, "explain": "Integral tank entry is confined-space work - purge vapors, monitor, and use safety attendants."}
    ]
  }

]

EXT_FLASHCARDS = [
    {"front":"Bond & ground before fueling","back":"Dissipates static to prevent fuel-vapor ignition"},
    {"front":"Avgas 100LL color","back":"Blue (Jet-A is clear/straw)"},
    {"front":"Datum","back":"Reference plane from which all arms are measured"},
    {"front":"Moment","back":"Weight x arm"},
    {"front":"CG","back":"Total moment / total weight"},
    {"front":"Exfoliation corrosion","back":"Corrosion that lifts metal in layers/flakes"},
    {"front":"Galvanic corrosion","back":"Between dissimilar metals with an electrolyte"},
    {"front":"Never use on aluminum","back":"Steel wool (embeds iron, causes corrosion)"},
    {"front":"Alodine / chromate conversion","back":"Corrosion coat + improves paint adhesion"},
    {"front":"Dirty Dozen count","back":"12 human-factors error precursors"},
    {"front":"SHELL model","back":"Software, Hardware, Environment, Liveware"},
    {"front":"Just culture","back":"Report errors without blame to learn from them"},
    {"front":"LOTO","back":"Lockout/Tagout - isolate energy sources before work"},
    {"front":"Hydraulic principle","back":"Pascal's Law - confined fluid transmits pressure equally"},
    {"front":"Skydrol color/type","back":"Purple phosphate-ester (transport aircraft)"},
    {"front":"MIL-H-5606 color","back":"Red mineral-based hydraulic fluid"},
    {"front":"Accumulator","back":"Stores hydraulic pressure, dampens surges (gas-precharged)"},
    {"front":"Oleo strut serviced with","back":"Nitrogen/air charge + hydraulic fluid"},
    {"front":"WOW/squat switch","back":"Prevents gear retraction on the ground"},
    {"front":"Split-rim wheel safety","back":"Fully deflate tire before removing rim bolts"},
    {"front":"Anti-skid","back":"Modulates brake pressure to prevent wheel lockup"},
    {"front":"Approach hot brakes from","back":"Fore or aft, never the side (explosion risk)"},
    {"front":"Pitot senses","back":"Ram/total pressure (for airspeed)"},
    {"front":"Static system drives","back":"Airspeed, altimeter, VSI"},
    {"front":"ADS-B Out","back":"Broadcasts GPS position for ATC surveillance"},
    {"front":"Gyro instrument principles","back":"Rigidity in space and precession"},
    {"front":"91.411 checks","back":"Altimeter/static system (24-month) test"},
    {"front":"Carb ice remedy","back":"Carburetor heat (warm air)"},
    {"front":"Fuel injection vs carb","back":"No carb ice, better cylinder fuel distribution"},
    {"front":"Bleed air source","back":"Engine compressor section (high-pressure air)"},
    {"front":"Fuel tank entry","back":"Confined space - purge vapors, use attendant"},
    {"front":"Type IV de-ice fluid","back":"Anti-ice fluid with longer holdover time"}
]

EXT_GLOSSARY = [
    {"term":"Accumulator","def":"Stores hydraulic pressure and dampens surges; gas-precharged"},
    {"term":"ADS-B","def":"Automatic Dependent Surveillance-Broadcast (GPS position)"},
    {"term":"AHRS","def":"Attitude and Heading Reference System (digital)"},
    {"term":"Anti-skid","def":"System modulating brakes to prevent wheel lockup"},
    {"term":"Arm","def":"Distance from the datum to a weight (for W&B)"},
    {"term":"Ballast","def":"Weight added to bring CG within limits (placarded)"},
    {"term":"Bleed Air","def":"High-pressure air tapped from the engine compressor"},
    {"term":"Carb Heat","def":"Warm air supplied to prevent/clear carburetor ice"},
    {"term":"Datum","def":"Reference plane for weight-and-balance measurements"},
    {"term":"Dirty Dozen","def":"12 human-factors precursors to maintenance error"},
    {"term":"Exfoliation","def":"Corrosion that lifts metal in layers/flakes"},
    {"term":"Filiform","def":"Thread-like corrosion under coatings"},
    {"term":"Galvanic Corrosion","def":"Corrosion between dissimilar metals with electrolyte"},
    {"term":"Intergranular","def":"Corrosion along a metal's grain boundaries"},
    {"term":"LOTO","def":"Lockout/Tagout - energy isolation procedure"},
    {"term":"MTOW","def":"Maximum Takeoff Weight"},
    {"term":"Moment","def":"Weight multiplied by arm (torque about datum)"},
    {"term":"Pitot","def":"Probe sensing ram/total pressure for airspeed"},
    {"term":"Precession","def":"Gyro response 90 deg from an applied force"},
    {"term":"Rigidity","def":"A spinning gyro's tendency to stay fixed in space"},
    {"term":"SHELL","def":"Human-factors model: Software/Hardware/Environment/Liveware"},
    {"term":"Squat Switch","def":"Weight-on-wheels sensor (see WOW)"},
    {"term":"Static Port","def":"Opening sensing ambient pressure for instruments"},
    {"term":"Sump Drain","def":"Low-point drain to remove water/sediment from tanks"},
    {"term":"Useful Load","def":"Max weight minus empty weight (fuel + payload)"},
    {"term":"VSI","def":"Vertical Speed Indicator (static-driven)"}
]

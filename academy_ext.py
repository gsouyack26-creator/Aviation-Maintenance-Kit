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
    ],
    "quiz": [
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
    ],
    "quiz": [
      {"q": "Moment equals:", "choices": ["Weight / arm","Weight x arm","Arm / weight","Weight + arm"], "answer": 1, "explain": "Moment = weight x arm (a torque about the datum)."},
      {"q": "CG is calculated as:", "choices": ["Total weight / total moment","Total moment / total weight","Arm x datum","Weight x MTOW"], "answer": 1, "explain": "CG = total moment divided by total weight."},
      {"q": "The datum is:", "choices": ["The heaviest point","A reference plane for measurements","The CG","The tail"], "answer": 1, "explain": "The datum is a reference plane from which all arms are measured."},
      {"q": "Ballast must be:", "choices": ["Loose in the cabin","Placarded and secured","Painted red","Removed for flight"], "answer": 1, "explain": "Permanent/temporary ballast must be secured and placarded per approved data."},
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
      {"heading": "Treatment", "body": "Remove all corrosion products (mechanical/chemical), assess to damage limits per SRM, neutralize, restore protective finish. Non-powered abrasives on aluminum (no steel wool - it embeds iron). Document; re-inspect on schedule."}
    ],
    "quiz": [
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
    ],
    "quiz": [
      {"q": "How many items in the Dirty Dozen?", "choices": ["10","12","14","6"], "answer": 1, "explain": "The Dirty Dozen is 12 human-factors error precursors."},
      {"q": "The SHELL model's second L is:", "choices": ["Logic","Liveware (people)","Loading","Lift"], "answer": 1, "explain": "SHELL = Software, Hardware, Environment, Liveware - the human element."},
      {"q": "A just culture encourages:", "choices": ["Hiding mistakes","Reporting errors to learn without blame","Punishing all errors","Ignoring reports"], "answer": 1, "explain": "Just culture invites honest error reporting so the system can improve."},
      {"q": "The Swiss-cheese model describes:", "choices": ["Cheese storage","Layered defenses with holes that can align","Fuel filtering","A rivet pattern"], "answer": 1, "explain": "Accidents occur when holes in successive defensive layers align."},
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
    ],
    "quiz": [
      {"q": "Hydraulics rely on which principle?", "choices": ["Bernoulli's","Pascal's Law","Ohm's Law","Charles' Law"], "answer": 1, "explain": "Pascal's Law - confined fluid transmits pressure equally, enabling force multiplication."},
      {"q": "Skydrol is what fluid type?", "choices": ["Mineral","Vegetable","Phosphate-ester","Synthetic oil"], "answer": 2, "explain": "Skydrol is a phosphate-ester fluid used in transport aircraft - corrosive, needs PPE."},
      {"q": "An accumulator does what?", "choices": ["Filters fluid","Stores pressure and dampens surges","Cools the fluid","Measures flow"], "answer": 1, "explain": "The accumulator stores hydraulic pressure and absorbs pressure spikes; it's precharged with gas."},
      {"q": "Mixing hydraulic fluid types causes:", "choices": ["Better performance","Seal damage/system failure","Color change only","Nothing"], "answer": 1, "explain": "Incompatible fluids attack seals - never mix mineral and phosphate-ester types."},
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
    ],
    "quiz": [
      {"q": "An oleo strut is serviced with:", "choices": ["Only air","Nitrogen/air and hydraulic fluid","Only fluid","Grease"], "answer": 1, "explain": "The air-oil oleo strut uses both a gas charge and hydraulic fluid for proper extension/damping."},
      {"q": "The WOW/squat switch prevents:", "choices": ["Overheating","Gear retraction on the ground","Brake fade","Tire wear"], "answer": 1, "explain": "The weight-on-wheels switch inhibits gear retraction while on the ground."},
      {"q": "Before removing split-rim wheel bolts you must:", "choices": ["Heat the tire","Fully deflate the tire","Add air","Spin the wheel"], "answer": 1, "explain": "Deflate first - a pressurized split rim can blow apart with lethal force."},
      {"q": "Anti-skid systems:", "choices": ["Increase speed","Prevent wheel lockup/skidding","Cool tires","Steer the nose"], "answer": 1, "explain": "Anti-skid modulates brake pressure to keep wheels from locking, maximizing braking."},
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
    ],
    "quiz": [
      {"q": "The pitot tube senses:", "choices": ["Static pressure","Ram (total) pressure","Temperature","Voltage"], "answer": 1, "explain": "Pitot senses ram/total pressure; static ports sense ambient. Together they drive the air data instruments."},
      {"q": "Which instruments use the static system?", "choices": ["Tachometer","Airspeed, altimeter, VSI","Oil pressure","Ammeter"], "answer": 1, "explain": "Airspeed, altimeter, and VSI all reference static (and pitot for airspeed) pressure."},
      {"q": "ADS-B Out primarily provides:", "choices": ["Engine data","Position/surveillance broadcast","Fuel flow","Cabin temp"], "answer": 1, "explain": "ADS-B Out broadcasts GPS-derived position for ATC surveillance - now required airspace."},
      {"q": "Gyro instruments rely on:", "choices": ["Rigidity and precession","Bernoulli","Combustion","Capacitance only"], "answer": 0, "explain": "Gyroscopic rigidity in space and precession drive attitude, heading, and turn indicators."},
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
    ],
    "quiz": [
      {"q": "Carburetor icing is countered with:", "choices": ["Mixture rich","Carburetor heat","More RPM","Fuel additive"], "answer": 1, "explain": "Carb heat supplies warm air to melt/prevent ice from the temperature drop in the venturi."},
      {"q": "Sump drains are checked for:", "choices": ["Oil level","Water and sediment","Voltage","Tire pressure"], "answer": 1, "explain": "Draining sumps removes water and sediment that settle at the tank low point."},
      {"q": "Continuous-flow fuel injection advantage over carbs:", "choices": ["Cheaper","No carb ice, better fuel distribution","Lighter only","Louder"], "answer": 1, "explain": "Injection eliminates carburetor icing and distributes fuel more evenly to cylinders."},
      {"q": "Turbine fuel scheduling is managed by:", "choices": ["A carburetor","Fuel control unit / FADEC","The pilot manually only","A magneto"], "answer": 1, "explain": "The FCU or FADEC schedules fuel with rpm, temperature, and air data inputs."},
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

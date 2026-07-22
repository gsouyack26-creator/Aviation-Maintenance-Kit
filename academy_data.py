"""Aviation Maintenance Academy - Course Data"""

MODULES = [
  {
    "id": "orientation", "title": "Orientation & Setup", "track": "general", "icon": "&#x1F9ED;",
    "sections": [
      {"heading": "The A&P World", "body": "In the U.S., aircraft mechanics hold an <b>FAA Mechanic Certificate</b> with <b>Airframe (A)</b> and/or <b>Powerplant (P)</b> ratings. Knowledge splits into: <b>General</b> (shared), <b>Airframe</b> (structure/systems), <b>Powerplant</b> (engines/props). Every action is regulated, traceable to approved data, and permanently documented."},
      {"heading": "Get Your Free Textbooks", "body": "Download from FAA Handbooks page:<ul><li><b>FAA-H-8083-30B</b> AMTH General</li><li><b>FAA-H-8083-31B</b> AMTH Airframe</li><li><b>FAA-H-8083-32B</b> AMTH Powerplant</li><li><b>AC 43.13-1B</b> Acceptable Methods</li></ul>Bookmark <b>eCFR Title 14</b> and <b>FAA DRS</b>."},
      {"heading": "Safety Mindset", "body": "<b>FOD</b> (Foreign Object Damage) - account for every tool/part. The <b>Dirty Dozen</b> human-factors errors: communication, complacency, knowledge, distraction, teamwork, fatigue, resources, pressure, assertiveness, stress, awareness, norms. <i>If it is not documented, it did not happen.</i>"},
      {"heading": "Course Road Map", "body": "20 modules across 3 tracks (~180 study hours). Each has lessons, formulas, labs, and quizzes. Complete all + pass the Final Exam for your certificate."}
    ,
      {"heading": "Career Pathways", "body": "A&P mechanics work across very different environments: <b>general aviation (GA) shops</b> (varied, hands-on, small aircraft), <b>Part 121 airlines</b> (structured, high-volume, specialized line/heavy maintenance), <b>Part 135 charter/cargo</b>, corporate/business aviation, and <b>repair stations</b> (Part 145) doing component overhaul. Many mechanics later pursue an <b>Inspection Authorization (IA)</b>, move into avionics specialization, or transition into quality, training, or management roles."}],
    "quiz": [
      {"q": "What do A and P stand for?", "choices": ["Airframe & Powerplant","Aviation & Propulsion","Assembly & Parts","Aerospace & Performance"], "answer": 0, "explain": "A&P = Airframe and Powerplant ratings on an FAA Mechanic Certificate."},
      {"q": "Which AC is the shop bible for repair methods?", "choices": ["AC 91-67","AC 43.13-1B","AC 20-62","AC 65-12"], "answer": 1, "explain": "AC 43.13-1B covers acceptable methods, techniques, and practices."},
      {"q": "What does FOD stand for?", "choices": ["Flight Ops Directive","Foreign Object Damage/Debris","Fuel-Oil Distribution","Federal Ops Document"], "answer": 1, "explain": "FOD = Foreign Object Damage/Debris. Loose items in an engine can be catastrophic."},
      {"q": "How many A&P knowledge domains?", "choices": ["2","3","4","5"], "answer": 1, "explain": "Three: General, Airframe, Powerplant."},
      {"q": "Which of these best describes a Part 145 repair station?", "choices": ["An airline flight department", "A certificated organization authorized to perform maintenance/overhaul under FAA oversight", "A flight training school", "An aircraft manufacturer only"], "answer": 1, "explain": "A Part 145 repair station is an FAA-certificated organization authorized to perform specific maintenance, repair, or overhaul work."},
      {"q": "Which is NOT a Dirty Dozen item?", "choices": ["Fatigue","Complacency","Enthusiasm","Distraction"], "answer": 2, "explain": "Enthusiasm is not one of the 12 human-factors error precursors."}
    ]
  },
  {
    "id": "math_physics", "title": "Mathematics & Physics", "track": "general", "icon": "&#x1F4D0;",
    "sections": [
      {"heading": "Shop Math", "body": "Ratios, percentages, area/volume, powers/roots, US-metric conversion. Master formula transposition. <b>Cylinder displacement</b> = (pi/4) x bore^2 x stroke x #cyl."},
      {"heading": "Forces, Work & Power", "body": "<b>Work</b> = Force x distance (W=Fd). <b>Power</b> = Work/time (P=W/t). <b>Mechanical advantage</b> = load/effort. These underpin hydraulics, jacks, and engine output."},
      {"heading": "Gas Laws", "body": "Critical for pressurization/pneumatics/oxygen:<ul><li><b>Boyle:</b> P1V1 = P2V2 (temp constant)</li><li><b>Charles:</b> V1/T1 = V2/T2 (press constant)</li><li><b>Combined:</b> P1V1/T1 = P2V2/T2</li></ul>Use absolute temperature (Kelvin/Rankine)."},
      {"heading": "Heat & Expansion", "body": "Transfer: conduction, convection, radiation. Materials expand when heated - matters for fits, clearances, cable tension (temp-correct tensiometer readings)."},
      {"heading": "Bernoulli & Pascal", "body": "<b>Bernoulli:</b> faster flow = lower pressure (lift, carburetors, venturi). <b>Pascal:</b> pressure in confined fluid transmits equally (hydraulic systems multiply force)."}
    ,
      {"heading": "Applying the Formulas", "body": "A wrench with a 10-inch handle applying 20 lb of force produces a torque of <b>200 in-lb</b> (Torque = Force x distance) - the same principle behind a torque wrench's specification. Mechanical advantage from a pulley or lever lets a smaller force move a larger load over a longer distance, but total work stays the same (ignoring friction) - this is why calculating the right tool or technique for a job matters as much as brute force."}],
    "quiz": [
      {"q": "Cylinder displacement formula:", "choices": ["(pi/4) x bore^2 x stroke x #cyl","pi x bore x stroke","bore^2 x stroke / 4","pi/2 x bore x stroke"], "answer": 0, "explain": "Displacement = (pi/4) x bore^2 x stroke x number of cylinders."},
      {"q": "In Boyle's Law, what is constant?", "choices": ["Pressure","Volume","Temperature","Mass"], "answer": 2, "explain": "Boyle's Law: P1V1=P2V2 when temperature is constant."},
      {"q": "Pascal's Law is the basis for:", "choices": ["Electrical systems","Hydraulic systems","Ignition","Induction"], "answer": 1, "explain": "Pascal's Law - pressure transmits equally in confined fluid - is the principle behind hydraulics."},
      {"q": "Work equals:", "choices": ["Force x time","Force x distance","Power x distance","Mass x velocity"], "answer": 1, "explain": "Work = Force x distance (W=Fd)."},
      {"q": "A wrench with a 10-inch handle applies 20 lb of force to a bolt. The torque produced is:", "choices": ["2 in-lb","20 in-lb","200 in-lb","2000 in-lb"], "answer": 2, "explain": "Torque = Force x distance = 20 lb x 10 in = 200 in-lb."},
      {"q": "Bernoulli explains:", "choices": ["Hydraulic multiplication","How lift is generated","Thermal expansion","Ohm's Law"], "answer": 1, "explain": "Faster flow = lower pressure explains how wings generate lift."}
    ]
  },
  {
    "id": "materials_hardware", "title": "Materials & Hardware", "track": "general", "icon": "&#x1F529;",
    "sections": [
      {"heading": "Aluminum Alloys", "body": "Key alloys: <b>2024-T3</b> (high strength, fatigue - skins/ribs), <b>7075-T6</b> (highest strength - spars/fittings), <b>6061-T6</b> (corrosion resistant, weldable). <b>Alclad</b> = clad with pure Al for corrosion protection. The -T suffix = temper condition."},
      {"heading": "Steel, Titanium, Magnesium", "body": "<b>4130 chromoly</b> - standard aircraft steel (engine mounts, gear, tubes). <b>Titanium</b> - strength of steel, 60% weight (firewalls, fasteners). <b>Magnesium</b> - lightest structural metal but flammable (Class D fire!)."},
      {"heading": "Composites", "body": "Fiberglass, carbon fiber, Kevlar in epoxy/polyester. <b>Honeycomb sandwich</b> for stiffness. Inspect: tap test (dull=disbond), ultrasonic. Repair: scarf/step-lap patches, vacuum bag + cure."},
      {"heading": "Aircraft Hardware", "body": "AN/MS/NAS bolts - head markings = grade. Grip length must match joint. <b>Positive locking:</b> safety wire, cotter pins, self-locking nuts. <b>Rivets:</b> AN470 (universal), AN426 (flush). Codes: AD=2117, DD=2024 (ice-box)."},
      {"heading": "Fluid Lines & Fittings", "body": "Rigid tube (5052-O Al, steel) bent to min 3xOD radius. Flex hose for vibration. <b>AN fittings = 37 degree flare</b> (never mix with 45 degree plumbing). Fire-sleeve on flammable-fluid lines."}
    ],
    "quiz": [
      {"q": "Alclad means:", "choices": ["Al clad with pure Al for corrosion","A composite type","Chromate treatment","Al-titanium alloy"], "answer": 0, "explain": "Alclad = high-strength alloy with pure aluminum cladding for corrosion resistance."},
      {"q": "AD rivet alloy:", "choices": ["2024","2117","7075","Steel"], "answer": 1, "explain": "AD = 2117-T3, the most common rivet. Drives as-received."},
      {"q": "Burning magnesium needs which extinguisher?", "choices": ["Class A","Class B","Class C","Class D"], "answer": 3, "explain": "Magnesium is combustible metal = Class D (dry powder)."},
      {"q": "AN fittings use what flare angle?", "choices": ["45 deg","37 deg","30 deg","90 deg"], "answer": 1, "explain": "AN (aircraft) fittings use 37 degrees. 45 is automotive - never mix."},
      {"q": "4130 chromoly is used for:", "choices": ["Wing skins","Engine mounts/fuselage tubes","Windows only","Prop blades"], "answer": 1, "explain": "4130 is the standard aircraft structural steel for mounts, gear, tubes."}
    ]
  },
  {
    "id": "electricity", "title": "Aircraft Electricity", "track": "general", "icon": "&#x26A1;",
    "sections": [
      {"heading": "DC Fundamentals", "body": "<b>Ohm's Law: E = I x R.</b> <b>Power: P = I x E = I^2 x R.</b> Series: same current, voltages add, Rt=sum. Parallel: same voltage, currents add, 1/Rt = 1/R1 + 1/R2 + ..."},
      {"heading": "AC Basics", "body": "Aircraft use <b>400 Hz</b> AC (lighter transformers). Capacitance (leads current), inductance (lags current), impedance. Transformers step voltage. Rectifiers convert AC to DC."},
      {"heading": "Batteries", "body": "<b>Lead-acid:</b> check specific gravity with hydrometer. <b>Ni-Cad:</b> lighter, higher discharge - but <b>THERMAL RUNAWAY</b> danger (cascading overheat = fire). Monitor cell temps during charging."},
      {"heading": "Generation & Distribution", "body": "14V or 28V DC bus systems. Alternators (engine-driven). Voltage regulators. Essential/main/avionics buses with tie relays. External power (GPU) for ground ops."},
      {"heading": "Wiring & Protection", "body": "AWG sizing by current + voltage drop. Bundle/route to avoid chafe/heat. <b>Circuit breakers</b> (never hold in a popping breaker!). Fuses. Mil-spec connectors. Read schematics."}
    ,
      {"heading": "Circuit Troubleshooting", "body": "A <b>voltage-drop test</b> (checking voltage loss across a connection or wire under load) finds high-resistance faults that a simple continuity check can miss. Compare live circuit voltage at the load to the source - excessive drop points to a bad connector, corroded ground, or damaged wire. Always verify continuity to ground and check for shorts to structure before assuming a component itself has failed."}],
    "quiz": [
      {"q": "28V bus, 7 ohm load. Current?", "choices": ["4 A","196 A","0.25 A","35 A"], "answer": 0, "explain": "I = E/R = 28/7 = 4 amps."},
      {"q": "In parallel, what stays constant?", "choices": ["Current","Resistance","Voltage","Power"], "answer": 2, "explain": "Parallel: voltage is the same across all branches."},
      {"q": "Aircraft AC frequency:", "choices": ["60 Hz","50 Hz","400 Hz","1000 Hz"], "answer": 2, "explain": "400 Hz allows smaller/lighter transformers and motors."},
      {"q": "Ni-Cad danger:", "choices": ["Sulfation","Thermal runaway","Freezing","Reverse polarity"], "answer": 1, "explain": "Ni-Cad batteries can experience thermal runaway - cascading overheat causing fire."},
      {"q": "A voltage-drop test is useful because it can detect:", "choices": ["Only a completely open circuit", "High-resistance connections that a simple continuity check may miss", "Battery amp-hour capacity only", "AC frequency drift"], "answer": 1, "explain": "Voltage-drop testing under load reveals corroded or loose connections that still pass a basic continuity check but cause excessive resistance."},
      {"q": "Never do this with a popping breaker:", "choices": ["Replace it","Check circuit","Hold it in","Record it"], "answer": 2, "explain": "Holding in a popping breaker overrides protection against an active fault - fire risk."}
    ]
  },
  {
    "id": "inspection_ndt", "title": "Inspection & NDT", "track": "general", "icon": "&#x1F50D;",
    "sections": [
      {"heading": "Visual Inspection", "body": "The most common method. Tools: flashlight, mirror, magnifier, <b>borescope</b>. Good lighting is critical. Look for: cracks, corrosion, wear, security, chafing, leaks, proper safetying."},
      {"heading": "Dye Penetrant (PT)", "body": "Detects <b>surface-breaking cracks</b> in non-porous materials. Process: Clean, Apply penetrant, Dwell, Remove excess, Developer, Inspect. Fluorescent (UV) is more sensitive than visible dye."},
      {"heading": "Magnetic Particle (MT)", "body": "Surface/near-surface flaws in <b>ferrous metals only</b>. Magnetize part, apply iron particles, particles gather at cracks. Circular mag finds lengthwise cracks; longitudinal finds transverse. <b>Demagnetize</b> after."},
      {"heading": "Eddy Current (ET)", "body": "Surface/subsurface cracks, conductivity, coating thickness on any <b>conductive</b> material. Coil generates field; defects change impedance. No contact needed. Heavy use around fastener holes."},
      {"heading": "Ultrasonic & Radiographic", "body": "<b>UT:</b> sound waves reflect off internal flaws; measures thickness. Great for composites/forgings. <b>RT (X-ray):</b> radiation through part onto film. Shows internal structure. Requires radiation safety certification."}
    ,
      {"heading": "Selecting the Right Method", "body": "Choice of NDT method depends on the material, flaw type, and location. <b>Magnetic particle</b> only works on ferrous metals. <b>Dye penetrant</b> finds only surface-breaking flaws in any non-porous material. <b>Eddy current</b> is excellent for surface/near-surface cracks in conductive metals (including aluminum) without couplant. <b>Ultrasonic</b> finds subsurface flaws and measures thickness in any material. <b>Radiographic (X-ray)</b> reveals internal voids/inclusions but requires strict radiation safety controls."}],
    "quiz": [
      {"q": "Which NDT works ONLY on ferrous metals?", "choices": ["Dye penetrant","Eddy current","Magnetic particle","Ultrasonic"], "answer": 2, "explain": "Magnetic particle needs a magnetizable (ferrous) part."},
      {"q": "Dye penetrant finds:", "choices": ["Internal voids","Subsurface cracks","Surface-breaking cracks only","Corrosion under paint"], "answer": 2, "explain": "Penetrant only enters surface-breaking discontinuities."},
      {"q": "After MT inspection you must:", "choices": ["Repaint","Demagnetize","Heat-treat","Replace"], "answer": 1, "explain": "Residual magnetism attracts chips and interferes with instruments."},
      {"q": "Which method measures remaining wall thickness?", "choices": ["Visual","Dye penetrant","Ultrasonic","Magnetic particle"], "answer": 2, "explain": "Ultrasonic precisely measures remaining material thickness."},
      {"q": "To detect a subsurface crack in an aluminum structure, the most appropriate NDT method would be:", "choices": ["Magnetic particle inspection", "Dye penetrant inspection", "Ultrasonic or eddy current inspection", "Visual inspection only"], "answer": 2, "explain": "Magnetic particle only works on ferrous metal, and dye penetrant only finds surface-breaking flaws - ultrasonic or eddy current can detect subsurface flaws in aluminum."},
      {"q": "Most commonly used inspection method:", "choices": ["Radiographic","Eddy current","Visual","Ultrasonic"], "answer": 2, "explain": "Visual inspection is the foundation - performed on every task."}
    ]
  },
  {
    "id": "structures", "title": "Aircraft Structures", "track": "airframe", "icon": "&#x1F3D7;",
    "sections": [
      {"heading": "Structural Types", "body": "<b>Truss:</b> welded steel tubes. <b>Monocoque:</b> skin carries all load (eggshell). <b>Semi-monocoque:</b> skin + frames/longerons/stringers (modern standard - damage tolerant)."},
      {"heading": "Wing Structure", "body": "<b>Spars</b> carry bending. <b>Ribs</b> maintain airfoil shape. <b>Stringers</b> stiffen skin. <b>Stressed skin</b> carries shear. <b>Wet wing</b> = sealed structure IS the fuel tank."},
      {"heading": "Loads & Stations", "body": "5 load types: tension, compression, shear, bending, torsion. <b>Station numbering:</b> FS (fuselage), BL (buttock line L/R), WL (waterline vertical) - locates any point precisely."},
      {"heading": "Control Systems", "body": "Primary: aileron (roll), elevator (pitch), rudder (yaw). Secondary: flaps, slats, trim tabs, spoilers. Types: cable/pulley, push-pull rod, torque tube, fly-by-wire."},
      {"heading": "Rigging", "body": "Aligning controls to spec. Cable tension via <b>tensiometer</b> (temp-corrected). Turnbuckles (safetied). Surface travel via protractor/fixture. <b>Balance</b> after repair/paint to prevent <b>flutter</b>."}
    ,
      {"heading": "Repair Philosophy", "body": "A structural repair must restore the original <b>strength, stiffness, contour, and corrosion protection</b> without adding excessive weight. A <b>doubler</b> reinforces a damaged area by spreading load around the repair; its size and rivet pattern come from approved data (AC 43.13-1B or manufacturer structural repair manual), not guesswork. Repairs must never be based on \"it looks strong enough\" - use approved data for material, thickness, and fastener pattern."}],
    "quiz": [
      {"q": "Semi-monocoque uses:", "choices": ["Skin only","Skin + frames + stringers","Truss tubes","Composites only"], "answer": 1, "explain": "Semi-monocoque: skin shares load with internal frames, longerons, and stringers."},
      {"q": "Primary wing bending load carrier:", "choices": ["Ribs","Skin","Spar","Stringers"], "answer": 2, "explain": "Spars are the main beams carrying wing bending loads."},
      {"q": "What measures cable tension?", "choices": ["Protractor","Torque wrench","Tensiometer","Dynamometer"], "answer": 2, "explain": "A tensiometer measures cable tension (correct for temperature)."},
      {"q": "Why balance control surfaces after repaint?", "choices": ["Appearance","Prevent flutter","Reduce drag","Weight savings"], "answer": 1, "explain": "Paint shifts CG; if aft of hinge line, destructive flutter can occur."},
      {"q": "The primary purpose of a doubler in a structural sheet metal repair is to:", "choices": ["Improve appearance only", "Spread load around the damaged/repaired area to restore strength", "Reduce weight", "Provide a mounting point for hardware"], "answer": 1, "explain": "A doubler reinforces the repair area, redistributing stress around the damage per approved repair data."},
      {"q": "Wet wing means:", "choices": ["Wing in rain","Wing sealed as fuel tank","Deice boots","Composite wing"], "answer": 1, "explain": "Integral tank - the sealed wing structure IS the fuel container."}
    ]
  },
  {
    "id": "sheet_metal", "title": "Sheet Metal & Riveting", "track": "airframe", "icon": "&#x1F528;",
    "sections": [
      {"heading": "Layout & Bends", "body": "<b>Bend Allowance</b> = (0.01743 x R + 0.0078 x T) x N degrees. <b>Setback (90 deg)</b> = R + T. Mark bend/sight lines. Brake bend. Min radius depends on alloy/temper."},
      {"heading": "Rivet Selection", "body": "Rules: <b>Diameter = 3 x thickness</b>. <b>Length = grip + 1.5D</b>. <b>Edge distance: 2-2.5D</b>. <b>Pitch: 4-6D</b>. <b>Transverse: 2.5D min</b>. Shop head: 1.5D wide x 0.5D high."},
      {"heading": "Rivet Types", "body": "AN470 (universal), AN426 (flush). Alloy codes: <b>AD=2117</b> (drives as-is), <b>DD=2024</b> (ice-box: heat-treat, refrigerate, drive cold within 20 min). Blind rivets (Cherry/Hi-Lok) where bucking bar cannot reach."},
      {"heading": "Riveting Procedure", "body": "1. Drill (rivet dia + 0.003 clearance). 2. Deburr both sides. 3. Cleco (temp fasteners). 4. Buck with gun + bar (perpendicular). 5. Inspect: shop head 1.5Dx0.5D, no cracks, flush for AN426."},
      {"heading": "Repair Philosophy", "body": "Restore/exceed original strength. Match rivet pattern. <b>Never reduce edge distance.</b> Follow SRM or AC 43.13-1B. <b>Stop-drill</b> crack ends immediately. Classify: negligible, repairable, replace."}
    ,
      {"heading": "Layout & Fastening Practice", "body": "<b>Clecos</b> temporarily hold sheets aligned and under clamping pressure during drilling and fitting, before final rivets are installed - this prevents holes from being drilled slightly out of alignment. Deburr every drilled hole to remove sharp edges that could start a crack. Dimple or countersink for flush fasteners per the thickness and rivet type specified in the repair data, and always match existing hole patterns exactly when replacing a panel."}],
    "quiz": [
      {"q": "For 0.050 in skin, rivet diameter:", "choices": ["1/16","3/32","5/32","1/4"], "answer": 2, "explain": "3 x 0.050 = 0.150 -> closest standard is 5/32 (0.156)."},
      {"q": "Setback for 90 deg, R=0.125, T=0.032:", "choices": ["0.093","0.125","0.157","0.250"], "answer": 2, "explain": "Setback = R+T = 0.125+0.032 = 0.157 inches."},
      {"q": "DD rivet must be:", "choices": ["Driven anytime","Heat-treated and refrigerated, driven cold","Driven hot","Used on steel only"], "answer": 1, "explain": "DD=2024 (ice-box). Heat-treat, refrigerate, drive within ~20 min before it hardens."},
      {"q": "Min edge distance for 1/8 in rivet:", "choices": ["1/8","3/16","1/4 to 5/16","1/2"], "answer": 2, "explain": "Edge = 2D to 2.5D. For 0.125: 0.250 to 0.3125 (1/4 to 5/16)."},
      {"q": "Clecos are used during sheet metal repair primarily to:", "choices": ["Permanently fasten the repair", "Temporarily hold sheets aligned and clamped before final riveting", "Measure rivet spacing", "Deburr drilled holes"], "answer": 1, "explain": "Clecos are temporary fasteners that hold layers in alignment and clamped together while drilling/fitting, and are removed as final rivets are installed."},
      {"q": "First action for a skin crack:", "choices": ["Rivet a patch","Stop-drill crack ends","Remove panel","Ignore if small"], "answer": 1, "explain": "Stop-drilling eliminates stress concentration at crack tip, preventing propagation."}
    ]
  },
  {
    "id": "airframe_systems", "title": "Airframe Systems", "track": "airframe", "icon": "&#x2699;",
    "sections": [
      {"heading": "Hydraulics", "body": "1500-3000 psi typical. Components: reservoir, pump, accumulator, valves, actuators, filters. Fluids (NEVER mix): <b>MIL-PRF-5606</b> (mineral, red), <b>Skydrol</b> (phosphate-ester, purple - corrosive! PPE required)."},
      {"heading": "Landing Gear", "body": "<b>Oleo struts:</b> nitrogen + hydraulic fluid. Check extension. Retraction: hydraulic/electric; up/down locks; <b>squat/WOW switch</b> prevents retract on ground. Brakes: disc, bleed, anti-skid. Tires: <b>nitrogen</b> inflation."},
      {"heading": "Fuel Systems", "body": "Boost pumps, selectors, strainers/sumps, cross-feed. Tanks: integral/bladder/rigid. Sump for water. Grades: 100LL (blue avgas), Jet A (clear/straw). <b>NEVER mis-fuel.</b> Ground/bond during fueling."},
      {"heading": "Environmental", "body": "<b>Pressurization:</b> bleed air, outflow valve, cabin altitude 6-8000 ft at FL350. <b>AC:</b> air-cycle packs or vapor-cycle. <b>Oxygen:</b> gaseous or chemical. <b>No oil/grease near O2</b> = auto-ignition risk!"},
      {"heading": "Ice/Rain & Fire", "body": "Anti-ice (prevent) vs de-ice (remove): boots, bleed air heat, electric heat, TKS weeping wing. Fire: continuous-loop detection, Halon bottles/squibs, firewall shutoff valves. Test per schedule."}
    ,
      {"heading": "System Interdependencies", "body": "Airframe systems often share resources and can fail together in non-obvious ways: a hydraulic pump failure can affect both brakes and gear retraction if they share a system; a bleed-air leak can trigger both a pressurization fault and an overheat warning in the same bay. When troubleshooting one system's fault, always consider what else shares its power source, hydraulic system, or bleed-air supply - fixing the wrong system wastes time and can mask the real problem."}],
    "quiz": [
      {"q": "Skydrol requires:", "choices": ["No special handling","PPE - corrosive","Heating","Mixing with mineral oil"], "answer": 1, "explain": "Skydrol (phosphate-ester) is corrosive to skin, eyes, paint. PPE mandatory."},
      {"q": "Aircraft tires inflated with:", "choices": ["Air","Nitrogen","Helium","CO2"], "answer": 1, "explain": "Nitrogen is inert - no moisture, stable pressure with temp change."},
      {"q": "Why no oil near O2 fittings?", "choices": ["Clogs system","Auto-ignition/explosion","Reduces flow","Voids warranty"], "answer": 1, "explain": "Oil/grease + high-pressure O2 can spontaneously ignite explosively."},
      {"q": "Squat switch prevents:", "choices": ["Overspeed","Gear retraction on ground","Depressurization","Cross-feed"], "answer": 1, "explain": "Weight-on-wheels switch inhibits gear retract while on the ground."},
      {"q": "When multiple aircraft systems fail or malfunction at the same time, a mechanic should first consider that they:", "choices": ["Are always unrelated coincidences", "May share a common power source, hydraulic system, or air supply", "Should each be replaced individually without investigation", "Indicate a software update is needed"], "answer": 1, "explain": "Shared resources (hydraulic systems, electrical buses, bleed air) can cause seemingly unrelated systems to fail together from a single root cause."},
      {"q": "Deice boots work by:", "choices": ["Heating","Inflating to crack ice","Chemical spray","Vibration"], "answer": 1, "explain": "Boots inflate and flex to break the ice bond; ice sheds in airstream."}
    ]
  },
  {
    "id": "recip_engines", "title": "Reciprocating Engines", "track": "powerplant", "icon": "&#x1F527;",
    "sections": [
      {"heading": "4-Stroke Cycle", "body": "Intake, Compression, Power, Exhaust. One power stroke per <b>2 crank revolutions (720 deg)</b> per cylinder. <b>CR</b> = V(BDC)/V(TDC), typically 7:1-8.7:1. Higher CR needs higher octane (detonation risk)."},
      {"heading": "Construction", "body": "Configs: horizontally-opposed (most GA), radial, inline, V. Parts: crankcase, crankshaft, connecting rods, pistons/rings, cylinders, valves, camshaft/lifters, accessory case."},
      {"heading": "Fuel & Induction", "body": "Air filter, carb heat/alternate air, manifold. <b>Carb icing</b> even in warm humid air. Float/pressure carbs, continuous-flow injection. Mixture control (rich for power, lean for cruise). Turbo/supercharging."},
      {"heading": "Ignition", "body": "<b>Dual magnetos</b> - engine-driven, self-contained. Two plugs/cyl for redundancy + better combustion. <b>E-gap timing</b> (internal) + <b>mag-to-engine timing</b> (core task). Spark plugs: gap, reach, heat range, rotation."},
      {"heading": "Lube & Cooling", "body": "Wet sump (opposed) vs dry sump (radial). Oil: lubricate, cool, clean, seal. Filter, cooler, SOAP analysis. <b>Air cooling:</b> cylinder fins + <b>baffles</b> (direct air) + <b>cowl flaps</b> (regulate). Missing baffles = hot spots = failure."}
    ,
      {"heading": "Common Failure Modes", "body": "<b>Detonation</b> (uncontrolled explosive combustion, often from low-octane fuel, over-lean mixture, or excessive heat) can destroy pistons and rings quickly. <b>Pre-ignition</b> (combustion starting before the spark from a hot spot like a glowing deposit) causes similar damage. <b>Shock cooling</b> from rapid power reduction can crack cylinders. Recognizing detonation/pre-ignition symptoms (rough running, high CHT, power loss) early prevents catastrophic engine damage."}],
    "quiz": [
      {"q": "Crank revolutions per power stroke (per cyl):", "choices": ["1","2","4","0.5"], "answer": 1, "explain": "4-stroke: one power stroke every 720 deg (2 full revolutions)."},
      {"q": "Compression ratio:", "choices": ["Bore/stroke","V(BDC)/V(TDC)","Intake P/exhaust P","Power/weight"], "answer": 1, "explain": "CR = total volume at BDC divided by clearance volume at TDC."},
      {"q": "Why dual magnetos?", "choices": ["More power only","Redundancy + better combustion","Less weight","Legal only"], "answer": 1, "explain": "Redundancy (one failing is survivable) plus two sparks give more complete combustion."},
      {"q": "Carb icing can occur in:", "choices": ["Freezing only","Above 80F only","Warm humid (50-70F, moist)","Altitude only"], "answer": 2, "explain": "Venturi + fuel evaporation drops carb temp 60F+ below ambient. Common at 50-70F with humidity."},
      {"q": "Detonation in a reciprocating engine is most commonly caused by:", "choices": ["Overly rich mixture and low RPM", "Low-octane fuel, excessive heat, or an over-lean mixture", "Cold weather starts", "Normal cruise power settings"], "answer": 1, "explain": "Detonation results from conditions that raise cylinder temperature/pressure beyond the fuel's ability to burn smoothly - low octane fuel, excess heat, or over-lean mixtures are common causes."},
      {"q": "Missing baffles cause:", "choices": ["Over-cooling","Localized overheating/failure","Oil leaks only","No effect"], "answer": 1, "explain": "Baffles direct cooling air. Missing = no directed airflow = hot spots = cracking."}
    ]
  },
  {
    "id": "turbine_engines", "title": "Turbine Engines", "track": "powerplant", "icon": "&#x2708;",
    "sections": [
      {"heading": "Brayton Cycle", "body": "Intake, Compress, Burn (constant pressure), Expand/Exhaust. Combustion is <b>continuous</b> (not intermittent). All sections work simultaneously. Smooth, high power-to-weight."},
      {"heading": "Sections", "body": "Inlet (pressure recovery) -> <b>Compressor</b> (axial or centrifugal, 15:1 to 40:1) -> Combustor (continuous burn) -> <b>Turbine</b> (drives compressor/fan) -> Exhaust/nozzle. Spools: N1 (LP), N2 (HP)."},
      {"heading": "Engine Types", "body": "<b>Turbojet:</b> all thrust from exhaust. <b>Turbofan:</b> bypass air (5:1-12:1 ratio) - quiet, efficient, airliners. <b>Turboprop:</b> drives prop via gearbox. <b>Turboshaft:</b> drives shaft (helicopters/APUs)."},
      {"heading": "Systems", "body": "Fuel: FCU or <b>FADEC</b>. Ignition: high-energy igniters (start + continuous mode only - combustion self-sustains). Oil: dry-sump synthetic, <b>chip detectors</b> (metal = wear). Instruments: N1/N2, <b>ITT/EGT</b> (primary limit), torque, fuel flow."},
      {"heading": "Inspection & Faults", "body": "<b>Borescope</b> hot section (cracks/burn/erosion). Start faults: <b>Hot start</b> (over-temp), <b>Hung start</b> (won't accelerate to idle), <b>Wet start</b> (no light-off). <b>Trend monitoring</b> (N1/EGT/vibration over time)."}
    ,
      {"heading": "Engine Health Monitoring", "body": "<b>Trend monitoring</b> tracks EGT, N1/N2, oil pressure/temp, and fuel flow over time to catch gradual deterioration before it becomes a failure. A slow, steady <b>EGT rise</b> at a given power setting over many flights often signals compressor or turbine efficiency loss (erosion, fouling) long before any single reading would exceed a limit. Borescope inspections combined with trend data give the clearest picture of internal engine condition without teardown."}],
    "quiz": [
      {"q": "Turbine combustion is:", "choices": ["Intermittent","Continuous","Only during start","Cyclic"], "answer": 1, "explain": "Gas turbines burn fuel continuously. All sections operate simultaneously."},
      {"q": "Most common on airliners:", "choices": ["Turbojet","Turboprop","Turbofan","Turboshaft"], "answer": 2, "explain": "Turbofans: bypass air provides quiet, efficient thrust at high bypass ratios."},
      {"q": "Hot start means:", "choices": ["EGT exceeds limit during start","Runs too cool","Oil overheats","Normal warmup"], "answer": 0, "explain": "Temperature exceeds limits during start - too much fuel vs airflow. Can damage hot section."},
      {"q": "Igniters used:", "choices": ["Continuously","Start and continuous-ignition mode only","Never after first start","To cool combustor"], "answer": 1, "explain": "Once lit, combustion is self-sustaining. Igniters fire only for start and CI mode."},
      {"q": "A gradual, steady rise in EGT at a constant power setting over many flights most likely indicates:", "choices": ["A normal break-in effect with no concern", "Slowly developing compressor or turbine efficiency loss", "A faulty EGT gauge only", "Overly rich fuel scheduling by design"], "answer": 1, "explain": "A slow upward trend in EGT at the same power setting typically reflects gradually declining internal engine efficiency (erosion, fouling, wear) and warrants investigation via trend data and borescope."},
      {"q": "Chip detectors indicate:", "choices": ["Normal ops","Metal wear - investigate","Low oil","Over-temp"], "answer": 1, "explain": "Magnetic plugs capture ferrous particles = internal wear = investigate/overhaul."}
    ]
  },
  {
    "id": "propellers", "title": "Propellers & Engine Inst.", "track": "powerplant", "icon": "&#x1F300;",
    "sections": [
      {"heading": "Prop Types", "body": "Fixed-pitch (one angle, compromise). Ground-adjustable. <b>Constant-speed</b> (governor adjusts angle to hold RPM). <b>Feathering</b> (90 deg = min drag, shut-down engine). <b>Reversing</b> (negative pitch = braking)."},
      {"heading": "Governor Operation", "body": "Uses engine oil (200-300 psi) vs counterweights/springs in hub. Pilot sets RPM -> flyweight senses speed -> overspeed: more pitch (more load); underspeed: less pitch. On-speed = equilibrium."},
      {"heading": "Prop Inspection", "body": "Leading-edge nicks = stress risers -> fatigue cracks. Dress per limits (blend radius). <b>Exceeds limits = condemn blade.</b> Track: tips in same plane. Static/dynamic balance. <b>Prop strike = mandatory teardown</b> of prop + engine."},
      {"heading": "Engine Instruments", "body": "Recip: tach (RPM), MP (manifold pressure), EGT, CHT, oil T/P, fuel flow. Turbine: N1/N2, <b>ITT/EGT</b> (PRIMARY limit), torque, fuel flow. Arcs: <b>green</b>=normal, <b>yellow</b>=caution, <b>red line</b>=never exceed."},
      {"heading": "Fire Protection & R&R", "body": "Engine fire zones: continuous-loop detection + extinguisher bottles/squibs + firewall shutoff valves. Engine R&R: disconnect all, hoist, inspect mounts/firewall, reinstall, ground-run + leak check + full records."}
    ],
    "quiz": [
      {"q": "Constant-speed prop changes ___ to hold RPM:", "choices": ["Engine power","Blade angle","Diameter","Fuel flow"], "answer": 1, "explain": "Governor adjusts blade angle (pitch) to maintain selected RPM."},
      {"q": "Feathering means:", "choices": ["Blades to 90 deg (min drag)","Removing prop","Blades flat","Reversing"], "answer": 0, "explain": "Feathering = edge-on to airstream, minimum drag on a shut-down engine."},
      {"q": "After prop strike:", "choices": ["Inspect prop only","Teardown prop AND engine","Continue if looks OK","Replace prop only"], "answer": 1, "explain": "Massive forces transmit through crankshaft - mandatory teardown of prop, engine, accessories."},
      {"q": "Primary turbine limit instrument:", "choices": ["N1","Fuel flow","ITT/EGT","Oil pressure"], "answer": 2, "explain": "ITT/EGT is THE critical limit - exceeding it damages hot-section components."},
      {"q": "Green-yellow-red arcs:", "choices": ["Fuel types","Normal-caution-never exceed","Oil grades","Temp only"], "answer": 1, "explain": "Standard markings: green=normal, yellow=caution, red line=never exceed."}
    ]
  },
  {
    "id": "regulations_records", "title": "Regulations & Records", "track": "general", "icon": "&#x1F4CB;",
    "sections": [
      {"heading": "Who May Maintain (43.3)", "body": "A&P mechanic, repair stations (Part 145), manufacturers, pilots (preventive maintenance only - oil/tires/plugs on own aircraft, Part 43 App A(c)). Pilots may NOT do inspections or structural repairs."},
      {"heading": "Return to Service (43.7)", "body": "After work, authorized person must approve RTS: A&P (for own work), <b>IA</b> (annuals + major work), repair station. Without proper RTS entry = aircraft NOT airworthy even if work is perfect."},
      {"heading": "Records (43.9/43.11)", "body": "Compliant entry needs 4 items: <b>1)</b> Description of work (or data ref), <b>2)</b> Date completed, <b>3)</b> Name of person doing work, <b>4)</b> Signature + cert number + kind of cert approving RTS. Inspections add: was/was not approved + discrepancy list."},
      {"heading": "ADs & Approved Data", "body": "<b>ADs (Part 39):</b> legally mandatory fixes for unsafe conditions. Track compliance. <b>Approved data:</b> mfr manual, IPC, SRM, SBs (advisory unless AD-referenced), AC 43.13-1B, Form 337 (major repairs/alterations)."},
      {"heading": "Path to A&P", "body": "1) Experience (30 mo both) OR Part 147 school. 2) Written tests (General+Airframe+Powerplant). 3) Oral & practical with DME. 4) Certificate (no expiration - but exercise within 6mo of each 24mo period). 5) After 3yr -> eligible for <b>IA</b>."}
    ],
    "quiz": [
      {"q": "A pilot may perform:", "choices": ["Annual inspections","Structural repairs","Listed preventive maintenance on own aircraft","Engine overhaul"], "answer": 2, "explain": "Pilots: only specific preventive maintenance listed in Part 43 App A(c) on own aircraft."},
      {"q": "Which form records major repairs?", "choices": ["Form 8610-2","Form 337","Form 8710","AD form"], "answer": 1, "explain": "FAA Form 337 documents major repairs and alterations."},
      {"q": "43.9 entry requires all EXCEPT:", "choices": ["Description","Date","Stock price","Signature+cert# approving RTS"], "answer": 2, "explain": "The 4 elements: description, date, performer name, signature+cert#+kind approving RTS."},
      {"q": "An AD is:", "choices": ["Optional guidance","Legally mandatory","Pilot advisory","Training doc"], "answer": 1, "explain": "ADs are mandatory - correct unsafe conditions. Non-compliance = unairworthy."},
      {"q": "A&P certificate expires:", "choices": ["Every 2 years","Every 5 years","Never (exercise or re-test)","At age 65"], "answer": 2, "explain": "Never expires, but must exercise privileges within 6mo of each 24mo period or re-test."}
    ]
  }
]

TRACKS = [
    {"id":"general","name":"General","color":"#3b82f6","modules":["orientation","math_physics","materials_hardware","electricity","inspection_ndt","regulations_records"]},
    {"id":"airframe","name":"Airframe","color":"#10b981","modules":["structures","sheet_metal","airframe_systems"]},
    {"id":"powerplant","name":"Powerplant","color":"#f59e0b","modules":["recip_engines","turbine_engines","propellers"]}
]

RANKS = [
    {"level":1,"name":"Student","xp":0},
    {"level":2,"name":"Apprentice","xp":100},
    {"level":3,"name":"Trainee Mechanic","xp":250},
    {"level":4,"name":"Junior Mechanic","xp":500},
    {"level":5,"name":"Mechanic","xp":800},
    {"level":6,"name":"Senior Mechanic","xp":1200},
    {"level":7,"name":"Lead Mechanic","xp":1700},
    {"level":8,"name":"Inspector","xp":2300},
    {"level":9,"name":"Master Mechanic","xp":3000},
    {"level":10,"name":"A&P Examiner","xp":4000}
]

XP = {"lesson":10,"quiz_perfect":50,"quiz_pass":25,"flashcard":2,"exam_pass":200,"practical_task":15,"focus_session":20}

ACHIEVEMENTS = [
    {"id":"first_lesson","name":"First Lesson","desc":"Complete your first lesson","icon":"&#x1F4D6;"},
    {"id":"perfect_quiz","name":"Ace!","desc":"Score 100% on any quiz","icon":"&#x1F4AF;"},
    {"id":"all_general","name":"General Certified","desc":"Complete all General modules","icon":"&#x1F393;"},
    {"id":"all_airframe","name":"Airframe Rated","desc":"Complete all Airframe modules","icon":"&#x1F6E9;"},
    {"id":"all_powerplant","name":"Powerplant Rated","desc":"Complete all Powerplant modules","icon":"&#x1F527;"},
    {"id":"full_ap","name":"Full A&P","desc":"Complete every module","icon":"&#x2708;"},
    {"id":"exam_pass","name":"Examiner Approved","desc":"Pass the final exam","icon":"&#x1F3C6;"},
    {"id":"flash_50","name":"Card Shark","desc":"Review 50 flashcards","icon":"&#x1F0CF;"},
    {"id":"streak_7","name":"Week Warrior","desc":"7-day study streak","icon":"&#x1F525;"},
    {"id":"speed_demon","name":"Speed Demon","desc":"Perfect quiz under 60 seconds","icon":"&#x26A1;"},
    {"id":"triple_crown","name":"Triple Crown","desc":"Complete General, Airframe, and Powerplant tracks fully","icon":"&#x1F451;"},
    {"id":"sim_explorer","name":"Sim Explorer","desc":"Try 10 different simulators","icon":"&#x1F9EA;"},
    {"id":"documentarian","name":"Documentarian","desc":"Export the Study Guide, Notes, and Glossary at least once each","icon":"&#x1F4C4;"}
]

FLASHCARDS = [
    {"front":"Ohm's Law","back":"E = I x R (Voltage = Current x Resistance)"},
    {"front":"Power formula","back":"P = I x E = I^2 R = E^2/R"},
    {"front":"Bend Allowance","back":"BA = (0.01743R + 0.0078T) x N degrees"},
    {"front":"Setback (90 deg)","back":"R + T (inside radius + thickness)"},
    {"front":"Rivet diameter rule","back":"Approx 3 x skin thickness"},
    {"front":"Rivet edge distance","back":"2D to 2.5D minimum"},
    {"front":"Rivet pitch","back":"4D to 6D center-to-center"},
    {"front":"Shop head dimensions","back":"1.5D wide x 0.5D high"},
    {"front":"CG formula","back":"CG = total moments / total weights"},
    {"front":"Compression ratio","back":"V(BDC) / V(TDC)"},
    {"front":"Brake Horsepower","back":"BHP = (Torque x RPM) / 5252"},
    {"front":"Combined Gas Law","back":"P1V1/T1 = P2V2/T2"},
    {"front":"Work formula","back":"W = Force x distance"},
    {"front":"Power (mechanical)","back":"P = Work / time"},
    {"front":"AD stands for","back":"Airworthiness Directive (mandatory fix)"},
    {"front":"FOD stands for","back":"Foreign Object Damage/Debris"},
    {"front":"NDT stands for","back":"Non-Destructive Testing"},
    {"front":"FADEC","back":"Full Authority Digital Engine Control"},
    {"front":"Diff compression: air out exhaust","back":"Leaking exhaust valve"},
    {"front":"Diff compression: air out intake","back":"Leaking intake valve"},
    {"front":"Diff compression: air out breather","back":"Worn piston rings"},
    {"front":"AN flare angle","back":"37 degrees (aircraft standard)"},
    {"front":"4130 steel used for","back":"Engine mounts, landing gear, fuselage tubes"},
    {"front":"Alclad purpose","back":"Pure Al cladding for corrosion protection"},
    {"front":"DD rivet alloy","back":"2024-T4 (ice-box: heat-treat, refrigerate, drive cold)"},
    {"front":"AD rivet alloy","back":"2117-T3 (drives as-received)"},
    {"front":"Skydrol is","back":"Phosphate-ester hydraulic fluid - corrosive, PPE required"},
    {"front":"Squat/WOW switch","back":"Detects weight-on-wheels; prevents gear retract on ground"},
    {"front":"43.9 requires (4 items)","back":"Description, date, performer name, signature+cert#+kind"},
    {"front":"Aircraft AC frequency","back":"400 Hz (lighter transformers than 60 Hz)"},
    {"front":"Mag check: excess RPM drop","back":"Faulty mag, dead plugs, or timing off"},
    {"front":"Hot start (turbine)","back":"EGT/ITT exceeds limit during start"},
    {"front":"Hung start (turbine)","back":"Lights but won't accelerate to idle"},
    {"front":"Feathering","back":"Prop blades at 90 deg = minimum drag (shut-down engine)"},
    {"front":"Prop strike requires","back":"Teardown inspection: prop + engine + accessories"},
    {"front":"Boyle's Law","back":"P1V1 = P2V2 (temperature constant)"},
    {"front":"Part 43 governs","back":"Maintenance, preventive maintenance, rebuilding, alteration"},
    {"front":"Part 65 governs","back":"Certification of airmen other than flight crew"},
    {"front":"Dye penetrant detects","back":"Surface-breaking cracks in non-porous materials"},
    {"front":"Magnetic particle requires","back":"Ferrous (magnetic) material only"}
]

GLOSSARY = [
    {"term":"A&P","def":"Airframe and Powerplant mechanic certificate ratings"},
    {"term":"AD","def":"Airworthiness Directive - mandatory corrective action"},
    {"term":"Alclad","def":"High-strength Al clad with pure Al for corrosion resistance"},
    {"term":"AOA","def":"Angle of Attack - angle between chord line and relative wind"},
    {"term":"APU","def":"Auxiliary Power Unit - small turbine for ground power"},
    {"term":"Baffle","def":"Sheet metal directing cooling air over cylinders"},
    {"term":"Bernoulli","def":"Faster fluid velocity = decreased pressure"},
    {"term":"Borescope","def":"Optical instrument for internal inspection without disassembly"},
    {"term":"Brayton Cycle","def":"Thermodynamic cycle of gas turbines (continuous combustion)"},
    {"term":"Bucking Bar","def":"Mass held behind rivet while gun forms shop head"},
    {"term":"CG","def":"Center of Gravity - aircraft balance point"},
    {"term":"Cleco","def":"Temporary spring fastener holding sheets during riveting"},
    {"term":"CR","def":"Compression Ratio = V(BDC)/V(TDC)"},
    {"term":"DME","def":"Designated Mechanic Examiner - administers A&P practical tests"},
    {"term":"EGT","def":"Exhaust Gas Temperature - critical turbine limit"},
    {"term":"FADEC","def":"Full Authority Digital Engine Control"},
    {"term":"FOD","def":"Foreign Object Damage/Debris"},
    {"term":"Form 337","def":"FAA form documenting major repairs/alterations"},
    {"term":"Governor","def":"Maintains constant prop RPM by adjusting blade angle"},
    {"term":"IA","def":"Inspection Authorization - annuals and major work approval"},
    {"term":"ITT","def":"Interstage Turbine Temperature - engine limit gauge"},
    {"term":"Longeron","def":"Major lengthwise structural member in fuselage"},
    {"term":"Magneto","def":"Self-contained ignition generator for recip engines"},
    {"term":"Monocoque","def":"Structure where skin carries all loads"},
    {"term":"N1/N2","def":"Low/high-pressure spool speeds (percent RPM)"},
    {"term":"NDT","def":"Non-Destructive Testing"},
    {"term":"Oleo Strut","def":"Air-oil shock absorber in landing gear"},
    {"term":"Otto Cycle","def":"Thermodynamic cycle of 4-stroke recip engines"},
    {"term":"Pascal","def":"Pressure in confined fluid transmits equally"},
    {"term":"RTS","def":"Return to Service - formal airworthiness approval"},
    {"term":"Semi-monocoque","def":"Skin + frames + stringers (modern standard)"},
    {"term":"Skydrol","def":"Phosphate-ester hydraulic fluid - corrosive"},
    {"term":"SOAP","def":"Spectrometric Oil Analysis Program"},
    {"term":"Spar","def":"Primary wing beam carrying bending loads"},
    {"term":"SRM","def":"Structural Repair Manual"},
    {"term":"STC","def":"Supplemental Type Certificate - approved modification"},
    {"term":"TBO","def":"Time Between Overhaul"},
    {"term":"TCDS","def":"Type Certificate Data Sheet - approved config and limits"},
    {"term":"Tensiometer","def":"Measures control cable tension"},
    {"term":"Thermal Runaway","def":"Cascading Ni-Cad overheat - fire risk"},
    {"term":"Torque Wrench","def":"Applies precise rotational force to fasteners"},
    {"term":"Turnbuckle","def":"Adjusts cable tension (must be safetied)"},
    {"term":"WOW Switch","def":"Weight-On-Wheels switch - ground/air detection"},
    {"term":"Zonal Inspection","def":"Inspection organized by physical aircraft zones"}
]

# ---------------------------------------------------------------------------
# Expansion pack merge (see academy_ext.py). Extends the core lists so the
# build stays a single import. Adding new modules here keeps TRACKS in sync.
# ---------------------------------------------------------------------------
from academy_ext import EXT_MODULES, EXT_FLASHCARDS, EXT_GLOSSARY

_existing_ids = {m["id"] for m in MODULES}
for _m in EXT_MODULES:
    if _m["id"] not in _existing_ids:
        MODULES.append(_m)

FLASHCARDS.extend(EXT_FLASHCARDS)
GLOSSARY.extend(EXT_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD = {
    "general":    ["ground_ops", "weight_balance", "corrosion", "human_factors"],
    "airframe":   ["fluid_power", "landing_gear", "avionics"],
    "powerplant": ["fuel_systems"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Expansion pack 3 merge (see academy_ext3.py) - Wave 2: 5 new modules.
# ---------------------------------------------------------------------------
from academy_ext3 import EXT3_MODULES, EXT3_FLASHCARDS, EXT3_GLOSSARY

_existing_ids2 = {m["id"] for m in MODULES}
for _m in EXT3_MODULES:
    if _m["id"] not in _existing_ids2:
        MODULES.append(_m)

FLASHCARDS.extend(EXT3_FLASHCARDS)
GLOSSARY.extend(EXT3_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD2 = {
    "general":    ["advanced_electrical", "career_path"],
    "airframe":   ["composites_adv", "ice_rain_protection"],
    "powerplant": ["engine_overhaul"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD2.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# ---------------------------------------------------------------------------
_seen_terms = set()
_deduped_glossary = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms:
        _seen_terms.add(_key)
        _deduped_glossary.append(_g)
GLOSSARY = _deduped_glossary

# ---------------------------------------------------------------------------
# Wave 3 expansion (academy_ext5): aerodynamics, environmental_oxygen,
# turbine_fuel_ignition, engine_instruments, welding_fabrication
# ---------------------------------------------------------------------------
from academy_ext5 import EXT5_MODULES, EXT5_FLASHCARDS, EXT5_GLOSSARY

_existing_ids3 = {m["id"] for m in MODULES}
for _m in EXT5_MODULES:
    if _m["id"] not in _existing_ids3:
        MODULES.append(_m)

FLASHCARDS.extend(EXT5_FLASHCARDS)
GLOSSARY.extend(EXT5_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD3 = {
    "airframe":   ["aerodynamics", "environmental_oxygen"],
    "powerplant": ["turbine_fuel_ignition", "engine_instruments"],
    "general":    ["welding_fabrication"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD3.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 3 merge.)
# ---------------------------------------------------------------------------
_seen_terms3 = set()
_deduped_glossary3 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms3:
        _seen_terms3.add(_key)
        _deduped_glossary3.append(_g)
GLOSSARY = _deduped_glossary3

# ---------------------------------------------------------------------------
# Wave 4 expansion (academy_ext7): precision_tools, flight_controls_rigging,
# fire_protection, prop_governing, apu_testcell
# ---------------------------------------------------------------------------
from academy_ext7 import EXT7_MODULES, EXT7_FLASHCARDS, EXT7_GLOSSARY

_existing_ids4 = {m["id"] for m in MODULES}
for _m in EXT7_MODULES:
    if _m["id"] not in _existing_ids4:
        MODULES.append(_m)

FLASHCARDS.extend(EXT7_FLASHCARDS)
GLOSSARY.extend(EXT7_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD4 = {
    "general":    ["precision_tools"],
    "airframe":   ["flight_controls_rigging", "fire_protection"],
    "powerplant": ["prop_governing", "apu_testcell"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD4.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 4 merge.)
# ---------------------------------------------------------------------------
_seen_terms4 = set()
_deduped_glossary4 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms4:
        _seen_terms4.add(_key)
        _deduped_glossary4.append(_g)
GLOSSARY = _deduped_glossary4

# ---------------------------------------------------------------------------
# Wave 5 expansion (academy_ext9): human_factors, nde_inspection,
# ice_rain_protection, recip_overhaul, turbine_overhaul
# ---------------------------------------------------------------------------
from academy_ext9 import EXT9_MODULES, EXT9_FLASHCARDS, EXT9_GLOSSARY

_existing_ids5 = {m["id"] for m in MODULES}
for _m in EXT9_MODULES:
    if _m["id"] not in _existing_ids5:
        MODULES.append(_m)

FLASHCARDS.extend(EXT9_FLASHCARDS)
GLOSSARY.extend(EXT9_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD5 = {
    "general":    ["human_factors"],
    "airframe":   ["nde_inspection", "ice_rain_protection"],
    "powerplant": ["recip_overhaul", "turbine_overhaul"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD5.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 5 merge.)
# ---------------------------------------------------------------------------
_seen_terms5 = set()
_deduped_glossary5 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms5:
        _seen_terms5.add(_key)
        _deduped_glossary5.append(_g)
GLOSSARY = _deduped_glossary5

# ---------------------------------------------------------------------------
# Wave 6 expansion (academy_ext11): corrosion_control, hydraulic_systems,
# landing_gear, turbine_theory, engine_lubrication
# ---------------------------------------------------------------------------
from academy_ext11 import EXT11_MODULES, EXT11_FLASHCARDS, EXT11_GLOSSARY

_existing_ids6 = {m["id"] for m in MODULES}
for _m in EXT11_MODULES:
    if _m["id"] not in _existing_ids6:
        MODULES.append(_m)

FLASHCARDS.extend(EXT11_FLASHCARDS)
GLOSSARY.extend(EXT11_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD6 = {
    "general":    ["corrosion_control"],
    "airframe":   ["hydraulic_systems", "landing_gear_systems"],
    "powerplant": ["turbine_theory", "engine_lubrication"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD6.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 6 merge.)
# ---------------------------------------------------------------------------
_seen_terms6 = set()
_deduped_glossary6 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms6:
        _seen_terms6.add(_key)
        _deduped_glossary6.append(_g)
GLOSSARY = _deduped_glossary6

# ---------------------------------------------------------------------------
# Wave 7 expansion (academy_ext13): pneumatic_systems, wiring_harness_repair,
# cabin_pressurization, borescope_inspection, recip_ignition
# ---------------------------------------------------------------------------
from academy_ext13 import EXT13_MODULES, EXT13_FLASHCARDS, EXT13_GLOSSARY

_existing_ids7 = {m["id"] for m in MODULES}
for _m in EXT13_MODULES:
    if _m["id"] not in _existing_ids7:
        MODULES.append(_m)

FLASHCARDS.extend(EXT13_FLASHCARDS)
GLOSSARY.extend(EXT13_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD7 = {
    "general":    ["wiring_harness_repair"],
    "airframe":   ["pneumatic_systems", "cabin_pressurization"],
    "powerplant": ["borescope_inspection", "recip_ignition"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD7.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 7 merge.)
# ---------------------------------------------------------------------------
_seen_terms7 = set()
_deduped_glossary7 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms7:
        _seen_terms7.add(_key)
        _deduped_glossary7.append(_g)
GLOSSARY = _deduped_glossary7

# ---------------------------------------------------------------------------
# Wave 8 expansion (academy_ext15): nondestructive_electrical, aircraft_batteries,
# fuel_metering, turbine_starting, sheet_metal_repair_adv
# ---------------------------------------------------------------------------
from academy_ext15 import EXT15_MODULES, EXT15_FLASHCARDS, EXT15_GLOSSARY

_existing_ids8 = {m["id"] for m in MODULES}
for _m in EXT15_MODULES:
    if _m["id"] not in _existing_ids8:
        MODULES.append(_m)

FLASHCARDS.extend(EXT15_FLASHCARDS)
GLOSSARY.extend(EXT15_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD8 = {
    "general":    ["nondestructive_electrical", "aircraft_batteries"],
    "airframe":   ["sheet_metal_repair_adv"],
    "powerplant": ["fuel_metering", "turbine_starting"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD8.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 8 merge.)
# ---------------------------------------------------------------------------
_seen_terms8 = set()
_deduped_glossary8 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms8:
        _seen_terms8.add(_key)
        _deduped_glossary8.append(_g)
GLOSSARY = _deduped_glossary8

# ---------------------------------------------------------------------------
# Wave 9 expansion (academy_ext17): hoisting_jacking, avionics_troubleshooting,
# oxygen_systems_adv, gas_turbine_performance, aircraft_finishes
# ---------------------------------------------------------------------------
from academy_ext17 import EXT17_MODULES, EXT17_FLASHCARDS, EXT17_GLOSSARY

_existing_ids9 = {m["id"] for m in MODULES}
for _m in EXT17_MODULES:
    if _m["id"] not in _existing_ids9:
        MODULES.append(_m)

FLASHCARDS.extend(EXT17_FLASHCARDS)
GLOSSARY.extend(EXT17_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD9 = {
    "general":    ["hoisting_jacking"],
    "airframe":   ["avionics_troubleshooting", "oxygen_systems_adv", "aircraft_finishes"],
    "powerplant": ["gas_turbine_performance"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD9.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 9 merge.)
# ---------------------------------------------------------------------------
_seen_terms9 = set()
_deduped_glossary9 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms9:
        _seen_terms9.add(_key)
        _deduped_glossary9.append(_g)
GLOSSARY = _deduped_glossary9
# ---------------------------------------------------------------------------
# Wave 10 expansion (academy_ext19): aircraft_welding_gas, aircraft_electrical_bonding,
# aircraft_scheduled_inspections, aircraft_fabric_covering, engine_condition_monitoring
# ---------------------------------------------------------------------------
from academy_ext19 import EXT19_MODULES, EXT19_FLASHCARDS, EXT19_GLOSSARY

_existing_ids10 = {m["id"] for m in MODULES}
for _m in EXT19_MODULES:
    if _m["id"] not in _existing_ids10:
        MODULES.append(_m)

FLASHCARDS.extend(EXT19_FLASHCARDS)
GLOSSARY.extend(EXT19_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD10 = {
    "general":    ["aircraft_scheduled_inspections"],
    "airframe":   ["aircraft_welding_gas", "aircraft_electrical_bonding", "aircraft_fabric_covering"],
    "powerplant": ["engine_condition_monitoring"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD10.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 10 merge.)
# ---------------------------------------------------------------------------
_seen_terms10 = set()
_deduped_glossary10 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms10:
        _seen_terms10.add(_key)
        _deduped_glossary10.append(_g)
GLOSSARY = _deduped_glossary10
# ---------------------------------------------------------------------------
# Wave 11 expansion (academy_ext21): turbocharging_systems, fadec_engine_controls,
# emergency_equipment_systems, ground_support_equipment, fuel_quantity_indicating
# ---------------------------------------------------------------------------
from academy_ext21 import EXT21_MODULES, EXT21_FLASHCARDS, EXT21_GLOSSARY

_existing_ids11 = {m["id"] for m in MODULES}
for _m in EXT21_MODULES:
    if _m["id"] not in _existing_ids11:
        MODULES.append(_m)

FLASHCARDS.extend(EXT21_FLASHCARDS)
GLOSSARY.extend(EXT21_GLOSSARY)
GLOSSARY.sort(key=lambda x: x["term"].lower())

_TRACK_ADD11 = {
    "general":    ["ground_support_equipment"],
    "airframe":   ["emergency_equipment_systems", "fuel_quantity_indicating"],
    "powerplant": ["turbocharging_systems", "fadec_engine_controls"],
}
for _t in TRACKS:
    for _id in _TRACK_ADD11.get(_t["id"], []):
        if _id not in _t["modules"]:
            _t["modules"].append(_id)

# ---------------------------------------------------------------------------
# Safety net: dedupe glossary by term (case-insensitive), keep first occurrence.
# (Re-applied after Wave 11 merge.)
# ---------------------------------------------------------------------------
_seen_terms11 = set()
_deduped_glossary11 = []
for _g in GLOSSARY:
    _key = _g["term"].strip().lower()
    if _key not in _seen_terms11:
        _seen_terms11.add(_key)
        _deduped_glossary11.append(_g)
GLOSSARY = _deduped_glossary11
# ---------------------------------------------------------------------------
# Safety net: normalize any module sections that used the alternate {"h","p"}
# key convention (found in a Wave 10/11 authoring regression) to the standard
# {"heading","body"} convention expected by the renderer in build_aviation_academy.py.
# ---------------------------------------------------------------------------
for _m in MODULES:
    for _s in _m["sections"]:
        if "heading" not in _s and "h" in _s:
            _s["heading"] = _s.pop("h")
        if "body" not in _s and "p" in _s:
            _s["body"] = _s.pop("p")

# ---------------------------------------------------------------------------
# FAA source alignment: stamp each module with a citation to the relevant
# official FAA Aviation Maintenance Technician Handbook (FAA-H-8083 series),
# so learners can see exactly which authoritative source each module's
# subject matter is drawn from / aligned to. This is a good-faith content
# citation, NOT a claim of licensed FAA test-bank question alignment.
# ---------------------------------------------------------------------------
_FAA_HANDBOOK_BY_TRACK = {
    "general":    "FAA-H-8083-30A \u2014 Aviation Maintenance Technician Handbook: General",
    "airframe":   "FAA-H-8083-31 \u2014 Aviation Maintenance Technician Handbook: Airframe",
    "powerplant": "FAA-H-8083-32B \u2014 Aviation Maintenance Technician Handbook: Powerplant",
}
_track_of_module = {}
for _t in TRACKS:
    for _mid in _t["modules"]:
        _track_of_module[_mid] = _t["id"]
for _m in MODULES:
    if not _m.get("faa_ref"):
        _trk = _track_of_module.get(_m["id"], _m.get("track"))
        _m["faa_ref"] = _FAA_HANDBOOK_BY_TRACK.get(_trk, "FAA-H-8083 Series \u2014 Aviation Maintenance Technician Handbook")

# ---------------------------------------------------------------------------
# Subject Practice Tests feature: add the "Subject Master" achievement,
# earned for passing all three timed subject tests (General/Airframe/
# Powerplant), modeled on the FAA Airman Knowledge Test structure.
# ---------------------------------------------------------------------------
if not any(a["id"] == "subject_master" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "subject_master",
        "name": "Subject Master",
        "desc": "Pass all three timed Subject Practice Tests (General, Airframe, Powerplant) at 70%+",
        "icon": "&#x23F1;",
    })

# ---------------------------------------------------------------------------
# Mock Oral Exam feature: add the "Oral Ready" achievement, earned for
# self-grading 80%+ on a full Mock Oral round.
# ---------------------------------------------------------------------------
if not any(a["id"] == "oral_ready" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "oral_ready",
        "name": "Oral Ready",
        "desc": "Score 80%+ (self-graded) on a full Mock Oral Exam round",
        "icon": "&#x1F3A4;",
    })

# ---------------------------------------------------------------------------
# Practical Task Log feature: add the "Practical Task Veteran" achievement,
# earned for logging 15+ of the 20 ACS-style hands-on practical tasks.
# ---------------------------------------------------------------------------
if not any(a["id"] == "practical_task_veteran" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "practical_task_veteran",
        "name": "Practical Task Veteran",
        "desc": "Log 15+ of the 20 ACS-style hands-on Practical Tasks",
        "icon": "&#x1F527;",
    })

# ---------------------------------------------------------------------------
# "Exam Ready" achievement, earned for reaching 90%+ overall Exam Readiness
# (the weighted composite of modules, quizzes, subject tests, oral, practical
# tasks, and the final exam) -- the single best-in-class milestone that ties
# every study surface in the app together.
# ---------------------------------------------------------------------------
if not any(a["id"] == "exam_ready" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "exam_ready",
        "name": "Exam Ready",
        "desc": "Reach 90%+ overall Exam Readiness across every pillar",
        "icon": "&#x1F680;",
    })

# ---------------------------------------------------------------------------
# "Daily Devotee" achievement, earned for a 7-day Daily Challenge answer
# streak -- rewards consistent day-over-day engagement with the quick
# spaced-practice question shown on the dashboard.
# ---------------------------------------------------------------------------
if not any(a["id"] == "challenge_streak" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "challenge_streak",
        "name": "Daily Devotee",
        "desc": "Answer the Daily Challenge on 7 consecutive days",
        "icon": "&#x1F4C6;",
    })

# ---------------------------------------------------------------------------
# "Deep Focus" achievement, earned after completing 5 Pomodoro-style Focus
# Timer study sessions from the dashboard -- rewards sustained,
# distraction-free study time rather than just quiz/flashcard activity.
# ---------------------------------------------------------------------------
if not any(a["id"] == "focus_5" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "focus_5",
        "name": "Deep Focus",
        "desc": "Complete 5 Focus Timer study sessions",
        "icon": "&#x1F9D8;",
    })

if not any(a["id"] == "curator" for a in ACHIEVEMENTS):
    ACHIEVEMENTS.append({
        "id": "curator",
        "name": "Curator",
        "desc": "Star 5 Reference Library or Glossary items for quick access",
        "icon": "&#x2B50;",
    })

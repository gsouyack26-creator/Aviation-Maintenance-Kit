"""Aviation Maintenance Academy - Wave 5 content pack.
Adds 5 new modules balanced across tracks. Merged in academy_data.py.
"""

EXT9_MODULES = [
  {
    "id": "human_factors", "title": "Human Factors & Maintenance Error", "track": "general", "icon": "&#x1F9E0;",
    "sections": [
      {"heading": "The Dirty Dozen", "body": "A well-known list of the twelve most common human factors that lead to maintenance errors: lack of communication, complacency, lack of knowledge, distraction, lack of teamwork, fatigue, lack of resources, pressure, lack of assertiveness, stress, lack of awareness, and norms. Recognizing these in yourself and coworkers is the first step to preventing errors."},
      {"heading": "SHELL Model", "body": "The SHELL model frames human factors around interfaces: <b>Software</b> (procedures, manuals), <b>Hardware</b> (tools, equipment), <b>Environment</b> (lighting, noise, weather), <b>Liveware</b> (the people involved - self and others). Most errors occur at the boundary where Liveware interacts poorly with one of the other elements."},
      {"heading": "Fatigue & Shift Work", "body": "Fatigue degrades attention, decision-making, and memory - comparable to alcohol impairment at extreme levels. Shift work, especially rotating or night shifts, disrupts circadian rhythm. Fatigue risk management includes adequate rest periods, workload planning, and self-reporting when unfit for safety-critical tasks."},
      {"heading": "Error-Reduction Tools", "body": "Techniques include: written <b>checklists</b> and sign-offs, <b>duplicate/independent inspections</b> for critical systems, <b>task cards</b> that force step-by-step documentation, and a strong <b>reporting culture</b> (non-punitive) that surfaces near-misses before they become incidents. Distraction management (e.g., 'sterile' focus periods for critical steps) also reduces skipped-step errors."}
    ],
    "quiz": [
      {"q": "The 'Dirty Dozen' in maintenance human factors refers to:", "choices": ["Twelve types of aircraft damage","Twelve common human factors that lead to maintenance errors","A tool inventory list","Twelve FAA regulations"], "answer": 1, "explain": "The Dirty Dozen is a list of twelve human factors (e.g., fatigue, complacency, distraction) commonly linked to maintenance errors."},
      {"q": "In the SHELL model, what does the 'L' in the center stand for?", "choices": ["Liveware (people)","Lighting","Logistics","Landing gear"], "answer": 0, "explain": "The central Liveware represents the person performing the task, interacting with Software, Hardware, and Environment."},
      {"q": "Extreme fatigue can impair performance comparably to:", "choices": ["Caffeine overuse","Alcohol impairment","Overtraining","Excess vitamin intake"], "answer": 1, "explain": "Research shows severe fatigue can degrade performance to a degree comparable with alcohol intoxication."},
      {"q": "Why are duplicate/independent inspections required on critical systems?", "choices": ["To slow down work","To catch errors a single inspector might miss","To increase paperwork for its own sake","They are optional"], "answer": 1, "explain": "A second, independent set of eyes catches errors the original mechanic may be blind to due to expectation bias."},
      {"q": "A non-punitive reporting culture primarily helps by:", "choices": ["Hiding mistakes","Surfacing near-misses and hazards before they cause an incident","Reducing paperwork","Increasing overtime"], "answer": 1, "explain": "When people aren't punished for honest reporting, hazards and near-misses get surfaced and corrected proactively."}
    ]
  },
  {
    "id": "nde_inspection", "title": "Nondestructive Inspection (NDI/NDT)", "track": "airframe", "icon": "&#x1F50E;",
    "sections": [
      {"heading": "Visual & Dye Penetrant", "body": "<b>Visual inspection</b> (aided by mirrors, borescopes, magnification) is the most common NDI method. <b>Dye penetrant</b> inspection reveals surface-breaking cracks: penetrant is applied, excess removed, then a developer draws penetrant back out of any crack, showing a visible indication - effective on non-porous materials like aluminum and steel."},
      {"heading": "Magnetic Particle Inspection", "body": "Used on ferromagnetic materials only (steel, some alloys). The part is magnetized, then iron particles are applied; particles cluster at flux leakage points caused by surface or near-surface cracks, revealing the defect. Cannot be used on aluminum, titanium, or other non-magnetic materials."},
      {"heading": "Eddy Current & Ultrasonic", "body": "<b>Eddy current</b> inspection induces electrical currents in conductive material via a probe coil; cracks and corrosion disrupt the current, changing the probe's signal - good for surface/near-surface flaws, especially around fastener holes. <b>Ultrasonic</b> inspection sends high-frequency sound waves through material; reflections from internal flaws or the back wall reveal thickness loss, delaminations, or subsurface defects."},
      {"heading": "Radiographic (X-ray) Inspection", "body": "X-ray/radiographic inspection passes radiation through a part onto film or a digital detector, revealing internal defects, corrosion, or foreign objects by density differences. Requires strict radiation safety controls and is often used for spot welds, composite structures, and complex castings/forgings."}
    ],
    "quiz": [
      {"q": "Dye penetrant inspection is effective for detecting:", "choices": ["Internal voids deep in a part","Surface-breaking cracks on non-porous materials","Magnetic field strength","Fuel contamination"], "answer": 1, "explain": "Dye penetrant reveals cracks that break the surface of a non-porous material by capillary action drawing dye back out."},
      {"q": "Magnetic particle inspection can only be used on:", "choices": ["Any material","Ferromagnetic materials like steel","Composites only","Plastics"], "answer": 1, "explain": "Magnetic particle inspection relies on magnetizing the part, so it only works on ferromagnetic materials."},
      {"q": "Eddy current inspection is especially useful around:", "choices": ["Fastener holes for surface/near-surface flaws","Fuel tank interiors only","Tire pressure checks","Cabin pressurization seals"], "answer": 0, "explain": "Eddy current probes are commonly used to detect cracks around fastener holes and other surface/near-surface flaws."},
      {"q": "Ultrasonic inspection detects flaws by:", "choices": ["Measuring color change","Analyzing reflections of high-frequency sound waves","Applying magnetic particles","Using dye penetrant"], "answer": 1, "explain": "Ultrasonic inspection sends sound waves into the material and interprets reflections to find internal or subsurface flaws."},
      {"q": "Radiographic (X-ray) inspection is often chosen for:", "choices": ["Simple visual checks","Complex castings, spot welds, or composite structures where internal defects must be seen","Measuring cable tension","Checking oil pressure"], "answer": 1, "explain": "X-ray inspection reveals internal defects via density differences and is common for castings, welds, and composites."}
    ]
  },
  {
    "id": "ice_rain_protection", "title": "Ice & Rain Protection Systems", "track": "airframe", "icon": "&#x2744;",
    "sections": [
      {"heading": "Types of Ice Hazards", "body": "<b>Structural icing</b> forms on wings, tail, and other surfaces, disrupting airflow and adding weight/drag. <b>Induction icing</b> forms in the engine air intake or carburetor, restricting airflow or fuel/air mixture. <b>Pitot/static icing</b> blocks airspeed and altitude sensing, a critical instrument hazard."},
      {"heading": "Anti-Ice vs. De-Ice", "body": "<b>Anti-ice</b> systems prevent ice from forming in the first place (e.g., continuously heated pitot probes, bleed-air heated wing leading edges). <b>De-ice</b> systems allow a small amount of ice to form, then remove it periodically (e.g., pneumatic boots that inflate/deflate to crack and shed ice, or electrically heated elements cycled on a timer)."},
      {"heading": "Pneumatic Boot Systems", "body": "Rubber boots on the leading edge inflate with engine bleed air or a pneumatic pump in a specific sequence, cracking accumulated ice which is then carried away by airflow. Boots must be inspected for cracking, deterioration, and proper adhesion; improper inflation sequencing can actually 'ice bridge' if boots are cycled too early on some designs."},
      {"heading": "Windshield & Rain Protection", "body": "Heated windshields prevent ice formation and fogging while providing some bird-strike resistance. Rain removal uses <b>hydrophobic coatings</b>, mechanical <b>wipers</b>, or high-velocity <b>bleed-air/pneumatic rain removal</b> systems that blast rain off the windshield surface at speed."}
    ],
    "quiz": [
      {"q": "Induction icing primarily affects:", "choices": ["Wing leading edges only","Engine air intake/carburetor airflow or fuel-air mixture","Cabin windows","Landing gear doors"], "answer": 1, "explain": "Induction icing forms in the engine's air intake or carburetor, restricting airflow or disrupting the fuel/air mixture."},
      {"q": "What is the key difference between anti-ice and de-ice systems?", "choices": ["No difference","Anti-ice prevents ice formation; de-ice allows some ice then removes it periodically","De-ice is only for engines","Anti-ice is only electrical"], "answer": 1, "explain": "Anti-ice systems run continuously to prevent ice; de-ice systems let a small amount form, then shed it periodically."},
      {"q": "How do pneumatic deicing boots remove ice?", "choices": ["By melting it with heat","By inflating/deflating in sequence to crack and shed accumulated ice","By spraying de-icing fluid","By vibrating at high frequency"], "answer": 1, "explain": "Pneumatic boots cyclically inflate to crack the ice bond, then airflow carries the shed ice away."},
      {"q": "What can happen if pneumatic boots are cycled too early on certain designs?", "choices": ["Nothing, it's always safe","'Ice bridging' where a shell of ice forms over the inflated boot shape","Improved efficiency","Reduced drag"], "answer": 1, "explain": "Cycling too early can create an ice bridge that the boot can no longer break, reducing deicing effectiveness."},
      {"q": "Which hazard specifically threatens airspeed and altitude indications?", "choices": ["Structural icing on the tail","Pitot/static icing","Windshield fogging","Induction icing"], "answer": 1, "explain": "Pitot/static icing blocks the sensing ports needed for accurate airspeed and altitude information."}
    ]
  },
  {
    "id": "recip_overhaul", "title": "Reciprocating Engine Overhaul Practices", "track": "powerplant", "icon": "&#x1F527;",
    "sections": [
      {"heading": "Overhaul Triggers", "body": "Reciprocating engines are typically overhauled at a manufacturer-recommended <b>TBO (Time Between Overhaul)</b> in hours, or sooner if a qualifying event occurs (sudden stoppage, over-temperature, metal in oil, prop strike). TBO is a recommendation for most operators (not mandatory under Part 91) but often mandatory under Part 135/121 operations or per an approved maintenance program."},
      {"heading": "Teardown & Inspection", "body": "Overhaul disassembles the engine completely; parts are cleaned, then inspected using NDI methods (magnetic particle for steel parts, dye penetrant for aluminum) against manufacturer service limits. Parts exceeding wear limits are replaced; crankshafts and camshafts are commonly magnetic-particle inspected for cracks."},
      {"heading": "Reassembly & Break-In", "body": "Reassembly follows the overhaul manual's torque values and sequences exactly. New rings and reconditioned/new cylinders often require a specific <b>break-in procedure</b> (mineral oil, higher power settings initially) to properly seat rings against cylinder walls - improper break-in can cause glazed cylinders and excess oil consumption for the engine's life."},
      {"heading": "Run-In & Documentation", "body": "After reassembly, the engine undergoes a run-in on a test stand or aircraft per the manual, checking oil pressure/temperature, compression, magneto timing, and for leaks. Overhaul generates extensive documentation: yellow tags on parts, logbook entries, and (for a certified/documented overhaul) an FAA Form 8130-3 or equivalent."}
    ],
    "quiz": [
      {"q": "What does TBO stand for?", "choices": ["Total Bearing Output","Time Between Overhaul","Torque Balance Operation","Turbine Bypass Order"], "answer": 1, "explain": "TBO (Time Between Overhaul) is the manufacturer-recommended operating time before overhaul."},
      {"q": "Under Part 91 operations, TBO is generally treated as:", "choices": ["Mandatory in all cases","A recommendation, not mandatory (unless required by an approved program)", "Illegal to exceed", "Only applicable to turbine engines"], "answer": 1, "explain": "For most Part 91 operators, TBO is a manufacturer recommendation rather than a hard regulatory limit."},
      {"q": "Which event would typically require an overhaul sooner than scheduled TBO?", "choices": ["Routine oil change","Sudden stoppage or prop strike","Normal landing","Scheduled inspection"], "answer": 1, "explain": "Sudden stoppage, prop strikes, over-temp events, or metal in the oil are qualifying events that can force an early overhaul."},
      {"q": "Why is a specific break-in procedure needed for new rings/cylinders?", "choices": ['It is optional and rarely followed', 'To properly seat the rings against cylinder walls, preventing glazing and excess oil consumption', 'To test the paint finish', 'To calibrate the propeller'], "answer": 1, "explain": "Proper break-in seats new rings correctly; skipping it can cause glazed cylinder walls and lifelong excess oil consumption."},
      {"q": "What is checked during the post-overhaul run-in?", "choices": ["Only visual paint quality","Oil pressure/temperature, compression, magneto timing, and leaks", "Cabin pressurization", "Passenger seat belts"], "answer": 1, "explain": "The run-in verifies multiple operating parameters and checks for leaks before the engine is returned to service."}
    ]
  },
  {
    "id": "turbine_overhaul", "title": "Turbine Engine Overhaul & Module Repair", "track": "powerplant", "icon": "&#x1F6E9;",
    "sections": [
      {"heading": "Modular Construction", "body": "Modern turbine engines are built in <b>modules</b> (e.g., fan, compressor, combustor, turbine sections) that can be removed and replaced independently. This modular approach allows a single failed module to be repaired or replaced without a full engine teardown, reducing cost and turnaround time."},
      {"heading": "On-Condition & Life-Limited Parts", "body": "Turbine engines are largely maintained <b>on-condition</b> (via borescope inspection, oil analysis, trend monitoring) rather than a fixed overhaul interval, but certain <b>life-limited parts</b> (LLPs) - typically rotating parts like disks and shafts - have hard cyclic or hourly limits regardless of condition, driven by fatigue life analysis."},
      {"heading": "Borescope Inspection", "body": "A <b>borescope</b> is inserted through access ports to visually inspect internal turbine/compressor blades, combustor liners, and other hot-section components without disassembly. Findings (cracks, erosion, foreign object damage, coating loss) are compared against manufacturer serviceable limits to decide on continued operation, repair, or module removal."},
      {"heading": "Hot Section & Repair Considerations", "body": "The <b>hot section</b> (combustor, turbine) experiences the most severe thermal stress and typically drives overhaul/inspection intervals. Repairs may include blade weld/braze repair, recoating (thermal barrier coatings), and balance checks after any rotor work - imbalance in a high-speed turbine rotor can cause severe vibration and premature bearing wear."}
    ],
    "quiz": [
      {"q": "What is the main advantage of modular turbine engine construction?", "choices": ["Lower initial purchase cost only","A failed module can be repaired/replaced without a full engine teardown","It eliminates the need for inspections","It only applies to piston engines"], "answer": 1, "explain": "Modular construction lets technicians address a specific section without disassembling the entire engine."},
      {"q": "What best describes 'on-condition' maintenance for turbine engines?", "choices": ["Replacing parts at a fixed hourly interval regardless of condition","Maintaining based on inspection findings and trend monitoring rather than a fixed overhaul interval","Never inspecting the engine","Only applicable to piston engines"], "answer": 1, "explain": "On-condition maintenance relies on borescope inspection, oil analysis, and trend monitoring rather than a hard TBO."},
      {"q": "Life-limited parts (LLPs) are typically:", "choices": ["Any part on the engine","Rotating parts like disks/shafts with hard cyclic or hourly limits based on fatigue analysis","Only external cowling parts","Never replaced"], "answer": 1, "explain": "LLPs are usually rotating components with strict cyclic/hourly limits driven by fatigue life analysis, regardless of condition."},
      {"q": "What is a borescope used for?", "choices": ["Measuring fuel flow","Visually inspecting internal engine components through access ports without disassembly","Balancing propellers","Testing electrical continuity"], "answer": 1, "explain": "A borescope allows internal visual inspection of blades, liners, and hot-section parts without opening up the engine."},
      {"q": "Why is a balance check important after rotor blade repair work?", "choices": ["It is not important","Imbalance in a high-speed rotor can cause severe vibration and premature bearing wear","It only affects paint appearance","It only matters for piston engines"], "answer": 1, "explain": "Even small imbalance in a high-speed turbine rotor can cause vibration and accelerate bearing wear/failure."}
    ]
  }
]

EXT9_FLASHCARDS = [
  {"front": "Dirty Dozen (human factors)", "back": "Twelve common human factors behind maintenance errors: fatigue, complacency, distraction, etc."},
  {"front": "SHELL model center", "back": "Liveware (the person) interacting with Software, Hardware, and Environment."},
  {"front": "Duplicate inspection purpose", "back": "A second, independent inspector catches errors the original mechanic may miss."},
  {"front": "Dye penetrant inspection use", "back": "Detects surface-breaking cracks on non-porous materials like aluminum and steel."},
  {"front": "Magnetic particle inspection limitation", "back": "Only works on ferromagnetic materials (e.g., steel) - not aluminum or titanium."},
  {"front": "Eddy current inspection strength", "back": "Detects surface/near-surface flaws, especially around fastener holes."},
  {"front": "Ultrasonic inspection principle", "back": "Sound wave reflections reveal internal/subsurface flaws and thickness loss."},
  {"front": "Anti-ice vs de-ice", "back": "Anti-ice prevents ice formation continuously; de-ice allows some ice then sheds it periodically."},
  {"front": "Pneumatic boot ice removal", "back": "Sequenced inflation/deflation cracks and sheds accumulated ice."},
  {"front": "Ice bridging risk", "back": "Cycling deice boots too early can form an ice shell the boot can no longer break."},
  {"front": "TBO definition", "back": "Time Between Overhaul - manufacturer-recommended hours before engine overhaul."},
  {"front": "Break-in procedure purpose", "back": "Properly seats new rings against cylinder walls, preventing glazing and excess oil use."},
  {"front": "Turbine modular construction benefit", "back": "A failed module can be repaired/replaced without full engine teardown."},
  {"front": "On-condition maintenance", "back": "Maintenance driven by inspection/trend data rather than a fixed overhaul interval."},
  {"front": "Life-limited parts (LLPs)", "back": "Rotating parts like disks/shafts with hard cyclic/hourly limits from fatigue analysis."},
  {"front": "Borescope", "back": "Instrument inserted through access ports to visually inspect internals without disassembly."},
]

EXT9_GLOSSARY = [
  {"term": "Dirty Dozen", "def": "Twelve common human factors linked to maintenance errors, e.g., fatigue, complacency, distraction."},
  {"term": "SHELL Model", "def": "A human factors framework: Software, Hardware, Environment, Liveware (people)."},
  {"term": "Fatigue Risk Management", "def": "Practices (rest periods, workload planning, self-reporting) to reduce fatigue-related error risk."},
  {"term": "Dye Penetrant Inspection", "def": "NDI method revealing surface-breaking cracks in non-porous materials using capillary-drawn dye."},
  {"term": "Magnetic Particle Inspection", "def": "NDI method using magnetized parts and iron particles to reveal cracks in ferromagnetic materials."},
  {"term": "Eddy Current Inspection", "def": "NDI method using induced electrical currents to detect surface/near-surface flaws in conductive material."},
  {"term": "Ultrasonic Inspection", "def": "NDI method using high-frequency sound wave reflections to detect internal or subsurface flaws."},
  {"term": "Anti-Ice System", "def": "A system that continuously prevents ice formation on a protected surface."},
  {"term": "De-Ice System", "def": "A system that allows limited ice accumulation, then periodically removes it."},
  {"term": "Ice Bridging", "def": "A failure mode where deicing boots cycled too early allow an unbroken ice shell to form over them."},
  {"term": "TBO (Time Between Overhaul)", "def": "Manufacturer-recommended operating hours before an engine overhaul is due."},
  {"term": "Break-In Procedure", "def": "A controlled initial operating period after overhaul that properly seats new rings/cylinders."},
  {"term": "Modular Engine Construction", "def": "Turbine engine design built from independently removable/replaceable sections (fan, compressor, combustor, turbine)."},
  {"term": "Life-Limited Part (LLP)", "def": "A part with a hard cyclic/hourly retirement limit based on fatigue life analysis, regardless of condition."},
  {"term": "Borescope", "def": "An optical inspection instrument inserted through small access ports to view internal components."},
]

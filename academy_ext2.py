# -*- coding: utf-8 -*-
"""Aviation Maintenance Academy - Content Expansion Pack 2
Adds: 2 extra quiz Qs/module, new flashcards, new glossary terms, 3 new sims, new reference cards.
Merged into the build at build_aviation_academy.py.
"""

EXT2_QUIZ = {
  "orientation": [
    {"q":"Which rating(s) can be combined on one Mechanic Certificate?","choices":["Airframe and Powerplant","Pilot and Airframe","Only one at a time","Inspector and Pilot"],"answer":0,"explain":"A mechanic certificate can carry Airframe (A), Powerplant (P), or both (A&P)."},
    {"q":"Legal maintenance must always be traceable to:","choices":["Personal judgment","Approved data","The nearest hardware store","Verbal instruction only"],"answer":1,"explain":"All maintenance/alterations must be performed using data approved by the FAA (manuals, ADs, TCDS, etc.)."}
  ],
  "math_physics": [
    {"q":"Mechanical advantage is defined as:","choices":["Load / effort","Effort / load","Force x time","Work / power"],"answer":0,"explain":"Mechanical advantage = load / effort - how much a machine multiplies your input force."},
    {"q":"Why must absolute temperature be used in gas law calculations?","choices":["It's tradition","Gas laws are ratios that break down at 0 on relative scales","Absolute temp is easier to measure","It isn't required"],"answer":1,"explain":"Kelvin/Rankine start at true zero, so the proportional relationships in Boyle's/Charles's Laws hold correctly."}
  ],
  "materials_hardware": [
    {"q":"Which alloy is prized for firewalls and fasteners needing steel-like strength at lower weight?","choices":["6061-T6","Titanium","Magnesium","1100 aluminum"],"answer":1,"explain":"Titanium offers near-steel strength at about 60% of the weight - ideal for firewalls and high-strength fasteners."},
    {"q":"A tap test on a composite structure that sounds dull/dead most likely indicates:","choices":["Normal structure","A disbond/delamination","Correct cure","Proper torque"],"answer":1,"explain":"A dull/dead tap tone versus a sharp, consistent tone across a composite panel signals a disbond or delamination beneath the surface."}
  ],
  "electricity": [
    {"q":"In a purely resistive AC circuit, voltage and current are:","choices":["90 degrees out of phase","In phase","180 degrees out of phase","Unrelated"],"answer":1,"explain":"With pure resistance, voltage and current rise and fall together - no phase shift, unlike inductive/capacitive loads."},
    {"q":"A lead-acid battery's state of charge is commonly checked with a:","choices":["Ohmmeter only","Hydrometer (specific gravity) or load test","Compression tester","Tachometer"],"answer":1,"explain":"Specific gravity (hydrometer) or a load test reveals actual battery condition better than voltage alone."}
  ],
  "inspection_ndt": [
    {"q":"Dye penetrant inspection is limited to detecting flaws that are:","choices":["Anywhere inside the part","Open to the surface","Only in ferrous metals","Only under paint"],"answer":1,"explain":"Penetrant only reveals discontinuities open to the surface - it cannot find subsurface or internal defects."},
    {"q":"Eddy current inspection requires the material to be:","choices":["Ferromagnetic","Electrically conductive","Transparent","Painted"],"answer":1,"explain":"Eddy current works on any electrically conductive material (not just ferrous), unlike magnetic particle."}
  ],
  "structures": [
    {"q":"In a semi-monocoque fuselage, primary bending loads are carried mainly by:","choices":["The skin alone","Longerons/stringers with the skin","Passenger seats","Paint finish"],"answer":1,"explain":"Semi-monocoque construction shares loads between skin and internal stiffeners (longerons/stringers/frames), unlike pure monocoque where skin alone carries the load."},
    {"q":"Flight control rigging is checked against manufacturer data using:","choices":["Guesswork","Rigging pins/fixtures and travel-board/protractor measurements","Only visual inspection","Weight and balance sheet"],"answer":1,"explain":"Proper rigging uses specified fixtures/pins and measured control-surface travel limits per the maintenance manual."}
  ],
  "sheet_metal": [
    {"q":"Edge distance for a rivet (center of hole to edge of sheet) is typically at least:","choices":["1x rivet diameter","2x rivet diameter","5x rivet diameter","10x rivet diameter"],"answer":1,"explain":"Standard minimum edge distance is 2x the rivet shank diameter to avoid the sheet cracking/splitting."},
    {"q":"A rivet that is over-driven (head too flat/thin) can cause:","choices":["Improved strength","Cracking of the rivet head","Better corrosion resistance","No effect"],"answer":1,"explain":"Overdriving thins and can crack the rivet head, weakening the joint - shop head diameter/height must stay in spec."}
  ],
  "airframe_systems": [
    {"q":"A hydraulic system relief valve's purpose is to:","choices":["Increase system pressure","Limit maximum system pressure","Filter contamination","Cool the fluid"],"answer":1,"explain":"Relief valves protect the system by dumping fluid back to the reservoir once a maximum pressure is reached."},
    {"q":"Cabin pressurization outflow valves primarily control:","choices":["Cabin temperature","Cabin altitude (pressure differential)","Fuel flow","Hydraulic pressure"],"answer":1,"explain":"Outflow valves regulate how much air leaves the cabin, setting the pressure differential and effective cabin altitude."}
  ],
  "recip_engines": [
    {"q":"In the 4-stroke cycle, the power stroke occurs during which stroke?","choices":["Intake","Compression","Power (expansion)","Exhaust"],"answer":2,"explain":"After compression and ignition, the power (expansion) stroke drives the piston down, producing usable work."},
    {"q":"Firing order matters mainly to ensure:","choices":["Even fuel color","Balanced power delivery and reduced vibration","Lower oil pressure","Higher compression ratio"],"answer":1,"explain":"Correct firing order spreads power pulses evenly around the crankshaft, smoothing power delivery and reducing vibration/stress."}
  ],
  "turbine_engines": [
    {"q":"In the Brayton cycle, compression, combustion, and expansion happen:","choices":["In four separate strokes","Continuously and simultaneously in different sections","Only at idle","Only during start"],"answer":1,"explain":"Unlike the reciprocating Otto cycle, turbine engines run all phases continuously and simultaneously in different sections of the engine."},
    {"q":"EGT/ITT limits exist mainly to protect:","choices":["The fuel pump","Turbine blades/hot section from thermal damage","The propeller","The landing gear"],"answer":1,"explain":"Exceeding exhaust/turbine inlet temperature limits accelerates hot-section fatigue and can cause blade damage or failure."}
  ],
  "propellers": [
    {"q":"A constant-speed propeller maintains a set RPM primarily by changing:","choices":["Engine timing","Blade pitch angle","Fuel mixture","Manifold pressure directly"],"answer":1,"explain":"The governor adjusts blade pitch (angle of attack) to hold selected RPM as power/airspeed change."},
    {"q":"Propeller track and balance checks are performed to detect:","choices":["Fuel contamination","Blade tip path misalignment / vibration sources","Ignition timing errors","Battery voltage drop"],"answer":1,"explain":"Track (tip path alignment) and balance checks catch conditions that cause vibration and accelerate component wear."}
  ],
  "regulations_records": [
    {"q":"A Form 337 is used to document:","choices":["A routine oil change","A major repair or major alteration","Daily flight hours","Fuel receipts"],"answer":1,"explain":"FAA Form 337 documents major repairs and major alterations, becoming a permanent aircraft record."},
    {"q":"An Airworthiness Directive (AD) is:","choices":["An optional service bulletin","A mandatory FAA-issued correction for an unsafe condition","A manufacturer's warranty claim","A logbook entry style guide"],"answer":1,"explain":"ADs are legally mandatory corrective actions issued by the FAA when an unsafe condition exists in a product."}
  ],
  "ground_ops": [
    {"q":"When towing, the nosewheel steering bypass pin is used to:","choices":["Lock the steering for takeoff","Disconnect steering linkage so towing doesn't damage it","Increase steering angle","Engage the parking brake"],"answer":1,"explain":"The bypass pin decouples the steering system so external towing forces don't damage the linkage/stops."},
    {"q":"Type IV deicing fluid differs from Type I mainly because it:","choices":["Is only for washing","Is unheated anti-icing fluid providing holdover protection","Is used only in summer","Removes paint"],"answer":1,"explain":"Type IV is a thickened, unheated anti-icing fluid designed to cling to surfaces and provide longer holdover time against re-freezing."}
  ],
  "weight_balance": [
    {"q":"After a major repair or alteration affecting weight, the mechanic should typically:","choices":["Ignore it if under 5 lb","Update or reweigh and update the W&B record","Wait for next annual","Estimate visually"],"answer":1,"explain":"Any change affecting weight/CG must be reflected in the aircraft's weight and balance record, often requiring a reweigh."},
    {"q":"If a computed CG falls just aft of the aft limit, the immediate concern is:","choices":["Extra fuel burn","Reduced/negative longitudinal stability and control","Improved climb rate","Nothing significant"],"answer":1,"explain":"An aft-of-limit CG reduces stability and can make the aircraft difficult or impossible to control safely."}
  ],
  "corrosion": [
    {"q":"Galvanic corrosion is most likely when you have:","choices":["Two identical metals in dry air","Dissimilar metals in contact with an electrolyte","Any painted surface","A vacuum environment"],"answer":1,"explain":"Galvanic corrosion needs dissimilar metals (different in the galvanic series) plus an electrolyte to complete the circuit."},
    {"q":"Filiform corrosion typically appears as:","choices":["Deep pits","Thread-like trails under a coating","Even surface pitting","Blue-green stains only"],"answer":1,"explain":"Filiform corrosion forms characteristic thread-like filaments that travel under a paint/coating film."}
  ],
  "human_factors": [
    {"q":"A 'safety net' in maintenance human factors refers to:","choices":["A literal net under the aircraft","Independent checks like buy-back inspections that catch errors before they matter","A type of PPE","An insurance policy"],"answer":1,"explain":"Safety nets are process barriers (independent inspection, checklists, buy-back) designed to catch an error before it becomes a failure."},
    {"q":"Which best describes an 'error chain'?","choices":["A single random mistake","A series of small contributing factors that combine into an incident","A tool storage system","A type of torque wrench"],"answer":1,"explain":"Most maintenance incidents result from a chain of smaller contributing errors/conditions, not one isolated mistake."}
  ],
  "fluid_power": [
    {"q":"Why must Skydrol never be mixed with mineral-based hydraulic fluid?","choices":["Color mismatch only","They are chemically incompatible and destroy seals/contaminate the system","Skydrol is cheaper","No real reason, it's just convention"],"answer":1,"explain":"Skydrol (phosphate ester) and mineral-based fluids (MIL-H-5606/83282) are chemically incompatible; mixing damages seals and system integrity."},
    {"q":"A hydraulic accumulator's main job is to:","choices":["Filter fluid only","Store pressure/dampen surges and pump pulsations","Cool the fluid","Generate flow"],"answer":1,"explain":"Accumulators store pressurized fluid (gas-precharged) to smooth pump pulsations and provide emergency backup pressure."}
  ],
  "landing_gear": [
    {"q":"An oleo strut absorbs landing shock primarily using:","choices":["A solid rubber block","Compressed air/nitrogen and metered oil flow","Springs only","Friction pads"],"answer":1,"explain":"Oleo struts combine a gas spring (air/nitrogen) with metered hydraulic fluid flow through an orifice to absorb and dissipate landing energy."},
    {"q":"Anti-skid systems function by:","choices":["Locking the brakes fully","Modulating brake pressure to prevent wheel lockup","Disabling brakes below 10 knots only","Increasing tire pressure"],"answer":1,"explain":"Anti-skid modulates brake application in response to wheel speed sensors to prevent skidding/lockup and maximize braking effectiveness."}
  ],
  "avionics": [
    {"q":"A blocked static port would most directly affect:","choices":["Only the ADF","Airspeed, altimeter, and VSI readings","Radio reception","Fuel quantity gauge"],"answer":1,"explain":"Static pressure feeds the airspeed indicator, altimeter, and VSI - a blockage causes erroneous readings on all of them."},
    {"q":"Bonding/shielding of avionics wiring is primarily intended to:","choices":["Add weight for balance","Reduce electromagnetic interference and static buildup","Improve paint adhesion","Increase resistance intentionally"],"answer":1,"explain":"Proper bonding and shielded/twisted wiring reduce EMI coupling into sensitive avionics signals and bleed off static charge."}
  ],
  "fuel_systems": [
    {"q":"The main advantage of fuel injection over a float carburetor is:","choices":["Lower cost","Reduced susceptibility to carburetor icing and more even fuel distribution","Simpler design","No need for a mixture control"],"answer":1,"explain":"Fuel injection meters fuel directly into the intake/cylinders, avoiding the venturi icing risk of float carburetors and often improving distribution."},
    {"q":"Water contamination in fuel is checked for primarily by:","choices":["Smell test only","Sump draining and visual/chemical water-detection check","Running the engine longer","Ignoring it, fuel self-purifies"],"answer":1,"explain":"Sump drains let you visually and chemically check for water (which is denser and settles at low points) before flight."}
  ]
}

EXT2_FLASHCARDS = [
  {"front":"Mechanical Advantage","back":"Load / Effort - how much a machine multiplies input force"},
  {"front":"Absolute Temperature","back":"Temperature scale starting at true zero (Kelvin/Rankine) - required for gas law math"},
  {"front":"Titanium (aviation use)","back":"Near-steel strength at ~60% weight; used for firewalls and high-strength fasteners"},
  {"front":"Tap Test","back":"Listening for dull/dead sound vs sharp tone to find composite disbonds/delaminations"},
  {"front":"AC Resistive Circuit Phase","back":"Voltage and current are in phase (no shift) with pure resistance"},
  {"front":"Hydrometer","back":"Measures specific gravity of battery electrolyte to check state of charge"},
  {"front":"Penetrant Inspection Limit","back":"Only detects flaws open to the surface - can't find subsurface defects"},
  {"front":"Eddy Current Requirement","back":"Material must be electrically conductive (not necessarily ferrous)"},
  {"front":"Semi-Monocoque","back":"Fuselage design sharing bending loads between skin and internal stiffeners (longerons/stringers)"},
  {"front":"Rivet Edge Distance","back":"Minimum ~2x rivet shank diameter from hole center to sheet edge"},
  {"front":"Over-Driven Rivet","back":"Head too flat/thin - risks cracking and joint weakness"},
  {"front":"Hydraulic Relief Valve","back":"Limits maximum system pressure by dumping fluid back to reservoir"},
  {"front":"Cabin Outflow Valve","back":"Controls how much air leaves the cabin, setting pressure differential/cabin altitude"},
  {"front":"4-Stroke Power Stroke","back":"The expansion stroke after ignition that drives the piston down and produces work"},
  {"front":"Firing Order Purpose","back":"Spreads power pulses evenly around the crankshaft for smooth, balanced power delivery"},
  {"front":"Brayton Cycle","back":"Continuous simultaneous compression/combustion/expansion in different turbine engine sections"},
  {"front":"EGT/ITT Limit Purpose","back":"Protects turbine blades/hot section from thermal damage/fatigue"},
  {"front":"Constant-Speed Propeller","back":"Governor changes blade pitch angle to hold selected RPM as conditions change"},
  {"front":"Propeller Track","back":"Check of blade tip path alignment - misalignment causes vibration"},
  {"front":"Form 337","back":"FAA form documenting a major repair or major alteration"},
  {"front":"Airworthiness Directive (AD)","back":"Mandatory FAA-issued correction for an unsafe condition"},
  {"front":"Nosewheel Bypass Pin","back":"Decouples steering linkage during towing to prevent damage"},
  {"front":"Type IV Deicing Fluid","back":"Thickened, unheated anti-icing fluid providing longer holdover time"},
  {"front":"Aft CG Risk","back":"Reduced/negative longitudinal stability and difficult control"},
  {"front":"Skydrol Mixing","back":"Never mix with mineral hydraulic fluid - chemically incompatible, destroys seals"},
  {"front":"Oleo Strut Action","back":"Combines gas spring (air/nitrogen) with metered oil flow through an orifice to absorb shock"},
  {"front":"Anti-Skid System","back":"Modulates brake pressure using wheel-speed sensors to prevent lockup"},
  {"front":"Blocked Static Port Effect","back":"Erroneous airspeed, altimeter, and VSI readings (all three share the static source)"},
  {"front":"Fuel Injection Advantage","back":"Avoids carburetor icing risk and improves fuel distribution vs float carburetor"},
  {"front":"Fuel Sump Check","back":"Visual/chemical check for water, which settles at low points since it's denser than fuel"}
]

EXT2_GLOSSARY = [
  {"term":"Bypass Pin","def":"Pin that disconnects nosewheel steering linkage for towing"},
  {"term":"Constant-Speed Prop","def":"Propeller whose governor varies blade pitch to hold set RPM"},
  {"term":"Delamination","def":"Separation between layers in a composite laminate"},
  {"term":"Disbond","def":"Loss of adhesive bond between composite/honeycomb layers"},
  {"term":"Electrolyte","def":"Conductive fluid enabling galvanic/battery chemical reactions"},
  {"term":"Error Chain","def":"Series of small contributing factors combining into an incident"},
  {"term":"Firing Order","def":"Sequence in which engine cylinders fire to balance power delivery"},
  {"term":"Governor (prop)","def":"Device that adjusts propeller blade pitch to maintain selected RPM"},
  {"term":"Hot Section","def":"Combustor, turbine, and exhaust area of a gas turbine engine"},
  {"term":"Hung Start","def":"Turbine engine lights off but fails to reach idle RPM"},
  {"term":"Outflow Valve","def":"Cabin valve controlling air exit rate to set pressurization"},
  {"term":"Relief Valve","def":"Hydraulic/pneumatic valve limiting maximum system pressure"},
  {"term":"Safety Net (human factors)","def":"Independent process check (e.g., buy-back inspection) that catches errors"},
  {"term":"Setback (sheet metal)","def":"Distance from bend tangent line to the mold line, used in flat layout"},
  {"term":"Specific Gravity","def":"Ratio used to gauge battery electrolyte state of charge via hydrometer"},
  {"term":"Track (propeller)","def":"Alignment of blade tip paths - mismatch causes vibration"},
  {"term":"Type IV Fluid","def":"Thickened, unheated anti-icing fluid providing extended holdover time"}
]

EXT2_SIMS = [
  {"id":"torque",   "title":"Torque Wrench Extension", "icon":"&#x1F529;", "cat":"General",    "desc":"Compute the dial/gauge reading when using an extension/adapter on a torque wrench."},
  {"id":"densalt",  "title":"Density Altitude",         "icon":"&#x1F321;", "cat":"General",    "desc":"Estimate density altitude from field elevation, altimeter setting, and OAT."},
  {"id":"vdrop",    "title":"Wire Size & Voltage Drop",  "icon":"&#x1F50C;", "cat":"Electrical", "desc":"Check voltage drop for a wire run and whether the gauge is adequate."}
]

EXT2_REFERENCE = [
  {"cat":"Formulas","title":"Torque Wrench w/ Extension","body":"TW = TE x (L / (L + A)). TW=wrench setting, TE=target (true) torque, L=wrench handle length, A=extension length beyond the wrench's drive. Always measure L from the wrench's pivot/square drive to the handle grip center."},
  {"cat":"Formulas","title":"Density Altitude (rule of thumb)","body":"Pressure Altitude = Field Elevation + [(29.92 - Altimeter Setting) x 1000]. Density Altitude &asymp; Pressure Altitude + [120 x (OAT - ISA Temp at that altitude)]. High density altitude = reduced engine/prop performance."},
  {"cat":"Formulas","title":"Voltage Drop","body":"Vdrop = I x R(wire). Max recommended drop is typically 2% (avionics/critical) to 5-10% (general) of source voltage over the full circuit length (there and back). Check wire tables (AWG vs length vs current) in AC 43.13-1B Ch.11."},
  {"cat":"Hardware","title":"Standard Torque Striping","body":"Torque-seal / paint stripe across a fastener and adjacent structure after final torque - a broken or misaligned stripe on later inspection flags a fastener that has loosened or been disturbed."},
  {"cat":"Regs","title":"Logbook Entry Example (43.9)","body":"\"Removed L/H main gear tire P/N 123-456, installed new S/N 789 IAW AMM 32-45-11. Ops check normal. No defects noted.\" &mdash; Date, Total Time, and mechanic's Name/Cert#/Type + signature must follow."},
  {"cat":"Regs","title":"AD Compliance Record Example","body":"\"Complied with AD 2024-12-08 para (f)(1) by visual inspection of wing spar IAW AD instructions. No cracking found. Next due: 500 hrs or 12 months, whichever occurs first.\" Must reference the AD number, method of compliance, and recurring interval if any."},
  {"cat":"Electrical","title":"Common Wire Gauges (AWG)","body":"22 AWG: ~7A. 20 AWG: ~11A. 18 AWG: ~16A. 16 AWG: ~22A. 14 AWG: ~32A. 12 AWG: ~41A (continuous, free air, exact rating varies by insulation/bundle/altitude - always confirm in AC 43.13-1B wire tables)."},
  {"cat":"Powerplant","title":"Density Altitude Effects","body":"High density altitude (hot, high elevation, low pressure) reduces air density &rarr; less power, less prop efficiency, longer takeoff roll, reduced climb. Always check performance charts, not just gut feel, on hot/high days."}
]

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
      {"heading": "Career Pathways", "body": "A&P mechanics work across very different environments: <b>general aviation (GA) shops</b> (varied, hands-on, small aircraft), <b>Part 121 airlines</b> (structured, high-volume, specialized line/heavy maintenance), <b>Part 135 charter/cargo</b>, corporate/business aviation, and <b>repair stations</b> (Part 145) doing component overhaul. Many mechanics later pursue an <b>Inspection Authorization (IA)</b>, move into avionics specialization, or transition into quality, training, or management roles."}, {"heading": "Understanding the FAA Knowledge and Practical Tests", "body": "The path to A&P certification culminates in FAA knowledge tests (written), an oral examination, and a practical test covering general, airframe, and powerplant areas, each administered separately and requiring passing scores before certification is issued. The Airman Certification Standards (ACS) or Practical Test Standards define exactly what knowledge and skills are tested, so structuring study time around the ACS task lists rather than general reading ensures efficient exam preparation. Many successful candidates keep a running log of practice questions missed and revisit those specific ACS areas repeatedly until mastery, rather than simply re-reading entire chapters."}, {"heading": "Mechanic Privileges and Limitations Under Part 65", "body": "An A&P certificate grants specific privileges but also carries limitations defined in 14 CFR Part 65. Certificated mechanics may approve for return to service work they performed or supervised, but cannot approve major repairs or alterations without appropriate Inspection Authorization (IA) or unless the work is covered by an approved data package. Mechanics must exercise their privileges only within the scope of their rating (airframe, powerplant, or both) and may not perform or supervise duties they are not qualified for. Recency of experience requirements mean a mechanic who has not performed maintenance functions for 24 months must demonstrate current knowledge to their employer before exercising certificate privileges again. Understanding these boundaries early in training helps students see how the certificate they are working toward defines their professional responsibilities."}, {"heading": "Building Effective Study Habits for A&P Coursework", "body": "Success in A&P training depends heavily on developing consistent study habits early, since the volume of technical material across airframe and powerplant curricula can overwhelm students who rely solely on classroom time without structured review outside class. Spaced repetition, reviewing material at increasing intervals rather than cramming immediately before a test, has been shown to significantly improve long-term retention of technical facts like torque values, regulatory references, and system operating principles that must be recalled accurately during practical and oral examinations. Active recall techniques, such as attempting to explain a system's operation aloud or working through practice questions without looking at notes first, build stronger retention than passive re-reading of textbook material. Forming or joining a study group with fellow students provides opportunities to explain concepts to peers, which reinforces the explainer's own understanding while also exposing gaps in comprehension that solo study might not reveal, and many successful mechanics credit this collaborative approach as significant in helping them pass both the written and oral/practical portions of their certification tests."},
    {"heading": "Time Management and Balancing Coursework with Hands-On Practice", "body": "Successful A&P students balance three demands: classroom/theory study, hands-on shop practice, and the documentation/logging of practical experience required for FAA testing eligibility, and neglecting any one of the three creates a gap that becomes harder to close later in the program. A common pitfall is focusing heavily on passing written knowledge tests while under-practicing hands-on skills, resulting in a student who can pass the oral and written exams but struggles during the practical (skills) test where actual task performance under an examiner's observation is required. Effective students maintain a simple study log tracking which subject areas and practical tasks they have covered, revisit weaker areas rather than only repeating tasks they already do well, and treat every shop lab session as an opportunity to practice the professional habits (tool control, cleanliness, documentation discipline) that will matter throughout their career, not just as a box to check off the syllabus."},
    {"heading": "Navigating FAA Advisory Circulars and Guidance Material", "body": "Advisory Circulars published by the FAA provide guidance material that explains acceptable methods, techniques, and practices for complying with the regulations found in Title 14 of the Code of Federal Regulations, and understanding how to locate and interpret relevant Advisory Circulars is a core professional skill for a maintenance technician. Advisory Circulars are numbered to correspond to the regulatory part they support, such as those addressing airworthiness standards, maintenance practices, or specific systems, and a technician researching an unfamiliar maintenance question should first identify the applicable regulatory part, then search for Advisory Circulars numbered under that part for detailed guidance. It is important to understand that Advisory Circulars are generally not themselves regulatory requirements; they describe one acceptable means of compliance, and a technician may use an alternative method if it also satisfies the underlying regulation and is acceptable to the FAA, though in practice many operators and repair stations adopt Advisory Circular guidance directly into their procedures for consistency and ease of demonstrating compliance. Advisory Circulars are revised periodically, and using an outdated version can lead to following superseded guidance, so technicians should always verify they are referencing the current version through the FAA's official publication system rather than a saved older copy. Some Advisory Circulars carry more mandatory weight in practice, such as those referenced directly within an operator's FAA-approved maintenance program or those tied to Airworthiness Directive compliance methods, and in those specific applications the flexibility to choose alternative means may not exist."}],
    "quiz": [ {"q": "Why is active recall (attempting to explain a concept without looking at notes) generally more effective for retention than passive re-reading?", "choices": ["Active recall is faster but always less effective", "Active recall builds stronger retention by forcing genuine retrieval of information, revealing gaps that passive re-reading would not expose", "There is no meaningful difference between the two study methods", "Passive re-reading is always superior for technical material"], "answer": 1}, {"q": "Under 14 CFR Part 65, if a mechanic has not exercised the privileges of their certificate for 24 months, what must happen before they can approve work for return to service again?", "choices": ["They must retake the FAA written exam", "They must demonstrate to the satisfaction of the Administrator or employer that they are current and competent", "Their certificate is automatically revoked", "They must complete a new oral and practical test"], "answer": 1}, {"q": "What document defines exactly what knowledge and skills are tested on FAA A&P exams?", "choices": ["Any textbook of choice", "The Airman Certification Standards (ACS) or Practical Test Standards", "A random practice test website", "The aircraft flight manual"], "answer": 1, "explain": "The ACS/PTS define the specific task lists and standards examiners use, making them the most efficient guide for structuring exam preparation."},
      {"q": "What do A and P stand for?", "choices": ["Airframe & Powerplant","Aviation & Propulsion","Assembly & Parts","Aerospace & Performance"], "answer": 0, "explain": "A&P = Airframe and Powerplant ratings on an FAA Mechanic Certificate."},
      {"q": "Which AC is the shop bible for repair methods?", "choices": ["AC 91-67","AC 43.13-1B","AC 20-62","AC 65-12"], "answer": 1, "explain": "AC 43.13-1B covers acceptable methods, techniques, and practices."},
      {"q": "What does FOD stand for?", "choices": ["Flight Ops Directive","Foreign Object Damage/Debris","Fuel-Oil Distribution","Federal Ops Document"], "answer": 1, "explain": "FOD = Foreign Object Damage/Debris. Loose items in an engine can be catastrophic."},
      {"q": "How many A&P knowledge domains?", "choices": ["2","3","4","5"], "answer": 1, "explain": "Three: General, Airframe, Powerplant."},
      {"q": "Which of these best describes a Part 145 repair station?", "choices": ["An airline flight department", "A certificated organization authorized to perform maintenance/overhaul under FAA oversight", "A flight training school", "An aircraft manufacturer only"], "answer": 1, "explain": "A Part 145 repair station is an FAA-certificated organization authorized to perform specific maintenance, repair, or overhaul work."},
      {"q": "Which is NOT a Dirty Dozen item?", "choices": ["Fatigue","Complacency","Enthusiasm","Distraction"], "answer": 2, "explain": "Enthusiasm is not one of the 12 human-factors error precursors."},
    {"q": "Why is it a common pitfall for A&P students to focus heavily on written knowledge tests while under-practicing hands-on skills?", "choices": ["Written knowledge tests are the only component that matters for certification", "It can result in a student who passes written and oral exams but struggles during the hands-on practical test", "Hands-on practice has no bearing on any FAA testing requirement", "The FAA does not require any hands-on skills demonstration"], "answer": 1},
    {"q": "What is the general relationship between FAA Advisory Circulars and the regulations they support?", "choices": ["Advisory Circulars describe an acceptable means of compliance with regulations but are generally not regulatory requirements themselves", "Advisory Circulars replace the need to follow the Code of Federal Regulations entirely", "Advisory Circulars are always legally mandatory regardless of context", "Advisory Circulars are only published for engine-related regulations"], "answer": 0}
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
      {"heading": "Applying the Formulas", "body": "A wrench with a 10-inch handle applying 20 lb of force produces a torque of <b>200 in-lb</b> (Torque = Force x distance) - the same principle behind a torque wrench's specification. Mechanical advantage from a pulley or lever lets a smaller force move a larger load over a longer distance, but total work stays the same (ignoring friction) - this is why calculating the right tool or technique for a job matters as much as brute force."}, {"heading": "Applying Trigonometry to Rigging and Structural Angles", "body": "Trigonometric relationships are directly applicable to aircraft maintenance tasks such as calculating cable rigging tension changes across different sling or turnbuckle angles, determining control surface deflection angles from linear actuator travel, and computing structural load components when a force is applied at an angle to a structural member rather than directly along its axis. Understanding that a force applied at an angle has both a component along the member's axis and a component perpendicular to it (found using sine and cosine of the angle) explains why rigging angle changes can significantly affect the actual load experienced by cables, struts, and fittings even when the total applied force remains constant. Mechanics who can apply basic right-triangle trigonometry to these practical scenarios can better understand why manufacturer rigging specifications call out precise angles rather than treating angle as a minor detail."}, {"heading": "Unit Conversion Discipline in Maintenance Calculations", "body": "Aviation maintenance frequently requires converting between measurement systems, such as inches to millimeters, pounds to kilograms, or PSI to kilopascals, and errors in unit conversion are a persistent source of maintenance mistakes that can have serious safety consequences, from over-torquing a fastener to miscalculating weight and balance. Mechanics must develop the discipline of explicitly writing out units at every step of a calculation, not just the final answer, since carrying units through intermediate steps helps catch errors like accidentally multiplying by a conversion factor instead of dividing, or using an outdated or incorrect conversion constant. When a maintenance manual specifies a value in one unit system but available tools or gauges display a different unit system, mechanics must perform the conversion carefully and, where possible, double-check the result using a second method or reference table rather than relying on a single mental calculation. Dimensional analysis, tracking units through a multi-step calculation to confirm the final result has the expected unit, provides a powerful self-check that can catch many calculation errors before they result in an incorrect maintenance action."},
    {"heading": "Torque, Moment Arm, and Rotational Force Calculations", "body": "Torque is the rotational equivalent of force, calculated as force multiplied by the perpendicular distance from the pivot point to the line of force application (the moment arm), and understanding this relationship is essential for correctly using torque wrenches, calculating bolt preload, and analyzing control surface balance and rigging geometry. A torque wrench with an extension or adapter that changes the effective length from the wrench's pivot to the fastener changes the actual torque applied at the fastener for a given wrench reading, requiring a compensating calculation so the fastener receives the specified torque rather than the wrench's dial reading; using an extension without adjusting for this effect is a common source of over- or under-torqued fasteners. Balance and moment calculations for components such as control surfaces or propeller blades similarly rely on multiplying weight by distance from a reference point (the balance axis or hinge line), and technicians must keep units consistent (inch-pounds versus foot-pounds, for example) throughout a calculation to avoid an error of a factor of twelve."},
    {"heading": "Center of Pressure and Its Relationship to Structural and Control Loads", "body": "The center of pressure on an airfoil or control surface is the point at which the resultant aerodynamic force can be considered to act, and unlike the center of gravity, its location shifts with changes in angle of attack, airspeed, and flap or control surface deflection, making it a dynamic rather than fixed point during flight. Understanding center of pressure movement is essential for interpreting why control surface loads and hinge moments vary so significantly across the flight envelope, since the distance between the center of pressure and the hinge line determines the moment the control system, cables, pushrods, or actuators must resist or overcome. On a typical cambered airfoil, the center of pressure moves forward as angle of attack increases and aft as angle of attack decreases, a behavior that influences aircraft pitch stability characteristics and is a key consideration in the design of the tail surfaces that provide longitudinal stability. For structural analysis, engineers must consider the full range of center of pressure locations across all anticipated flight conditions, not just a single design case, since a structure adequate for one loading condition may be under-designed for another where the center of pressure has shifted to a more demanding position. Technicians benefit from this concept primarily when evaluating why certain control surface repairs or modifications require engineering approval, since altering a surface's shape, mass distribution, or hinge location can change center of pressure behavior in ways that affect flutter margins and control forces throughout the flight envelope."}],
    "quiz": [ {"q": "Why should mechanics explicitly write out units at every step of a conversion calculation, not just the final answer?", "choices": ["Writing units is purely a formatting preference with no practical benefit", "Carrying units through each step helps catch errors like using an incorrect conversion factor or performing the wrong operation", "Units only matter for the final answer, not intermediate steps", "Unit tracking has no relationship to calculation accuracy"], "answer": 1}, {"q": "Why does the angle at which a force is applied to a structural member matter for the load it experiences?", "choices": ["Angle has no effect on load distribution", "The force splits into axial and perpendicular components based on the angle, using sine and cosine relationships", "Only the total force magnitude matters, never the angle", "Angles only matter for electrical calculations"], "answer": 1, "explain": "A force applied at an angle to a structural member splits into a component along the member's axis and a component perpendicular to it, determined by the angle's sine and cosine, which is why rigging angles matter for actual load experienced."},
      {"q": "Cylinder displacement formula:", "choices": ["(pi/4) x bore^2 x stroke x #cyl","pi x bore x stroke","bore^2 x stroke / 4","pi/2 x bore x stroke"], "answer": 0, "explain": "Displacement = (pi/4) x bore^2 x stroke x number of cylinders."},
      {"q": "In Boyle's Law, what is constant?", "choices": ["Pressure","Volume","Temperature","Mass"], "answer": 2, "explain": "Boyle's Law: P1V1=P2V2 when temperature is constant."},
      {"q": "Pascal's Law is the basis for:", "choices": ["Electrical systems","Hydraulic systems","Ignition","Induction"], "answer": 1, "explain": "Pascal's Law - pressure transmits equally in confined fluid - is the principle behind hydraulics."},
      {"q": "Work equals:", "choices": ["Force x time","Force x distance","Power x distance","Mass x velocity"], "answer": 1, "explain": "Work = Force x distance (W=Fd)."},
      {"q": "A wrench with a 10-inch handle applies 20 lb of force to a bolt. The torque produced is:", "choices": ["2 in-lb","20 in-lb","200 in-lb","2000 in-lb"], "answer": 2, "explain": "Torque = Force x distance = 20 lb x 10 in = 200 in-lb."},
      {"q": "Bernoulli explains:", "choices": ["Hydraulic multiplication","How lift is generated","Thermal expansion","Ohm's Law"], "answer": 1, "explain": "Faster flow = lower pressure explains how wings generate lift."},
    {"q": "Why must a technician adjust the torque wrench setting when using an extension that changes the effective length from the wrench's pivot to the fastener?", "choices": ["Extensions never affect the actual torque delivered to the fastener", "An extension changes the effective moment arm, so the actual torque at the fastener differs from the wrench's dial reading unless compensated for", "Torque wrenches automatically compensate for any extension used", "Extensions can only be used with digital torque wrenches, never adjustable click-type wrenches"], "answer": 1},
    {"q": "How does the center of pressure differ from the center of gravity on an airfoil?", "choices": ["The center of pressure shifts with angle of attack, airspeed, and control deflection, while the center of gravity is a fixed mass property", "The center of pressure and center of gravity are always located at the identical point", "The center of gravity moves with airspeed while the center of pressure remains fixed", "There is no meaningful difference between the two concepts"], "answer": 0}
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
    , {"heading": "Sealants and Adhesive Bonding", "body": "Aircraft assembly increasingly relies on structural adhesives and sealants alongside mechanical fasteners, including epoxy film adhesives for composite bonding, polysulfide sealants for fuel tank and pressurized area sealing, and pressure-sensitive tapes for temporary or non-structural applications. Proper surface preparation, including cleaning and sometimes chemical etching or abrasion, is critical since adhesive bond strength depends heavily on substrate condition. Shelf life and pot life of two-part adhesives must be tracked, and cure schedules (time, temperature, pressure) must be followed precisely per the material specification sheet."}, {"heading": "Fastener Torque and Preload Fundamentals", "body": "Proper fastener torque establishes the correct clamping force (preload) between joined parts, and both under-torquing and over-torquing create problems: under-torqued fasteners can loosen under vibration or allow joint movement leading to fatigue failure, while over-torqued fasteners can yield the fastener material, strip threads, or crush gaskets and seals beyond their design compression range. Torque values specified in maintenance data account for the specific fastener material, thread condition (dry vs. lubricated), and the mating material, so substituting a different lubricant or applying torque values intended for a different fastener material can result in incorrect actual clamping force despite hitting the specified torque wrench reading. Torque-to-yield fasteners used in some high-load applications are specifically designed to be tightened to a point near their yield strength and typically cannot be reused after removal, since removing and retightening a torque-to-yield fastener a second time does not restore its original clamping characteristics."}, {"heading": "Identifying and Selecting Correct Aircraft Fasteners", "body": "Aircraft fasteners are marked with head codes and material identification systems that allow mechanics to identify grade, material, and manufacturer without needing to consult external documentation for every part, and correctly identifying these markings is essential since visually similar fasteners can have vastly different strength and corrosion properties. AN, MS, and NAS standard fasteners each follow specific part numbering conventions that encode diameter, length, head style, and material, and substituting a fastener outside these specifications, even one that appears to fit, can result in a repair that does not meet the original design's strength requirements. Mechanics must never substitute a hardware-store bolt or screw for an aircraft-grade fastener, since commercial hardware typically lacks the controlled manufacturing processes, material certification, and fatigue-life testing that aviation fasteners undergo. When a specific approved fastener is unavailable, mechanics must reference the illustrated parts catalog or maintenance manual for approved substitutes rather than assuming visual similarity indicates equivalent function."},
    {"heading": "Rivet Types, Head Styles, and Material Designation Codes", "body": "Solid rivets are identified by head style (universal/round head, flush/countersunk head for aerodynamically smooth surfaces, and others) and by a material/temper code stamped or marked on the rivet head or indicated by a dimple/dash pattern, such as AD (2117-T4 aluminum, general purpose), DD (2024-T4, higher strength but requiring ice-box storage before installation since it age-hardens at room temperature), and others each suited to specific structural applications and installation requirements. Using the wrong rivet alloy for an application, such as substituting a lower-strength AD rivet where a DD rivet's higher shear strength was specified, can result in a structural repair that looks correct but does not meet the design's actual strength requirement, which is why repair data always specifies exact rivet part numbers or material designations rather than leaving material selection to technician judgment. Ice-box rivets (like DD/2024-T4) must be stored refrigerated after heat-treating and installed within a specified time after removal from cold storage, since they progressively harden at room temperature and become too hard to properly form a rivet head once the time limit is exceeded."},
    {"heading": "Heat Treatment Processes and Their Effect on Aluminum Alloy Properties", "body": "Aluminum alloys used in aircraft structures achieve their useful strength through heat treatment processes that are fundamentally different from the heat treatment of steel, and technicians must understand these processes to avoid inadvertently degrading material properties during repair or fabrication work. Precipitation-hardening aluminum alloys, such as those in the 2000 and 7000 series, are first solution heat-treated at an elevated temperature to dissolve alloying elements into the aluminum matrix, then rapidly quenched to trap those elements in solution, and finally aged, either at room temperature over days for natural aging or at a moderately elevated temperature for a controlled time for artificial aging, allowing the alloying elements to precipitate as fine particles that impede dislocation movement and increase strength. Because the properties depend on this precise sequence, any subsequent exposure of the material to elevated temperature, such as from welding, improper hot forming, or even a fire nearby, can re-dissolve the precipitated particles and revert the material toward its softer, weaker as-quenched or annealed condition, a change that is not visually apparent and can only be confirmed through hardness testing or conductivity testing. This is why structural repair manuals specify maximum temperature limits and time-at-temperature limits for operations like hot forming aluminum parts, and why heat-damaged aluminum structure discovered after a fire or overheat event requires material property verification before it can be returned to service, since visual inspection alone cannot detect strength loss from overheat. Alclad sheet, which has a thin pure aluminum cladding layer bonded to a stronger core alloy for corrosion protection, requires special care during heat treatment verification since the cladding layer's properties differ from the core and can complicate certain testing methods."}],
    "quiz": [ {"q": "Why must mechanics never substitute a hardware-store bolt for a required aircraft-grade AN, MS, or NAS fastener, even if it appears to fit?", "choices": ["Hardware-store bolts are always more expensive", "Commercial hardware typically lacks the controlled manufacturing, material certification, and fatigue testing that aviation fasteners require", "There is no meaningful difference between hardware types", "Aircraft fasteners are identical to commercial hardware by design"], "answer": 1}, {"q": "Why can substituting a different thread lubricant affect the actual clamping force achieved even if the specified torque wrench reading is met?", "choices": ["Lubricant type has no effect on clamping force", "Torque values are calibrated for specific friction conditions, and different lubricants change the friction coefficient", "All lubricants produce identical friction characteristics", "Torque wrenches automatically compensate for lubricant type"], "answer": 1, "explain": "Torque specifications assume a specific friction condition (dry or a specific lubricant); using a different lubricant changes the friction coefficient, meaning the same torque reading may not produce the intended clamping preload."}, {"q": "What is critical to achieving proper structural adhesive bond strength?", "choices": ["Using expired adhesive for extra tack", "Proper surface preparation of the substrate before bonding", "Applying adhesive as thick as possible", "Skipping the cure schedule"], "answer": 1, "explain": "Adhesive bond strength depends heavily on substrate surface condition; improper cleaning or preparation is a leading cause of bond failure."},
      {"q": "Alclad means:", "choices": ["Al clad with pure Al for corrosion","A composite type","Chromate treatment","Al-titanium alloy"], "answer": 0, "explain": "Alclad = high-strength alloy with pure aluminum cladding for corrosion resistance."},
      {"q": "AD rivet alloy:", "choices": ["2024","2117","7075","Steel"], "answer": 1, "explain": "AD = 2117-T3, the most common rivet. Drives as-received."},
      {"q": "Burning magnesium needs which extinguisher?", "choices": ["Class A","Class B","Class C","Class D"], "answer": 3, "explain": "Magnesium is combustible metal = Class D (dry powder)."},
      {"q": "AN fittings use what flare angle?", "choices": ["45 deg","37 deg","30 deg","90 deg"], "answer": 1, "explain": "AN (aircraft) fittings use 37 degrees. 45 is automotive - never mix."},
      {"q": "4130 chromoly is used for:", "choices": ["Wing skins","Engine mounts/fuselage tubes","Windows only","Prop blades"], "answer": 1, "explain": "4130 is the standard aircraft structural steel for mounts, gear, tubes."},
    {"q": "Why must ice-box rivets such as 2024-T4 (DD) be installed within a specified time after removal from cold storage?", "choices": ["Ice-box rivets have no time-sensitive material property", "They progressively age-harden at room temperature and become too hard to properly form a rivet head once the time limit is exceeded", "Cold storage is only for shipping convenience and has no effect on material properties", "All rivet types require identical ice-box storage regardless of alloy"], "answer": 1},
    {"q": "Why can exposing a precipitation-hardened aluminum alloy to elevated temperature after heat treatment weaken it in a way not visible to inspection?", "choices": ["The heat can re-dissolve the precipitated particles that provide strength, reverting the material toward a softer condition undetectable without hardness or conductivity testing", "Aluminum alloys are completely immune to any strength change from heat exposure", "Visual discoloration always reliably indicates the exact strength loss", "Heat treatment has no relationship to precipitation of alloying elements"], "answer": 0}
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
      {"heading": "Circuit Troubleshooting", "body": "A <b>voltage-drop test</b> (checking voltage loss across a connection or wire under load) finds high-resistance faults that a simple continuity check can miss. Compare live circuit voltage at the load to the source - excessive drop points to a bad connector, corroded ground, or damaged wire. Always verify continuity to ground and check for shorts to structure before assuming a component itself has failed."}, {"heading": "Diode and Semiconductor Basics in Aircraft Circuits", "body": "Diodes are used throughout aircraft electrical systems for functions including preventing reverse current flow (protecting a circuit if power is momentarily reversed), voltage spike suppression across relay coils and inductive loads, and signal rectification in certain sensor and charging circuits. A failed diode can fail either open (blocking all current, even in the intended direction) or shorted (allowing current to flow in both directions, defeating its protective purpose), and testing with a multimeter's diode-check function verifies proper one-direction conduction rather than relying on a simple continuity check, which cannot distinguish a good diode from certain fault conditions. Technicians replacing diodes must match not just current rating but also reverse voltage rating and switching characteristics, since substituting a diode with insufficient reverse voltage rating can lead to a repeat failure under normal operating conditions."}, {"heading": "Series, Parallel, and Series-Parallel Circuit Analysis", "body": "Understanding how components are connected within a circuit, whether in series (single current path through all components), parallel (multiple current paths with the same voltage across each branch), or series-parallel combinations, is fundamental to predicting circuit behavior and troubleshooting faults. In a series circuit, current is the same through every component while voltage divides proportionally to resistance, meaning a single open component halts current everywhere in that circuit, which explains why one burned-out bulb in an old-style series string of lights would darken the entire string. In a parallel circuit, voltage is the same across every branch while current divides based on each branch's resistance, meaning one branch can fail open without affecting current flow in the other branches, which is why most aircraft systems use parallel wiring so a single load failure does not disable unrelated systems. Applying Ohm's Law and Kirchhoff's voltage and current laws to these circuit configurations allows mechanics to calculate expected voltage drops and currents at test points, which is essential for confirming whether a measured value during troubleshooting indicates normal operation or a developing fault."},
    {"heading": "Capacitors and Inductors in AC Circuit Behavior", "body": "Capacitors store energy in an electric field and oppose changes in voltage, causing current to lead voltage in an AC circuit, while inductors store energy in a magnetic field and oppose changes in current, causing current to lag voltage; both introduce reactance that combines with resistance to form impedance, the total opposition to AC current flow. Aircraft circuits use capacitors for filtering (smoothing rectified DC, suppressing electrical noise) and inductors in chokes, transformers, and filter networks; a failed capacitor (shorted or open) or a failed inductor winding can cause anything from noisy audio in a comm system to complete loss of a filtered power supply rail. Because reactance changes with frequency, a circuit that operates correctly at one frequency can behave very differently at another, which is why avionics power supply and filter troubleshooting must consider the actual signal or ripple frequency involved, not just DC resistance measurements."},
    {"heading": "Electromagnetic Interference (EMI) and Bonding/Grounding Practices", "body": "Electromagnetic interference is unwanted electrical noise that can degrade the performance of avionics, communication, and navigation equipment, originating from sources such as motor and generator brush arcing, switching power supplies, ignition systems, and static electricity buildup from airflow over the airframe. Aircraft bonding—the practice of electrically connecting metal structural components together with low-resistance bonding jumpers—serves multiple purposes: it provides a return path for electrical current, equalizes electrical potential across the structure to prevent arcing at gaps and joints, and provides a path for lightning and static discharge current, all of which reduce both EMI generation and the risk of arcing-induced ignition sources near fuel systems. Grounding connects electrical circuits and equipment chassis to the aircraft structure, which serves as the common electrical reference (return path) in most aircraft electrical systems, since a single-wire return system uses the airframe itself as the ground return conductor rather than a dedicated wire back to the source. Bonding jumper resistance is checked periodically with a low-resistance ohmmeter (milliohmmeter) against the maintenance manual limit, typically a fraction of an ohm, since increased resistance indicates corrosion, loose attachment, or a damaged jumper that can allow EMI-generating potential differences to develop and degrade both electrical performance and lightning/static protection."}],
    "quiz": [ {"q": "In a parallel circuit, what happens to current flow in the other branches if one branch fails open?", "choices": ["All current flow in the entire circuit stops immediately", "The other branches continue to carry current normally since each has its own independent path", "Voltage across all branches drops to zero", "The circuit automatically converts to a series configuration"], "answer": 1}, {"q": "What is a key function of diodes used across relay coils and inductive loads in aircraft circuits?", "choices": ["Increasing circuit resistance", "Suppressing voltage spikes generated when the inductive load is switched off", "Reducing circuit weight", "Providing illumination"], "answer": 1, "explain": "Diodes placed across relay coils and inductive loads suppress the voltage spike that occurs when the inductive load is de-energized, protecting other circuit components from that transient."},
      {"q": "28V bus, 7 ohm load. Current?", "choices": ["4 A","196 A","0.25 A","35 A"], "answer": 0, "explain": "I = E/R = 28/7 = 4 amps."},
      {"q": "In parallel, what stays constant?", "choices": ["Current","Resistance","Voltage","Power"], "answer": 2, "explain": "Parallel: voltage is the same across all branches."},
      {"q": "Aircraft AC frequency:", "choices": ["60 Hz","50 Hz","400 Hz","1000 Hz"], "answer": 2, "explain": "400 Hz allows smaller/lighter transformers and motors."},
      {"q": "Ni-Cad danger:", "choices": ["Sulfation","Thermal runaway","Freezing","Reverse polarity"], "answer": 1, "explain": "Ni-Cad batteries can experience thermal runaway - cascading overheat causing fire."},
      {"q": "A voltage-drop test is useful because it can detect:", "choices": ["Only a completely open circuit", "High-resistance connections that a simple continuity check may miss", "Battery amp-hour capacity only", "AC frequency drift"], "answer": 1, "explain": "Voltage-drop testing under load reveals corroded or loose connections that still pass a basic continuity check but cause excessive resistance."},
      {"q": "Never do this with a popping breaker:", "choices": ["Replace it","Check circuit","Hold it in","Record it"], "answer": 2, "explain": "Holding in a popping breaker overrides protection against an active fault - fire risk."},
    {"q": "In an AC circuit, what is the key difference between how a capacitor and an inductor respond to changes in voltage and current?", "choices": ["They respond identically since both are reactive components", "A capacitor opposes changes in voltage (current leads voltage), while an inductor opposes changes in current (current lags voltage)", "Capacitors only function in DC circuits and inductors only in AC circuits", "Neither component has any effect on circuit behavior"], "answer": 1},
    {"q": "What is one primary purpose of aircraft structural bonding jumpers?", "choices": ["To increase the aircraft's overall weight for balance purposes", "To equalize electrical potential across structure and provide a path for lightning/static discharge current, reducing arcing risk", "To insulate metal components from each other", "To replace the need for a battery"], "answer": 1}
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
      {"heading": "Selecting the Right Method", "body": "Choice of NDT method depends on the material, flaw type, and location. <b>Magnetic particle</b> only works on ferrous metals. <b>Dye penetrant</b> finds only surface-breaking flaws in any non-porous material. <b>Eddy current</b> is excellent for surface/near-surface cracks in conductive metals (including aluminum) without couplant. <b>Ultrasonic</b> finds subsurface flaws and measures thickness in any material. <b>Radiographic (X-ray)</b> reveals internal voids/inclusions but requires strict radiation safety controls."}, {"heading": "NDT Personnel Certification Levels", "body": "Nondestructive testing personnel are certified to specific levels (commonly Level I, II, and III per NAS 410 or similar standards) that define the scope of tasks each level is qualified to perform: Level I technicians can perform specific NDT tasks under Level II or III supervision following written procedures, Level II technicians can independently set up equipment, perform tests, and interpret/evaluate results per established procedures, and Level III personnel can develop procedures, interpret codes and standards, and provide overall technical direction for an NDT program. Maintenance organizations must verify that NDT inspections are performed and results interpreted by personnel holding the appropriate certification level for that specific method and application, since an inspection performed or interpreted by underqualified personnel may not be considered valid even if the correct equipment and technique were used. Certification requires both initial training/examination and periodic recertification, along with documented recent experience in the specific method to maintain currency."}, {"heading": "Documenting and Reporting NDT Inspection Results", "body": "NDT inspection results must be documented with sufficient detail to be traceable and defensible, including the specific method used, equipment and calibration standard employed, technique parameters (such as penetrant dwell time or magnetic field strength), inspector certification level, and a clear description of any indications found with their location, size, and disposition. A finding that is merely noted as 'crack found, repaired' without supporting detail fails to provide the traceability needed if the part's history is later questioned or if a similar failure occurs on a fleet-wide basis requiring root cause investigation. Photographs or sketches accompanying written findings, particularly for borderline indications near acceptance limits, provide valuable supplementary documentation that can be reviewed by engineering or a Level III inspector without requiring re-inspection of the physical part. Reporting must also distinguish clearly between a rejected indication requiring disposition and information collected purely for trend monitoring purposes, since conflating these categories in records can create ambiguity about whether a part was actually airworthy at the time of inspection."},
    {"heading": "Thermographic (Infrared) Inspection Applications", "body": "Thermographic inspection uses an infrared camera to detect subsurface anomalies in composite structures, bonded joints, and some metallic assemblies by observing how heat applied to the surface (via flash lamp, hot air, or ambient solar heating) flows through and dissipates from the material; a disbond, delamination, or water ingress creates a localized difference in thermal conductivity that appears as a temperature anomaly on the infrared image before it equalizes with surrounding material. This method is particularly valuable for large-area composite skin inspection where it can screen wide areas quickly compared to point-by-point ultrasonic scanning, but it is generally less sensitive to very small or deep defects than ultrasonic methods and is affected by ambient conditions such as wind, direct sun angle, and moisture, so inspection timing and environmental control are part of a valid thermographic procedure. Because thermal patterns can also result from underlying structure, fastener heads, or paint variations that are not defects, thermographic inspection interpretation requires training to distinguish true anomalies from normal thermal signatures."},
    {"heading": "Acoustic Emission and Vibration Analysis Inspection Techniques", "body": "Acoustic emission (AE) testing detects the high-frequency stress waves released when a material undergoes crack growth, plastic deformation, or fiber breakage under load, using sensitive piezoelectric sensors bonded to the structure while it is subjected to a controlled proof load; the technique is well suited to monitoring pressure vessels, composite pressure bottles, and large structures during proof testing because it can detect active flaw growth in real time across a wide area from a limited number of sensor locations, unlike point-by-point methods such as dye penetrant or eddy current. Vibration analysis, used extensively for rotating machinery condition monitoring, measures vibration amplitude and frequency spectrum from accelerometers mounted on engines, gearboxes, and other rotating assemblies, then compares the measured frequency content against known characteristic frequencies (such as shaft rotational speed, bearing defect frequencies, and blade-pass frequencies) to identify developing faults like bearing wear, imbalance, misalignment, or gear tooth damage before they progress to failure. Both techniques are considered condition-based or on-condition monitoring tools that can extend inspection intervals or detect problems between scheduled inspections, but they require baseline data for comparison and trained analysts to correctly interpret the signatures, since environmental noise and normal operational variation can produce signals that must be distinguished from genuine developing faults."}],
    "quiz": [ {"q": "Why should an NDT inspection report include detailed technique parameters and indication descriptions rather than a brief summary like 'crack found, repaired'?", "choices": ["Detailed documentation is only useful for training new inspectors", "Detailed records provide traceability needed for later review, including fleet-wide root cause investigation if similar failures occur", "Brief summaries are always preferred for efficiency", "NDT documentation requirements do not vary in detail level"], "answer": 1}, {"q": "What can a Level II NDT technician typically do that a Level I technician cannot?", "choices": ["Nothing, the levels have identical scope", "Independently set up equipment, perform tests, and interpret/evaluate results per established procedures", "Only clean parts before inspection", "Only perform administrative recordkeeping"], "answer": 1, "explain": "Level II technicians can independently set up, perform, and interpret NDT results per established procedures, while Level I technicians work under supervision following written procedures."},
      {"q": "Which NDT works ONLY on ferrous metals?", "choices": ["Dye penetrant","Eddy current","Magnetic particle","Ultrasonic"], "answer": 2, "explain": "Magnetic particle needs a magnetizable (ferrous) part."},
      {"q": "Dye penetrant finds:", "choices": ["Internal voids","Subsurface cracks","Surface-breaking cracks only","Corrosion under paint"], "answer": 2, "explain": "Penetrant only enters surface-breaking discontinuities."},
      {"q": "After MT inspection you must:", "choices": ["Repaint","Demagnetize","Heat-treat","Replace"], "answer": 1, "explain": "Residual magnetism attracts chips and interferes with instruments."},
      {"q": "Which method measures remaining wall thickness?", "choices": ["Visual","Dye penetrant","Ultrasonic","Magnetic particle"], "answer": 2, "explain": "Ultrasonic precisely measures remaining material thickness."},
      {"q": "To detect a subsurface crack in an aluminum structure, the most appropriate NDT method would be:", "choices": ["Magnetic particle inspection", "Dye penetrant inspection", "Ultrasonic or eddy current inspection", "Visual inspection only"], "answer": 2, "explain": "Magnetic particle only works on ferrous metal, and dye penetrant only finds surface-breaking flaws - ultrasonic or eddy current can detect subsurface flaws in aluminum."},
      {"q": "Most commonly used inspection method:", "choices": ["Radiographic","Eddy current","Visual","Ultrasonic"], "answer": 2, "explain": "Visual inspection is the foundation - performed on every task."},
    {"q": "Why is thermographic (infrared) inspection particularly useful for screening large composite skin areas compared to point-by-point ultrasonic inspection?", "choices": ["It is more sensitive to very small, deep defects than ultrasonic methods", "It can screen wide areas quickly by observing heat flow anomalies caused by disbonds or delaminations, though it is generally less sensitive to small/deep defects", "It is unaffected by ambient environmental conditions", "It cannot be used on any composite structures"], "answer": 1},
    {"q": "What makes acoustic emission testing particularly useful for proof-testing large pressure vessels or composite tanks?", "choices": ["It requires disassembly of the vessel before testing", "It can detect active flaw growth in real time across a wide area from limited sensor locations during loading", "It only works on unpressurized structures", "It replaces the need for any other NDT method"], "answer": 1}
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
      {"heading": "Repair Philosophy", "body": "A structural repair must restore the original <b>strength, stiffness, contour, and corrosion protection</b> without adding excessive weight. A <b>doubler</b> reinforces a damaged area by spreading load around the repair; its size and rivet pattern come from approved data (AC 43.13-1B or manufacturer structural repair manual), not guesswork. Repairs must never be based on \"it looks strong enough\" - use approved data for material, thickness, and fastener pattern."}, {"heading": "Fail-Safe and Redundant Structural Design Philosophy", "body": "Fail-safe structural design ensures that the failure of a single structural member does not lead to catastrophic loss of the aircraft, achieved through redundant load paths (multiple structural members sharing a load so that one can fail while others continue carrying it), crack-arrest features that stop a crack from propagating across an entire structural section, and damage-tolerant design that accounts for the aircraft continuing to operate safely for a defined period even with certain types of damage present before repair. Understanding fail-safe design philosophy helps technicians recognize why some structural damage, while requiring repair, does not necessarily ground the aircraft immediately, whereas damage to a single, non-redundant critical structural member may require immediate grounding since no backup load path exists. Structural repair manuals define specific inspection intervals and repair time limits for different damage types precisely because they are built around this fail-safe and damage-tolerance philosophy rather than a simple pass/fail damage assessment."}, {"heading": "Stress Concentration and Design Features to Minimize It", "body": "Stress concentrations occur at geometric discontinuities such as holes, notches, sharp corners, or abrupt cross-section changes, where applied load causes localized stress significantly higher than the average stress across the surrounding structure, making these locations preferential sites for fatigue crack initiation even when the overall structure is not overloaded. Aircraft structural design incorporates features specifically to minimize stress concentration effects, such as generous fillet radii at cross-section changes, properly sized and positioned fastener holes with adequate edge distance, and smooth transitions rather than abrupt steps in thickness or width. Repairs must preserve these stress-reducing design features; for example, drilling a repair hole too close to an existing hole or structural edge creates a new stress concentration that the original design did not account for, potentially creating a fatigue-critical location where none existed before. Understanding stress concentration principles helps mechanics recognize why seemingly minor deviations from approved repair geometry, such as a slightly undersized fillet radius or incorrectly positioned rivet hole, can have outsized effects on a structure's fatigue life despite looking visually acceptable."},
    {"heading": "Lightning Strike Protection and Damage Assessment for Airframe Structures", "body": "Aircraft structures incorporate lightning protection through bonding straps, conductive mesh embedded in composite skins, static dischargers, and diverter strips that route strike current safely to the airframe and overboard rather than through fuel tanks or avionics bays. Zone 1 areas (wingtips, nose, tail surfaces) receive direct attachment and require heavier protection than Zone 2/3 areas where current is swept aft. After a suspected or confirmed lightning strike, technicians must inspect entry and exit points for burn marks, pitting, and paint blistering; check bonding jumper resistance across structural joints; and for composite structures, tap-test or use ultrasonic inspection around strike points to detect delamination from the internal arcing and rapid heating of resin, since composite laminates can suffer significant subsurface damage with minimal visible surface indication. Fuel tank areas require special attention to fastener sealing and bonding continuity, as arcing at an unbonded fastener inside a tank is a fire ignition source. Static dischargers (wicks) are inspected for erosion and resistance value per the maintenance manual and replaced when resistance exceeds limits, since degraded dischargers allow static buildup that causes radio noise."},
    {"heading": "Composite-to-Metal Structural Joint Design and Galvanic Isolation", "body": "Joints connecting composite structure to metallic structure require careful design consideration beyond simple mechanical load transfer, since carbon fiber composite materials are electrically conductive and, particularly in contact with aluminum, create a galvanic couple in the presence of moisture that can cause accelerated corrosion of the aluminum component at the joint interface. Galvanic isolation is achieved through methods such as a fiberglass isolation ply between the carbon composite and aluminum surfaces, non-conductive sealant applied at the interface during assembly, or specification of more galvanically compatible fastener and structure materials such as titanium in place of aluminum for direct-contact hardware, and technicians performing repairs at these joints must preserve or restore the specified isolation method exactly rather than substituting a different approach that seems functionally similar. Fastener installation at composite-to-metal joints also requires attention to torque values and washer specifications different from typical metal-to-metal joints, since composite material can be crushed or delaminated by excessive clamp-up force in a way that metal structure would not be, while insufficient clamp-up can allow joint movement that induces fretting damage at the interface over repeated load cycles. Sealant application at these joints serves the dual purpose of environmental sealing against moisture intrusion and maintaining the galvanic isolation barrier, so any repair that disturbs the sealant must restore it using the specified sealant type and application method rather than a generic sealant that may not provide equivalent isolation performance. Inspection of composite-to-metal joints for corrosion should specifically examine the metal side of the interface for pitting or staining even when the composite surface itself appears undamaged, since galvanic corrosion effects concentrate at the metal component while the composite material itself is not directly consumed by the galvanic reaction."}],
    "quiz": [ {"q": "Why can a repair hole drilled too close to an existing structural edge create a fatigue problem even if the repair otherwise appears sound?", "choices": ["Hole spacing has no effect on structural fatigue life", "Insufficient edge distance creates a stress concentration that increases the likelihood of fatigue crack initiation at that location", "All repair holes are equally safe regardless of position", "Fatigue only depends on material type, never geometry"], "answer": 1}, {"q": "What does fail-safe structural design rely on to prevent catastrophic failure from a single structural member failing?", "choices": ["Making every part impossible to break", "Redundant load paths and damage-tolerant design that allow continued safe operation despite the failure", "Eliminating all structural inspections", "Using only the lightest possible materials"], "answer": 1, "explain": "Fail-safe design uses redundant load paths and damage-tolerant features so that a single structural member's failure does not lead to catastrophic loss, since other members continue carrying the load."},
      {"q": "Semi-monocoque uses:", "choices": ["Skin only","Skin + frames + stringers","Truss tubes","Composites only"], "answer": 1, "explain": "Semi-monocoque: skin shares load with internal frames, longerons, and stringers."},
      {"q": "Primary wing bending load carrier:", "choices": ["Ribs","Skin","Spar","Stringers"], "answer": 2, "explain": "Spars are the main beams carrying wing bending loads."},
      {"q": "What measures cable tension?", "choices": ["Protractor","Torque wrench","Tensiometer","Dynamometer"], "answer": 2, "explain": "A tensiometer measures cable tension (correct for temperature)."},
      {"q": "Why balance control surfaces after repaint?", "choices": ["Appearance","Prevent flutter","Reduce drag","Weight savings"], "answer": 1, "explain": "Paint shifts CG; if aft of hinge line, destructive flutter can occur."},
      {"q": "The primary purpose of a doubler in a structural sheet metal repair is to:", "choices": ["Improve appearance only", "Spread load around the damaged/repaired area to restore strength", "Reduce weight", "Provide a mounting point for hardware"], "answer": 1, "explain": "A doubler reinforces the repair area, redistributing stress around the damage per approved repair data."},
      {"q": "Wet wing means:", "choices": ["Wing in rain","Wing sealed as fuel tank","Deice boots","Composite wing"], "answer": 1, "explain": "Integral tank - the sealed wing structure IS the fuel container."},
    {"q": "Why does a lightning strike on a composite structure often show minimal surface damage despite significant internal harm?", "choices": ["Composite resin is non-conductive and blocks all current", "Rapid internal arcing and heating can delaminate layers beneath a largely intact surface", "Composite structures are never struck due to their non-metallic nature", "Lightning current always exits through the same point it enters"], "answer": 1},
    {"q": "Why is galvanic isolation specifically important at composite-to-metal structural joints, particularly with carbon fiber composite and aluminum?", "choices": ["Carbon fiber composite is electrically conductive and can form a galvanic couple with aluminum in the presence of moisture, causing accelerated corrosion of the aluminum", "Composite materials are never electrically conductive under any circumstances", "Galvanic isolation is only a cosmetic consideration with no effect on structural integrity", "Aluminum is immune to galvanic corrosion regardless of adjacent material"], "answer": 0}
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
      {"heading": "Layout & Fastening Practice", "body": "<b>Clecos</b> temporarily hold sheets aligned and under clamping pressure during drilling and fitting, before final rivets are installed - this prevents holes from being drilled slightly out of alignment. Deburr every drilled hole to remove sharp edges that could start a crack. Dimple or countersink for flush fasteners per the thickness and rivet type specified in the repair data, and always match existing hole patterns exactly when replacing a panel."}, {"heading": "Rivet Spacing and Edge Distance Calculations", "body": "Proper rivet spacing and edge distance are critical to joint strength, with minimum edge distance (typically expressed as a multiple of rivet diameter, such as 2D from the sheet edge to the rivet centerline) preventing the sheet material from tearing out around the rivet under load, and minimum rivet-to-rivet spacing preventing excessive stress concentration between adjacent fasteners that could cause the material between them to fail. Maximum spacing limits also apply, since rivets spaced too far apart fail to adequately distribute load across the joint and can allow the sheets to separate or flutter between fastener points under aerodynamic or vibration loads. Repair doublers and patches must follow the same edge distance and spacing rules as original design, not looser tolerances, since a repair joint is often carrying concentrated load at a point where the original structure has already been compromised by damage."}, {"heading": "Bend Radius and Minimum Bend Radius Requirements", "body": "When forming sheet metal, the bend radius (the radius of curvature at the bend) must meet or exceed the material's minimum bend radius, a value determined by the material's thickness, alloy, and temper, since bending too tightly (using too small a radius) can crack or significantly weaken the material at the bend, particularly for harder tempers of aluminum that have less ductility than softer, more workable tempers. Minimum bend radius charts, provided in structural repair manuals, specify the smallest allowable radius for each combination of material thickness and temper, and mechanics must consult these charts rather than assuming a bend that looks acceptable is actually within allowable limits. The bend allowance and setback calculations used to determine flat-pattern layout dimensions before forming depend on the specific bend radius used, meaning changing the bend radius from what was originally planned requires recalculating these layout dimensions to ensure the finished part meets its required final dimensions. Some materials, particularly higher-strength aluminum alloys in harder tempers, may require annealing (softening through heat treatment) before forming a tight bend, followed by re-heat-treating afterward to restore the required strength, adding process complexity that mechanics must account for when planning a sheet metal repair."},
    {"heading": "Sheet Metal Forming Methods: Stretch Forming, Drop Hammer, and Hydroforming", "body": "Beyond simple brake-formed bends, aircraft sheet metal parts with complex contours are produced using specialized forming methods. Stretch forming clamps a flat blank at both ends and pulls it over a form block while applying tension, plastically stretching the metal to conform to compound curves without wrinkling—commonly used for wing and fuselage skins. Drop hammer forming uses matched male and female dies with a falling weight (ram) to strike the blank repeatedly, progressively forming it into the die cavity shape; it is suited to smaller, deeply contoured parts produced in batches. Hydroforming uses fluid pressure acting through a rubber diaphragm to press a blank into or around a single die, producing uniform pressure distribution that reduces thinning and is economical for low-volume production since only one die half is needed. Each method affects the resulting grain structure and cold work distribution differently, which is why repair replacement parts should be manufactured using an equivalent forming process when structural equivalency is required, and why formed parts should be inspected for cracks at areas of maximum stretch, such as sharp compound-curve transitions."},
    {"heading": "Countersinking and Dimpling Techniques for Flush-Riveted Skins", "body": "Flush riveting, used extensively on high-speed aircraft skins to minimize aerodynamic drag, requires that the rivet head be recessed to sit flush with or very slightly below the skin surface, achieved through either countersinking the hole itself into thicker material or dimpling thinner sheet material to form a depression matching the rivet head shape without removing material from an already-thin sheet. Countersinking is appropriate when sheet thickness is sufficient that removing material to form the countersink angle still leaves adequate remaining material thickness at the hole edge to support the rivet load, and the technician must verify remaining edge thickness against the minimum specified in the structural repair manual, since a countersink cut too deep into thin material creates a knife-edge condition that provides essentially no support for the rivet and can crack under load. Dimpling, used on thinner sheet stock where countersinking would remove too much material, uses a male and female dimpling die set to press a countersunk-shaped depression into the sheet without removing any material, preserving the sheet's full thickness and strength around the hole while still achieving a flush rivet head fit. Coin dimpling adds a secondary radius-forming step that improves the dimple's shape accuracy and consistency compared to simple pressure dimpling alone, and is often specified for critical structural applications where dimple quality directly affects fastener load distribution. Rivet head to countersink or dimple fit must be checked to ensure the head sits flush within a very small tolerance, neither protruding above the surface, which defeats the aerodynamic purpose and can catch on ground handling equipment, nor sunk below the surface, which reduces the rivet's shear capacity and can trap moisture that promotes corrosion at the recessed head."}],
    "quiz": [ {"q": "Why must mechanics consult minimum bend radius charts rather than judging by appearance whether a bend radius is acceptable?", "choices": ["Bend radius has no effect on material integrity", "Bending tighter than the minimum allowable radius for a given material thickness and temper can crack or weaken the material even if it looks acceptable", "All bend radii are equally safe for any material", "Minimum bend radius charts are only advisory, not required"], "answer": 1}, {"q": "What is the purpose of minimum edge distance requirements for rivets?", "choices": ["Purely cosmetic appearance", "Preventing the sheet material from tearing out around the rivet under load", "Reducing the total number of rivets needed", "Making rivet installation faster only"], "answer": 1, "explain": "Minimum edge distance prevents the sheet material near the rivet from tearing out under load, which is why edge distance is typically specified as a multiple of rivet diameter."},
      {"q": "For 0.050 in skin, rivet diameter:", "choices": ["1/16","3/32","5/32","1/4"], "answer": 2, "explain": "3 x 0.050 = 0.150 -> closest standard is 5/32 (0.156)."},
      {"q": "Setback for 90 deg, R=0.125, T=0.032:", "choices": ["0.093","0.125","0.157","0.250"], "answer": 2, "explain": "Setback = R+T = 0.125+0.032 = 0.157 inches."},
      {"q": "DD rivet must be:", "choices": ["Driven anytime","Heat-treated and refrigerated, driven cold","Driven hot","Used on steel only"], "answer": 1, "explain": "DD=2024 (ice-box). Heat-treat, refrigerate, drive within ~20 min before it hardens."},
      {"q": "Min edge distance for 1/8 in rivet:", "choices": ["1/8","3/16","1/4 to 5/16","1/2"], "answer": 2, "explain": "Edge = 2D to 2.5D. For 0.125: 0.250 to 0.3125 (1/4 to 5/16)."},
      {"q": "Clecos are used during sheet metal repair primarily to:", "choices": ["Permanently fasten the repair", "Temporarily hold sheets aligned and clamped before final riveting", "Measure rivet spacing", "Deburr drilled holes"], "answer": 1, "explain": "Clecos are temporary fasteners that hold layers in alignment and clamped together while drilling/fitting, and are removed as final rivets are installed."},
      {"q": "First action for a skin crack:", "choices": ["Rivet a patch","Stop-drill crack ends","Remove panel","Ignore if small"], "answer": 1, "explain": "Stop-drilling eliminates stress concentration at crack tip, preventing propagation."},
    {"q": "What is a key advantage of hydroforming over matched-die drop hammer forming for low-volume sheet metal parts?", "choices": ["It requires two matched hardened steel dies", "It only works on titanium alloys", "It uses fluid pressure through a diaphragm against a single die, reducing tooling cost and cost", "It eliminates the need for any inspection after forming"], "answer": 2},
    {"q": "Why is dimpling used instead of countersinking on thin sheet metal stock for flush rivets?", "choices": ["Dimpling preserves the sheet's full material thickness around the hole, avoiding the knife-edge weakness that deep countersinking into thin material would create", "Dimpling is always faster to perform than countersinking regardless of sheet thickness", "Countersinking cannot be used on any aircraft structure under any circumstance", "Dimpling eliminates the need for any rivet head flushness inspection"], "answer": 0}
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
      {"heading": "System Interdependencies", "body": "Airframe systems often share resources and can fail together in non-obvious ways: a hydraulic pump failure can affect both brakes and gear retraction if they share a system; a bleed-air leak can trigger both a pressurization fault and an overheat warning in the same bay. When troubleshooting one system's fault, always consider what else shares its power source, hydraulic system, or bleed-air supply - fixing the wrong system wastes time and can mask the real problem."}, {"heading": "Cross-System Fault Propagation Analysis", "body": "Modern aircraft systems are highly interconnected, meaning a fault in one system can manifest symptoms in an apparently unrelated system, such as a hydraulic system pressure loss causing landing gear extension problems that also trigger cascading electrical warnings from position sensors, or an electrical bus fault disabling both a fuel pump and an unrelated avionics display fed from the same bus. Effective troubleshooting of multi-system symptom presentations requires consulting the aircraft's systems interconnection diagrams or fault isolation manual rather than treating each symptom as an independent problem, since chasing each symptom separately can waste significant time when a single root cause bus, valve, or sensor explains all of them. Technicians should always ask whether multiple simultaneous system anomalies share a common power source, hydraulic supply, or pneumatic source before assuming multiple independent failures have occurred."}, {"heading": "System Integration Testing After Major Maintenance", "body": "After major maintenance affecting multiple interconnected airframe systems, such as a landing gear overhaul that also involved hydraulic line replacement, integration testing verifies that all affected systems function correctly together, not just individually, since isolated component tests can miss interaction faults that only appear under combined operating conditions. Integration testing often follows a specific sequence defined in the maintenance manual, starting with lower-risk static ground checks before progressing to functional tests under increasing levels of system activation, ensuring any fault is caught at the earliest, safest opportunity rather than during a more demanding test condition. Cross-system dependencies, such as hydraulic pressure affecting both landing gear actuation and flight control operation simultaneously, mean that a fault introduced in one system during maintenance can manifest as an apparent problem in a seemingly unrelated system, making thorough integration testing essential rather than relying solely on testing the specific system that was worked on. Sign-off for return to service after major multi-system maintenance should reference completion of the full integration test sequence, not merely the individual component functional checks."},
    {"heading": "Structural Load Path Interaction with Systems Routing", "body": "Hydraulic lines, wire bundles, and ducting are often routed through or near primary structural load paths (spars, frames, longerons), and any hole, bracket, or clamp added to support system routing represents a potential stress concentration in the structure that must be engineered, not improvised. Maintenance personnel performing system repairs must never drill an unauthorized hole through a spar cap or other primary structure to route a wire or line, since even a small unapproved penetration in a highly loaded member can create a fatigue crack initiation site; any new routing path through structure requires an engineering-approved repair or modification, not field judgment. Conversely, structural repairs (doublers, patches) must account for existing systems routing so that a repair doesn't clamp down on or restrict clearance for a hydraulic line or wire bundle, since chafing or pinching introduced by a structural repair is itself a systems discrepancy waiting to occur."},
    {"heading": "Environmental Control System Integration with Pressurization and Avionics Cooling", "body": "The environmental control system (ECS) does not operate in isolation; it is tightly integrated with cabin pressurization control and avionics cooling, since all three functions typically draw from the same conditioned bleed air or air cycle machine output. Pressurization is normally maintained by outflow valves that regulate the rate at which conditioned air exits the pressure vessel, working in concert with the ECS air supply rate so that a controlled cabin altitude schedule is maintained as the aircraft climbs and descends; a failure or miscoordination between ECS air supply and outflow valve control can cause either excessive pressure differential or inability to maintain cabin altitude. Avionics cooling systems often bleed conditioned air, or in some designs a dedicated cooling air path, to remove heat from avionics bays and electronic equipment racks, since modern digital avionics generate substantial heat that must be continuously removed to prevent thermal shutdown or component degradation; a blocked avionics cooling inlet or failed cooling fan can cause nuisance equipment faults or shutdowns that are sometimes misdiagnosed as avionics failures rather than a cooling system problem. Because these systems share air sources and are interdependent, troubleshooting an ECS or pressurization discrepancy should always include checking whether avionics cooling airflow is affected, and vice versa, and technicians should consult the applicable system schematic to understand the specific air distribution architecture for the aircraft type being serviced."}],
    "quiz": [ {"q": "Why is system integration testing necessary after maintenance affecting multiple interconnected airframe systems, beyond testing each system individually?", "choices": ["Individual component tests are always sufficient and integration testing is unnecessary", "Integration testing catches interaction faults between systems that only appear under combined operating conditions, which isolated tests can miss", "Integration testing is only a formality with no diagnostic value", "Cross-system dependencies never affect airframe system testing"], "answer": 1}, {"q": "What should technicians consider before assuming multiple simultaneous system anomalies are independent failures?", "choices": ["Nothing, each symptom should always be treated separately", "Whether the anomalies share a common power source, hydraulic supply, or pneumatic source", "Only the most recently reported symptom", "The color of the affected components"], "answer": 1, "explain": "Multiple simultaneous system anomalies often share a single root cause tied to a common power, hydraulic, or pneumatic source, so checking for shared sources before treating each symptom independently saves troubleshooting time."},
      {"q": "Skydrol requires:", "choices": ["No special handling","PPE - corrosive","Heating","Mixing with mineral oil"], "answer": 1, "explain": "Skydrol (phosphate-ester) is corrosive to skin, eyes, paint. PPE mandatory."},
      {"q": "Aircraft tires inflated with:", "choices": ["Air","Nitrogen","Helium","CO2"], "answer": 1, "explain": "Nitrogen is inert - no moisture, stable pressure with temp change."},
      {"q": "Why no oil near O2 fittings?", "choices": ["Clogs system","Auto-ignition/explosion","Reduces flow","Voids warranty"], "answer": 1, "explain": "Oil/grease + high-pressure O2 can spontaneously ignite explosively."},
      {"q": "Squat switch prevents:", "choices": ["Overspeed","Gear retraction on ground","Depressurization","Cross-feed"], "answer": 1, "explain": "Weight-on-wheels switch inhibits gear retract while on the ground."},
      {"q": "When multiple aircraft systems fail or malfunction at the same time, a mechanic should first consider that they:", "choices": ["Are always unrelated coincidences", "May share a common power source, hydraulic system, or air supply", "Should each be replaced individually without investigation", "Indicate a software update is needed"], "answer": 1, "explain": "Shared resources (hydraulic systems, electrical buses, bleed air) can cause seemingly unrelated systems to fail together from a single root cause."},
      {"q": "Deice boots work by:", "choices": ["Heating","Inflating to crack ice","Chemical spray","Vibration"], "answer": 1, "explain": "Boots inflate and flex to break the ice bond; ice sheds in airstream."},
    {"q": "Why is it unacceptable for a technician to drill an unauthorized hole through a spar cap to route a new wire or line?", "choices": ["It is acceptable as long as the hole is small", "Even a small unapproved penetration in a highly loaded structural member can create a fatigue crack initiation site", "Spar caps are never part of the primary structural load path", "Drilling holes in structure has no effect on fatigue life"], "answer": 1},
    {"q": "Why might a blocked avionics cooling inlet be mistaken for an avionics component failure?", "choices": ["Avionics cooling has no relationship to equipment performance", "Insufficient cooling airflow can cause thermal shutdowns or faults that mimic an actual avionics failure", "Avionics bays never require cooling", "Blocked cooling inlets only affect cabin pressurization, not avionics"], "answer": 1}
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
      {"heading": "Common Failure Modes", "body": "<b>Detonation</b> (uncontrolled explosive combustion, often from low-octane fuel, over-lean mixture, or excessive heat) can destroy pistons and rings quickly. <b>Pre-ignition</b> (combustion starting before the spark from a hot spot like a glowing deposit) causes similar damage. <b>Shock cooling</b> from rapid power reduction can crack cylinders. Recognizing detonation/pre-ignition symptoms (rough running, high CHT, power loss) early prevents catastrophic engine damage."}, {"heading": "Detonation and Pre-Ignition Distinguishing Characteristics", "body": "Detonation is an uncontrolled, explosive combustion of the fuel-air mixture occurring after normal spark ignition, typically caused by excessive cylinder temperature, low-octane fuel for the engine's compression ratio, or overly lean mixture at high power, producing a characteristic knocking sound and rapid cylinder head temperature rise that can cause piston and cylinder damage within a short time if not corrected. Pre-ignition is combustion beginning before the spark plug fires, usually caused by a hot spot in the combustion chamber such as a glowing carbon deposit or damaged spark plug, and tends to cause even more severe and rapid engine damage than detonation since combustion timing is essentially uncontrolled. Both conditions require immediate power reduction and mixture/cooling correction if suspected in flight, and post-flight inspection after a suspected detonation or pre-ignition event should include cylinder borescope inspection and compression testing, since internal damage may not be externally visible."}, {"heading": "Cylinder Compression Testing and Interpretation", "body": "Cylinder compression testing evaluates the mechanical health of a reciprocating engine's cylinders by measuring how well each cylinder holds pressure, revealing problems with valve seating, piston ring sealing, or cylinder wall condition before they progress to more serious failures. A differential compression test, the method most commonly used on certificated aircraft engines, applies regulated shop air to the cylinder at top-dead-center compression stroke and measures how much pressure the cylinder holds compared to the input pressure, with excessive leakage indicating a sealing problem, and listening at the exhaust, intake, and case breather while the test is performed helps identify whether leakage is past exhaust valves, intake valves, or piston rings respectively. A single low-compression reading should prompt further investigation rather than immediate cylinder removal, since the specific leakage path identified through listening often points toward a more targeted repair, such as simply lapping a valve, rather than requiring full cylinder replacement. Compression readings should also be tracked and trended over time rather than evaluated only against a pass/fail threshold at a single point, since a gradually declining trend can reveal developing wear before it reaches a level requiring immediate corrective action."},
    {"heading": "Valve Overlap and Its Effect on Engine Breathing", "body": "Valve overlap is the brief period near top dead center at the end of the exhaust stroke and beginning of the intake stroke when both the exhaust and intake valves are open simultaneously, allowing the incoming fresh air-fuel charge to help push out remaining exhaust gas and improving cylinder scavenging, particularly beneficial at higher RPM where gas flow momentum assists this effect. Excessive valve overlap (from incorrect valve timing or worn/stretched valve train components) can allow some fresh charge to escape out the exhaust before the exhaust valve closes, wasting fuel and reducing low-speed torque, while insufficient overlap due to incorrect timing reduces the scavenging benefit and can leave more residual exhaust gas diluting the fresh charge, most noticeable as reduced high-RPM power. Because valve timing is established by the camshaft and its correct relationship to crankshaft position, verifying camshaft timing marks and gear/chain alignment during any engine work involving valve train disassembly is essential, since correct valve overlap depends entirely on that timing relationship being correct."},
    {"heading": "Volumetric Efficiency and Its Effect on Engine Power Output", "body": "Volumetric efficiency describes how effectively a reciprocating engine fills its cylinders with the fuel-air charge compared to the theoretical maximum the cylinder displacement could hold at ambient conditions, and it is a major factor determining how much power an engine can actually produce relative to its displacement. Several factors reduce volumetric efficiency below the theoretical ideal, including intake manifold restrictions and bends that create pressure drops, valve timing that does not perfectly match the engine's operating speed range, residual exhaust gas remaining in the cylinder from the previous cycle that displaces incoming fresh charge, and intake air heating from contact with hot engine components before it even reaches the cylinder. Naturally aspirated engines typically achieve volumetric efficiencies noticeably below one hundred percent across most of their operating range, while properly designed turbocharging or supercharging systems can push volumetric efficiency above one hundred percent by force-feeding charge into the cylinder at higher than ambient pressure, which is precisely why turbocharged engines can produce significantly more power from the same displacement. Technicians troubleshooting an engine with unexplained power loss should consider volumetric efficiency factors such as a partially restricted air filter, a leaking intake gasket allowing unmetered air entry, or exhaust system restrictions that impede scavenging, since these degrade volumetric efficiency and reduce power even when ignition and fuel metering systems are functioning correctly. Altitude also reduces volumetric efficiency's real-world power effect because lower ambient air density means each intake stroke draws in a smaller mass of air even at identical volumetric efficiency percentage, which is the fundamental reason naturally aspirated engines lose power with increasing altitude."}],
    "quiz": [ {"q": "During a differential compression test, what does hearing air leakage at the exhaust pipe most likely indicate?", "choices": ["A problem with the piston rings", "A leakage path past the exhaust valve seating", "A problem with the intake manifold only", "Normal, expected behavior requiring no further investigation"], "answer": 1}, {"q": "What is the key difference between detonation and pre-ignition in a reciprocating engine?", "choices": ["They are identical conditions with different names", "Detonation occurs after normal spark ignition; pre-ignition begins combustion before the spark fires, often from a hot spot", "Pre-ignition only occurs at low power settings", "Detonation never causes engine damage"], "answer": 1, "explain": "Detonation is explosive combustion occurring after normal spark timing, while pre-ignition begins combustion before the spark fires, typically from a hot spot like a glowing carbon deposit, and tends to cause more severe damage."},
      {"q": "Crank revolutions per power stroke (per cyl):", "choices": ["1","2","4","0.5"], "answer": 1, "explain": "4-stroke: one power stroke every 720 deg (2 full revolutions)."},
      {"q": "Compression ratio:", "choices": ["Bore/stroke","V(BDC)/V(TDC)","Intake P/exhaust P","Power/weight"], "answer": 1, "explain": "CR = total volume at BDC divided by clearance volume at TDC."},
      {"q": "Why dual magnetos?", "choices": ["More power only","Redundancy + better combustion","Less weight","Legal only"], "answer": 1, "explain": "Redundancy (one failing is survivable) plus two sparks give more complete combustion."},
      {"q": "Carb icing can occur in:", "choices": ["Freezing only","Above 80F only","Warm humid (50-70F, moist)","Altitude only"], "answer": 2, "explain": "Venturi + fuel evaporation drops carb temp 60F+ below ambient. Common at 50-70F with humidity."},
      {"q": "Detonation in a reciprocating engine is most commonly caused by:", "choices": ["Overly rich mixture and low RPM", "Low-octane fuel, excessive heat, or an over-lean mixture", "Cold weather starts", "Normal cruise power settings"], "answer": 1, "explain": "Detonation results from conditions that raise cylinder temperature/pressure beyond the fuel's ability to burn smoothly - low octane fuel, excess heat, or over-lean mixtures are common causes."},
      {"q": "Missing baffles cause:", "choices": ["Over-cooling","Localized overheating/failure","Oil leaks only","No effect"], "answer": 1, "explain": "Baffles direct cooling air. Missing = no directed airflow = hot spots = cracking."},
    {"q": "What is the benefit of valve overlap during the exhaust-to-intake transition near top dead center?", "choices": ["It has no effect on engine performance at any RPM", "It allows the incoming fresh charge to help push out remaining exhaust gas, improving cylinder scavenging, especially at higher RPM", "It only matters for diesel engines, not reciprocating aircraft engines", "Valve overlap always reduces engine performance and should be minimized"], "answer": 1},
    {"q": "Why can turbocharged engines achieve volumetric efficiency above one hundred percent while naturally aspirated engines cannot?", "choices": ["Turbocharging force-feeds the charge into the cylinder at higher than ambient pressure, unlike naturally aspirated intake", "Turbocharged engines have larger cylinder displacement than naturally aspirated engines by definition", "Volumetric efficiency above one hundred percent is not physically possible in any engine", "Naturally aspirated engines always have better valve timing than turbocharged engines"], "answer": 0}
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
      {"heading": "Engine Health Monitoring", "body": "<b>Trend monitoring</b> tracks EGT, N1/N2, oil pressure/temp, and fuel flow over time to catch gradual deterioration before it becomes a failure. A slow, steady <b>EGT rise</b> at a given power setting over many flights often signals compressor or turbine efficiency loss (erosion, fouling) long before any single reading would exceed a limit. Borescope inspections combined with trend data give the clearest picture of internal engine condition without teardown."}, {"heading": "Turbine Engine Start Cycle Fuel and Ignition Sequencing", "body": "Turbine engine starting requires precise sequencing of starter engagement (to bring the engine to a minimum rotational speed), fuel introduction (timed to begin only after adequate airflow is established through the compressor), and ignition activation (timed to ignite the fuel-air mixture as it enters the combustor), with FADEC or electronic engine control systems managing this sequence automatically on modern engines. A start sequence fault at any stage, such as fuel being introduced too early (before adequate airflow), too much fuel being scheduled (causing a hot start with excessive turbine temperature), or ignition failing to activate at the right time (causing a hung start or no-light condition), produces characteristically different symptoms that experienced technicians and pilots learn to recognize from the start sequence indications. Understanding the normal sequence and timing allows a technician to interpret which specific stage of the start sequence a reported anomaly occurred in, narrowing troubleshooting focus rather than treating every abnormal start as a generic fault."}, {"heading": "N1 and N2 Spool Speed Relationships and Indications", "body": "Twin-spool and triple-spool turbine engines have independently rotating compressor-turbine assemblies (commonly designated N1 for the low-pressure spool and N2 for the high-pressure spool, with N3 on triple-spool designs), each operating at its own speed determined by the aerodynamic and mechanical loads on that particular spool. N1 speed is often the primary parameter used for setting thrust on many turbofan engines since it correlates closely with the fan's air-moving capacity and thus thrust output, while N2 speed relates more to the core engine's combustion and gas generation process. Understanding the normal relationship between N1 and N2 for a specific engine model helps mechanics recognize abnormal indications, such as an N2 that is not responding proportionally to N1 changes, which could indicate a core engine mechanical problem, sensor fault, or FADEC scheduling issue rather than a normal operating variation. During troubleshooting, comparing actual N1/N2 relationships against the expected relationship documented in the engine's performance charts, rather than relying on general intuition about typical engine behavior, provides the most reliable basis for determining whether an observed indication reflects a genuine anomaly."},
    {"heading": "Thrust Reverser Types and Deployment Sequencing", "body": "Thrust reversers redirect engine exhaust flow forward to decelerate the aircraft during landing rollout or aborted takeoff. Turbojet and low-bypass turbofan installations often use target-type (clamshell) reversers that pivot aft-fuselage-mounted doors into the exhaust path to block and redirect gas flow forward. High-bypass turbofans typically use cascade-type reversers in the fan cowl, where translating sleeves slide aft to expose cascade vanes while blocker doors simultaneously close off the normal fan duct path, redirecting the bulk of fan bypass air (which produces most of the thrust) forward through the cascades. Deployment is sequenced and interlocked so reversers can only be commanded when the aircraft is on the ground (via a ground/air logic input, often from landing gear or wheel-speed sensors) and only after the translating sleeve is confirmed unlocked; thrust lever position is similarly interlocked to prevent reverse thrust selection in flight. Maintenance inspection focuses on actuator and drive system condition, sleeve track and roller wear, blocker door seal condition, and functional testing of the position sensors and interlock logic, since an inadvertent in-flight deployment or a reverser that fails to stow is a critical safety hazard."},
    {"heading": "Turbine Blade Internal Cooling Methods and Air Passage Design", "body": "Modern turbine engines operate with gas temperatures at the turbine inlet that can exceed the melting point of the blade alloys themselves, which is possible only because turbine blades, particularly in the high-pressure turbine section, incorporate internal cooling passages that route relatively cooler compressor bleed air through the blade interior to keep metal temperature within the alloy's safe operating range despite the much hotter surrounding gas flow. Internal convection cooling routes bleed air through serpentine passages cast into the blade interior during manufacture, absorbing heat from the blade walls as the air travels through and exits at the blade tip or trailing edge, while film cooling adds rows of small holes on the blade's external surface that allow a thin layer of cooler air to form a protective film over the hot external surface, reducing direct heat transfer from the combustion gas to the blade material. Some advanced blade designs incorporate additional features such as internal turbulence-promoting ribs that increase the cooling air's contact with internal passage walls, improving heat transfer efficiency without requiring a proportionally larger cooling airflow, since cooling air diverted from the compressor represents a direct efficiency penalty on overall engine performance that engine designers work to minimize while still providing adequate cooling. Because cooling passage geometry is extremely intricate and often includes passages too small and complex to inspect visually from outside the blade, borescope inspection of the blade's external film cooling holes for blockage from deposits or coating material is one of the few direct inspection methods available in the field, and any significant blockage detected can indicate reduced cooling effectiveness that increases the risk of localized overheat damage even if the engine's overall EGT indication appears normal. Damage to the thermal barrier coating applied over many turbine blades, which provides an additional insulating layer beyond the internal cooling itself, is a serious finding since coating loss exposes the underlying blade metal directly to combustion gas temperatures the base alloy alone was never intended to withstand for extended periods."}],
    "quiz": [ {"q": "On many turbofan engines, why is N1 (low-pressure spool speed) often used as the primary parameter for setting thrust?", "choices": ["N1 has no relationship to thrust output", "N1 correlates closely with the fan's air-moving capacity, which directly relates to the thrust produced", "N2 is always used instead of N1 for thrust setting", "Thrust setting has no relationship to spool speeds"], "answer": 1}, {"q": "Why is precise sequencing of starter engagement, fuel introduction, and ignition critical during turbine engine starting?", "choices": ["Sequencing has no real effect on start success", "Fuel introduced too early or ignition mistimed can cause hot starts, hung starts, or no-light conditions", "All turbine engines start identically regardless of sequence", "Only the starter matters; fuel and ignition timing is irrelevant"], "answer": 1, "explain": "Each stage of the start sequence must occur at the right time; mistiming fuel introduction or ignition can cause characteristic fault conditions like hot starts, hung starts, or failure to light."},
      {"q": "Turbine combustion is:", "choices": ["Intermittent","Continuous","Only during start","Cyclic"], "answer": 1, "explain": "Gas turbines burn fuel continuously. All sections operate simultaneously."},
      {"q": "Most common on airliners:", "choices": ["Turbojet","Turboprop","Turbofan","Turboshaft"], "answer": 2, "explain": "Turbofans: bypass air provides quiet, efficient thrust at high bypass ratios."},
      {"q": "Hot start means:", "choices": ["EGT exceeds limit during start","Runs too cool","Oil overheats","Normal warmup"], "answer": 0, "explain": "Temperature exceeds limits during start - too much fuel vs airflow. Can damage hot section."},
      {"q": "Igniters used:", "choices": ["Continuously","Start and continuous-ignition mode only","Never after first start","To cool combustor"], "answer": 1, "explain": "Once lit, combustion is self-sustaining. Igniters fire only for start and CI mode."},
      {"q": "A gradual, steady rise in EGT at a constant power setting over many flights most likely indicates:", "choices": ["A normal break-in effect with no concern", "Slowly developing compressor or turbine efficiency loss", "A faulty EGT gauge only", "Overly rich fuel scheduling by design"], "answer": 1, "explain": "A slow upward trend in EGT at the same power setting typically reflects gradually declining internal engine efficiency (erosion, fouling, wear) and warrants investigation via trend data and borescope."},
      {"q": "Chip detectors indicate:", "choices": ["Normal ops","Metal wear - investigate","Low oil","Over-temp"], "answer": 1, "explain": "Magnetic plugs capture ferrous particles = internal wear = investigate/overhaul."},
    {"q": "On a high-bypass turbofan with a cascade-type thrust reverser, what happens when the reverser is deployed?", "choices": ["The core exhaust nozzle physically rotates 180 degrees", "Translating sleeves slide aft exposing cascade vanes while blocker doors redirect fan bypass air forward", "The propeller blades reverse pitch", "Only the engine core airflow is reversed, bypass air is unaffected"], "answer": 1},
    {"q": "Why do modern turbine engines require internal blade cooling despite gas temperatures that can exceed the blade alloy's melting point?", "choices": ["Internal cooling passages route compressor bleed air through the blade to keep metal temperature within the alloy's safe range despite hotter surrounding gas", "Turbine blade alloys never actually experience temperatures near their melting point in any engine", "Cooling air passages exist only to reduce blade weight, not for thermal management", "Film cooling and internal cooling serve identical functions and only one method is ever used per engine"], "answer": 0}
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
    , {"heading": "Propeller Balancing", "body": "Propeller vibration causes premature wear on the engine, accessories, and airframe, so both static and dynamic balancing are performed during overhaul and periodically in service. Static balancing checks that the prop balances horizontally about its hub axis with no heavy blade, while dynamic balancing uses electronic vibration analysis equipment with the engine running to identify and correct out-of-balance conditions by adding or removing small balance weights. Track and balance procedures must follow the propeller manufacturer's specific tolerances, and excessive vibration that cannot be resolved by balancing may indicate a bent blade, damaged hub, or engine mount issue requiring further investigation."}, {"heading": "Propeller De-Ice and Anti-Ice System Function", "body": "Propeller ice protection systems use either electrically heated elements bonded to the blade leading edge (cycling on and off in a timed sequence to shed ice without excessive power draw) or, on some older designs, alcohol-based fluid anti-ice systems that flow de-icing fluid through slinger rings to the blade surface. Electrically heated propeller de-ice systems require verification of proper element resistance and cycling timer function, since a failed heating element on one blade while others function normally can create an aerodynamic imbalance from asymmetric ice accumulation, in addition to the obvious loss of ice protection on that blade. Technicians troubleshooting propeller ice protection complaints must check both the electrical supply (slip rings or brushes that transfer power from the stationary airframe to the rotating propeller) and the heating elements themselves, since slip ring wear or brush contact issues are a common cause of intermittent or blade-specific ice protection failures."}, {"heading": "Propeller Track and Blade Angle Verification", "body": "Propeller track measures whether all blades on a multi-blade propeller sweep through the same rotational plane, verified by measuring the distance from a fixed reference point to a specific point on each blade as the propeller is rotated through a full revolution, with excessive track deviation indicating a bent blade, improperly seated blade in the hub, or hub damage that must be corrected before the propeller is considered airworthy. Blade angle verification, checking that each blade is set to the correct pitch angle specified by the propeller manufacturer, uses a specialized protractor or digital angle gauge referenced to a specific point on the blade profile, and blade angle errors between blades on the same propeller (even if each individual blade seems close to the target) can cause vibration and uneven thrust distribution across the propeller disk. Both track and blade angle checks are typically performed together during propeller installation, after any blade removal/reinstallation, or when investigating a vibration complaint, since either fault alone can produce vibration symptoms that might otherwise be attributed to engine mounting, balance, or other unrelated causes. Mechanics must follow the specific propeller manufacturer's procedure and tolerances exactly, since track and blade angle tolerances vary between propeller models and are not universally standardized."},
    {"heading": "Propeller Blade Twist and Airfoil Design Along the Span", "body": "Propeller blades are twisted along their length (higher blade angle near the hub, progressively lower blade angle toward the tip) because the blade's rotational speed, and therefore its relative airspeed through the air, increases from hub to tip; without this twist, the blade tip would operate at a very different angle of attack than the root for a given aircraft airspeed and rotational speed, causing inefficient or even stalled airflow at some point along the blade span. This twist is designed into the blade during manufacture and cannot be field-adjusted; a bent, twisted, or repaired blade that alters this designed twist distribution changes the aerodynamic loading along the blade in ways that can cause vibration, reduced efficiency, or in severe cases, dangerous imbalance, which is why blade straightening or twist correction is a specialized repair requiring specific approved data, not something performed by field judgment even by an experienced technician. Blade airfoil cross-section shape also typically varies from root to tip to match the different local operating conditions, further reinforcing why unauthorized blade reshaping or repair beyond approved limits is prohibited."},
    {"heading": "Propeller Efficiency and Advance Ratio Relationship to Airspeed", "body": "Propeller efficiency describes the ratio of useful thrust power produced to the shaft power delivered by the engine, and this efficiency varies significantly with the propeller's advance ratio, a dimensionless parameter relating the aircraft's forward airspeed to the propeller's rotational speed and diameter. At low advance ratios, such as during static ground operation or slow flight at high RPM, a fixed-pitch propeller optimized for cruise operates inefficiently because the blade angle of attack relative to the resultant airflow is far from its optimal value, which is why static thrust per horsepower is noticeably lower than cruise thrust per horsepower for most propeller and engine combinations. As advance ratio increases with rising airspeed at constant RPM, a fixed-pitch propeller's efficiency initially rises toward a peak and then falls off as the blade angle of attack becomes too shallow or even negative at very high advance ratios, which is why a fixed-pitch propeller is inherently a compromise optimized for one flight regime, typically either climb or cruise, but not both simultaneously. Constant-speed propellers address this limitation by continuously adjusting blade pitch angle to maintain a favorable local angle of attack across a wide range of advance ratios, allowing the propeller to maintain efficiency across takeoff, climb, and cruise conditions by trading blade angle for the changing relationship between forward speed and rotational speed. This is why a constant-speed propeller installation allows selection of a higher RPM for takeoff and climb, where the flatter blade angle needed at low advance ratio produces good thrust, then a lower RPM for cruise, where the propeller is repitched to a coarser angle appropriate for the higher advance ratio at cruise airspeed, together delivering meaningfully better overall efficiency than any single fixed pitch setting could provide across the full flight profile."}],
    "quiz": [ {"q": "What does excessive propeller blade track deviation typically indicate?", "choices": ["Normal wear that requires no action", "A bent blade, improperly seated blade in the hub, or hub damage", "Only a cosmetic issue with no airworthiness implications", "A fuel system malfunction unrelated to the propeller"], "answer": 1}, {"q": "What problem can result if one blade's heating element fails while others on the same propeller function normally?", "choices": ["No problem, other blades fully compensate", "Aerodynamic imbalance from asymmetric ice accumulation on that blade", "The propeller automatically shuts down", "Only a cosmetic issue with no operational effect"], "answer": 1, "explain": "If one blade fails to shed ice while others do, the resulting asymmetric ice accumulation can create an aerodynamic and mass imbalance across the propeller."}, {"q": "What does dynamic propeller balancing use to identify out-of-balance conditions?", "choices": ["A visual inspection only", "Electronic vibration analysis equipment with the engine running", "Static weighing on a bench", "Sound level meters"], "answer": 1, "explain": "Dynamic balancing uses vibration analysis equipment while the engine runs to detect and correct out-of-balance conditions that static balancing alone cannot catch."},
      {"q": "Constant-speed prop changes ___ to hold RPM:", "choices": ["Engine power","Blade angle","Diameter","Fuel flow"], "answer": 1, "explain": "Governor adjusts blade angle (pitch) to maintain selected RPM."},
      {"q": "Feathering means:", "choices": ["Blades to 90 deg (min drag)","Removing prop","Blades flat","Reversing"], "answer": 0, "explain": "Feathering = edge-on to airstream, minimum drag on a shut-down engine."},
      {"q": "After prop strike:", "choices": ["Inspect prop only","Teardown prop AND engine","Continue if looks OK","Replace prop only"], "answer": 1, "explain": "Massive forces transmit through crankshaft - mandatory teardown of prop, engine, accessories."},
      {"q": "Primary turbine limit instrument:", "choices": ["N1","Fuel flow","ITT/EGT","Oil pressure"], "answer": 2, "explain": "ITT/EGT is THE critical limit - exceeding it damages hot-section components."},
      {"q": "Green-yellow-red arcs:", "choices": ["Fuel types","Normal-caution-never exceed","Oil grades","Temp only"], "answer": 1, "explain": "Standard markings: green=normal, yellow=caution, red line=never exceed."},
    {"q": "Why are propeller blades manufactured with twist along their length rather than a uniform blade angle from root to tip?", "choices": ["Twist is purely a manufacturing artifact with no aerodynamic purpose", "Rotational speed and relative airspeed increase from hub to tip, so twist maintains an appropriate angle of attack along the entire blade span", "All propeller blades are actually untwisted and appear twisted only due to an optical illusion", "Twist only matters for propellers operating in reverse pitch"], "answer": 1},
    {"q": "Why do constant-speed propellers achieve better overall efficiency across a flight profile than fixed-pitch propellers?", "choices": ["They continuously adjust blade pitch to maintain a favorable angle of attack across a wide range of advance ratios", "They eliminate the need for any RPM changes during flight", "They always produce more static thrust than any fixed-pitch propeller regardless of advance ratio", "They operate independently of airspeed and rotational speed relationships"], "answer": 0}
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
    , {"heading": "Airworthiness Directives Compliance Tracking", "body": "Airworthiness Directives (ADs) are legally enforceable regulations issued by the FAA to correct unsafe conditions found in aircraft, engines, propellers, or appliances, and compliance is mandatory unless an alternative means of compliance (AMOC) is approved. Recurring ADs require tracking of compliance intervals (flight hours, calendar time, or cycles) in maintenance records, and a lapsed recurring AD renders the aircraft unairworthy even if the aircraft otherwise appears sound. Technicians must verify AD applicability by model, serial number, and configuration, and document compliance method, date, and next due interval in the permanent aircraft records."}, {"heading": "Major vs. Minor Alterations and Repairs", "body": "FAA regulations distinguish between major and minor alterations/repairs based on their potential effect on airworthiness, weight and balance, structural strength, performance, or flight characteristics, with major alterations/repairs requiring FAA Form 337 documentation and, in many cases, approval via a Supplemental Type Certificate (STC), field approval, or other approved data before the work can be performed. Minor alterations/repairs, while still requiring proper documentation in the aircraft records, do not require the same level of FAA approval process, but the determination of major versus minor is not always obvious and requires reference to specific guidance (such as AC 43-210 or type-specific data) rather than technician judgment alone in ambiguous cases. Misclassifying a major alteration as minor is a common and serious documentation error, since it can result in an aircraft being represented as airworthy when the alteration was never properly approved, creating both a safety and legal liability issue."}, {"heading": "Airworthiness Directives Compliance Tracking Methods", "body": "Airworthiness Directive (AD) compliance tracking requires a systematic method to ensure every applicable AD is identified, its compliance method and interval are correctly determined, and evidence of compliance is properly documented and retrievable, since an aircraft operating with an overdue AD is not legally airworthy regardless of how well it otherwise appears to be maintained. Many operators use dedicated AD tracking software or a maintenance tracking program's built-in AD module that flags upcoming due dates based on the aircraft's specific configuration, serial numbers of installed components, and operating hours/cycles, reducing reliance on manual review of the full AD list for every applicability determination. When a new AD is issued, mechanics or the person responsible for airworthiness must determine applicability carefully, checking not just the aircraft model listed but also specific serial number ranges, installed equipment, or modification status that may exclude an otherwise similar aircraft from the AD's applicability. Terminating action ADs, which permanently resolve a recurring inspection requirement once a specific modification or replacement is performed, must be tracked distinctly from ADs requiring ongoing recurring compliance, since confusing these categories can result in either unnecessary repeated inspections or, more seriously, missing an ongoing requirement that was mistakenly treated as terminated."},
    {"heading": "Preventive Maintenance Items Owners and Pilots May Perform", "body": "14 CFR Part 43 Appendix A lists specific preventive maintenance tasks that an aircraft owner/operator holding at least a private pilot certificate (and not requiring an A&P certificate) may legally perform on an aircraft they own or operate, such as replacing safety wire, servicing landing gear wheel bearings, replacing bulbs and reflectors, and other similarly limited-scope tasks, provided the aircraft is not operated for hire. Any preventive maintenance performed under this provision must still be logged in the aircraft records with a description of the work, the date, and the signature and certificate number of the person performing it, and returned to service per the same recordkeeping requirements that apply to any other maintenance entry. A&P mechanics and IAs should be familiar with this owner-performed maintenance provision because they may encounter aircraft where some maintenance history reflects legitimate owner-performed preventive maintenance rather than certificated mechanic work, and must be able to recognize whether logged owner-performed work falls within the Appendix A scope or whether it exceeded the owner's authorized privileges."},
    {"heading": "Repair Station Ratings and Scope of Authorized Work", "body": "Certificated repair stations operate under specific ratings that define the precise scope of maintenance, preventive maintenance, or alteration work they are authorized to perform, and a repair station may only perform work falling within its issued ratings and the specific limitations listed on its operations specifications. Ratings are typically organized by class, such as airframe, powerplant, radio, instrument, accessory, and propeller classes, and within each class a repair station may hold a limited rating restricting it to specific makes and models or a broader rating covering entire classes of articles, with the exact scope documented in the repair station's capability list that must be kept current and available for reference. A repair station accepting work beyond its authorized ratings, even informally or as a favor, exposes both the repair station and potentially the returning-to-service technician to regulatory violation, since the work was never within the scope the FAA evaluated when issuing the certificate and surveilling the station's quality system. When a repair station wishes to expand its capability, such as adding a new aircraft make and model to its airframe rating, it must satisfy the FAA that it has the necessary housing, equipment, technical data, and qualified personnel for that specific addition before the capability list can be amended, a process that involves genuine demonstration of capability rather than simple paperwork. Technicians working within a repair station must be familiar with which specific ratings and capability list entries apply to the work they are performing, since exceeding the station's authorized scope on a work order, even if the individual technician is personally skilled enough to perform the task, does not make the work legally authorized under the repair station's certificate."}],
    "quiz": [ {"q": "Why must mechanics carefully verify an Airworthiness Directive's specific applicability criteria, not just the general aircraft model listed?", "choices": ["All ADs apply universally to every aircraft of a given model regardless of configuration", "Some ADs specify serial number ranges, installed equipment, or modification status that can exclude an otherwise similar aircraft from applicability", "Applicability determination is unnecessary once an AD is issued", "AD applicability never depends on aircraft-specific details"], "answer": 1}, {"q": "What is required for a major alteration or repair that is not required for a minor one?", "choices": ["Nothing, the requirements are identical", "FAA Form 337 documentation and approval via STC, field approval, or other approved data", "Only a verbal notification to the FAA", "No documentation whatsoever"], "answer": 1, "explain": "Major alterations and repairs require FAA Form 337 documentation and approval through an STC, field approval, or other approved data, unlike minor alterations which have simpler documentation requirements."}, {"q": "What happens if a recurring Airworthiness Directive compliance interval lapses?", "choices": ["Nothing, as long as the aircraft looks fine", "The aircraft becomes unairworthy even if it appears mechanically sound", "The AD is automatically waived", "Only a logbook note is needed"], "answer": 1, "explain": "ADs are legally mandatory; a lapsed recurring AD compliance interval renders the aircraft unairworthy regardless of its apparent physical condition."},
      {"q": "A pilot may perform:", "choices": ["Annual inspections","Structural repairs","Listed preventive maintenance on own aircraft","Engine overhaul"], "answer": 2, "explain": "Pilots: only specific preventive maintenance listed in Part 43 App A(c) on own aircraft."},
      {"q": "Which form records major repairs?", "choices": ["Form 8610-2","Form 337","Form 8710","AD form"], "answer": 1, "explain": "FAA Form 337 documents major repairs and alterations."},
      {"q": "43.9 entry requires all EXCEPT:", "choices": ["Description","Date","Stock price","Signature+cert# approving RTS"], "answer": 2, "explain": "The 4 elements: description, date, performer name, signature+cert#+kind approving RTS."},
      {"q": "An AD is:", "choices": ["Optional guidance","Legally mandatory","Pilot advisory","Training doc"], "answer": 1, "explain": "ADs are mandatory - correct unsafe conditions. Non-compliance = unairworthy."},
      {"q": "A&P certificate expires:", "choices": ["Every 2 years","Every 5 years","Never (exercise or re-test)","At age 65"], "answer": 2, "explain": "Never expires, but must exercise privileges within 6mo of each 24mo period or re-test."},
    {"q": "What must an aircraft owner/pilot do when they perform a preventive maintenance task authorized under 14 CFR Part 43 Appendix A?", "choices": ["No documentation is required since these are minor tasks", "Log the work in the aircraft records with a description, date, and their signature and certificate number, per standard recordkeeping requirements", "Have an A&P mechanic re-perform and re-document the same task", "Preventive maintenance may only be performed by certificated A&P mechanics"], "answer": 1},
    {"q": "What defines the specific scope of maintenance work a certificated repair station is authorized to perform?", "choices": ["Its issued ratings by class and the specific limitations documented in its capability list and operations specifications", "The personal skill level of any individual technician on staff", "Repair stations are authorized to perform any maintenance task without any scope limitation", "Only the size of the repair station's physical facility"], "answer": 0}
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

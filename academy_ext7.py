"""Aviation Maintenance Academy - Wave 4 content pack.
Adds 5 new modules balanced across tracks. Merged in academy_data.py.
"""

EXT7_MODULES = [
  {
    "id": "precision_tools", "title": "Precision Measurement & Shop Tools", "track": "general", "icon": "&#x1F4CF;",
    "sections": [
      {"heading": "Measuring Tools", "body": "<b>Steel rule</b> for rough measurements; <b>calipers</b> (vernier, dial, digital) for +/-0.001 in; <b>micrometers</b> for precise outside/inside/depth readings; <b>dial indicators</b> for runout, deflection, and alignment checks; <b>feeler gauges</b> for small, exact gaps (e.g., valve clearance, control surface rigging)."},
      {"heading": "Reading a Micrometer", "body": "A standard 0-1 in micrometer: each full turn of the thimble = 0.025 in (25 thousandths). The sleeve shows 0.025 in graduations; the thimble shows 0.001 in graduations. Add sleeve reading + thimble reading for total. Digital micrometers eliminate the mental math but still require zero-checks before use."},
      {"heading": "Torque Wrenches", "body": "Three common types: <b>beam</b> (simple, no calibration drift), <b>click-type</b> (must be reset to lowest setting after use to preserve calibration), and <b>digital</b> (direct readout, some log data). All torque wrenches require periodic calibration per manufacturer/shop schedule - an out-of-cal wrench can under- or over-torque fasteners, risking loosening or thread damage."},
      {"heading": "Calibration & Tool Control", "body": "Precision tools carry calibration due dates/stickers; using an expired tool is a quality escape. <b>Tool control programs</b> (shadow boards, sign-out logs, FOD accountability) ensure every tool is accounted for before closing up an aircraft - a missing tool in a control surface or engine bay is a safety-of-flight issue."}
    ],
    "quiz": [
      {"q": "One full turn of a standard 0-1 in micrometer thimble equals how much?", "choices": ["0.001 in","0.010 in","0.025 in","0.100 in"], "answer": 2, "explain": "One full thimble revolution on a standard mic = 0.025 in (25 thousandths)."},
      {"q": "Why must a click-type torque wrench be reset to its lowest setting after use?", "choices": ["To save battery","To preserve internal spring calibration","It is required by TSA","It prevents rust"], "answer": 1, "explain": "Leaving a click-type wrench set at a high torque keeps the internal spring compressed, causing calibration drift over time."},
      {"q": "What tool is best for checking valve clearance?", "choices": ["Dial indicator","Feeler gauge","Vernier caliper","Steel rule"], "answer": 1, "explain": "Feeler gauges are thin, precisely-sized blades used to check small, exact gaps like valve clearance."},
      {"q": "What is the purpose of a shadow board in tool control?", "choices": ["Decoration","Instantly show a missing tool by its empty outline","Store spare parts","Track employee hours"], "answer": 1, "explain": "A shadow board outlines each tool's shape so a missing tool is immediately obvious at a glance."},
      {"q": "Using a torque wrench past its calibration due date is best described as:", "choices": ["Acceptable if it 'feels right'","A quality/safety escape - do not use","Required for old aircraft","Only a problem on turbine engines"], "answer": 1, "explain": "An out-of-calibration torque wrench may not deliver accurate values, risking improperly torqued fasteners."}
    ]
  },
  {
    "id": "flight_controls_rigging", "title": "Flight Controls & Rigging", "track": "airframe", "icon": "&#x1F6E9;",
    "sections": [
      {"heading": "Primary & Secondary Controls", "body": "<b>Primary</b>: ailerons (roll), elevator (pitch), rudder (yaw). <b>Secondary</b>: flaps, slats, spoilers, trim tabs, and speedbrakes. Control surfaces are moved by cables, pushrods, torque tubes, or fly-by-wire actuators, depending on aircraft design."},
      {"heading": "Cable Rigging Basics", "body": "Cable systems use turnbuckles for tensioning; correct <b>cable tension</b> (checked with a tensiometer, corrected for ambient temperature) is critical - too loose causes slack/lag, too tight causes excess friction and wear. Cables route through fairleads and pulleys; inspect for fraying, corrosion, and proper pulley alignment."},
      {"heading": "Rigging Checks", "body": "Rigging verifies control surfaces travel the correct degrees of deflection in each direction and that controls are <b>neutral</b> when the cockpit control is centered. Travel is checked with a protractor/inclinometer against the AMM/SRM-specified range. Symmetry between left/right control surfaces (e.g., ailerons) is essential for balanced flight."},
      {"heading": "Autopilot & Trim Interface", "body": "Many aircraft route autopilot servo inputs and electric trim through the same cable/pushrod runs as manual controls, using clutches or slip mechanisms so the pilot can always override. Always verify freedom of movement (no binding) through full range after any rigging work, and complete a control-check/duplicate-inspection per maintenance program requirements."}
    ],
    "quiz": [
      {"q": "Which of these is a PRIMARY flight control?", "choices": ["Flap","Elevator","Spoiler","Trim tab"], "answer": 1, "explain": "Elevator (pitch), ailerons (roll), and rudder (yaw) are the three primary flight controls."},
      {"q": "What tool checks cable tension?", "choices": ["Feeler gauge","Tensiometer","Dial indicator","Micrometer"], "answer": 1, "explain": "A tensiometer measures cable tension, which must be corrected for ambient temperature per the applicable chart."},
      {"q": "What does a rigging check verify besides correct travel range?", "choices": ["Paint color","Engine RPM","Neutral position when cockpit control is centered","Fuel quantity"], "answer": 2, "explain": "Rigging verifies both correct deflection range AND that surfaces sit neutral when the cockpit control is centered."},
      {"q": "Why do autopilot servos often use a clutch/slip mechanism in the control run?", "choices": ["To save weight","So the pilot can always physically override the autopilot","To reduce cost","To increase speed"], "answer": 1, "explain": "Slip clutches let the autopilot drive the controls while still allowing the pilot to overpower it if needed."},
      {"q": "What must be checked after rigging work before returning the aircraft to service?", "choices": ["Only that the surface moves at all","Full range of motion with no binding, plus required duplicate inspection","Cockpit lighting","Fuel color"], "answer": 1, "explain": "Freedom of movement through the full range and a duplicate/control-check inspection are required after rigging work."}
    ]
  },
  {
    "id": "fire_protection", "title": "Fire & Overheat Detection Systems", "track": "airframe", "icon": "&#x1F525;",
    "sections": [
      {"heading": "Fire Detection Methods", "body": "<b>Thermocouple/thermoswitch</b> systems detect a rate of temperature rise or a fixed threshold; <b>continuous-loop (Kidde/Fenwal-style)</b> sensors detect overheat/fire along their entire length and can pinpoint zones; <b>smoke detectors</b> (photoelectric) protect cargo/lavatory areas; <b>optical (flame) detectors</b> sense UV/IR radiation from flame."},
      {"heading": "Extinguishing Systems", "body": "Engine/APU fire bottles typically use <b>Halon 1301</b> or newer clean agents, discharged into the nacelle/APU compartment on crew command, sometimes with a backup second-shot bottle. Portable cabin extinguishers use Halon, water, or dry chemical depending on the fire class (A/B/C/electrical)."},
      {"heading": "Overheat vs. Fire Warning", "body": "Overheat warnings alert to abnormally high temps before flame is confirmed, while fire warnings indicate an actual detected flame condition - crew procedures and required actions differ (e.g., overheat may allow continued monitoring; a fire warning triggers immediate engine/APU securing and bottle discharge). System test switches allow ground/preflight functional checks."},
      {"heading": "Maintenance & Inspection", "body": "Continuous-loop sensing elements are inspected for chafing, kinks, and secure clamping (they must not touch structure directly, which can cause false readings). Fire bottle pressure/weight is checked against placarded limits; squibs (discharge cartridges) have service-life limits and must be replaced on schedule regardless of use."}
    ],
    "quiz": [
      {"q": "What advantage does a continuous-loop fire detector have?", "choices": ["It never needs testing","It only works in cold weather","It can detect and often pinpoint a fire/overheat anywhere along its length","It replaces all extinguishers"], "answer": 2, "explain": "Continuous-loop systems sense along their entire length, helping pinpoint the affected zone."},
      {"q": "What extinguishing agent has traditionally been used in engine fire bottles?", "choices": ["Water","Halon 1301 or clean agent equivalent","Sand","CO2 only"], "answer": 1, "explain": "Halon 1301 (or approved clean-agent replacements) is the traditional engine/APU fire bottle agent."},
      {"q": "How does an overheat warning differ from a fire warning?", "choices": ["They are identical","Overheat indicates high temp without confirmed flame; fire indicates a detected flame condition","Overheat is only for engines","Fire warnings are always false alarms"], "answer": 1, "explain": "Overheat = abnormal temperature rise; fire = an actual detected flame/fire condition, requiring different crew actions."},
      {"q": "Why must continuous-loop sensing elements avoid touching aircraft structure?", "choices": ["Aesthetics","It can cause false or nuisance warnings due to chafing/short paths","It voids the warranty","It reduces weight"], "answer": 1, "explain": "Chafing or contact with structure can create electrical/thermal paths that trigger false detections."},
      {"q": "What is true about fire bottle discharge squibs (cartridges)?", "choices": ["They never need replacement","They have service-life limits and must be replaced on schedule regardless of use","They are reusable indefinitely","They are only found on turboprops"], "answer": 1, "explain": "Squibs have a shelf/service life and must be replaced on schedule even if never fired."}
    ]
  },
  {
    "id": "prop_governing", "title": "Propeller Governing & Constant-Speed Systems", "track": "powerplant", "icon": "&#x1F300;",
    "sections": [
      {"heading": "Fixed-Pitch vs. Constant-Speed", "body": "A <b>fixed-pitch</b> propeller has one efficient blade angle for a given condition (climb or cruise, not both). A <b>constant-speed</b> propeller uses a governor to vary blade angle automatically, holding a selected RPM across a range of power/airspeed conditions for near-optimal efficiency throughout the flight envelope."},
      {"heading": "Governor Operation", "body": "The governor uses engine-driven flyweights and a pilot valve to direct oil pressure to/from the propeller hub piston. Underspeed causes the governor to decrease pitch (increase RPM tendency); overspeed causes it to increase pitch (decrease RPM tendency) - a classic feedback control loop maintaining the selected RPM."},
      {"heading": "Feathering & Reversing", "body": "<b>Feathering</b> rotates the blades to a near-edge-on angle to minimize drag after an engine failure (common on multi-engine aircraft and turboprops). <b>Reverse pitch</b> rotates blades to a negative angle to produce reverse thrust for braking on landing rollout - common on turboprop transports."},
      {"heading": "Overspeed & Malfunctions", "body": "A propeller <b>overspeed</b> (governor failure, linkage failure) can cause excessive RPM, structural risk, and loss of control authority; many systems have a separate overspeed governor/limiter as backup. Symptoms of governor malfunction include RPM surging, failure to respond to power lever changes, or inability to feather."}
    ],
    "quiz": [
      {"q": "What is the main advantage of a constant-speed propeller over fixed-pitch?", "choices": ["Lower cost","Lighter weight","Near-optimal efficiency across a range of conditions via automatic blade angle change","No maintenance required"], "answer": 2, "explain": "A governor automatically adjusts blade angle to hold RPM, keeping efficiency high across varying power/airspeed."},
      {"q": "In a governor, what happens when the engine tends toward overspeed?", "choices": ["Governor decreases blade angle","Governor increases blade angle to absorb more load and slow RPM","Governor shuts off oil pressure permanently","Nothing happens"], "answer": 1, "explain": "On overspeed tendency, the governor increases pitch (blade angle), increasing load and pulling RPM back down."},
      {"q": "What is the purpose of feathering a propeller?", "choices": ["Increase thrust","Minimize drag after an engine failure","Increase RPM","Improve fuel color"], "answer": 1, "explain": "Feathering turns blades nearly edge-on to the airflow, minimizing drag from a stopped/failed engine."},
      {"q": "What is reverse pitch used for?", "choices": ["Climb performance","Producing reverse thrust for braking on landing rollout","Cruise efficiency","Engine starting"], "answer": 1, "explain": "Reverse pitch rotates blades to a negative angle, producing reverse thrust to help slow the aircraft on rollout."},
      {"q": "What backup system helps protect against a propeller overspeed?", "choices": ["A second, separate overspeed governor/limiter","The fuel gauge","The landing gear","The pitot heat system"], "answer": 0, "explain": "Many constant-speed prop systems include a backup overspeed governor/limiter independent of the primary governor."}
    ]
  },
  {
    "id": "apu_testcell", "title": "APU Systems & Engine Test Procedures", "track": "powerplant", "icon": "&#x2699;",
    "sections": [
      {"heading": "APU Purpose & Operation", "body": "The <b>Auxiliary Power Unit</b> is a small turbine engine (usually tail-mounted) providing electrical power, bleed air (for pneumatics/air conditioning/engine starting), and sometimes hydraulic power on the ground and, on some aircraft, in flight as backup. APUs have their own fire detection/extinguishing, fuel supply, and starting system (often electric)."},
      {"heading": "APU Limitations & Monitoring", "body": "APU operation is limited by altitude (many cannot be started or run above a certain altitude), EGT limits, and duty cycle. Cockpit/APU control panel monitors RPM, EGT, and fault codes; an APU fire or overtemp triggers automatic securing of the unit and bottle discharge on many installations."},
      {"heading": "Engine Ground Runs", "body": "Post-maintenance <b>engine ground runs</b> verify proper operation before flight release: idle stability, acceleration/deceleration response, instrument readings (oil pressure/temp, EGT, fuel flow, vibration) against limits, and leak checks. Runs are performed per the AMM procedure, often requiring a qualified run-up certified technician and specific chock/tie-down/FOD-area precautions."},
      {"heading": "Test Cell / Trim Runs", "body": "Overhauled engines may be run in a <b>test cell</b> (a controlled facility with calibrated instrumentation) to verify performance against factory specifications before installation. <b>Trim runs</b> on-aircraft after certain maintenance adjust fuel control/FADEC parameters and confirm the engine meets thrust/EGT margins for the installed condition."}
    ],
    "quiz": [
      {"q": "What does an APU primarily provide?", "choices": ["Extra passenger seating","Electrical power and bleed air (and sometimes hydraulics) on the ground/in flight","Extra fuel storage","Weather radar"], "answer": 1, "explain": "APUs typically supply electrical power, bleed air, and sometimes hydraulic power independent of the main engines."},
      {"q": "Why are APUs often limited to operating below a certain altitude?", "choices": ["Noise regulations only","Performance/certification limitations at altitude","Weight restrictions","Fuel color changes"], "answer": 1, "explain": "APUs have altitude limitations for starting and continuous operation based on their design and certification."},
      {"q": "What is verified during a post-maintenance engine ground run?", "choices": ["Only that it starts","Idle stability, acceleration response, and instrument readings against limits, plus leak checks","Passenger comfort","Radio frequencies"], "answer": 1, "explain": "Ground runs confirm proper operation across multiple parameters and check for leaks before flight release."},
      {"q": "What is a test cell used for?", "choices": ["Testing passenger seats","Running an overhauled engine in a controlled facility to verify performance against factory specs","Storing tools","Charging batteries"], "answer": 1, "explain": "A test cell provides calibrated instrumentation to verify an overhauled engine meets factory performance specs."},
      {"q": "What does a 'trim run' after certain on-aircraft maintenance typically adjust?", "choices": ["Cabin lighting","Fuel control/FADEC parameters to confirm thrust/EGT margins","Seat positions","Landing gear rigging"], "answer": 1, "explain": "Trim runs fine-tune fuel control or FADEC parameters and confirm the engine meets performance margins as installed."}
    ]
  }
]

EXT7_FLASHCARDS = [
  {"front": "Micrometer thimble - one full turn", "back": "0.025 in (25 thousandths) on a standard 0-1 in mic."},
  {"front": "Click-type torque wrench storage rule", "back": "Reset to lowest setting after use to preserve spring calibration."},
  {"front": "Feeler gauge use", "back": "Checks small, exact gaps like valve clearance or rigging tolerances."},
  {"front": "Tool control shadow board", "back": "Outlines each tool's shape so a missing tool is instantly visible."},
  {"front": "Primary flight controls", "back": "Ailerons (roll), elevator (pitch), rudder (yaw)."},
  {"front": "Secondary flight controls", "back": "Flaps, slats, spoilers, trim tabs, speedbrakes."},
  {"front": "Cable tension tool", "back": "Tensiometer - reading must be corrected for ambient temperature."},
  {"front": "Rigging check verifies", "back": "Correct travel range AND neutral position when cockpit control is centered."},
  {"front": "Continuous-loop fire detector advantage", "back": "Senses along its entire length and can help pinpoint the affected zone."},
  {"front": "Engine fire bottle agent (traditional)", "back": "Halon 1301 or an approved clean-agent replacement."},
  {"front": "Overheat vs fire warning", "back": "Overheat = high temp without confirmed flame; Fire = detected flame condition."},
  {"front": "Fire bottle squibs", "back": "Discharge cartridges with a service-life limit; replaced on schedule regardless of use."},
  {"front": "Constant-speed propeller advantage", "back": "Governor auto-adjusts blade angle to hold RPM, giving near-optimal efficiency across conditions."},
  {"front": "Governor response to overspeed tendency", "back": "Increases blade angle (pitch) to add load and pull RPM back down."},
  {"front": "Feathering a propeller", "back": "Rotates blades near edge-on to minimize drag after engine failure."},
  {"front": "APU primary outputs", "back": "Electrical power and bleed air, sometimes hydraulic power, on ground or as backup in flight."},
]

EXT7_GLOSSARY = [
  {"term": "Vernier Caliper", "def": "A measuring tool using a sliding vernier scale for readings typically to 0.001 in."},
  {"term": "Dial Indicator", "def": "A precision instrument that measures small linear displacements, used for runout and alignment checks."},
  {"term": "Tool Control Program", "def": "A shop system (shadow boards, sign-out logs) ensuring every tool is accounted for, preventing FOD."},
  {"term": "Turnbuckle", "def": "An adjustable fitting used to set and maintain proper tension in a control cable."},
  {"term": "Fairlead", "def": "A guide that keeps a control cable aligned and prevents excessive rubbing as it passes through structure."},
  {"term": "Duplicate Inspection", "def": "A required second, independent inspection of critical flight control work before return to service."},
  {"term": "Continuous-Loop Detector", "def": "A fire/overheat sensing element that responds to heat anywhere along its length, sometimes allowing zone pinpointing."},
  {"term": "Squib", "def": "An explosive discharge cartridge used to release fire-extinguishing agent from a bottle; has a service-life limit."},
  {"term": "Constant-Speed Propeller", "def": "A propeller with a governor that automatically varies blade angle to maintain a selected RPM."},
  {"term": "Feathering", "def": "Rotating propeller blades to a near edge-on angle to minimize drag, typically after engine failure."},
  {"term": "Overspeed Governor", "def": "A backup governor/limiter that protects against propeller RPM exceeding safe limits if the primary governor fails."},
  {"term": "Auxiliary Power Unit (APU)", "def": "A small turbine engine, often tail-mounted, providing electrical, pneumatic, and sometimes hydraulic power independent of main engines."},
  {"term": "Test Cell", "def": "A controlled facility with calibrated instrumentation used to verify an overhauled engine's performance against factory specs."},
  {"term": "Trim Run", "def": "An on-aircraft engine run after maintenance that adjusts fuel control/FADEC parameters and confirms performance margins."},
]

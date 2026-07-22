# -*- coding: utf-8 -*-
"""Aviation Maintenance Academy - Content Expansion Pack 5 (Wave 3)
Adds 5 new modules balanced toward Airframe/Powerplant. Merged in academy_data.py.
"""

EXT5_MODULES = [
  {
    "id": "aerodynamics", "title": "Aerodynamics Fundamentals", "track": "airframe", "icon": "&#x1FA82;",
    "sections": [
      {"heading": "Four Forces of Flight", "body": "<b>Lift</b> (up, from the wing), <b>Weight</b> (down, gravity), <b>Thrust</b> (forward, powerplant), <b>Drag</b> (rearward, resistance). Steady, level, unaccelerated flight requires Lift=Weight and Thrust=Drag."},
      {"heading": "Lift Generation", "body": "Airfoil shape + angle of attack (AOA) accelerate air over the upper surface, lowering pressure (Bernoulli) while also deflecting airflow downward (Newton's 3rd law reaction). Lift increases with AOA up to the <b>critical angle of attack</b>, beyond which the wing stalls."},
      {"heading": "Drag Types", "body": "<b>Parasite drag</b> (form, skin friction, interference) increases with speed squared. <b>Induced drag</b> (from wingtip vortices/lift generation) decreases with speed. Total drag is lowest at <b>L/D max</b> speed - best glide/range speed."},
      {"heading": "Stalls & Load Factor", "body": "A stall is a critical-AOA event, not simply a low-airspeed event - it can happen at any airspeed with enough AOA (e.g., a steep turn). <b>Load factor</b> (G) increases stall speed: Stall speed increases with the square root of load factor. Steeper banks and turbulence increase load factor and stall risk."},
      {"heading": "Stability & Control", "body": "<b>Longitudinal stability</b> (pitch) depends on CG location relative to the wing's center of lift and horizontal stabilizer effect. <b>Lateral</b> (roll, ailerons/dihedral) and <b>directional</b> (yaw, rudder/vertical fin) stability keep the aircraft tracking predictably. A mechanic's rigging work directly affects all three."}
    ],
    "quiz": [
      {"q": "In steady, level, unaccelerated flight:", "choices": ["Lift > Weight and Thrust > Drag", "Lift = Weight and Thrust = Drag", "Only thrust matters", "Weight must exceed lift"], "answer": 1, "explain": "Steady level flight requires the four forces to balance: Lift equals Weight, Thrust equals Drag."},
      {"q": "A wing stalls when it exceeds:", "choices": ["A specific airspeed only", "The critical angle of attack", "Maximum RPM", "The service ceiling"], "answer": 1, "explain": "A stall is fundamentally an AOA event - it can occur at any airspeed if the critical angle of attack is exceeded."},
      {"q": "Induced drag behaves as speed increases:", "choices": ["It increases with speed", "It decreases with speed", "It's unaffected by speed", "It only exists at high speed"], "answer": 1, "explain": "Induced drag (from lift generation/wingtip vortices) decreases as airspeed increases, opposite of parasite drag."},
      {"q": "Increasing load factor (G) in a steep turn does what to stall speed?", "choices": ["Decreases it", "Increases it (with the square root of load factor)", "Has no effect", "Only affects turbine aircraft"], "answer": 1, "explain": "Stall speed increases with the square root of load factor - a 2G turn raises stall speed by about 41%."},
      {"q": "Longitudinal stability is most directly affected by:", "choices": ["Rudder trim only", "CG location relative to the wing's center of lift", "Tire pressure", "Paint scheme"], "answer": 1, "explain": "CG position relative to the center of lift (plus horizontal stabilizer effect) governs pitch/longitudinal stability - a mechanic's W&B work matters here."}
    ]
  },
  {
    "id": "environmental_oxygen", "title": "Environmental & Oxygen Systems", "track": "airframe", "icon": "&#x1F6C1;",
    "sections": [
      {"heading": "Cabin Pressurization", "body": "Pressurized aircraft maintain a lower <b>cabin altitude</b> than actual flight altitude using bleed air and outflow valves. <b>Pressure differential</b> (cabin minus ambient) is limited by structural design - exceeding it risks structural damage; a <b>pressure relief valve</b> protects against overpressurization."},
      {"heading": "Environmental Control System (ECS)", "body": "Bleed air (turbine) or engine-driven compressors cool/heat and condition cabin air via <b>packs</b ) (air cycle machines) or vapor-cycle systems. Includes temperature control, humidity/moisture management, and air distribution/mixing valves."},
      {"heading": "Supplemental Oxygen", "body": "Required above certain cabin altitudes per regulation (crew/passenger requirements differ by altitude and duration). Systems: <b>gaseous</b> (high-pressure cylinders, most common), <b>chemical generators</b> (single-use, passenger drop-down masks), <b>liquid oxygen (LOX)</b> (less common, high-density storage)."},
      {"heading": "Oxygen System Safety", "body": "High-pressure oxygen + any hydrocarbon (oil, grease) = explosion risk - use only oxygen-approved lubricants/cleaning agents. Servicing requires slow fill to avoid adiabatic heating. Leak checks use approved leak-detection compound (never soap that could contain oil)."}
    ],
    "quiz": [
      {"q": "Cabin altitude refers to:", "choices": ["The aircraft's actual flight altitude", "The equivalent pressure altitude maintained inside the cabin", "Ground elevation at departure", "Cruise speed"], "answer": 1, "explain": "Pressurization keeps the cabin at a lower equivalent altitude (higher pressure) than the aircraft's actual flight altitude."},
      {"q": "A pressure relief valve on a pressurized cabin protects against:", "choices": ["Underpressurization only", "Structural damage from overpressurization", "Engine overspeed", "Fuel contamination"], "answer": 1, "explain": "The relief valve vents excess pressure to prevent exceeding the structure's designed maximum pressure differential."},
      {"q": "Which oxygen system is most common for gaseous supplemental oxygen?", "choices": ["Chemical generators only", "High-pressure gaseous cylinders", "LOX exclusively", "Compressed nitrogen"], "answer": 1, "explain": "High-pressure gaseous oxygen cylinders are the most widely used supplemental oxygen source in aviation."},
      {"q": "Why must oxygen system components avoid contact with oil/grease?", "choices": ["It stains the fittings", "High-pressure oxygen with hydrocarbons creates an explosion hazard", "It reduces flow rate slightly", "No real hazard exists"], "answer": 1, "explain": "Oxygen combined with hydrocarbon contamination under pressure can ignite explosively - only oxygen-approved lubricants are permitted."},
      {"q": "Slow-filling an oxygen system is important to avoid:", "choices": ["Wasting oxygen", "Adiabatic heating that could ignite contamination or damage components", "Overfilling the gauge", "Freezing the line"], "answer": 1, "explain": "Rapid compression during fast fills generates adiabatic heat, which combined with any contamination is a fire/explosion risk."}
    ]
  },
  {
    "id": "turbine_fuel_ignition", "title": "Turbine Fuel & Ignition Systems", "track": "powerplant", "icon": "&#x1F525;",
    "sections": [
      {"heading": "Turbine Fuel Systems", "body": "Fuel flows from tanks through boost pumps, filters, and a <b>fuel control unit (FCU)</b> (hydromechanical or FADEC-electronic) that schedules fuel flow for the requested power setting, altitude, and temperature. <b>Fuel nozzles/atomizers</b> spray fuel into the combustor for efficient burning."},
      {"heading": "FADEC", "body": "<b>Full Authority Digital Engine Control</b> computers manage fuel scheduling, limits (N1/N2/EGT), and protection automatically - reducing pilot workload and protecting the engine from exceedances. Dual-channel redundancy is standard; a channel fault typically reverts to the other channel."},
      {"heading": "Igniters & Ignition Systems", "body": "Turbine engines use high-energy <b>igniter plugs</b> (not spark plugs like reciprocating engines) fired by an ignition exciter, typically only needed for starting and inclement-weather/continuous ignition - combustion is self-sustaining once established."},
      {"heading": "Start Sequence & Faults", "body": "Normal start: starter motor spins N2, igniters fire, fuel introduced, light-off (EGT rise), N1/N2 accelerate to idle. <b>Hot start</b> = EGT exceeds limit. <b>Hung start</b> = light-off but stalls below idle. <b>No start</b> = no light-off (check fuel, ignition, starter air/electrical power)."}
    ],
    "quiz": [
      {"q": "The fuel control unit's (FCU) main job is to:", "choices": ["Cool the fuel", "Schedule fuel flow for the requested power, altitude, and temperature", "Filter oil", "Control landing gear"], "answer": 1, "explain": "The FCU (hydromechanical or FADEC) meters fuel flow appropriately based on power lever position and ambient/engine conditions."},
      {"q": "FADEC stands for:", "choices": ["Fixed Aircraft Data Engine Computer", "Full Authority Digital Engine Control", "Fuel Air Detection Engine Circuit", "Forward Auxiliary Drive Engine Cell"], "answer": 1, "explain": "Full Authority Digital Engine Control - a computer system managing fuel scheduling and engine limit protection."},
      {"q": "Turbine engines use igniter plugs mainly during:", "choices": ["Continuous cruise operation", "Starting and adverse weather/continuous ignition conditions", "Shutdown only", "Taxi only"], "answer": 1, "explain": "Once combustion is established it's self-sustaining; igniters are primarily needed for start and icing/heavy precipitation conditions."},
      {"q": "A 'hung start' is characterized by:", "choices": ["No light-off at all", "Light-off occurs but the engine stalls below idle RPM", "EGT exceeding limits", "Normal acceleration to idle"], "answer": 1, "explain": "A hung start lights off but fails to accelerate to idle - often due to insufficient starter assist or fuel scheduling issue."},
      {"q": "A dual-channel FADEC fault in one channel typically results in:", "choices": ["Complete engine shutdown", "Automatic reversion to the other channel", "No effect on operation logged", "Immediate overspeed"], "answer": 1, "explain": "Redundant dual-channel FADEC design allows the healthy channel to take over if one channel faults, maintaining engine control."}
    ]
  },
  {
    "id": "engine_instruments", "title": "Engine Instruments & Monitoring", "track": "powerplant", "icon": "&#x1F4CA;",
    "sections": [
      {"heading": "Reciprocating Engine Instruments", "body": "<b>Tachometer</b> (RPM), <b>Manifold pressure</b> (power setting on constant-speed-prop aircraft), <b>Oil pressure/temperature</b>, <b>Cylinder head temperature (CHT)</b>, <b>Fuel flow/pressure</b>, <b>EGT</b> for leaning. Each has a green (normal), yellow (caution), red (limit) arc/marking."},
      {"heading": "Turbine Engine Instruments", "body": "<b>N1/N2 (or Ng/Np)</b> - fan/compressor and turbine spool speeds as % of max. <b>EGT/ITT</b> - exhaust/inlet turbine temperature, the key limiting parameter. <b>Torque</b> (turboprops) - actual power output indicator. <b>Fuel flow</b> for engine health/leaning trend monitoring."},
      {"heading": "Engine Trend Monitoring", "body": "Recording EGT, oil temp/pressure, fuel flow, and vibration over time reveals gradual degradation (e.g., rising EGT margin loss signals compressor/turbine wear) before it becomes a failure - a maintenance best practice beyond simple pass/fail checks at each flight."},
      {"heading": "Instrument Power & Failure Modes", "body": "Electronic engine instruments (EIS/glass displays) depend on sensors + processing; a failed sensor can show an erroneous reading rather than obviously failing - cross-check against other parameters. Mechanical gauges (direct-reading, e.g., some oil pressure gauges) are simpler but still need periodic calibration/leak checks."}
    ],
    "quiz": [
      {"q": "On many constant-speed-prop reciprocating engines, power setting is primarily indicated by:", "choices": ["Tachometer alone", "Manifold pressure (with RPM held constant by the governor)", "Oil temperature", "Fuel flow only"], "answer": 1, "explain": "With a constant-speed prop holding RPM steady, manifold pressure becomes the primary power-setting indicator."},
      {"q": "EGT/ITT is critical on turbine engines because it:", "choices": ["Indicates oil level", "Is the key limiting parameter protecting the hot section from damage", "Controls fuel color", "Measures airspeed"], "answer": 1, "explain": "Exceeding EGT/ITT limits accelerates hot-section wear/damage - it's the primary protective limit parameter on turbines."},
      {"q": "Engine trend monitoring is valuable because it:", "choices": ["Replaces the need for inspections entirely", "Reveals gradual degradation before it becomes an in-flight failure", "Only matters for brand-new engines", "Has no maintenance value"], "answer": 1, "explain": "Tracking parameters like EGT margin over time can catch developing problems (e.g., compressor wear) long before a failure occurs."},
      {"q": "A failed sensor on a glass engine display might:", "choices": ["Always show an obvious blank/error", "Show an erroneous but plausible-looking reading", "Shut down the engine automatically", "Have no possible failure mode"], "answer": 1, "explain": "Sensor failures can produce misleading in-range-looking readings - cross-checking against other engine parameters is a key habit."},
      {"q": "Torque indication is most associated with which engine type?", "choices": ["Piston engines", "Turboprop engines", "Ramjets only", "Electric motors"], "answer": 1, "explain": "Turboprop engines commonly use a torque gauge as the primary power-output indicator, since propeller thrust relates directly to shaft torque."}
    ]
  },
  {
    "id": "welding_fabrication", "title": "Welding & Metal Fabrication", "track": "general", "icon": "&#x1F527;",
    "sections": [
      {"heading": "Aircraft Welding Processes", "body": "<b>Oxy-fuel (gas) welding</b> - traditional for steel tube structures, gives a wide heat-affected zone. <b>TIG (GTAW)</b> - precise, clean welds, standard for aluminum and stainless/steel repairs on certified aircraft today; uses inert shielding gas (argon) to prevent oxidation."},
      {"heading": "Welder & Weldment Approval", "body": "Aircraft welding on certificated aircraft structure generally requires an <b>FAA-approved welding process</b> and, for repairs, reference to approved data (AC 43.13-1B or the aircraft's SRM). Welder qualification/certification may be required by the operator/repair station even beyond A&P privileges for critical structure."},
      {"heading": "Base Metals & Filler Selection", "body": "4130 chromoly steel tube structures use matching or compatible filler rod. Aluminum structures (less common to weld vs rivet) need alloy-matched filler and careful heat control to avoid warping thin sheet. Never weld high-strength heat-treated parts without engineering approval - welding heat can destroy the temper."},
      {"heading": "Post-Weld Inspection & Treatment", "body": "Visual inspection for uniform bead, no undercut/porosity/cracks. Dye penetrant or X-ray for critical structural welds. <b>Stress relieving/normalizing</b> may be required after welding on hardened steel. Corrosion-proof (paint/primer) promptly after any weld repair on steel."}
    ],
    "quiz": [
      {"q": "TIG welding is preferred over oxy-fuel for many modern aircraft repairs because it:", "choices": ["Is always cheaper", "Gives cleaner, more precise welds with inert-gas shielding", "Requires no skill", "Works only on aluminum"], "answer": 1, "explain": "TIG (GTAW) produces precise, clean welds using argon shielding gas, making it the standard for both steel and aluminum aircraft repairs today."},
      {"q": "Structural aircraft welding repairs must be performed using:", "choices": ["Any convenient method", "An FAA-approved process referencing approved data (AC 43.13-1B/SRM)", "Only oxy-fuel welding", "Whatever the mechanic prefers"], "answer": 1, "explain": "Welding on certificated structure must follow FAA-approved processes and approved repair data - it's not left to personal preference."},
      {"q": "Welding heat-treated high-strength steel parts without engineering approval risks:", "choices": ["No effect at all", "Destroying the part's temper/heat treatment and its strength", "Improving strength", "Only cosmetic discoloration"], "answer": 1, "explain": "Welding heat can undo heat-treatment (temper), significantly weakening a high-strength part unless properly re-treated per engineering data."},
      {"q": "After welding on a hardened steel structural part, you may need to:", "choices": ["Do nothing further", "Perform stress relieving/normalizing per approved data", "Paint immediately with no other treatment", "Sand only"], "answer": 1, "explain": "Stress relieving or normalizing restores appropriate material properties after the heat and stress of welding on hardened steel."},
      {"q": "Post-weld inspection of a critical structural weld often includes:", "choices": ["Visual only, never anything else", "Dye penetrant or X-ray (radiographic) inspection", "Weighing the part", "Nothing - welds are self-verifying"], "answer": 1, "explain": "Critical welds are commonly inspected with dye penetrant or radiography to detect cracks, porosity, or incomplete fusion not visible to the eye."}
    ]
  }
]

EXT5_FLASHCARDS = [
  {"front":"Four Forces of Flight","back":"Lift, Weight, Thrust, Drag - balanced in steady level flight"},
  {"front":"Critical Angle of Attack","back":"AOA beyond which the wing stalls, regardless of airspeed"},
  {"front":"L/D Max","back":"Speed of lowest total drag - best glide/range speed"},
  {"front":"Load Factor & Stall Speed","back":"Stall speed increases with the square root of load factor (G)"},
  {"front":"Cabin Altitude","back":"Equivalent pressure altitude maintained inside a pressurized cabin"},
  {"front":"Pressure Relief Valve (cabin)","back":"Protects the fuselage from overpressurization damage"},
  {"front":"Oxygen + Hydrocarbon Hazard","back":"High-pressure O2 with oil/grease creates an explosion risk - use only O2-approved lubricants"},
  {"front":"Fuel Control Unit (FCU)","back":"Schedules turbine engine fuel flow for power, altitude, temperature"},
  {"front":"FADEC","back":"Full Authority Digital Engine Control - automated fuel scheduling and engine limit protection"},
  {"front":"Igniter Plug (turbine)","back":"High-energy plug used mainly for start and adverse-weather continuous ignition"},
  {"front":"Hot Start (turbine)","back":"EGT exceeds limit during start sequence"},
  {"front":"N1/N2","back":"Fan/compressor and turbine spool speeds, shown as % of max"},
  {"front":"Engine Trend Monitoring","back":"Tracking EGT/oil/fuel-flow/vibration over time to catch degradation before failure"},
  {"front":"TIG Welding (GTAW)","back":"Precise inert-gas-shielded welding process standard for modern aircraft repairs"},
  {"front":"Welding Approved Data","back":"Structural aircraft welds must follow FAA-approved processes referencing AC 43.13-1B/SRM"},
  {"front":"Stress Relieving","back":"Post-weld heat treatment restoring proper material properties in hardened steel"}
]

EXT5_GLOSSARY = [
  {"term":"Angle of Attack (AOA)","def":"Angle between the wing chord line and relative wind"},
  {"term":"Cabin Altitude","def":"Equivalent pressure altitude maintained inside a pressurized cabin"},
  {"term":"Critical AOA","def":"Angle of attack beyond which the wing stalls"},
  {"term":"EGT Margin","def":"Difference between current and limit EGT, tracked for engine health trending"},
  {"term":"FADEC","def":"Full Authority Digital Engine Control"},
  {"term":"Fuel Control Unit (FCU)","def":"Meters turbine fuel flow per power/altitude/temperature"},
  {"term":"Ignition Exciter","def":"Provides high-energy pulses to turbine igniter plugs"},
  {"term":"Induced Drag","def":"Drag from lift generation/wingtip vortices, decreases with speed"},
  {"term":"L/D Max","def":"Speed giving lowest total drag - best glide/range"},
  {"term":"Load Factor","def":"Ratio of aerodynamic lift to aircraft weight (in Gs)"},
  {"term":"Parasite Drag","def":"Drag from form/skin friction/interference, increases with speed squared"},
  {"term":"Stress Relieving","def":"Post-weld heat treatment restoring material properties"},
  {"term":"TIG Welding","def":"Inert-gas-shielded precision welding process (GTAW)"},
  {"term":"N1 / N2","def":"Turbine spool speeds shown as percent of maximum"}
]

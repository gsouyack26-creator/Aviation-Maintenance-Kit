# -*- coding: utf-8 -*-
"""Aviation Maintenance Academy - Wave 11 content expansion pack.
5 new modules: turbocharging_systems, fadec_engine_controls, emergency_equipment_systems,
ground_support_equipment, fuel_quantity_indicating.
Merged in academy_data.py.
"""

EXT21_MODULES = [
    {
        "id": "turbocharging_systems",
        "title": "Turbocharging & Turbo-Normalizing Systems",
        "track": "powerplant",
        "icon": "&#x1F300;",
        "sections": [
            {
                "heading": "Turbocharger Operating Principle",
                "body": "A turbocharger uses exhaust gas energy to spin a turbine wheel, which drives a compressor wheel on the same shaft to compress intake air before it enters the engine, increasing the mass of air (and therefore fuel/air charge) delivered per cycle. Unlike a supercharger, which is mechanically driven off the engine crankshaft and consumes engine power, a turbocharger recovers otherwise-wasted exhaust energy, making it more efficient but introducing exhaust-side heat and lag considerations."
            },
            {
                "heading": "Turbo-Normalizing vs. Turbocharging",
                "body": "Turbo-normalized systems use the turbocharger only to restore sea-level-equivalent manifold pressure as altitude increases, typically capping manifold pressure near the engine's sea-level rated value; this extends the altitude at which full rated power is available but does not increase power above sea-level ratings. True turbocharged (turbo-boosted) systems can produce manifold pressures above sea-level normal, providing higher-than-sea-level power output, but require more conservative operating limits and monitoring to avoid overboost damage."
            },
            {
                "heading": "Wastegate and Overboost Protection",
                "body": "A wastegate valve diverts a portion of exhaust gas around the turbine wheel to control turbine (and therefore compressor) speed, preventing overboost. Wastegates may be manually controlled, or automatically controlled by a density controller or electronic control unit that senses manifold pressure and adjusts wastegate position to maintain a target pressure. A stuck or malfunctioning wastegate is a common cause of overboost events, which can cause detonation and engine damage if manifold pressure limits are exceeded."
            },
            {
                "heading": "Turbocharger Inspection and Maintenance",
                "body": "Turbocharger bearings operate at extremely high rotational speeds and temperatures, requiring reliable oil supply and cooling; oil starvation at shutdown (from turning the engine off abruptly after high-power operation) can cause coking of oil in the hot bearing housing, leading to bearing damage. Inspections check for excessive shaft play, exhaust leaks at turbine housing connections, and proper wastegate operation. Turbocharger failure can allow oil or debris into the intake or exhaust system, so post-failure inspection typically includes checking downstream components for contamination."
            },
      {"heading": "Overboost and Wastegate Troubleshooting", "body": "A turbocharged reciprocating engine that overboosts (manifold pressure exceeds the placarded limit) usually indicates a stuck or misadjusted wastegate valve failing to bypass enough exhaust gas away from the turbine, or a wastegate actuator/controller fault. Conversely, an engine that can't reach rated manifold pressure at altitude may have a wastegate stuck open, an exhaust leak upstream of the turbine reducing available energy to spin it, or a worn turbocharger bearing allowing excess blade-tip clearance and reduced compressor efficiency. Overboost events, even brief ones, should be logged and may require inspection per the engine manual due to potential detonation damage."}
        ],
        "quiz": [
      {"q": "A turbocharged engine that repeatedly exceeds its placarded manifold pressure limit (overboost) most likely has:", "choices": ["A perfectly functioning wastegate", "A stuck/misadjusted wastegate valve or actuator fault failing to bypass enough exhaust gas", "Too little fuel", "A cracked windshield"], "answer": 1, "explain": "Overboost typically points to a wastegate that isn't bypassing enough exhaust gas away from the turbine, whether from a stuck valve or actuator/controller fault."},
            {
                "q": "What powers a turbocharger's compressor wheel?",
                "choices": [
                    "Direct crankshaft drive belt",
                    "Exhaust gas energy driving a turbine wheel",
                    "Electric motor",
                    "Hydraulic pump"
                ],
                "answer": 1
            },
            {
                "q": "What is the main difference between turbo-normalizing and turbocharging?",
                "choices": [
                    "No difference",
                    "Turbo-normalizing restores sea-level pressure only; turbocharging can exceed it",
                    "Turbocharging is always weaker",
                    "Turbo-normalizing uses a supercharger"
                ],
                "answer": 1
            },
            {
                "q": "What does a wastegate control?",
                "choices": [
                    "Fuel flow",
                    "Turbine/compressor speed by diverting exhaust gas",
                    "Oil pressure",
                    "Propeller pitch"
                ],
                "answer": 1
            },
            {
                "q": "What can cause turbocharger bearing coking?",
                "choices": [
                    "Cold weather operation",
                    "Abrupt shutdown after high-power operation without cooldown",
                    "Using synthetic oil",
                    "Low altitude flight"
                ],
                "answer": 1
            },
            {
                "q": "Why check downstream components after a turbocharger failure?",
                "choices": [
                    "Not necessary",
                    "Failure can release oil/debris into intake or exhaust system",
                    "Only cosmetic concern",
                    "To check paint condition"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "fadec_engine_controls",
        "title": "FADEC & Electronic Engine Controls",
        "track": "powerplant",
        "icon": "&#x1F4BB;",
        "sections": [
            {
                "heading": "FADEC Fundamentals",
                "body": "Full Authority Digital Engine Control (FADEC) is a computer-based system that fully controls engine operating parameters (fuel flow, ignition timing where applicable, bleed air, variable geometry) without direct mechanical backup in most implementations. FADEC continuously monitors engine sensors (N1/N2 speed, EGT, torque, altitude, temperature) and adjusts fuel scheduling to optimize performance while protecting against exceedances such as overtemperature or overspeed."
            },
            {
                "heading": "Dual-Channel Redundancy",
                "body": "Most FADEC systems use dual, independent channels (Channel A and Channel B), each capable of fully controlling the engine, so that a single channel failure does not result in loss of engine control. The system automatically switches to the healthy channel upon detecting a fault, often without pilot action required, and annunciates the fault for crew awareness and maintenance follow-up."
            },
            {
                "heading": "FADEC Sensor Inputs and Protections",
                "body": "FADEC relies on accurate sensor data (thermocouples, speed sensors, pressure transducers) to make control decisions; a failed or drifting sensor can cause the FADEC to command an incorrect fuel schedule. Built-in protections include automatic power limiting to prevent exceeding temperature or overspeed limits, and many systems include a fault-tolerant reversion mode that uses alternate sensor data or a simplified control law if primary sensors are lost."
            },
            {
                "heading": "FADEC Maintenance and Software Considerations",
                "body": "FADEC maintenance includes verifying proper software configuration/version matches the approved engine configuration, checking sensor wiring and connectors for corrosion or damage (a common source of intermittent faults), and reviewing fault logs stored in the FADEC's non-volatile memory during troubleshooting. Software updates to FADEC systems require strict configuration control, since incorrect software loading can result in improper engine control and is a certification-critical concern."
            },
      {"heading": "FADEC Channel Redundancy and Fault Logic", "body": "Most FADEC systems use dual redundant channels (A and B) so a single channel fault doesn't cause loss of engine control - the system automatically switches to the healthy channel and annunciates the fault for maintenance action. A FADEC fault message doesn't always mean an engine problem; it can indicate a sensor, wiring, or the FADEC computer itself. Maintenance action requires pulling fault codes from the FADEC's non-volatile memory and cross-referencing the troubleshooting manual's fault isolation procedure rather than guessing based on symptoms alone."}
        ],
        "quiz": [
      {"q": "In a dual-channel FADEC system, if Channel A develops a fault, the typical result is:", "choices": ["Complete loss of engine control", "Automatic switchover to the healthy Channel B with a fault annunciation for maintenance", "The engine shuts down immediately", "No effect on engine operation or annunciation"], "answer": 1, "explain": "Dual-channel FADEC redundancy allows automatic switchover to the healthy channel while annunciating the fault for follow-up maintenance."},
            {
                "q": "What does FADEC stand for?",
                "choices": [
                    "Fixed Automatic Digital Engine Control",
                    "Full Authority Digital Engine Control",
                    "Fast Adaptive Diesel Engine Controller",
                    "Field Adjustable Digital Engine Computer"
                ],
                "answer": 1
            },
            {
                "q": "Why do most FADEC systems use dual channels?",
                "choices": [
                    "To save weight",
                    "Redundancy so a single channel failure doesn't cause loss of control",
                    "To reduce cost",
                    "For display purposes only"
                ],
                "answer": 1
            },
            {
                "q": "What happens with a failed/drifting FADEC sensor?",
                "choices": [
                    "No effect at all",
                    "FADEC may command an incorrect fuel schedule",
                    "Engine shuts down instantly always",
                    "Only affects cabin displays"
                ],
                "answer": 1
            },
            {
                "q": "Where are FADEC fault logs typically stored?",
                "choices": [
                    "Printed logbook only",
                    "The FADEC's non-volatile memory",
                    "Pilot's personal notes",
                    "Nowhere, they are not recorded"
                ],
                "answer": 1
            },
            {
                "q": "Why is FADEC software version control certification-critical?",
                "choices": [
                    "It isn't important",
                    "Incorrect software can cause improper engine control",
                    "Only affects fuel economy slightly",
                    "Software never changes"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "emergency_equipment_systems",
        "title": "Emergency Equipment & Evacuation Systems",
        "track": "airframe",
        "icon": "&#x1F6A8;",
        "sections": [
            {
                "heading": "Fire Extinguishing Equipment",
                "body": "Aircraft carry portable fire extinguishers (typically Halon or approved Halon-replacement agents in the cabin/cockpit) and, on larger aircraft, fixed engine/APU fire extinguishing systems using discharge bottles connected to distribution piping in the engine nacelle or APU compartment. Fixed system bottles are pressure-checked and weighed periodically to confirm agent quantity, since a leaking bottle may show correct pressure due to added nitrogen charge, but insufficient extinguishing agent."
            },
            {
                "heading": "Emergency Evacuation Slides and Rafts",
                "body": "Evacuation slides are packed in compartments (often in the door sill or a separate external pack) and deploy automatically or manually, inflating rapidly using a compressed gas cylinder. Slide/raft packs require periodic functional inspection and repack per the manufacturer's inspection interval; over-water aircraft carry rafts (sometimes slide/raft combination units) sized for the aircraft's maximum occupancy, and raft equipment (signaling devices, provisions) must be inspected for expiration dates."
            },
            {
                "heading": "Oxygen and Emergency Lighting",
                "body": "Emergency oxygen systems (chemical generator or gaseous cylinder-based) supply passenger oxygen masks automatically upon cabin depressurization above a set altitude threshold; chemical oxygen generators produce oxygen through an exothermic chemical reaction and generate significant heat, requiring careful installation clearance from flammable materials. Emergency lighting systems (floor path lighting, exit signs) must have independent battery backup power sufficient to operate for a minimum specified duration after main aircraft power loss."
            },
            {
                "heading": "Inspection and Servicing Requirements",
                "body": "Emergency equipment (extinguishers, oxygen bottles, slides, locator transmitters/ELTs) is tracked on a dedicated inspection schedule separate from routine airframe inspections, since expiration dates (for chemical generators, ELT batteries, hydrostatic test dates for cylinders) drive replacement independent of flight hours. A missing, expired, or discharged piece of required emergency equipment typically makes the aircraft unairworthy for the affected operation until corrected."
            },
      {"heading": "Emergency Equipment Inspection Intervals", "body": "Emergency equipment (fire extinguishers, oxygen bottles, escape slides/ropes, ELTs) has its own strict inspection/service-life tracking independent of the aircraft's general maintenance schedule - a fire extinguisher past its hydrostatic test date or an ELT battery past its replace-by date must be removed from service even if the aircraft is otherwise airworthy in every other respect. These items are tracked individually by serial number and expiration date in many maintenance tracking systems specifically because a missed emergency-equipment expiration is a common audit/inspection finding."}
        ],
        "quiz": [
      {"q": "Why are emergency equipment items (extinguishers, ELT batteries, escape slides) tracked individually by expiration date?", "choices": ["It is not actually required", "Because expired emergency equipment must be removed from service even if the rest of the aircraft is airworthy", "Only for cosmetic reasons", "They never expire"], "answer": 1, "explain": "Emergency equipment has independent service-life/expiration requirements, and expired items must be replaced regardless of the aircraft's overall airworthiness status."},
            {
                "q": "Why might a fire extinguisher bottle show correct pressure but insufficient agent?",
                "choices": [
                    "Impossible scenario",
                    "A leak can be masked by the nitrogen charge added for pressurization",
                    "Pressure gauges are inaccurate always",
                    "Agent quantity doesn't matter"
                ],
                "answer": 1
            },
            {
                "q": "How do most evacuation slides inflate?",
                "choices": [
                    "Manual foot pump",
                    "Compressed gas cylinder for rapid automatic/manual inflation",
                    "Electric air compressor",
                    "They don't inflate, they're rigid"
                ],
                "answer": 1
            },
            {
                "q": "What is a consideration for chemical oxygen generators?",
                "choices": [
                    "They are always cold",
                    "They produce heat via exothermic reaction, requiring clearance from flammables",
                    "They require electrical power to function",
                    "They never expire"
                ],
                "answer": 1
            },
            {
                "q": "What must emergency lighting systems have?",
                "choices": [
                    "No backup needed",
                    "Independent battery backup for a minimum specified duration",
                    "Only AC power connection",
                    "Manual crank power only"
                ],
                "answer": 1
            },
            {
                "q": "What typically drives emergency equipment replacement schedules?",
                "choices": [
                    "Flight hours only",
                    "Expiration dates independent of flight hours",
                    "Pilot preference",
                    "Random inspection"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "ground_support_equipment",
        "title": "Ground Support Equipment (GSE) Operations",
        "track": "general",
        "icon": "&#x1F69A;",
        "sections": [
            {
                "heading": "Ground Power Units (GPUs)",
                "body": "Ground power units supply external electrical power to the aircraft during maintenance and pre-flight operations without running onboard engines or APU, saving fuel and engine cycles. GPUs must supply correct voltage and frequency matching aircraft electrical system requirements (commonly 28V DC or 115V AC 400Hz for many aircraft types); connecting an incompatible GPU can damage sensitive avionics, so technicians must verify GPU output specifications match the aircraft before connection."
            },
            {
                "heading": "Ground Air Carts and Air Start Units",
                "body": "Air carts supply conditioned air for cabin heating/cooling during ground operations, while air start units (ASUs) provide high-pressure compressed air to pneumatically start engines without using the APU or engine-driven starter. ASU output pressure and flow must match the specific engine start requirements; using an undersized or incorrectly regulated air source can result in a failed or hung start."
            },
            {
                "heading": "Towing and Tug Operations",
                "body": "Aircraft towing requires a tow bar or towbarless tug rated for the specific aircraft's nose gear or main gear attachment points and weight, with a properly trained tow team including wing-walkers for large aircraft to prevent collision with obstacles. Nose gear steering limits (specified maximum turn angle) must never be exceeded during towing, as forcing the nose gear beyond its steering limit can cause structural damage to the steering mechanism or gear."
            },
            {
                "heading": "GSE Safety and FOD Prevention",
                "body": "Ground support equipment left near active aircraft (chocks, stands, carts) not properly secured or stored becomes a foreign object debris (FOD) and collision hazard, particularly in engine intake/exhaust danger zones. GSE operators must maintain safe clearance from wingtips, engine inlets, and control surfaces, and equipment must be inspected for damage, proper tire condition/pressure (for towed carts), and functioning brakes before use around aircraft."
            },
      {"heading": "GSE Pre-Use Inspection Discipline", "body": "Ground support equipment (tow bars, GPUs, air start units, deicing trucks, belt loaders) requires a documented pre-use inspection - a damaged or improperly rated tow bar/shear pin can cause nose gear structural damage during towing, and a GPU with degraded voltage regulation can damage sensitive avionics on aircraft power-up. Any GSE involved in an incident (a bump, overspeed tow, contact with the aircraft) must be reported and the aircraft inspected per the AMM's ground-handling damage assessment procedure before further dispatch, even if no obvious damage is visible."}
        ],
        "quiz": [
      {"q": "If ground support equipment makes accidental contact with an aircraft during towing/servicing, the correct response is to:", "choices": ["Ignore it if no damage is visible", "Report it and have the aircraft inspected per the AMM's ground-handling damage procedure", "Only note it informally", "Continue normal dispatch without inspection"], "answer": 1, "explain": "Any GSE contact incident requires formal reporting and an inspection per the AMM's damage assessment procedure, since damage may not be visible externally."},
            {
                "q": "Why must GPU output specifications be verified before connecting to an aircraft?",
                "choices": [
                    "Not necessary, all GPUs are the same",
                    "Incompatible voltage/frequency can damage sensitive avionics",
                    "GPUs never vary in output",
                    "Only affects lighting"
                ],
                "answer": 1
            },
            {
                "q": "What does an air start unit (ASU) provide?",
                "choices": [
                    "Electrical power",
                    "High-pressure compressed air for pneumatic engine starting",
                    "Hydraulic fluid",
                    "Fuel"
                ],
                "answer": 1
            },
            {
                "q": "What must never be exceeded during aircraft towing?",
                "choices": [
                    "Tow speed only",
                    "The nose gear steering angle limit",
                    "Fuel quantity",
                    "Cabin temperature"
                ],
                "answer": 1
            },
            {
                "q": "Why are wing-walkers used during towing of large aircraft?",
                "choices": [
                    "Decoration",
                    "To help prevent collision with obstacles",
                    "To check tire pressure",
                    "To operate the tow bar remotely"
                ],
                "answer": 1
            },
            {
                "q": "Why is unsecured GSE near aircraft a hazard?",
                "choices": [
                    "It isn't a hazard",
                    "It can become FOD or a collision hazard near intakes/exhaust",
                    "Only a cosmetic issue",
                    "It improves ramp organization"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "fuel_quantity_indicating",
        "title": "Fuel Quantity & Indicating Systems",
        "track": "airframe",
        "icon": "&#x26FD;",
        "sections": [
            {
                "heading": "Capacitance-Type Fuel Quantity Systems",
                "body": "Capacitance-type fuel probes use the fuel itself as part of a capacitor's dielectric; as fuel level changes, capacitance changes proportionally (since fuel and air have different dielectric constants), and this signal is processed by a fuel quantity indicating system computer to display quantity. Capacitance systems are common on larger and turbine aircraft because they are relatively insensitive to aircraft attitude changes compared to simple float-type systems, though they still require compensation for fuel density and temperature variations."
            },
            {
                "heading": "Float-Type and Mechanical Fuel Gauges",
                "body": "Simpler float-type fuel quantity systems use a float connected to a variable resistor (rheostat) or a mechanically linked indicator; as fuel level changes, the float position changes resistance or gauge needle position accordingly. Float-type systems are common on smaller general aviation aircraft, are simpler and cheaper to maintain, but can be less accurate during maneuvering flight (climbs, turns, descents) since fuel sloshes and the float doesn't reflect an average level."
            },
            {
                "heading": "Fuel Quantity System Calibration and Density Compensation",
                "body": "Because fuel is typically measured and billed by volume (gallons/liters) but engines consume fuel by mass, quantity indicating systems for larger aircraft often include a density (compensator) unit that adjusts the displayed reading based on actual fuel density, since fuel density varies with temperature and fuel batch. Systems are calibrated per the aircraft manufacturer's procedure, comparing indicated quantity against a known dripstick or sight-gauge reading at specified fuel levels."
            },
            {
                "heading": "Fuel Quantity System Troubleshooting",
                "body": "Common fuel quantity indication faults include probe wiring faults (opens/shorts causing full-scale or zero readings), a failed compensator unit, and probe contamination (water or debris affecting capacitance readings). Troubleshooting typically starts with comparing indicated quantity against a manual dripstick check; a significant discrepancy points to a system fault rather than an actual fuel quantity difference, and isolating individual tank probes (where multiple probes exist per tank) helps pinpoint a faulty unit."
            },
      {"heading": "Capacitance Probe System Troubleshooting", "body": "Capacitance-type fuel quantity systems calculate fuel amount from the dielectric difference between fuel and air sensed by tank probes - a probe with a cracked or contaminated element, or wiring with degraded insulation resistance, produces an erroneous reading (often reading full, empty, or fluctuating erratically) rather than a gradual drift. Cross-check any suspect fuel quantity indication against a manual dripstick/tab measurement or a known fuel-load calculation (fuel added minus fuel burned) before condemning the indicating system - the discrepancy check itself often points directly to which probe or compensator is faulty."}
        ],
        "quiz": [
      {"q": "A capacitance-type fuel quantity indication that fluctuates erratically rather than drifting slowly most likely indicates:", "choices": ["Normal fuel consumption", "A probe wiring or contamination issue causing an erroneous signal", "The tank is completely full", "A software update is needed only"], "answer": 1, "explain": "Erratic fluctuation (versus a slow drift matching fuel burn) points to an electrical/probe fault rather than an actual changing fuel level."},
            {
                "q": "How does a capacitance-type fuel probe sense fuel level?",
                "choices": [
                    "A float mechanically moves a needle",
                    "Fuel changes the capacitance of the probe (acting as dielectric)",
                    "A radar beam measures distance",
                    "A pressure switch"
                ],
                "answer": 1
            },
            {
                "q": "Why are capacitance systems preferred on larger/turbine aircraft over float systems?",
                "choices": [
                    "Cheaper always",
                    "Less sensitive to attitude changes",
                    "They require no calibration",
                    "They are lighter"
                ],
                "answer": 1
            },
            {
                "q": "Why do fuel quantity systems need density compensation?",
                "choices": [
                    "Fuel is billed by volume but consumed by mass, and density varies",
                    "Density never changes",
                    "Only for cosmetic display accuracy",
                    "Not actually needed"
                ],
                "answer": 1
            },
            {
                "q": "What is used to verify fuel quantity indication accuracy on the ground?",
                "choices": [
                    "Guessing based on flight time",
                    "A dripstick or sight-gauge check at known fuel levels",
                    "Asking the fuel truck driver",
                    "Checking tire pressure"
                ],
                "answer": 1
            },
            {
                "q": "What does a significant discrepancy between indicated and dripstick-checked quantity suggest?",
                "choices": [
                    "Normal variation, ignore it",
                    "A system fault rather than an actual quantity difference",
                    "The aircraft needs refueling immediately",
                    "Nothing, it's expected"
                ],
                "answer": 1
            }
        ]
    }
]

EXT21_FLASHCARDS = [
    {
        "front": "Turbocharger vs supercharger",
        "back": "Turbocharger uses exhaust energy; supercharger is mechanically driven off crankshaft"
    },
    {
        "front": "Turbo-normalizing purpose",
        "back": "Restores sea-level manifold pressure at altitude, doesn't exceed it"
    },
    {
        "front": "Wastegate function",
        "back": "Diverts exhaust gas around turbine to control speed/prevent overboost"
    },
    {
        "front": "Turbocharger bearing coking cause",
        "back": "Abrupt shutdown after high power without cooldown"
    },
    {
        "front": "FADEC meaning",
        "back": "Full Authority Digital Engine Control"
    },
    {
        "front": "Why dual-channel FADEC?",
        "back": "Redundancy so single channel failure doesn't lose engine control"
    },
    {
        "front": "FADEC fault log storage",
        "back": "Non-volatile memory within the FADEC"
    },
    {
        "front": "Fixed fire bottle pressure-only check risk",
        "back": "Nitrogen charge can mask agent leakage"
    },
    {
        "front": "Evacuation slide inflation method",
        "back": "Compressed gas cylinder, rapid deployment"
    },
    {
        "front": "Chemical oxygen generator hazard",
        "back": "Produces heat via exothermic reaction; needs flammable-material clearance"
    },
    {
        "front": "GPU compatibility risk",
        "back": "Wrong voltage/frequency can damage sensitive avionics"
    },
    {
        "front": "Nose gear towing limit",
        "back": "Never exceed the specified maximum steering angle"
    },
    {
        "front": "Capacitance fuel probe principle",
        "back": "Fuel changes probe capacitance as dielectric, proportional to level"
    },
    {
        "front": "Why fuel density compensation?",
        "back": "Fuel billed by volume, consumed by mass; density varies with temperature"
    },
    {
        "front": "Fuel quantity ground check method",
        "back": "Dripstick or sight-gauge comparison at known levels"
    },
    {
        "front": "GSE FOD hazard example",
        "back": "Unsecured chocks/stands near engine intakes/exhaust"
    }
]

EXT21_GLOSSARY = [
    {
        "term": "Turbocharger",
        "def": "Exhaust-driven turbine/compressor assembly that increases intake air density."
    },
    {
        "term": "Turbo-Normalizing",
        "def": "Turbocharging limited to restoring sea-level-equivalent manifold pressure at altitude."
    },
    {
        "term": "Wastegate",
        "def": "Valve diverting exhaust gas around the turbine to control boost and prevent overboost."
    },
    {
        "term": "FADEC",
        "def": "Full Authority Digital Engine Control; computer-based full engine control system."
    },
    {
        "term": "Dual-Channel Redundancy",
        "def": "Two independent control channels ensuring continued control after a single failure."
    },
    {
        "term": "Chemical Oxygen Generator",
        "def": "Device producing breathing oxygen via an exothermic chemical reaction."
    },
    {
        "term": "Evacuation Slide",
        "def": "Compressed-gas-inflated slide for rapid passenger emergency egress."
    },
    {
        "term": "Ground Power Unit (GPU)",
        "def": "External power source supplying aircraft electrical power during ground operations."
    },
    {
        "term": "Air Start Unit (ASU)",
        "def": "Ground equipment supplying high-pressure air for pneumatic engine starting."
    },
    {
        "term": "Capacitance Fuel Probe",
        "def": "Fuel quantity sensor using fuel as a capacitor dielectric to sense level."
    },
    {
        "term": "Density Compensator",
        "def": "Fuel quantity system component adjusting displayed quantity for fuel density variation."
    },
    {
        "term": "Dripstick",
        "def": "Calibrated manual dipstick used to verify fuel quantity indication accuracy."
    },
    {
        "term": "FOD",
        "def": "Foreign Object Debris; material posing a hazard to aircraft engines/structure."
    },
    {
        "term": "Overboost",
        "def": "Manifold pressure exceeding safe limits, risking detonation and engine damage."
    }
]

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
      {"heading": "Overboost and Wastegate Troubleshooting", "body": "A turbocharged reciprocating engine that overboosts (manifold pressure exceeds the placarded limit) usually indicates a stuck or misadjusted wastegate valve failing to bypass enough exhaust gas away from the turbine, or a wastegate actuator/controller fault. Conversely, an engine that can't reach rated manifold pressure at altitude may have a wastegate stuck open, an exhaust leak upstream of the turbine reducing available energy to spin it, or a worn turbocharger bearing allowing excess blade-tip clearance and reduced compressor efficiency. Overboost events, even brief ones, should be logged and may require inspection per the engine manual due to potential detonation damage."},
      {"heading": "Turbocharger Bearing and Oil Supply Requirements", "body": "Turbocharger bearings spin at extremely high RPM and rely on a continuous, adequate oil supply for both lubrication and cooling - shutting down a turbocharged engine abruptly after high-power operation without an adequate cool-down period can cause oil coking (oil breaking down from residual heat after oil flow stops), which contaminates and damages the bearing over time. This is why turbocharged engine operating procedures often specify a cool-down/idle period before shutdown, distinct from a naturally-aspirated engine's shutdown procedure, specifically to protect the turbocharger bearing from heat-related oil coking damage."}
        , {"heading": "Turbine Inlet Temperature Limits on Turbocharged Engines", "body": "Turbocharged reciprocating engines produce higher turbine inlet temperatures at the exhaust-driven turbine compared to naturally aspirated engines, and exceeding manufacturer temperature limits accelerates turbine wheel and housing degradation, potentially leading to premature failure. Pilots operating turbocharged engines are typically trained to monitor turbine inlet temperature (TIT) gauges alongside cylinder head temperature, since aggressive power reduction (rapid throttle closure) after high-power operation can cause a temperature spike at the turbine as residual heat migrates without adequate cooling airflow. Technicians investigating turbocharger premature failure complaints should review available TIT trend data if the aircraft is so equipped, since a pattern of temperature excursions during specific flight phases often points to a training or procedure issue rather than a hardware defect."},
    {"heading": "Intercooler Function and Charge Air Cooling Effects", "body": "Compressing intake air with a turbocharger raises its temperature significantly, which reduces air density and can push the fuel-air mixture toward detonation-prone conditions at high boost; an intercooler (air-to-air or air-to-liquid heat exchanger) placed between the turbocharger compressor discharge and the intake manifold cools the compressed charge air before it enters the engine, restoring some of the density lost to compression heating and providing a greater detonation margin at a given boost pressure. A partially blocked or leaking intercooler reduces cooling effectiveness, allowing charge air temperature to run higher than normal at a given boost setting, which can show up as reduced detonation margin or power loss without necessarily triggering an obvious fault indication, making intercooler core inspection for blockage, leaks, and fin damage a specific scheduled item on turbocharged installations equipped with one."},
    {"heading": "Turbocharger Failure Modes and Root Cause Analysis", "body": "Turbocharger failures generally trace back to one of a few root causes: oil starvation, oil contamination, foreign object damage, or overspeed/overtemperature operation. Oil starvation, often from a clogged oil supply line, low oil pressure, or extended shutdown without a proper cooldown period, causes the turbine and compressor wheel bearings to run dry, leading to rapid bearing wear, shaft seizure, or catastrophic bearing failure allowing the wheel to contact its housing. Oil contamination introduces abrasive particles that score bearing surfaces and shaft journals, often traceable to extended oil change intervals, a failing engine oil filter, or internal engine wear metal contamination. Foreign object damage occurs when debris enters the compressor inlet or exhaust turbine housing, causing blade nicks, bending, or complete blade loss that produces severe imbalance and, if a blade fragment travels downstream, potential secondary engine damage. Overspeed conditions, often from a stuck or improperly rigged wastegate, drive the turbine beyond its design speed, risking wheel burst. When a turbocharger failure is found, root cause analysis should include inspecting the oil supply and return lines for restriction, checking oil quality and filter condition, examining bearing surfaces and wheel blades for the specific damage pattern (uniform wear versus localized impact versus one-sided rubbing), and verifying wastegate function, since replacing the turbocharger without correcting the root cause typically leads to a repeat failure."},
    {"heading": "Turbocharger Oil Seal Condition and Bearing Housing Contamination", "body": "The turbocharger's turbine and compressor wheels are separated from the bearing housing by oil seals that prevent engine oil from migrating into either the exhaust side or the compressor side, and seal degradation is one of the most common turbocharger service issues since the seals operate in high-temperature, high-speed environments that promote wear and thermal degradation over the engine's service life. Oil migrating past a degraded compressor-side seal enters the induction system and appears as blue smoke during low-power operation such as descent and approach, or as oil residue on the intercooler core or induction ducting downstream of the compressor outlet, providing a diagnostic indicator the technician can use during pre-maintenance inspections. Oil passing the turbine-side seal is consumed in combustion but deposits carbon in the turbine housing and on the turbine wheel, which can accelerate wheel erosion and imbalance over time, and excessive turbine-side leakage may also deposit carbon in the exhaust system visible as oily soot around the turbocharger turbine outlet flange or exhaust pipe joints. Bearing housing oil contamination from sludge buildup, which occurs when insufficient oil flow allows oil to coke in the housing, is a significant turbocharger failure mechanism that is prevented primarily through proper engine shutdown procedure, since an immediate full-stop shutdown after high-power operation traps heat in the bearing housing and cokes any oil remaining there, whereas a proper cool-down period at low power allows continued oil circulation to carry heat away. Turbocharger bearing housing inspection during maintenance should check for evidence of coking or sludge buildup at the bearing surfaces and oil passages, since partial restriction of an oil passage can reduce bearing cooling and lubrication enough to accelerate wear significantly before total blockage produces obvious symptoms."},
    {"heading": "Turbocharger Compressor Surge Recognition and Prevention", "body": "Turbocharger compressor surge occurs when the compressor's discharge pressure exceeds what the incoming airflow can support at a given engine operating condition, causing a momentary flow reversal that produces a characteristic bang or shudder and a rapid, unstable drop in manifold pressure. Surge is more likely during rapid throttle reduction at high altitude or during aggressive power changes where the wastegate cannot respond quickly enough to prevent an excessive pressure ratio across the compressor. Recognizing surge symptoms, distinct from normal engine roughness, is important because repeated surge events can cause mechanical damage to the compressor wheel through excessive axial loading on the bearing system. Pilots are typically trained to make smooth, gradual throttle movements on turbocharged engines to avoid inducing surge, and technicians investigating a reported surge event should inspect the wastegate for proper function, verify the turbocharger's bearing condition, and check for any induction system restriction that could exacerbate the pressure differential across the compressor during power transients."}],
        "quiz": [ {"q": "Why can excessively lean mixture management be particularly problematic on a turbocharged reciprocating engine compared to a naturally aspirated one?", "choices": ["Mixture setting has no effect on turbocharged engines", "A lean mixture at high power increases exhaust gas temperature, which directly raises turbine inlet temperature and can damage the turbocharger's turbine wheel", "Lean mixtures always improve turbocharger performance with no downside", "TIT limits only apply to naturally aspirated engines"], "answer": 1}, {"q": "Why can rapid throttle closure after high-power operation cause a turbine inlet temperature spike?", "choices": ["It has no effect on temperature", "Residual heat migrates to the turbine without adequate cooling airflow", "It always cools the turbine instantly", "It only affects the compressor, not temperature"], "answer": 1, "explain": "Rapidly reducing power after high-power operation can cause residual heat to migrate toward the turbine section without sufficient cooling airflow, causing a temperature spike."},
      {"q": "Why do turbocharged engines often require a cool-down/idle period before shutdown that naturally-aspirated engines don't need?", "choices": ["Turbocharged engines don't actually need this", "It prevents oil coking that can damage the turbocharger bearing from residual heat after oil flow stops", "It only affects fuel consumption", "This is purely a manufacturer preference with no technical basis"], "answer": 1, "explain": "Without a cool-down period, residual heat in a turbocharger after shutdown can cause the stopped oil supply to coke (break down), contaminating and damaging the high-speed bearing over time."},
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
            },
    {"q": "What is the primary benefit of an intercooler on a turbocharged engine installation?", "choices": ["It increases the temperature of the intake charge for better combustion", "It cools the compressed charge air before intake, restoring density and providing greater detonation margin at a given boost pressure", "It filters particulates from the intake air", "It has no effect on engine performance and exists only for noise reduction"], "answer": 1},
    {"q": "A failed turbocharger shows uniform, dry-appearing bearing wear with no impact damage. What root cause should be investigated first?", "choices": ["Foreign object damage from compressor inlet debris", "Oil starvation or inadequate lubrication", "Wastegate overspeed condition", "Excessive intercooler cooling"], "answer": 1},
    {"q": "Why does proper engine cool-down procedure before shutdown help prevent turbocharger bearing housing coking?", "choices": ["Continued low-power operation maintains oil circulation through the bearing housing, carrying heat away and preventing oil from coking in the trapped hot housing", "Cool-down procedure only affects the engine's cylinder head temperature, not turbocharger components", "Turbocharger bearings do not receive engine oil and are not affected by oil coking", "Immediate shutdown after high power is the recommended procedure for turbocharger longevity"], "answer": 0},
    {"q": "What operating condition is most likely to induce turbocharger compressor surge?", "choices": ["Steady cruise power with no throttle movement", "Rapid throttle reduction at high altitude or aggressive power changes where the wastegate cannot respond quickly enough", "Idle power on the ground", "Surge only occurs during engine shutdown"], "answer": 1}
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
      {"heading": "FADEC Channel Redundancy and Fault Logic", "body": "Most FADEC systems use dual redundant channels (A and B) so a single channel fault doesn't cause loss of engine control - the system automatically switches to the healthy channel and annunciates the fault for maintenance action. A FADEC fault message doesn't always mean an engine problem; it can indicate a sensor, wiring, or the FADEC computer itself. Maintenance action requires pulling fault codes from the FADEC's non-volatile memory and cross-referencing the troubleshooting manual's fault isolation procedure rather than guessing based on symptoms alone."},
      {"heading": "FADEC Software Loading Procedures", "body": "FADEC software updates must be loaded using the exact procedure and approved data specified by the manufacturer - an interrupted software load (power loss, connection failure mid-transfer) can leave the FADEC computer in a corrupted, non-functional state requiring specialized recovery procedures or unit replacement, not just a simple retry. Verifying the correct software part number and configuration for the specific engine/aircraft combination before loading is critical, since loading software intended for a different engine variant or configuration can cause serious operational problems even if the load itself completes successfully."}
        , {"heading": "FADEC Data Bus Communication and Aircraft Interface", "body": "FADEC systems communicate with the aircraft's avionics through data buses such as ARINC 429 or ARINC 664, transmitting engine parameters to cockpit displays and receiving pilot throttle lever position and other control inputs. Data bus wiring integrity, connector condition, and proper bus termination are critical since intermittent bus faults can cause erratic engine parameter displays or delayed throttle response without triggering an obvious hard fault code. FADEC software updates delivered via the data bus interface must follow strict configuration control procedures to ensure the correct software version and engine-specific configuration data (data plate information matched to the specific engine serial number) are loaded, since a mismatched configuration can cause the FADEC to apply incorrect operating limits or control schedules for that particular engine."},
    {"heading": "FADEC Alternate and Manual Reversion Mode Logic", "body": "Most FADEC systems include a degraded operating mode, sometimes called alternate or manual mode, that the control logic engages automatically when it detects a sensor disagreement, internal fault, or loss of confidence in primary control law inputs it cannot resolve through cross-channel comparison. In this mode, the FADEC typically reverts to a simplified control schedule using a reduced sensor set or fixed schedules rather than the full closed-loop optimized control law, which can mean reduced fuel efficiency, altered response characteristics, or thrust/power limitations until the fault is cleared or the engine is shut down. Flight crews are alerted to reversion mode through a dedicated cockpit indication, and maintenance troubleshooting after a reversion event must retrieve the FADEC fault history to identify the specific fault that triggered the reversion, since simply confirming normal mode restored after a power cycle does not fix an underlying intermittent sensor or wiring fault."},
    {"heading": "FADEC Ground Maintenance Test and Fault Code Retrieval", "body": "FADEC systems store fault history in non-volatile memory that can be retrieved through a maintenance access port or aircraft-level maintenance computer, providing technicians with detailed fault codes, associated flight phase/conditions at the time of fault, and whether the fault was transient (self-cleared) or persistent, which is essential information since flight crew-reported symptoms alone often cannot distinguish between a sensor glitch and a serious control fault. A ground maintenance test sequence exercises FADEC-controlled actuators (fuel metering valve, variable geometry actuators, bleed valves) through their range while the FADEC monitors position feedback, allowing detection of a sluggish or binding actuator that might not have triggered an in-flight fault but represents developing wear. After clearing fault codes following a repair, a confirmation ground run is required to verify the fault does not recur under representative operating conditions, since simply clearing codes without confirming the fix leaves open the possibility the fault was intermittent and will return in flight."},
    {"heading": "FADEC Engine Trim and Adaptive Learning Functions", "body": "Full Authority Digital Engine Control systems incorporate adaptive learning algorithms that continuously adjust internal control parameters to compensate for engine-to-engine variation and gradual wear over the engine's service life, maintaining accurate thrust or power output without requiring manual trim adjustments for every minor deviation. These adaptive functions track parameters such as fan speed versus power lever angle relationships and update stored correction values within defined limits, allowing the control system to deliver consistent commanded thrust even as the engine's actual performance characteristics shift slightly with age. However, adaptive learning has bounded limits, and if an engine's actual performance drifts far enough that adaptive corrections reach their maximum authority, the FADEC will flag a maintenance message indicating the learning function is at a limit, which the technician must not ignore since it often signals developing hardware degradation rather than normal aging. After certain maintenance actions, such as engine or major component replacement, borescope-confirmed erosion findings, or software updates, the maintenance manual typically requires resetting the adaptive learning tables to prevent stale correction values calculated for the old hardware configuration from being incorrectly applied to the new configuration. The technician performs this reset through the maintenance laptop interface following the exact procedure and sequence specified, since resetting at the wrong point in a maintenance sequence can leave the system temporarily uncorrected and produce inaccurate thrust indications until new learning data accumulates."},
    {"heading": "FADEC Fuel Metering Unit Feedback and Closed-Loop Fuel Flow Control", "body": "The FADEC system commands fuel flow to the engine through a fuel metering unit that receives an electrical command signal representing desired fuel flow and translates that command into an actual metered fuel flow rate delivered to the fuel nozzles, and closed-loop control architecture, where the metering unit or an associated sensor provides feedback confirming the actual delivered fuel flow rate back to the FADEC, allows the control system to verify that the commanded fuel flow was actually achieved rather than simply assuming an open-loop command was executed correctly. This feedback loop is important because metering unit performance can be affected by factors such as fuel temperature, fuel specific gravity variations between different fuel batches, and metering unit component wear over time, all of which could cause an open-loop system to deliver a fuel flow different from the commanded value without any means of detecting the discrepancy, whereas a closed-loop system continuously adjusts the metering command to compensate for these factors and maintain the actual delivered fuel flow at the value needed to achieve the commanded engine parameter, such as a specific thrust or torque level. Maintenance verification of fuel metering unit and FADEC feedback loop function typically involves a specified ground test procedure that commands a range of fuel flow rates while monitoring the actual measured flow feedback, verifying the control loop tracks commanded flow within the specified tolerance across the tested range rather than only at a single test point. A fuel metering unit that has developed excessive internal wear or contamination may still pass a functional test at some flow rates while exhibiting degraded tracking accuracy at other flow rates, which is why comprehensive testing across the specified range, rather than a single spot check, provides more reliable verification of metering unit condition. Technicians should also verify that any fuel metering unit replacement or overhaul includes confirmation that the specific unit's characterization data, where the FADEC software requires unit-specific calibration parameters, has been correctly loaded and matched to the installed unit, since a mismatch between the FADEC's expected metering unit characteristics and the actual installed unit's behavior can degrade closed-loop control accuracy even with a fully functional metering unit."},
    {"heading": "FADEC Built-In Test Equipment Fault Storage and Maintenance Interface Access", "body": "FADEC systems continuously monitor their own internal circuits and sensor inputs through built-in test equipment functions, storing fault codes and associated parametric data when an anomaly is detected, whether the anomaly is currently active or was a transient condition that has since cleared. Maintenance personnel access this stored fault history through a dedicated maintenance interface, typically using a portable maintenance data loader or a dedicated cockpit-accessible maintenance panel, retrieving fault codes along with associated snapshot data such as the flight phase, altitude, and other engine parameters recorded at the time the fault occurred. This contextual data is essential for accurate troubleshooting, since a fault code alone often does not provide enough information to distinguish between a genuine component failure and a fault triggered by a transient condition, such as momentary electrical noise, that does not require component replacement. Technicians must follow the applicable troubleshooting manual's fault code interpretation logic precisely, since FADEC fault codes frequently have multiple possible root causes requiring a specific sequence of checks to correctly isolate the actual failed component rather than replacing a component based on the fault code alone."}],
        "quiz": [ {"q": "Why can a single data bus wiring fault cause confusing troubleshooting symptoms in a FADEC-equipped engine?", "choices": ["FADEC data buses only connect to a single system, so faults are always isolated", "A single bus fault can simultaneously affect cockpit displays, data recording, and maintenance diagnostics while the FADEC's actual control function remains unaffected", "Data bus faults always shut down the engine immediately", "FADEC systems do not use data buses"], "answer": 1}, {"q": "Why must FADEC software configuration data be matched to the specific engine serial number?", "choices": ["It is only a labeling formality", "A mismatched configuration can cause the FADEC to apply incorrect operating limits or schedules", "All engines use identical configuration data", "Configuration matching only affects cosmetic displays"], "answer": 1, "explain": "Engine-specific configuration data ensures the FADEC applies the correct operating limits and control schedules for that particular engine; a mismatch can cause improper engine control."},
      {"q": "Why is verifying the correct software part number critical before loading FADEC software, even if the load procedure itself would complete successfully?", "choices": ["Software part numbers don't actually matter", "Loading software for the wrong engine variant/configuration can cause serious operational problems even with a successful load", "All FADEC software is universally compatible", "This verification step is optional"], "answer": 1, "explain": "FADEC software must match the specific engine/aircraft configuration; loading the wrong version can cause serious operational problems even though the load transfer itself completes without error."},
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
            },
    {"q": "Why might a FADEC-controlled engine automatically revert to an alternate/manual control mode during flight?", "choices": ["As a routine scheduled mode change with no fault present", "When the FADEC detects a sensor disagreement or internal fault it cannot resolve through cross-channel comparison, using a simplified control schedule as a fallback", "Only when commanded manually by the flight crew for fuel savings", "FADEC systems have no alternate or manual mode"], "answer": 1},
    {"q": "Why is retrieving detailed FADEC fault history important beyond simply noting that a flight crew reported an engine indication anomaly?", "choices": ["Fault history retrieval is optional and provides no additional useful information", "It provides fault codes, associated conditions, and whether the fault was transient or persistent, which flight crew reports alone cannot distinguish", "FADEC systems do not retain any fault history", "Flight crew reports are always more detailed and accurate than stored fault codes"], "answer": 1},
    {"q": "What does it typically indicate when a FADEC's adaptive learning function reaches its maximum correction limit?", "choices": ["Developing hardware degradation that should be investigated rather than a normal aging trend", "A software bug that requires no technician action", "That the engine has been correctly test-run and no further monitoring is needed", "That adaptive learning should be permanently disabled"], "answer": 0},
    {"q": "Why does closed-loop fuel metering control provide an advantage over open-loop control in a FADEC system?", "choices": ["Feedback confirming actual delivered fuel flow allows the system to compensate for factors like fuel temperature and metering unit wear that could otherwise cause undetected flow discrepancies", "Closed-loop control eliminates any need for periodic fuel metering unit maintenance or testing", "Open-loop and closed-loop fuel metering systems produce identical performance under all conditions", "Closed-loop feedback only matters for measuring fuel temperature, not for verifying actual delivered flow"], "answer": 0},
    {"q": "Why is contextual snapshot data associated with a stored FADEC fault code important for troubleshooting?", "choices": ["Fault codes alone always provide complete diagnostic certainty", "It helps distinguish between a genuine component failure and a fault triggered by a transient condition that does not require replacement", "Snapshot data has no diagnostic value", "FADEC systems do not store any data associated with faults"], "answer": 1}
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
      {"heading": "Emergency Equipment Inspection Intervals", "body": "Emergency equipment (fire extinguishers, oxygen bottles, escape slides/ropes, ELTs) has its own strict inspection/service-life tracking independent of the aircraft's general maintenance schedule - a fire extinguisher past its hydrostatic test date or an ELT battery past its replace-by date must be removed from service even if the aircraft is otherwise airworthy in every other respect. These items are tracked individually by serial number and expiration date in many maintenance tracking systems specifically because a missed emergency-equipment expiration is a common audit/inspection finding."},
      {"heading": "Escape Slide Inspection and Packing", "body": "Evacuation slides/rafts require periodic detailed inspection (unpacking, inflating, checking for material degradation, and repacking per the exact manufacturer-specified fold pattern) since an improperly repacked slide can fail to deploy correctly or deploy with reduced inflation in an actual emergency, even though it appeared serviceable in its packed case. The repacking process itself requires specialized training and equipment (packing tables, specific fold sequences) - this is not a task that can be improvised even by an otherwise experienced mechanic without the specific slide-packing qualification."}
        , {"heading": "Emergency Locator Transmitter (ELT) Maintenance", "body": "Emergency Locator Transmitters (ELTs) must be tested per 91.207 requirements, including a monthly self-test and battery replacement based on manufacturer expiration date or after one cumulative hour of use, whichever comes first. ELT antenna connections must be checked for corrosion and secure mounting since a compromised antenna connection can prevent signal transmission even if the unit itself functions correctly during a self-test. Technicians must verify the ELT frequency (121.5/243.0 MHz or 406 MHz) and registration status match current regulatory requirements, since 406 MHz units provide precise GPS-encoded location data to search and rescue satellites while older analog units offer only general direction finding."}, {"heading": "Life Vest and Flotation Equipment Servicing", "body": "Life vests and other flotation equipment carried on aircraft operating over water require periodic inspection per the manufacturer's and operator's maintenance program, including checks of the inflation mechanism (CO2 cartridge pressure/weight, firing mechanism condition), fabric integrity, and oral inflation tube function. Automatic inflation mechanisms must be tested or the cartridge weighed to verify it has not lost gas charge, since an undercharged cartridge will fail to fully inflate the vest when needed, and expired or damaged cartridges must be replaced per the specified service life. Vest fabric is inspected for UV degradation, mildew, tears, or seam separation, particularly on vests stored in less climate-controlled areas of the cabin, since fabric degradation reduces buoyancy reliability. Packing and stowage location must also be verified correct per the aircraft's approved emergency equipment layout, since a life vest stowed in the wrong location or improperly repacked after inspection could delay access during an actual emergency."},
    {"heading": "Fire Extinguisher Discharge Cartridge and Pressure Gauge Checks", "body": "Portable and fixed fire extinguishing systems using pressurized or cartridge-actuated discharge require periodic verification that the discharge cartridge (a small explosive squib or pressurized gas cartridge that drives the extinguishing agent out) is within its service life and shows no signs of corrosion or damage, since a cartridge that fails to fire renders the entire extinguisher useless in an emergency regardless of how much agent remains in the bottle. Extinguisher pressure gauges must be checked against the manufacturer's normal operating range printed on or near the gauge, since a reading in the gauge's red/low zone indicates insufficient propellant to fully discharge the agent even if the bottle is otherwise full, while an overpressure reading may indicate a warming-related issue requiring investigation before further use. Fixed fire suppression bottles (engine, cargo, or APU fire bottles) additionally require weighing at scheduled intervals to confirm the agent charge has not leaked out through the discharge valve or fittings, since a bottle can show a normal-appearing pressure gauge reading while actually being significantly underweight if a slow agent leak has occurred alongside a compensating pressure change."},
    {"heading": "Emergency Equipment Placarding and Passenger Briefing Card Accuracy", "body": "Emergency equipment placards and passenger safety briefing cards must precisely match the actual equipment installed and its exact location on that specific aircraft, since incorrect or outdated placarding can mislead crew and passengers during an actual emergency when seconds matter. When emergency equipment is relocated, added, or removed during maintenance, such as repositioning a fire extinguisher, adding a life raft, or changing oxygen mask stowage locations, the technician must verify that all corresponding placards, briefing cards, and the aircraft's emergency equipment location diagram in the flight manual are updated to match before the aircraft returns to service. Placard wording, symbol usage, and even color coding often follow specific regulatory or manufacturer templates, and technicians should not improvise wording or substitute placards from a different aircraft type even if the equipment appears similar, since exact terminology can be required for crew training consistency across a fleet. Placards must remain legible and securely attached throughout the aircraft's service life, meaning technicians performing unrelated maintenance nearby should verify placard condition and inform the appropriate department if wear, fading, or damage is observed. During any modification affecting escape routes, exit operation, or emergency equipment accessibility, a review of the passenger briefing card and safety demonstration materials is required to confirm the printed and depicted information remains accurate for the modified configuration."},
    {"heading": "Portable Oxygen Bottle Hydrostatic Test Requirements and Pressure Gauge Verification", "body": "Portable oxygen bottles carried aboard aircraft for crew and passenger emergency use are pressure vessels subject to hydrostatic testing requirements at specified intervals to verify the bottle retains adequate structural margin against its rated burst pressure despite the cyclic pressurization, temperature exposure, and potential impact or corrosion damage accumulated during service, and a bottle that has exceeded its hydrostatic test due date must be removed from service and either tested or replaced before further use regardless of its apparent external condition. The hydrostatic test itself involves pressurizing the bottle, typically using a water jacket test method that measures the bottle's volumetric expansion under test pressure, to a specified multiple of its normal service pressure, with acceptance criteria based on the amount of permanent expansion remaining after the test pressure is released, since a bottle with excessive permanent expansion indicates loss of material strength that could lead to a burst failure under normal service pressure cycling. Between hydrostatic test intervals, portable oxygen bottles require periodic visual inspection for external corrosion, denting, or other damage, and the bottle's pressure gauge accuracy should be periodically verified, since a bottle showing adequate pressure on a faulty gauge could actually be significantly underfilled and unable to provide the intended duration of emergency oxygen when needed. Bottle markings, including the manufacture date, hydrostatic test dates, and pressure rating stamped or stenciled on the bottle, must remain legible throughout the bottle's service life, and a bottle with illegible or missing required markings should be treated as unable to verify compliance status and removed from service pending research or retest rather than assumed compliant based on apparent physical condition alone. Technicians handling portable oxygen bottles must maintain oxygen-clean practices consistent with those described for fixed oxygen system servicing, since these portable bottles present the same combustible contamination and fire hazard concerns as any other oxygen system component despite their smaller size and portable application."},
    {"heading": "Crew and Passenger Emergency Equipment Accessibility Verification", "body": "Beyond functional serviceability, emergency equipment such as fire extinguishers, life vests, and emergency exits must remain readily accessible to crew and passengers under realistic emergency conditions, meaning stowage location, retention mechanism function, and any required placarding must all be verified during scheduled inspections. Equipment that is functionally serviceable but obstructed by other cabin items, secured with an overly complex or stuck retention latch, or located behind signage that has become illegible does not meet the intent of emergency equipment requirements even though it might pass a narrow functional test in isolation. Technicians and cabin safety inspectors verify accessibility by physically testing the retrieval process for each piece of required equipment, confirming that retention latches release with reasonable force without requiring tools, and checking that placards identifying equipment location remain legible and are not obscured by other cabin modifications made since the aircraft's original certification. Accessibility findings during inspection, even when the equipment itself tests as functional, should be treated as significant discrepancies given their direct relationship to emergency response effectiveness during an actual event."}],
        "quiz": [ {"q": "Why must a life vest's CO2 inflation cartridge be weighed or tested periodically?", "choices": ["To check the vest's color has not faded", "To verify the cartridge has not lost gas charge, which would prevent full inflation when needed", "Cartridges never need inspection once installed", "To confirm the vest fits properly"], "answer": 1}, {"q": "When must an ELT battery be replaced per regulatory requirements?", "choices": ["Only when it fails a self-test", "By the manufacturer expiration date or after one cumulative hour of use, whichever comes first", "Every 10 years regardless of use", "Never, ELT batteries do not expire"], "answer": 1, "explain": "ELT battery replacement is required by the manufacturer's expiration date or after one cumulative hour of use, whichever occurs first."},
      {"q": "Why does evacuation slide repacking require specific manufacturer-trained qualification rather than general mechanic experience?", "choices": ["Repacking is trivial and requires no special training", "An improperly repacked slide can fail to deploy correctly in an actual emergency despite appearing serviceable", "Slides never need repacking", "Any mechanic can safely improvise the fold pattern"], "answer": 1, "explain": "Incorrect repacking (wrong fold pattern or technique) can cause a slide to fail to deploy properly in a real emergency, which is why specialized training and qualification are required for this specific task."},
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
            },
    {"q": "Why can a fixed fire suppression bottle show a normal-appearing pressure gauge reading while actually being deficient in extinguishing agent?", "choices": ["Pressure gauges always accurately reflect the exact quantity of agent remaining", "A slow agent leak can occur alongside a compensating pressure change, so gauge reading alone does not confirm agent quantity; scheduled weighing is required", "Fire bottles do not use pressure gauges", "Agent quantity has no relationship to bottle weight"], "answer": 1},
    {"q": "Why must emergency equipment placards be updated immediately when equipment location changes during maintenance?", "choices": ["Outdated placards can mislead crew and passengers during an actual emergency when accurate information is critical", "Placards are purely decorative and do not affect emergency response", "Regulations only require placard updates once per year regardless of changes", "Passenger briefing cards are unrelated to placard content"], "answer": 0},
    {"q": "Why must a portable oxygen bottle be removed from service once it exceeds its hydrostatic test due date, regardless of external appearance?", "choices": ["Hydrostatic testing verifies structural margin against burst pressure that cannot be confirmed through external visual inspection alone", "External appearance always accurately reflects a pressure vessel's internal structural condition", "Hydrostatic testing is only a recommendation and bottles remain fully serviceable past the due date", "Portable oxygen bottles are not classified as pressure vessels and are exempt from hydrostatic testing"], "answer": 0},
    {"q": "Why might functionally serviceable emergency equipment still fail an accessibility inspection?", "choices": ["Accessibility is never evaluated separately from function", "The equipment could be obstructed, have a stuck retention latch, or have illegible placarding despite passing a functional test in isolation", "Functional equipment is always automatically accessible", "Emergency equipment inspections only test electrical function"], "answer": 1}
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
      {"heading": "GSE Pre-Use Inspection Discipline", "body": "Ground support equipment (tow bars, GPUs, air start units, deicing trucks, belt loaders) requires a documented pre-use inspection - a damaged or improperly rated tow bar/shear pin can cause nose gear structural damage during towing, and a GPU with degraded voltage regulation can damage sensitive avionics on aircraft power-up. Any GSE involved in an incident (a bump, overspeed tow, contact with the aircraft) must be reported and the aircraft inspected per the AMM's ground-handling damage assessment procedure before further dispatch, even if no obvious damage is visible."},
      {"heading": "Ground Power Unit Quality Standards", "body": "A ground power unit (GPU) must supply voltage and frequency within tight tolerances matching the aircraft's electrical system requirements - a GPU with poor voltage regulation or excessive transient spikes during connection/disconnection can damage sensitive avionics equipment even during a routine, brief ground power hookup. Aircraft electrical systems typically have protection circuits, but relying on protection circuits to catch a consistently substandard GPU rather than maintaining GPU output quality within spec is a poor maintenance practice that risks eventual equipment damage."}
        , {"heading": "GSE Battery and Charging System Maintenance", "body": "Electric-powered ground support equipment, including electric tow tractors and battery-powered ground power units, requires regular battery maintenance including electrolyte level checks on flooded lead-acid batteries, terminal cleaning to prevent corrosion-induced voltage drop, and charging system verification to ensure batteries reach full charge without overcharging. GSE battery charging areas must have adequate ventilation due to hydrogen gas generation during charging, and charging equipment must be inspected for damaged cables or connectors that could create an ignition source in the presence of that hydrogen gas. A GSE unit with a battery that will not hold charge should be tagged out of service for battery replacement rather than continuing to run it on a partial charge, since unpredictable failure during towing or servicing operations creates a safety hazard."},
    {"heading": "Hydraulic Test Stand and Mule Servicing Requirements", "body": "Ground hydraulic test stands (mules) supply filtered, pressure- and flow-controlled hydraulic fluid to aircraft systems for functional checks, gear swings, and flight control tests without running the aircraft's own engine-driven pumps. Because the mule's fluid directly enters the aircraft's hydraulic system, its reservoir fluid type, cleanliness (particle count per the applicable NAS/ISO cleanliness class), and filter condition are just as critical as the aircraft's own system components; a contaminated or wrong-fluid-type mule can introduce contamination or seal-damaging fluid into an otherwise clean aircraft system in a single connection. Mules require scheduled fluid sampling, filter element replacement, and pressure relief valve verification per their own maintenance program, and quick-disconnect fittings must be capped and kept clean between uses to prevent contamination ingress at the connection point itself."},
    {"heading": "Tow Bar and Towbarless Tractor Inspection Requirements", "body": "Conventional tow bars connect to the aircraft nose gear via a pin or shear-pin fitting designed to fail at a defined load below the nose gear's structural limit, protecting the aircraft from towing overload damage; inspection of the tow bar head, pin, and shear-pin condition is critical since a worn or incorrect shear pin defeats this protection, either shearing too early during normal towing or failing to shear before nose gear damage occurs during an overload event. Towbarless tractors instead clamp directly onto the aircraft's nose wheel tires and lift them off the ground, requiring careful attention to the tractor's wheel cradle adjustment and lift capacity rating matched to the specific aircraft type, since an improperly adjusted cradle can apply uneven or excessive side loads to the nose gear during turns. Both tow bar and towbarless equipment require documented inspection of steering angle limit stops (mechanical or electronic on towbarless units) to prevent exceeding the aircraft's nose gear steering angle limits during ground maneuvering, since exceeding these limits can damage steering mechanism components even without an obvious impact event."},
    {"heading": "GSE Electrical Compatibility and Aircraft Interface Verification", "body": "Ground support equipment such as external power carts, air start units, and ground air conditioning carts must be verified compatible with the specific aircraft's electrical and pneumatic interface requirements before connection, since mismatched voltage, frequency, phase configuration, or pressure output can damage aircraft systems that were never designed to accept out-of-tolerance ground inputs. External power carts supplying alternating current must match the aircraft's required voltage and frequency within tolerance, and the technician should verify the cart's output readings on its own gauges before connecting, then monitor aircraft electrical system indications immediately after connection to confirm normal parameters before leaving equipment unattended. Ground air start units and air conditioning carts must match not only pressure and flow requirements but also, in some cases, air temperature limits, since excessively hot ground air can damage ducting or components not rated for sustained high temperature exposure. Physical connector compatibility is equally important; using an adapter to force a connection between incompatible plug types risks incorrect pin mapping that can send power to circuits never intended to receive it. Technicians must also verify GSE is properly grounded and bonded to the aircraft per the applicable procedure before connecting fuel or electrical service, since static discharge during connection is a recognized ignition hazard around fueling operations. Regular inspection and calibration of GSE gauges and safety interlocks is a maintenance function in its own right, since GSE that reads incorrectly can create a false sense of compliance with aircraft interface limits."},
    {"heading": "GSE Preventive Maintenance Program Structure and Inspection Intervals", "body": "Ground support equipment requires its own structured preventive maintenance program, distinct from but coordinated with the aircraft maintenance program it supports, since GSE reliability directly affects aircraft servicing safety and schedule performance, and equipment such as power carts, air start units, hydraulic mules, and towing tractors experience their own wear, fluid degradation, and component fatigue that must be addressed through scheduled inspection and servicing intervals appropriate to each equipment type's specific duty cycle and operating environment. A well-structured GSE preventive maintenance program defines inspection intervals based on equipment operating hours, calendar time, or a combination of both, recognizing that some GSE degradation mechanisms, such as engine wear on a diesel-powered ground power unit, correlate more closely with actual operating hours, while others, such as hydraulic hose aging or battery self-discharge and sulfation, progress on a calendar basis largely independent of how much the equipment has actually been used. Documentation of GSE maintenance history, similar in principle to aircraft maintenance records though typically governed by the operator's internal quality system rather than the same regulatory framework applied to aircraft records, allows tracking of recurring problems, verification that scheduled maintenance has been completed on time, and identification of specific units that may be approaching the end of their economical service life due to accumulating maintenance costs or declining reliability. Calibration of GSE gauges, meters, and test equipment interfaces, such as those on hydraulic test stands or power cart output monitoring displays, requires its own tracked calibration interval separate from the equipment's general preventive maintenance, since a GSE unit that is mechanically well-maintained but displaying inaccurate output readings on its gauges creates a false sense of compliance with aircraft interface limits during actual use. GSE removed from service for extended periods, whether for major repair or seasonal storage, should undergo a return-to-service inspection before being placed back into active use, verifying that fluids, batteries, tires, and safety systems have not degraded during the storage period to a condition that would compromise safe operation when returned to active service."},
    {"heading": "GSE Operator Training and Qualification Requirements for Ground Equipment", "body": "Ground support equipment, including tow tractors, ground power units, and hydraulic mules, requires operators to receive type-specific training and demonstrate qualification before operating the equipment independently, since improper operation can cause significant aircraft damage even when the equipment itself is fully serviceable. Training typically covers equipment-specific operating procedures, safe interface practices with the specific aircraft types the equipment will service, emergency shutdown procedures, and recognition of equipment malfunction indications that should prompt discontinuing use. Organizations operating GSE fleets maintain qualification records for each operator, often requiring periodic recurrent training or requalification, particularly following any incident involving the equipment or introduction of new equipment types to the fleet. Maintenance personnel responsible for GSE upkeep should coordinate with ground operations training programs to ensure operators are aware of any equipment-specific limitations or known issues that affect safe operation, since GSE maintenance information and operator training are complementary elements of an overall safe ground operations program rather than independent activities."}],
        "quiz": [ {"q": "Why is terminal corrosion a particular concern for battery-powered ground support equipment like electric tugs?", "choices": ["Corrosion only affects the equipment's cosmetic appearance", "Corrosion increases resistance at the terminal, reducing available current for high-current applications like electric tug motors", "Corrosion has no measurable electrical effect", "Terminal corrosion is only a concern for GSE batteries, never aircraft batteries"], "answer": 1}, {"q": "Why must GSE battery charging areas have adequate ventilation?", "choices": ["For worker comfort only", "To disperse hydrogen gas generated during charging and reduce ignition hazard", "To cool the batteries faster", "Ventilation is not actually required"], "answer": 1, "explain": "Battery charging generates hydrogen gas, and adequate ventilation is required to prevent a buildup that could be ignited by a spark or damaged equipment."},
      {"q": "Why does ground power unit (GPU) output quality matter even for a brief, routine ground power hookup?", "choices": ["GPU quality never affects the aircraft", "Poor voltage regulation or transient spikes can damage sensitive avionics even during brief use", "Aircraft protection circuits make GPU quality irrelevant", "GPUs are never connected directly to aircraft systems"], "answer": 1, "explain": "Even brief exposure to poor GPU voltage regulation or transient spikes can damage sensitive avionics equipment, making GPU output quality an important maintenance consideration, not just a backup protection-circuit concern."},
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
            },
    {"q": "Why is hydraulic fluid cleanliness on a ground hydraulic test stand (mule) just as critical as cleanliness within the aircraft's own hydraulic system?", "choices": ["Mule cleanliness has no bearing on the aircraft system since they are separate", "The mule's fluid directly enters the aircraft system during use, so contamination or wrong fluid type can be introduced into an otherwise clean aircraft system", "Mules are only used for pneumatic systems, not hydraulic", "Fluid cleanliness standards only apply to engine oil, not hydraulic fluid"], "answer": 1},
    {"q": "What is the purpose of a shear pin in a conventional tow bar's connection to the aircraft nose gear?", "choices": ["It has no functional purpose beyond securing the connection", "It is designed to fail at a defined load below the nose gear's structural limit, protecting the aircraft from towing overload damage", "It prevents the tow bar from being connected to the wrong aircraft type", "Shear pins are only used on towbarless tractors, never conventional tow bars"], "answer": 1},
    {"q": "Why must external power cart voltage and frequency be verified before connecting to an aircraft?", "choices": ["Mismatched electrical output can damage aircraft systems not designed to accept out-of-tolerance ground power", "Aircraft electrical systems automatically reject incompatible ground power without any risk", "Voltage and frequency matching is only relevant for turboprop aircraft", "GSE carts are incapable of producing incorrect voltage or frequency"], "answer": 0},
    {"q": "Why do some GSE preventive maintenance intervals need to be based on calendar time rather than only operating hours?", "choices": ["Some degradation mechanisms, such as hydraulic hose aging or battery sulfation, progress on a calendar basis largely independent of actual equipment usage", "All GSE degradation mechanisms correlate exactly with operating hours and calendar-based intervals serve no purpose", "GSE equipment never degrades when not in active use, making calendar-based intervals unnecessary", "Operating hour tracking is impossible for ground support equipment and calendar intervals are the only option"], "answer": 0},
    {"q": "Why is type-specific operator training important for ground support equipment even when the equipment is fully serviceable?", "choices": ["Operator training has no bearing on aircraft safety", "Improper operation by an untrained operator can cause significant aircraft damage even with fully serviceable equipment", "All GSE operates identically regardless of type", "Training requirements only apply to aircraft maintenance technicians, not GSE operators"], "answer": 1}
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
      {"heading": "Capacitance Probe System Troubleshooting", "body": "Capacitance-type fuel quantity systems calculate fuel amount from the dielectric difference between fuel and air sensed by tank probes - a probe with a cracked or contaminated element, or wiring with degraded insulation resistance, produces an erroneous reading (often reading full, empty, or fluctuating erratically) rather than a gradual drift. Cross-check any suspect fuel quantity indication against a manual dripstick/tab measurement or a known fuel-load calculation (fuel added minus fuel burned) before condemning the indicating system - the discrepancy check itself often points directly to which probe or compensator is faulty."},
      {"heading": "Fuel Quantity System Cross-Check Procedures", "body": "Before relying on an indicated fuel quantity for flight planning, especially after any fuel system maintenance, cross-checking the electronic indication against a mechanical dripstick or tank-tab measurement is standard practice - a discrepancy beyond the allowed tolerance means the indicating system (not necessarily the actual fuel quantity) is suspect and requires troubleshooting before dispatch. This cross-check habit catches probe/compensator faults that might otherwise go unnoticed until a more serious fuel-planning error occurs in flight."}
        , {"heading": "Fuel Quantity Indication System Wiring and Shielding Requirements", "body": "Capacitance fuel probe wiring requires careful shielding and grounding to prevent electromagnetic interference from corrupting the low-level capacitance signals used to compute fuel quantity, and improperly shielded or grounded wiring can cause erratic or inaccurate fuel quantity indications that are difficult to distinguish from actual probe or compensator faults. Wiring routed near high-current cables or radio transmitter antennas is particularly susceptible to interference, and repairs to fuel quantity wiring must restore the original shield termination and routing exactly per the wiring diagram rather than using generic wire replacement practices. Intermittent fuel quantity indication faults that correlate with radio transmission or specific electrical loads being switched on are a strong indicator of a shielding or grounding fault rather than a probe hardware problem."},
    {"heading": "Fuel Quantity System Built-In Test Equipment (BITE) Function", "body": "Modern fuel quantity indication systems (FQIS) incorporate Built-In Test Equipment that allows technicians to run a self-test sequence from a maintenance access panel or laptop interface, exercising each capacitance probe, compensator, and signal conditioning channel and reporting individual probe status, resistance/capacitance values, and fault codes without physically accessing each tank probe. BITE results should be cross-referenced against the AMM's expected value ranges for each probe, since a probe reading within a broad \u201cpass\u201d tolerance band may still be trending toward failure; recording BITE values over successive checks allows trend monitoring that can catch a degrading probe or connector before it causes a dispatch-affecting fault. BITE cannot detect certain faults such as probe positioning errors after tank maintenance or fuel density compensator miscalibration from a wiring issue outside the tested loop, so BITE passing is necessary but not always sufficient to confirm full system accuracy after tank entry work."},
    {"heading": "Fuel Quantity System Zero/Full Tank Calibration Check", "body": "A zero/full tank calibration check verifies the fuel quantity indicating system reads accurately at the extremes of tank capacity, since capacitance probe systems are typically calibrated using compensator units set for specific reference points, and an error at either extreme (indicating fuel remaining in a tank confirmed physically empty, or failing to indicate full when the tank is confirmed physically full via defueling/refueling to a known quantity) points to a compensator calibration or probe positioning issue distinct from a simple probe wiring fault. This check is typically required after any fuel tank entry, probe replacement, or compensator replacement, using a physical reference (drained to a measured zero, or filled to a measured full quantity via calibrated fuel truck metering or a dripstick/tank measurement) rather than relying on the system's own indication to verify itself. A system that reads accurately in the mid-range but has a zero or full-scale error is a specific, addressable calibration fault, and should not be confused with a general system accuracy problem, since the correction approach (compensator adjustment) differs from troubleshooting a wiring or probe fault causing broader inaccuracy."},
    {"heading": "Fuel Quantity System Density Compensation and Temperature Effects", "body": "Fuel quantity indicating systems that measure fuel by capacitance or other volume-sensitive methods must compensate for fuel density variation, since a given volume of fuel represents different masses depending on fuel temperature and specific fuel blend, and aircraft weight and balance calculations depend on mass, not volume. Capacitance-type fuel probes measure the dielectric properties of the fuel-air mixture within the tank, and because fuel's dielectric constant varies with temperature and composition, densitometer units or compensator circuits are incorporated into many systems to convert the raw capacitance reading into an accurate mass-based quantity display. Technicians performing fuel quantity system troubleshooting must understand that a system reading correctly at one fuel temperature can display an apparent error at a very different temperature even with no system fault, and comparing indicated quantity against a manual dip-stick or drip-stick measurement should account for the fuel temperature at the time of the check. Calibration and functional checks of fuel quantity systems typically specify a reference fuel density or require correction factors when using test fluids of different density than actual aircraft fuel, and using the wrong reference density during a ground calibration check can mask a real fault or create a false indication of one. When investigating a fuel quantity indication discrepancy, the technician should first confirm probe wiring continuity and connector condition, then verify densitometer or compensator function, before condemning the indicating system itself as faulty."},
    {"heading": "Fuel Quantity Indicating System Probe Compensator and Tank Unit Matching", "body": "Capacitance-type fuel quantity indicating systems rely on precise matching between individual tank probe units and the system's compensator and indicator electronics, since each probe is manufactured and calibrated to specific electrical characteristics that the system's processing electronics expect, and installing a probe with characteristics outside the expected range, whether from using an incorrect part number or from probe degradation over time, can introduce indication errors that are not attributable to any external wiring or connector fault. Tank unit probes are typically installed at multiple locations within each fuel tank to account for the tank's specific geometry and the fact that fuel does not always distribute perfectly evenly within an irregularly shaped tank during all attitudes and quantities, and the system's processing electronics combine the signals from these multiple probes using a calibrated algorithm specific to that tank's geometry to compute the actual fuel quantity, meaning a fault or drift affecting just one probe among several in a tank may produce a smaller, more subtle quantity indication error than a complete probe failure would, making such partial faults potentially more difficult to identify through simple observation of gross indication error. Compensator units, which correct for fuel dielectric constant variation as described in the module's coverage of density compensation, must themselves be verified for correct function since a compensator fault can introduce an error that affects the quantity indication for an entire tank rather than a single probe location, and troubleshooting an indication discrepancy should consider both individual probe faults and compensator faults as distinct possible root causes requiring different diagnostic approaches. When replacing a tank probe or compensator unit, verifying the replacement part's specific part number and, where applicable, its calibration or matching designation against the aircraft's parts list is essential, since some fuel quantity indicating system designs use probes that must be matched to a specific compensator or system configuration rather than being universally interchangeable across all installations of that general probe type. Functional verification after any fuel quantity system component replacement should include a check across the low, mid, and full range of tank quantity rather than a single-point check, since a matching or calibration error may produce accurate indication at one quantity level while showing significant error at other quantity levels within the same tank."},
    {"heading": "Fuel Quantity Indicating System Ground Test Procedures Using Calibrated Sticks", "body": "Ground test procedures using calibrated dip sticks or drip sticks provide an independent means of verifying fuel quantity independent of the electronic indicating system, serving both as a cross-check for system accuracy verification and as a fallback fuel quantity determination method if the electronic system is inoperative or its accuracy is in question. Calibrated sticks are inserted into designated access points in the fuel tank, and the fuel level reading at the stick, combined with reference tables accounting for aircraft attitude and any wing dihedral or tank shape irregularities, allows technicians to determine actual fuel quantity within the tank being measured. Technicians performing a stick check must ensure the aircraft is in the correct attitude specified for the procedure, since fuel quantity calculations from stick readings assume a specific reference attitude and can be significantly inaccurate if the aircraft is resting with an unusual pitch or roll angle due to landing gear servicing, tire pressure differences, or ground surface slope. Discrepancies discovered between a stick check and the electronic fuel quantity indication should be documented and investigated, since a significant and repeatable discrepancy points toward a calibration or probe issue within the electronic system requiring further troubleshooting."}],
        "quiz": [ {"q": "Why are fuel quantity indication system probes inside fuel tanks typically wired using intrinsically safe circuit designs?", "choices": ["To improve signal accuracy only", "To limit voltage and current to levels incapable of producing an ignition-capable spark in the flammable vapor environment of the tank", "Because intrinsically safe wiring is cheaper", "Fuel tank wiring has no special safety requirements"], "answer": 1}, {"q": "What type of fuel quantity indication fault suggests a wiring shielding or grounding problem rather than a probe hardware fault?", "choices": ["A fault that is always constant and unchanging", "An intermittent fault that correlates with radio transmission or specific electrical loads switching on", "A fault only present during engine shutdown", "A fault that only occurs on the ground"], "answer": 1, "explain": "Intermittent faults correlating with radio transmission or electrical load switching strongly suggest electromagnetic interference from inadequate shielding or grounding, not a probe hardware issue."},
      {"q": "Why is cross-checking an electronic fuel quantity indication against a manual dripstick/tab measurement standard practice, especially after fuel system maintenance?", "choices": ["Electronic indications are always perfectly accurate and need no verification", "It catches probe/compensator faults that could otherwise cause a fuel-planning error in flight", "Dripstick measurements are never accurate", "This cross-check is purely a formality with no real safety value"], "answer": 1, "explain": "Cross-checking catches indicating-system faults (like a bad probe or compensator) that could otherwise go undetected until they cause a real in-flight fuel-planning problem."},
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
            },
    {"q": "A fuel quantity indication system's BITE self-test reports all probes as \"pass.\" What limitation should a technician still keep in mind?", "choices": ["BITE passing guarantees the system is perfectly accurate with no further checks needed", "BITE may not detect certain faults such as probe positioning errors after tank maintenance, so a pass result is necessary but not always sufficient", "BITE only tests the cockpit gauge, not the tank probes", "BITE results cannot be trended over time"], "answer": 1},
    {"q": "Why is a zero/full tank calibration check performed using a physical reference rather than relying on the fuel quantity system's own indication?", "choices": ["The system's own indication is always sufficient to verify its own accuracy", "A physical reference (measured empty or full quantity) is needed to verify the system independently, since the system cannot validate itself", "Physical references are only used for mid-range accuracy checks, never zero/full checks", "Zero/full calibration checks do not require any reference at all"], "answer": 1},
    {"q": "Why do capacitance-type fuel quantity systems require density compensation?", "choices": ["Because fuel's dielectric constant varies with temperature and composition, and weight and balance depends on mass not volume", "Because capacitance probes cannot function at all without a densitometer installed", "Because density compensation eliminates the need for any manual fuel quantity verification", "Because fuel density never actually changes and compensation is only a manufacturer formality"], "answer": 0},
    {"q": "Why can a partial fault affecting just one probe among several in a fuel tank be more difficult to identify than a complete probe failure?", "choices": ["The system combines signals from multiple probes using a calibrated algorithm, so a single probe fault may produce only a subtle rather than gross quantity indication error", "All tank probes always fail simultaneously, making individual probe fault diagnosis unnecessary", "Fuel tanks contain only a single probe each, so multi-probe fault scenarios cannot occur", "Compensator faults and individual probe faults always produce identical symptoms with no distinguishing characteristics"], "answer": 0},
    {"q": "Why is aircraft attitude important when performing a fuel quantity stick check?", "choices": ["Aircraft attitude has no bearing on stick check accuracy", "Stick reading calculations assume a specific reference attitude, and deviation due to servicing, tire pressure, or ground slope can significantly skew results", "Stick checks are always performed with the aircraft airborne", "Attitude only matters for the electronic fuel quantity system, not stick checks"], "answer": 1}
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

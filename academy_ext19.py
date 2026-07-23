# -*- coding: utf-8 -*-
EXT19_MODULES = [
    {
        "id": "aircraft_welding_gas",
        "title": "Gas & Arc Welding for Airframe Repair",
        "track": "airframe",
        "icon": "&#x1F525;",
        "sections": [
            {
                "heading": "Oxy-Acetylene Welding Fundamentals",
                "body": "Oxy-acetylene welding uses a flame produced by burning acetylene gas with oxygen to melt and fuse metal. The neutral flame (equal oxygen and acetylene) is preferred for most steel welding, showing a well-defined inner cone with no excess feather. A carburizing flame (excess acetylene) has a feathery inner cone and adds carbon to the weld, useful for hard-surfacing. An oxidizing flame (excess oxygen) is hotter but can burn metal and is generally avoided except for brazing brass. Regulators reduce cylinder pressure to safe working pressure; acetylene should never be used above 15 psi due to explosion risk from unstable acetylide compounds at higher pressure."
            },
            {
                "heading": "Filler Rod and Flux Selection",
                "body": "Filler rod composition should closely match the base metal being welded. Mild steel structures typically use RG45 or similar low-carbon rod. Flux is required when welding aluminum or stainless steel to dissolve oxide layers that form instantly in air and prevent proper fusion; flux is not needed for mild steel oxy-acetylene welding. After welding aluminum with flux, all flux residue must be thoroughly removed with hot water and a stainless brush, as residual flux is corrosive and will continue attacking the metal."
            },
            {
                "heading": "TIG (GTAW) for Aircraft Structures",
                "body": "Gas Tungsten Arc Welding (TIG) uses a non-consumable tungsten electrode and inert shielding gas (argon) to produce high-quality, precise welds with minimal distortion, making it the preferred method for aircraft steel tubing, aluminum skins, and stainless exhaust systems. DCEN (direct current electrode negative) is used for steel; AC is typically used for aluminum because it provides the cleaning action needed to break up the oxide layer. Proper gas coverage (adequate flow rate, correct cup size, no drafts) is critical to prevent porosity and contamination of the weld puddle."
            },
            {
                "heading": "Weld Inspection and Repair Criteria",
                "body": "Aircraft welds are inspected visually for uniform ripple pattern, complete penetration, absence of undercut, and no evidence of porosity, cracks, or slag inclusion. A properly welded joint should show a fine, evenly spaced ripple with no icicles or lumps. Cracked or heavily corroded steel tubing structures are generally repaired by welding in a new section (splice) rather than patching, following AC 43.13-1B guidance for tubing structure repairs, including proper overlap and stress-relieving of the heat-affected zone where required."
            },
      {"heading": "Gas Welding Flame and Joint Prep", "body": "Oxy-acetylene welding on aircraft steel tubing requires a neutral flame (balanced oxygen/acetylene, no excess of either) - a carburizing (excess acetylene, feathery flame) or oxidizing (excess oxygen, hissing flame) setting produces a weak, brittle, or porous weld even if it looks acceptable visually. Joint fit-up (proper gap, clean bevel, tubes properly aligned/tacked before final welding) matters as much as flame adjustment; a rushed fit-up leads to incomplete penetration that a visual inspection after cooling may not reveal without further NDT."}
        , {"heading": "Post-Weld Heat Treatment and Stress Relief", "body": "Welded steel structures, especially those made from 4130 chromoly, often require post-weld normalizing or stress-relieving heat treatment to restore ductility and relieve residual stresses introduced by the welding thermal cycle. Without proper heat treatment, welded joints can retain brittle microstructures near the heat-affected zone that are prone to cracking under cyclic loading. Technicians must follow the applicable manufacturer or AC 43.13-1B guidance for time-temperature profiles, and welds on primary structure typically require inspection and sign-off by an appropriately rated welder before return to service."}, {"heading": "Welding Equipment Setup and Regulator Safety", "body": "Oxy-acetylene welding equipment requires correct regulator setup with pressure gauges rated for the specific gas service, since acetylene regulators and hoses use reverse (left-hand) threads specifically to prevent accidental cross-connection with oxygen equipment. Acetylene must never be used at line pressures above 15 psi due to its instability at higher pressures, and acetylene cylinders must always be stored and used in the upright position since the acetylene is dissolved in a stabilizing liquid (typically acetone) that can be drawn into the regulator if the cylinder is tipped. Flashback arrestors and check valves on both the oxygen and acetylene lines prevent flame or gas backflow into the hoses and regulators, a critical safety feature that must be verified functional before each use."}],
        "quiz": [ {"q": "Why must acetylene cylinders always be stored and used in the upright position?", "choices": ["For easier transport only", "Acetylene is dissolved in a stabilizing liquid that can be drawn into the regulator if tipped", "To save floor space", "Upright storage has no safety purpose"], "answer": 1, "explain": "Acetylene is dissolved in a stabilizing liquid inside the cylinder; tipping the cylinder risks drawing that liquid into the regulator, which is a serious hazard."}, {"q": "Why is post-weld heat treatment often required on 4130 chromoly steel structures?", "choices": ["To add color to the weld", "To restore ductility and relieve residual stresses in the heat-affected zone", "To increase weld porosity", "To reduce material cost"], "answer": 1, "explain": "Welding thermal cycles can leave brittle microstructures near the weld; heat treatment restores ductility and relieves stress that could otherwise lead to cracking."},
      {"q": "Using an oxidizing flame setting (excess oxygen) during oxy-acetylene welding of aircraft steel tubing typically results in:", "choices": ["A stronger weld than normal", "A weak, brittle, or porous weld despite possibly looking acceptable visually", "No effect on weld quality", "Faster welding with no downside"], "answer": 1, "explain": "An oxidizing flame setting produces a weld with reduced strength/quality due to oxidation of the weld metal, even if the visual appearance seems acceptable."},
            {
                "q": "What is the safe maximum acetylene pressure due to explosion risk?",
                "choices": [
                    "5 psi",
                    "15 psi",
                    "30 psi",
                    "50 psi"
                ],
                "answer": 1
            },
            {
                "q": "Which flame type is preferred for most steel oxy-acetylene welding?",
                "choices": [
                    "Oxidizing",
                    "Carburizing",
                    "Neutral",
                    "Reducing-only"
                ],
                "answer": 2
            },
            {
                "q": "Why is flux required when welding aluminum?",
                "choices": [
                    "To add carbon",
                    "To dissolve the oxide layer",
                    "To cool the weld faster",
                    "To increase flame temperature"
                ],
                "answer": 1
            },
            {
                "q": "Which current type is typically used for TIG welding aluminum?",
                "choices": [
                    "DCEN",
                    "AC",
                    "DCEP only at low amperage",
                    "No current, gas only"
                ],
                "answer": 1
            },
            {
                "q": "How are cracked steel tubing structures typically repaired per AC 43.13-1B?",
                "choices": [
                    "Patching over the crack",
                    "Welding in a new spliced section",
                    "Riveting a doubler",
                    "Bonding with adhesive"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "aircraft_electrical_bonding",
        "title": "Electrical Bonding & Static Discharge Systems",
        "track": "airframe",
        "icon": "&#x26A1;",
        "sections": [
            {
                "heading": "Purpose of Bonding",
                "body": "Electrical bonding connects metal components with low-resistance jumpers to establish a common electrical potential across the airframe. Bonding minimizes voltage differences between parts, reducing the risk of sparking, RF interference, and lightning-strike damage concentration. Bonding jumpers are typically braided copper straps with crimped or soldered terminals, installed across movable joints such as control surface hinges, engine mounts, and landing gear struts to maintain continuity even as components move or vibrate."
            },
            {
                "heading": "Static Dischargers (Static Wicks)",
                "body": "Static dischargers, or static wicks, are mounted at the trailing edges of wings, ailerons, elevators, and the rudder. They provide a low-resistance path to bleed off static charge that builds up from airflow friction (triboelectric charging), preventing charge buildup that would otherwise discharge as noisy corona and interfere with radio communications. Dischargers must be inspected for physical damage, proper resistance (typically checked with an ohmmeter against manufacturer specs, often under 1 megohm), and secure attachment; a missing or damaged wick can cause significant static-related radio noise."
            },
            {
                "heading": "Lightning Strike Protection",
                "body": "Composite aircraft structures, lacking the inherent conductivity of aluminum, often incorporate embedded metal mesh, foil, or expanded metal layers to provide a conductive path for lightning current, diverting it away from fuel tanks and sensitive avionics. Bonding straps connect these conductive layers across structural joints to maintain a continuous path. Fuel tank areas require special attention: bonding resistance requirements are stricter here because arcing near fuel vapors presents an explosion hazard."
            },
            {
                "heading": "Bonding Resistance Testing",
                "body": "Bonding resistance is measured with a low-resistance ohmmeter (milliohmmeter) capable of accurate readings in the milliohm range, since standard multimeters lack sufficient resolution and accuracy for bonding checks. Typical acceptable bonding resistance across a strap is a fraction of an ohm (often less than 0.003 ohm for critical fuel-system bonding, higher for general structure per manufacturer data). Corrosion at bonding jumper attachment points is a common cause of high resistance readings and failed bonding checks; cleaning and re-torquing the attachment often restores continuity."
            },
      {"heading": "Bonding Resistance Verification", "body": "Bonding straps and jumpers (connecting control surfaces, engine mounts, and other components to the aircraft's main structure) are checked with a low-resistance milliohmmeter, not a standard multimeter, since bonding resistance limits are typically specified in milliohms and a standard meter lacks the resolution/accuracy needed. A bonding strap with excessive resistance (from corrosion at the terminal, a partially broken strand, or a loose fastener) compromises lightning-strike current path and static discharge, potentially allowing damaging arcing at a joint that should instead conduct the current safely away."}
        , {"heading": "Bonding Jumper Installation Practices", "body": "Bonding jumpers must be as short and direct as possible to minimize resistance, with braided copper straps preferred over solid wire for flexing joints like control surfaces and landing gear. Jumpers are attached using star washers or serrated washers under the terminal lug to bite through anodizing or paint and ensure metal-to-metal contact. Avoid routing jumpers where they can be pinched, chafed, or subjected to repeated flexing fatigue. Each jumper should be inspected for corrosion, fraying strands, and secure terminal crimps during scheduled inspections, and any jumper exceeding resistance limits must be replaced, not just cleaned."}, {"heading": "Fastener Bonding Requirements on Composite Structures", "body": "Composite aircraft structures require special attention to bonding since the composite material itself is often non-conductive or only marginally conductive, meaning bonding paths must be engineered explicitly through embedded conductive layers (expanded copper foil or metal mesh) rather than relying on the structure itself. Fasteners penetrating composite skins for bonding purposes typically require conductive sealant or specific fastener coatings to maintain continuity across the joint, and standard bonding resistance checks used on metal structure may need adapted procedures and tolerances for composite bonding paths. Repairs to composite structure that do not restore the embedded conductive layer can leave a bonding discontinuity that is invisible until a lightning strike or static event reveals it."}],
        "quiz": [ {"q": "Why does bonding on composite aircraft structures require special engineering?", "choices": ["Composites are always more conductive than metal", "Composite material is often non-conductive, requiring embedded conductive layers for bonding paths", "Bonding is not needed on composites", "Composite fasteners never need coating"], "answer": 1, "explain": "Since composite material is largely non-conductive, bonding paths must be engineered through embedded conductive layers rather than relying on the base material."}, {"q": "Why are serrated or star washers used when installing bonding jumpers?", "choices": ["To add decorative finish", "To bite through anodizing or paint for solid metal-to-metal contact", "To reduce jumper weight", "To increase jumper flexibility"], "answer": 1, "explain": "Serrated washers cut through nonconductive coatings to guarantee low-resistance electrical continuity at the bonding point."},
      {"q": "Why is a milliohmmeter used to check bonding strap resistance rather than a standard multimeter?", "choices": ["It looks more professional", "Bonding resistance limits are specified in milliohms, requiring the finer resolution a standard multimeter lacks", "Multimeters cannot measure resistance at all", "Milliohmmeters are cheaper"], "answer": 1, "explain": "Bonding resistance specifications are typically in the milliohm range, well below the resolution of a standard multimeter, requiring a dedicated low-resistance meter."},
            {
                "q": "What is the primary purpose of electrical bonding jumpers on an airframe?",
                "choices": [
                    "Increase weight for balance",
                    "Establish a common low-resistance electrical potential",
                    "Improve paint adhesion",
                    "Reduce fuel consumption"
                ],
                "answer": 1
            },
            {
                "q": "Where are static dischargers typically mounted?",
                "choices": [
                    "Nose landing gear",
                    "Trailing edges of flight control surfaces",
                    "Cockpit windows",
                    "Engine cowling"
                ],
                "answer": 1
            },
            {
                "q": "What do static wicks help prevent?",
                "choices": [
                    "Engine overheating",
                    "Radio interference from static discharge",
                    "Hydraulic fluid leaks",
                    "Tire wear"
                ],
                "answer": 1
            },
            {
                "q": "Why do composite aircraft often embed metal mesh in the skin?",
                "choices": [
                    "To reduce drag",
                    "To provide a path for lightning current",
                    "To improve paint color",
                    "To add stiffness only"
                ],
                "answer": 1
            },
            {
                "q": "What instrument is required for accurate bonding resistance checks?",
                "choices": [
                    "Standard multimeter",
                    "Low-resistance ohmmeter (milliohmmeter)",
                    "Voltmeter",
                    "Ammeter clamp"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "aircraft_scheduled_inspections",
        "title": "Scheduled Inspection Programs & Airworthiness Directives",
        "track": "general",
        "icon": "&#x1F4CB;",
        "sections": [
            {
                "heading": "Inspection Program Types",
                "body": "Part 91 aircraft not used for hire generally require an annual inspection every 12 calendar months under 14 CFR 91.409. Aircraft used for hire or flight instruction for hire typically require 100-hour inspections in addition to (or instead of) the annual, depending on operation type. Progressive inspection programs and manufacturer-approved inspection programs (like those in a maintenance manual's inspection schedule) offer alternatives, spreading inspection tasks across multiple shorter events rather than one large annual inspection, which can reduce aircraft downtime."
            },
            {
                "heading": "Airworthiness Directives (ADs)",
                "body": "Airworthiness Directives are legally enforceable rules issued by the FAA to correct an unsafe condition in a product, and compliance is mandatory unless a specific exemption is granted. ADs may require one-time inspections, recurring inspections at specified intervals, or modifications/replacements of parts. Emergency ADs may require action before further flight when the unsafe condition poses an immediate hazard. AD compliance must be recorded in the aircraft's permanent maintenance records, including the AD number, method of compliance, and date/time of compliance."
            },
            {
                "heading": "Service Bulletins vs. ADs",
                "body": "Service Bulletins (SBs) are issued by manufacturers and are generally NOT mandatory unless referenced by an AD or a specific operator's approved maintenance program (or required by insurance/lease terms). However, many ADs are based on manufacturer SBs, incorporating them by reference and making compliance mandatory. Understanding whether a bulletin is 'FAA-mandated' (via an AD) versus 'manufacturer-recommended' (SB alone) is essential to correctly prioritizing and documenting compliance."
            },
            {
                "heading": "Inspection Documentation and Sign-off",
                "body": "A completed inspection requires a written, signed statement in the maintenance records including the type of inspection performed, aircraft total time, and a statement that the aircraft was found to be in airworthy condition (or a list of discrepancies if not airworthy). For an annual inspection, only an IA (Inspection Authorization holder) may perform and approve for return to service; a mechanic with an A&P certificate but no IA can perform the inspection but cannot approve it for return to service without IA sign-off."
            },
      {"heading": "Inspection Program Escalation Logic", "body": "Scheduled inspection programs (annual, 100-hour, progressive, or manufacturer-specific) are designed so that findings at one inspection level can escalate scope - if a routine check reveals unexpected wear or damage, the inspector isn't limited to the checklist items for that inspection tier and must expand the inspection scope to determine the full extent of the problem. This is why an 'annual inspection' checklist is a minimum starting point, not a ceiling - discovering corrosion or a crack during a routine item requires following it to its full extent, even if that means inspecting areas not originally on that inspection's checklist."},
      {"heading": "Progressive Inspection Program Structure", "body": "A progressive inspection program breaks the total inspection workload into smaller segments performed at shorter, more frequent intervals (rather than one large annual event), spreading maintenance downtime across the year while still covering 100% of required items within the specified overall cycle. This approach suits high-utilization aircraft where a single extended annual-inspection downtime would be operationally disruptive - but requires careful tracking to ensure every item is actually completed within its required interval across the segmented schedule, since a missed segment can result in an item silently falling out of compliance if tracking isn't rigorous."}
        , {"heading": "Special Inspections Triggered by Events", "body": "Beyond routine calendar or hour-based inspections, special inspections are triggered by specific events such as hard landings, lightning strikes, bird strikes, overspeed or overtemperature exceedances, and severe turbulence encounters, each with manufacturer-specified inspection scopes tailored to the type of event. A hard landing inspection, for example, typically requires detailed examination of landing gear attach structure, wing spar areas, and engine mount hardware even if no damage is visually apparent, since overstress damage can be internal or below the visible threshold. Skipping event-triggered special inspections because the aircraft \"flew fine\" afterward is a significant safety risk, since some overstress damage only manifests as a failure much later under normal operating loads."}],
        "quiz": [ {"q": "Why are event-triggered special inspections (e.g., after a hard landing) still necessary even if the aircraft appears to fly normally afterward?", "choices": ["They are optional and rarely necessary", "Overstress damage can be internal or below the visible threshold and may fail later under normal loads", "Special inspections are only for cosmetic damage", "The aircraft flying fine guarantees no damage occurred"], "answer": 1, "explain": "Overstress damage from events like hard landings can be hidden or internal, and normal-appearing flight afterward does not rule out damage that could fail later."},
      {"q": "What is a key risk of a progressive inspection program that spreads inspection items across many smaller segments rather than one large annual event?", "choices": ["There is no risk at all", "A missed segment can cause an item to silently fall out of compliance without rigorous tracking", "Progressive programs always inspect less than annual programs", "Progressive inspections take more total downtime than annual inspections"], "answer": 1, "explain": "Because items are spread across many smaller segments, a missed segment can allow a required inspection item to silently fall out of compliance unless tracking is rigorous."},
      {"q": "If a mechanic performing a routine 100-hour inspection discovers unexpected corrosion, the correct response is to:", "choices": ["Ignore it since it wasn't on the checklist", "Expand the inspection scope as needed to determine the full extent of the finding", "Wait until the next annual inspection", "Note it only if convenient"], "answer": 1, "explain": "Scheduled inspection checklists are a minimum baseline; any unexpected finding requires expanding the inspection scope to fully assess it, regardless of the original checklist scope."},
            {
                "q": "How often is an annual inspection required under 14 CFR 91.409?",
                "choices": [
                    "Every 6 calendar months",
                    "Every 12 calendar months",
                    "Every 100 flight hours",
                    "Every 24 calendar months"
                ],
                "answer": 1
            },
            {
                "q": "Is compliance with an Airworthiness Directive mandatory?",
                "choices": [
                    "No, it's a suggestion",
                    "Yes, unless a specific exemption is granted",
                    "Only for commercial operators",
                    "Only if the owner agrees"
                ],
                "answer": 1
            },
            {
                "q": "Are Service Bulletins generally mandatory on their own?",
                "choices": [
                    "Yes, always",
                    "No, unless referenced by an AD or required by an approved program",
                    "Only for turbine aircraft",
                    "Only within the first year of issue"
                ],
                "answer": 1
            },
            {
                "q": "Who must approve an aircraft for return to service after an annual inspection?",
                "choices": [
                    "Any A&P mechanic",
                    "An Inspection Authorization (IA) holder",
                    "The aircraft owner",
                    "A student mechanic under supervision"
                ],
                "answer": 1
            },
            {
                "q": "What must be recorded for AD compliance in maintenance records?",
                "choices": [
                    "Only the aircraft tail number",
                    "AD number, method of compliance, and date/time",
                    "Just a checkmark",
                    "Nothing, verbal confirmation suffices"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "aircraft_fabric_covering",
        "title": "Fabric Covering & Doped Finishes",
        "track": "airframe",
        "icon": "&#x1F9F5;",
        "sections": [
            {
                "heading": "Fabric Materials and Certification",
                "body": "Modern aircraft fabric covering primarily uses synthetic polyester fabric (such as Ceconite or Stits Poly-Fiber systems) rather than the cotton or linen historically used, offering greater strength, longer service life, and resistance to rot and mildew. Fabric coverings must be applied under an approved STC (Supplemental Type Certificate) process or per the aircraft's original type certificate data, with the specific process (envelope method, blanket method, or individual panel method) dictated by the covering system manufacturer's approved instructions."
            },
            {
                "heading": "Dope Application Process",
                "body": "Dope is a clear or pigmented liquid coating applied in multiple coats to shrink the fabric taut over the structure and provide a protective, weatherproof surface. Nitrate dope was historically used as a base coat for adhesion, followed by butyrate dope topcoats for its superior UV and weather resistance and lower flammability; nitrate dope alone is highly flammable and today, all-butyrate or non-flammable modern systems are preferred. Each dope coat must be allowed to fully cure before the next is applied, and proper ventilation during application is essential due to solvent vapors."
            },
            {
                "heading": "Rib Stitching and Reinforcing Tape",
                "body": "Fabric is attached to wing ribs using rib stitching (a specific lock-stitch pattern using waxed polyester cord) or approved rib-lacing clips, spaced according to the covering manual's specified interval (often related to airspeed category). Reinforcing tape (surface tape) is applied over rib stitching, seams, and structural members before final dope coats to distribute stress and prevent fabric from tearing at attachment points; tape width and adhesive method must follow the specific covering system's approved procedures."
            },
            {
                "heading": "Fabric Strength Testing",
                "body": "Fabric strength is checked periodically using a calibrated fabric tester (punch-type tester) that measures the force required to punch through the fabric; results are compared against the minimum strength value specified for the aircraft's category (typically listed in pounds per inch of tear strength, e.g., a common minimum threshold near 46-56 lbs depending on aircraft category and original certification basis). Fabric that tests below the minimum strength is considered unairworthy and must be re-covered before further flight, even if it appears visually sound."
            },
      {"heading": "Fabric Condition Testing", "body": "Fabric-covered aircraft skin strength is checked periodically with a calibrated fabric-strength tester (punch tester) that measures the force needed to puncture the fabric, compared against the minimum strength required by the fabric's process specification (e.g., certain STC'd polyester fabric systems). UV exposure and age progressively degrade fabric strength even without visible damage, which is why punch testing - not just a visual check - is required at defined intervals. A fabric that fails the punch test in any tested area requires recover or repair before further flight, regardless of how the fabric looks visually."}
        , {"heading": "Finishing Coats and UV Protection", "body": "After dope application and fabric tautening, finishing coats including aluminum pigmented dope or UV-blocking topcoats protect the fabric from ultraviolet degradation, which is the leading cause of premature fabric failure independent of mechanical wear. Silver or aluminum dope reflects UV radiation, while color topcoats provide the final aesthetic and additional UV barrier. Manufacturers specify minimum numbers of coats and dry film thickness, and applying insufficient UV protection can cut fabric service life dramatically even though the fabric appears sound. Punch testing during inspections should always be paired with a visual check of finish coat condition and chalking."}, {"heading": "Fabric Repair Patch Techniques", "body": "Small fabric damage such as tears or punctures can often be repaired with a doped-on fabric patch rather than requiring a full recover, provided the damage does not exceed the size limits specified in the applicable STC or manufacturer data. Patch material must match the original fabric weight and weave, with edges pinked or heat-sealed to prevent fraying, and the patch is typically oversized to extend well beyond the damage before doping in place with matching dope coats. Patches must be documented in the aircraft records with the STC or data reference used, the size and location of the repair, and the technician's certificate number, since undocumented fabric repairs are a common inspection discrepancy."}],
        "quiz": [ {"q": "What must fabric repair patch material match from the original covering?", "choices": ["Color only", "Fabric weight and weave", "Nothing, any fabric works", "Thickness only, not weave"], "answer": 1, "explain": "Patch fabric must match the original weight and weave to maintain consistent strength and proper dope adhesion across the repair."}, {"q": "What is the leading cause of premature fabric covering failure aside from mechanical damage?", "choices": ["Excessive humidity only", "Ultraviolet radiation degradation", "Cabin pressurization cycles", "Engine vibration"], "answer": 1, "explain": "UV radiation breaks down fabric fibers over time; aluminum/silver dope and UV-blocking topcoats are applied specifically to protect against this degradation."},
      {"q": "Why is a calibrated punch (fabric-strength) test required on fabric-covered aircraft rather than relying on visual inspection alone?", "choices": ["Visual inspection is always sufficient", "UV and age degrade fabric strength even without visible signs of damage", "Punch testing is only cosmetic", "Fabric never degrades with UV exposure"], "answer": 1, "explain": "Fabric can lose significant strength from UV/age exposure without any visible sign of deterioration, making a quantitative punch test necessary."},
            {
                "q": "What synthetic fabric type is commonly used in modern aircraft covering systems?",
                "choices": [
                    "Cotton",
                    "Linen",
                    "Polyester (e.g., Ceconite/Poly-Fiber)",
                    "Nylon canvas"
                ],
                "answer": 2
            },
            {
                "q": "Why was nitrate dope historically paired with butyrate topcoats?",
                "choices": [
                    "Nitrate is cheaper only",
                    "Nitrate provides good adhesion, butyrate adds weather/UV resistance",
                    "Butyrate can't be used alone at all",
                    "Color matching purposes only"
                ],
                "answer": 1
            },
            {
                "q": "What is the purpose of reinforcing (surface) tape over rib stitching?",
                "choices": [
                    "Purely decorative",
                    "Distribute stress and prevent tearing at attachment points",
                    "Increase aircraft weight",
                    "Replace the need for dope"
                ],
                "answer": 1
            },
            {
                "q": "How is fabric strength verified during inspection?",
                "choices": [
                    "Visual inspection only",
                    "A calibrated punch-type fabric tester",
                    "Tapping with a hammer",
                    "Weighing the fabric"
                ],
                "answer": 1
            },
            {
                "q": "What happens if fabric tests below minimum strength?",
                "choices": [
                    "It's fine if it looks good",
                    "It is unairworthy and must be re-covered",
                    "Add another dope coat and it's fine",
                    "Only needs a logbook note"
                ],
                "answer": 1
            }
        ]
    },
    {
        "id": "engine_condition_monitoring",
        "title": "Engine Condition Monitoring & Trend Analysis",
        "track": "powerplant",
        "icon": "&#x1F4C8;",
        "sections": [
            {
                "heading": "Purpose of Trend Monitoring",
                "body": "Engine condition monitoring tracks key parameters (EGT, oil temperature, oil pressure, fuel flow, vibration, oil consumption) over time to detect gradual degradation before it becomes a failure. A single data point rarely reveals a developing problem, but a trend\u2014such as EGT slowly rising over many flight hours at the same power setting\u2014can indicate developing issues like injector wear, compressor fouling, or turbine deterioration well before they trigger a warning light or in-flight event."
            },
            {
                "heading": "Oil Analysis (SOAP)",
                "body": "Spectrometric Oil Analysis Program (SOAP) testing detects trace metal particles suspended in engine oil, identifying wear patterns specific to different engine components (e.g., elevated iron may indicate cylinder/piston wear, elevated copper may indicate bushing or bearing wear). Regular SOAP sampling at consistent intervals (matching oil changes) builds a baseline for each engine; a sudden spike in a particular metal, even if still within a nominal range, is often more significant than a single high absolute reading, because it suggests a rapid change in wear rate."
            },
            {
                "heading": "Vibration Analysis",
                "body": "Vibration monitoring, particularly on turbine engines, uses accelerometers to detect imbalance, misalignment, or developing mechanical faults such as bearing wear or blade damage. Vibration signatures are analyzed by frequency; different fault types produce characteristic frequency patterns (e.g., a 1x rotor speed peak often indicates imbalance, while higher-frequency peaks can indicate bearing defects). Sustained vibration above manufacturer limits requires investigation even if the engine otherwise appears to perform normally."
            },
            {
                "heading": "Borescope and Video Trend Records",
                "body": "Periodic borescope inspections, recorded on video or as still images with clear reference markers, allow direct visual comparison of internal engine condition (turbine blades, combustor liner, compressor blades) across multiple inspection intervals. Maintaining a photographic/video trend history lets technicians distinguish between a pre-existing minor blemish and genuinely new or progressing damage, preventing both over-reaction to old, stable findings and under-reaction to newly developing defects."
            },
      {"heading": "Establishing a Reliable Baseline", "body": "Engine condition monitoring is only as good as its baseline - trend data must be gathered under consistent conditions (similar power setting, corrected for ambient temperature/altitude/bleed loads) or the comparison is meaningless. A new engine or one just out of overhaul needs several flights to establish a stable baseline before trend deviations become meaningful; comparing a freshly-installed engine's first flight data against a fleet-average baseline can produce a false alarm simply due to normal break-in characteristics. Data outliers from clearly abnormal flights (aborted takeoff, unusual weather) should be flagged and excluded from trend analysis rather than skewing the baseline."},
      {"heading": "Correlating Multiple Parameters for Diagnosis", "body": "Effective engine condition monitoring looks at multiple parameters together rather than any single one in isolation - a rising EGT alone might suggest several different problems, but combined with a corresponding drop in N1/N2 and a specific vibration signature, the pattern narrows toward a more specific likely cause (e.g., turbine blade damage versus a fuel control issue versus compressor fouling). Analysts trained in engine condition monitoring learn these multi-parameter signature patterns, since chasing a single parameter change in isolation often leads to an incorrect or overly broad initial diagnosis."}
        ],
        "quiz": [
      {"q": "Why is engine condition monitoring more effective when analyzing multiple parameters together rather than any single parameter alone?", "choices": ["Single parameters always give a complete diagnosis", "Combined parameter patterns (EGT, N1/N2, vibration) narrow down the likely specific cause more accurately than one parameter alone", "Multiple parameters are never correlated", "Analyzing multiple parameters is unnecessarily complex with no diagnostic benefit"], "answer": 1, "explain": "Combining multiple parameter trends (like EGT with N1/N2 and vibration signature) reveals specific fault signatures that a single parameter viewed in isolation cannot reliably distinguish."},
      {"q": "Why is a newly overhauled engine's first-flight data not immediately compared against long-term fleet trend baselines?", "choices": ["New engines never need monitoring", "Break-in characteristics can cause normal early readings to look like a deviation, risking a false alarm", "The data is always identical to the fleet average", "Fleet baselines don't apply to any engines"], "answer": 1, "explain": "New/overhauled engines have break-in characteristics that can appear as a deviation from established fleet trends, so a stable individual baseline is established first."},
            {
                "q": "Why is trend monitoring more valuable than a single data point?",
                "choices": [
                    "It's not, single readings are sufficient",
                    "It reveals gradual degradation before failure occurs",
                    "It reduces the need for oil changes",
                    "It replaces borescope inspections"
                ],
                "answer": 1
            },
            {
                "q": "What does SOAP testing analyze?",
                "choices": [
                    "Fuel octane rating",
                    "Trace metal particles in engine oil",
                    "Exhaust gas color",
                    "Cabin air quality"
                ],
                "answer": 1
            },
            {
                "q": "Why can a sudden spike in a wear metal matter even within a nominal range?",
                "choices": [
                    "It never matters",
                    "It suggests a rapid change in wear rate",
                    "It only affects fuel economy",
                    "It indicates the oil brand is wrong"
                ],
                "answer": 1
            },
            {
                "q": "What does a 1x rotor speed vibration peak often indicate?",
                "choices": [
                    "Normal operation always",
                    "Imbalance",
                    "Fuel contamination",
                    "Low oil pressure"
                ],
                "answer": 1
            },
            {
                "q": "Why maintain a photographic/video borescope trend history?",
                "choices": [
                    "For marketing photos",
                    "To distinguish pre-existing findings from newly progressing damage",
                    "It's not useful",
                    "To replace all inspections"
                ],
                "answer": 1
            }
        ]
    }
]

EXT19_FLASHCARDS = [
    {
        "front": "Neutral flame (oxy-acetylene)",
        "back": "Equal oxygen/acetylene; preferred for most steel welding"
    },
    {
        "front": "Why flux for aluminum welding?",
        "back": "Dissolves the instant oxide layer to allow fusion"
    },
    {
        "front": "TIG current for aluminum",
        "back": "AC \u2014 provides oxide-cleaning action"
    },
    {
        "front": "Purpose of bonding jumpers",
        "back": "Establish common low-resistance electrical potential"
    },
    {
        "front": "Static wick location",
        "back": "Trailing edges of wings and control surfaces"
    },
    {
        "front": "Bonding resistance test tool",
        "back": "Low-resistance ohmmeter (milliohmmeter)"
    },
    {
        "front": "Annual inspection interval",
        "back": "Every 12 calendar months (14 CFR 91.409)"
    },
    {
        "front": "Is an AD mandatory?",
        "back": "Yes, unless a specific exemption is granted"
    },
    {
        "front": "Who approves return to service after annual?",
        "back": "An IA (Inspection Authorization) holder"
    },
    {
        "front": "Modern fabric covering material",
        "back": "Synthetic polyester (Ceconite/Poly-Fiber systems)"
    },
    {
        "front": "Purpose of rib stitching",
        "back": "Attaches fabric to wing ribs securely"
    },
    {
        "front": "Fabric strength test tool",
        "back": "Calibrated punch-type fabric tester"
    },
    {
        "front": "SOAP testing purpose",
        "back": "Detects trace wear metals suspended in engine oil"
    },
    {
        "front": "Elevated iron in SOAP sample may indicate",
        "back": "Cylinder/piston wear"
    },
    {
        "front": "Vibration analysis use",
        "back": "Detect imbalance, misalignment, bearing/blade faults"
    },
    {
        "front": "Why keep borescope video trend history?",
        "back": "Distinguish old stable blemishes from new progressing damage"
    }
]

EXT19_GLOSSARY = [
    {
        "term": "Neutral Flame",
        "def": "Oxy-acetylene flame with equal oxygen and acetylene, preferred for steel welding."
    },
    {
        "term": "Carburizing Flame",
        "def": "Oxy-acetylene flame with excess acetylene, adds carbon to weld metal."
    },
    {
        "term": "GTAW (TIG)",
        "def": "Gas Tungsten Arc Welding; uses non-consumable tungsten electrode and inert gas shielding."
    },
    {
        "term": "Bonding Jumper",
        "def": "Low-resistance conductor connecting metal parts to equalize electrical potential."
    },
    {
        "term": "Static Discharger",
        "def": "Device (static wick) that bleeds off airframe static charge to reduce radio interference."
    },
    {
        "term": "Milliohmmeter",
        "def": "Precision low-resistance meter used for bonding and continuity checks."
    },
    {
        "term": "Airworthiness Directive (AD)",
        "def": "FAA-mandated corrective action for an unsafe condition; compliance is legally required."
    },
    {
        "term": "Service Bulletin (SB)",
        "def": "Manufacturer-issued recommendation, not mandatory unless referenced by an AD."
    },
    {
        "term": "Inspection Authorization (IA)",
        "def": "FAA certificate allowing approval of annual inspections for return to service."
    },
    {
        "term": "Ceconite",
        "def": "Brand of polyester aircraft covering fabric system."
    },
    {
        "term": "Rib Stitching",
        "def": "Lock-stitch method of attaching fabric covering to wing ribs."
    },
    {
        "term": "Fabric Punch Tester",
        "def": "Calibrated instrument measuring force to punch through covering fabric, checked against minimum strength."
    },
    {
        "term": "SOAP (Oil Analysis)",
        "def": "Spectrometric Oil Analysis Program; detects trace wear metals in engine oil."
    },
    {
        "term": "Trend Monitoring",
        "def": "Tracking engine parameters over time to detect gradual degradation before failure."
    }
]

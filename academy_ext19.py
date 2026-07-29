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
        , {"heading": "Post-Weld Heat Treatment and Stress Relief", "body": "Welded steel structures, especially those made from 4130 chromoly, often require post-weld normalizing or stress-relieving heat treatment to restore ductility and relieve residual stresses introduced by the welding thermal cycle. Without proper heat treatment, welded joints can retain brittle microstructures near the heat-affected zone that are prone to cracking under cyclic loading. Technicians must follow the applicable manufacturer or AC 43.13-1B guidance for time-temperature profiles, and welds on primary structure typically require inspection and sign-off by an appropriately rated welder before return to service."}, {"heading": "Welding Equipment Setup and Regulator Safety", "body": "Oxy-acetylene welding equipment requires correct regulator setup with pressure gauges rated for the specific gas service, since acetylene regulators and hoses use reverse (left-hand) threads specifically to prevent accidental cross-connection with oxygen equipment. Acetylene must never be used at line pressures above 15 psi due to its instability at higher pressures, and acetylene cylinders must always be stored and used in the upright position since the acetylene is dissolved in a stabilizing liquid (typically acetone) that can be drawn into the regulator if the cylinder is tipped. Flashback arrestors and check valves on both the oxygen and acetylene lines prevent flame or gas backflow into the hoses and regulators, a critical safety feature that must be verified functional before each use."}, {"heading": "Weld Discoloration as a Heat Input Indicator", "body": "The color of the heat-affected zone (HAZ) surrounding a weld on stainless steel provides mechanics with a visual indicator of how much heat was applied during welding, since different oxide colors form at specific temperature ranges as the metal cools from the weld pool outward. A light straw color indicates minimal heat input and good shielding gas coverage, while progressively darker colors moving through gold, purple, blue, and finally a dull gray or black indicate increasing heat input and potential over-heating that can degrade the material's corrosion resistance and mechanical properties. Excessive blue or black discoloration extending far from the weld bead suggests inadequate gas shielding or excessive heat input, either of which may require the weld to be rejected and redone per the applicable weld inspection criteria. Experienced welders and inspectors use this color pattern as a quick visual quality check before more rigorous inspection methods like dye penetrant or X-ray are applied."}, {"heading": "Preheating Requirements for Welding Thick-Section Steel", "body": "Welding thicker steel sections or certain steel alloys with higher carbon content may require preheating the base metal before welding begins, since rapid heating and cooling during welding on cold, thick material can create excessive thermal stress and hardening in the heat-affected zone that increases the risk of cracking, particularly in alloys susceptible to hydrogen-induced cracking or those with limited ductility in the as-welded condition. Preheat temperature and the method used to achieve and verify it (such as temperature-indicating crayons, contact pyrometers, or infrared thermometers) are specified in the welding procedure for the specific material and thickness combination, and preheat must be verified and maintained throughout the welding operation, not just applied once before starting, since heat loss during a multi-pass weld on a large structure can allow the material to cool below the required preheat temperature partway through the job. Interpass temperature control, maintaining minimum temperature between weld passes on a multi-pass weld, serves a similar purpose to initial preheat, preventing excessive cooling and associated stress buildup between passes on thicker sections requiring multiple weld passes to complete. Mechanics performing structural steel welding repairs must follow the approved welding procedure's preheat and interpass temperature requirements exactly, since deviating from these thermal management requirements can introduce cracking risk even when weld technique and filler material selection are otherwise correct."},
    {"heading": "Oxy-Acetylene Torch Tip Selection and Flame Adjustment Technique", "body": "Proper oxy-acetylene welding requires selecting a torch tip sized appropriately for the material thickness being welded, since an undersized tip cannot deliver adequate heat for the joint, resulting in poor fusion or excessive time in the heat-affected zone, while an oversized tip risks excessive heat input causing warping, burn-through, or unwanted metallurgical changes in the surrounding base metal. Flame adjustment is critical to weld quality: a neutral flame, characterized by a well-defined inner cone with no excess oxygen, oxidizing, or excess acetylene, carburizing, feather visible, is required for most aircraft welding applications since a carburizing flame can introduce excess carbon into the weld, embrittling it, while an oxidizing flame can burn out alloying elements and create a weak, porous weld. Technicians must adjust the oxygen and acetylene regulator pressures and torch valve settings to achieve and maintain a neutral flame throughout the welding operation, periodically checking flame character since flame quality can drift as cylinder pressure drops or as the torch tip heats up during extended use. Proper technique also requires holding the torch at the correct angle and distance from the workpiece to control heat input and puddle formation, since even with correct tip size and flame adjustment, poor torch handling technique, excessive dwell time, incorrect travel speed, or improper angle, can still produce a substandard weld."}],
        "quiz": [ {"q": "Why might preheating be required before welding thicker steel sections or certain higher-carbon steel alloys?", "choices": ["Preheating is purely a cosmetic step with no metallurgical purpose", "Rapid heating and cooling on cold, thick material can create excessive thermal stress and hardening that increases cracking risk in the heat-affected zone", "All steel welding requires identical preheat regardless of thickness or alloy", "Preheating is only relevant for aluminum welding, never steel"], "answer": 1}, {"q": "On a stainless steel weld, what does extensive dark blue or black discoloration in the heat-affected zone typically indicate?", "choices": ["Perfect weld quality with no concerns", "Excessive heat input or inadequate shielding gas coverage that may require the weld to be rejected", "The weld is under-heated", "The base metal was contaminated before welding"], "answer": 1}, {"q": "Why must acetylene cylinders always be stored and used in the upright position?", "choices": ["For easier transport only", "Acetylene is dissolved in a stabilizing liquid that can be drawn into the regulator if tipped", "To save floor space", "Upright storage has no safety purpose"], "answer": 1, "explain": "Acetylene is dissolved in a stabilizing liquid inside the cylinder; tipping the cylinder risks drawing that liquid into the regulator, which is a serious hazard."}, {"q": "Why is post-weld heat treatment often required on 4130 chromoly steel structures?", "choices": ["To add color to the weld", "To restore ductility and relieve residual stresses in the heat-affected zone", "To increase weld porosity", "To reduce material cost"], "answer": 1, "explain": "Welding thermal cycles can leave brittle microstructures near the weld; heat treatment restores ductility and relieves stress that could otherwise lead to cracking."},
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
            },
    {"q": "Why is a neutral oxy-acetylene flame required for most aircraft welding applications rather than a carburizing or oxidizing flame?", "choices": ["Flame character has no effect on weld quality", "A carburizing flame can embrittle the weld with excess carbon while an oxidizing flame can burn out alloying elements, both weakening the weld", "Neutral flames only matter for aesthetic weld appearance", "Carburizing and oxidizing flames are simply alternative names for the same flame type"], "answer": 1}
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
        , {"heading": "Bonding Jumper Installation Practices", "body": "Bonding jumpers must be as short and direct as possible to minimize resistance, with braided copper straps preferred over solid wire for flexing joints like control surfaces and landing gear. Jumpers are attached using star washers or serrated washers under the terminal lug to bite through anodizing or paint and ensure metal-to-metal contact. Avoid routing jumpers where they can be pinched, chafed, or subjected to repeated flexing fatigue. Each jumper should be inspected for corrosion, fraying strands, and secure terminal crimps during scheduled inspections, and any jumper exceeding resistance limits must be replaced, not just cleaned."}, {"heading": "Fastener Bonding Requirements on Composite Structures", "body": "Composite aircraft structures require special attention to bonding since the composite material itself is often non-conductive or only marginally conductive, meaning bonding paths must be engineered explicitly through embedded conductive layers (expanded copper foil or metal mesh) rather than relying on the structure itself. Fasteners penetrating composite skins for bonding purposes typically require conductive sealant or specific fastener coatings to maintain continuity across the joint, and standard bonding resistance checks used on metal structure may need adapted procedures and tolerances for composite bonding paths. Repairs to composite structure that do not restore the embedded conductive layer can leave a bonding discontinuity that is invisible until a lightning strike or static event reveals it."}, {"heading": "Bonding for Fuel System Components and Explosion Prevention", "body": "Fuel system components, including tanks, filler caps, fuel lines, and fueling equipment, require careful electrical bonding to prevent static charge buildup that could produce a spark capable of igniting fuel vapors, particularly during fueling and defueling operations when friction and fluid flow generate static electricity. Bonding jumpers connect fuel nozzles, hoses, and grounding points to the aircraft and fueling equipment, establishing a common electrical potential so no spark-producing voltage differential can develop between them. Internal fuel tank components, such as boost pump wiring and level sensors, must meet stringent bonding and shielding requirements since any internal spark inside a fuel tank containing flammable vapor could be catastrophic; this is why fuel tank wiring is subject to strict maintenance practices under fuel tank safety programs like those addressing Center Wing Tank ignition sources. Mechanics performing fuel system maintenance must verify bonding continuity and follow approved procedures precisely, since improper bonding in fuel systems is a demonstrated cause of fuel tank explosions in aviation history."}, {"heading": "Bonding Continuity Testing Equipment and Technique", "body": "Bonding resistance testing uses a specialized bonding/grounding ohmmeter capable of accurately measuring the very low resistance values (typically fractions of an ohm) required for aircraft bonding connections, since standard multimeters lack the resolution and accuracy needed at these low resistance levels and can give misleadingly acceptable readings for a bonding path that is actually marginal or degraded. Proper technique requires clean, tight probe contact directly on bare metal at both measurement points, since any paint, corrosion, or oxide film between the probe tip and the actual metal substrate can introduce measurement error that masks a true bonding resistance problem, making surface preparation at test points an important step before measurement rather than an optional convenience. Bonding jumpers, straps, and their attachment hardware must be inspected for physical damage, corrosion, and secure attachment, since a bonding jumper that measures acceptable resistance today can develop increased resistance over time due to loosening, corrosion, or fatigue if not adequately protected and periodically re-verified. Bonding test point locations, resistance limits, and required test equipment specifications are documented in the aircraft's maintenance manual, and mechanics must follow these specific requirements rather than assuming general electrical continuity testing principles apply identically to structural bonding verification."},
    {"heading": "Bonding Jumper Material Selection and Environmental Durability", "body": "Bonding jumper material and construction must be selected to withstand the specific environmental conditions at its installation location while maintaining low electrical resistance throughout its service life. Jumpers in areas exposed to significant flexing or vibration, such as across movable control surface hinges or engine mounts, require flexible braided construction that can withstand repeated flexing cycles without fatigue failure of individual strands, while jumpers in more static locations may use simpler solid or less flexible conductor designs. Jumper terminal end fittings must be compatible with the structure they attach to, using appropriate plating or material to avoid introducing a new galvanic corrosion couple at the attachment point itself, and attachment hardware, bolts and washers, must provide adequate contact pressure and area to maintain low resistance without loosening over time due to vibration. Jumpers installed in areas exposed to fluids, such as near hydraulic or fuel system components, must use materials and finishes resistant to those specific fluids, since fluid exposure can accelerate corrosion of an improperly specified jumper material, progressively increasing resistance until the jumper no longer provides adequate bonding function even though it may appear physically intact. Technicians selecting replacement bonding jumpers must match not just the electrical requirements but also the mechanical and environmental service conditions of the specific installation location, since a jumper that is electrically adequate but mechanically or environmentally mismatched for its location will likely fail prematurely."},
    {"heading": "Static Discharger Design, Installation Spacing, and Replacement Criteria", "body": "Static dischargers, also called static wicks, provide a controlled path for static electrical charge that accumulates on the aircraft's surfaces during flight through corona discharge from the discharger's fine wire or resistive tip into the surrounding airstream, preventing the random arcing and electrical noise that uncontrolled static buildup would create in radio and navigation receiver frequencies. Their effectiveness depends on both the discharger's design, specifically its ability to initiate corona discharge at relatively low voltage differentials, and its placement at the trailing edges and extremities of wings, horizontal and vertical stabilizers, and control surfaces where static charge naturally concentrates at sharp edges in high electric field gradient regions. Installation and spacing requirements are specified in the aircraft's maintenance manual and must be strictly followed, since undershooting the required number of dischargers or mislocating them on surfaces with lower charge concentration can leave charge accumulation at tips and trailing edges where the uninstalled dischargers were intended to function. Physical condition inspection of static dischargers includes checking the discharge element, typically a fine wire or carbon-impregnated resistive tip, for loss of material from electrical erosion or mechanical damage, since a worn or broken discharge element loses the fine point geometry that initiates corona at a sufficiently low voltage, degrading its function even though the mounting bracket and electrical connection may remain intact. Electrical resistance measurement of each discharger from the mounting base to the tip should be within the manufacturer's specified range, since the resistor element within the discharger body limits current during a direct lightning strike to protect the attachment point structure, and a discharger with an out-of-range resistance, either too low which would concentrate excessive current during a strike or too high which would impair normal discharge function, should be replaced."}],
        "quiz": [ {"q": "Why must bonding resistance testing use a specialized low-resistance ohmmeter rather than a standard multimeter?", "choices": ["Standard multimeters are always sufficient for bonding testing", "Standard multimeters lack the resolution and accuracy needed at the very low resistance values required for bonding verification, potentially masking a marginal connection", "Bonding resistance testing requires no special equipment", "Multimeters cannot measure resistance at all"], "answer": 1}, {"q": "Why is proper electrical bonding especially critical for fuel system components?", "choices": ["It has no real safety purpose, only regulatory compliance", "To prevent static charge buildup and spark potential that could ignite flammable fuel vapors", "To reduce fuel consumption", "To improve fuel gauge accuracy only"], "answer": 1}, {"q": "Why does bonding on composite aircraft structures require special engineering?", "choices": ["Composites are always more conductive than metal", "Composite material is often non-conductive, requiring embedded conductive layers for bonding paths", "Bonding is not needed on composites", "Composite fasteners never need coating"], "answer": 1, "explain": "Since composite material is largely non-conductive, bonding paths must be engineered through embedded conductive layers rather than relying on the base material."}, {"q": "Why are serrated or star washers used when installing bonding jumpers?", "choices": ["To add decorative finish", "To bite through anodizing or paint for solid metal-to-metal contact", "To reduce jumper weight", "To increase jumper flexibility"], "answer": 1, "explain": "Serrated washers cut through nonconductive coatings to guarantee low-resistance electrical continuity at the bonding point."},
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
            },
    {"q": "Why must bonding jumpers across control surface hinges use flexible braided construction rather than solid conductor material?", "choices": ["Braided construction has no advantage over solid conductor for this application", "Braided construction withstands repeated flexing cycles without fatigue failure of individual strands, needed at moving joints", "Solid conductors provide better bonding at moving joints", "Flexing has no effect on bonding jumper integrity"], "answer": 1},
    {"q": "Why is individual resistance measurement of static dischargers required rather than relying on visual condition inspection alone?", "choices": ["The resistor element inside the discharger limits current during lightning strikes and affects normal discharge performance, and out-of-range resistance is not detectable visually", "Visual inspection is always sufficient to determine static discharger serviceability", "Static discharger resistance never changes during service and does not require measurement", "Resistance measurement only applies to dischargers on composite surfaces, not metal aircraft"], "answer": 0}
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
        , {"heading": "Special Inspections Triggered by Events", "body": "Beyond routine calendar or hour-based inspections, special inspections are triggered by specific events such as hard landings, lightning strikes, bird strikes, overspeed or overtemperature exceedances, and severe turbulence encounters, each with manufacturer-specified inspection scopes tailored to the type of event. A hard landing inspection, for example, typically requires detailed examination of landing gear attach structure, wing spar areas, and engine mount hardware even if no damage is visually apparent, since overstress damage can be internal or below the visible threshold. Skipping event-triggered special inspections because the aircraft \"flew fine\" afterward is a significant safety risk, since some overstress damage only manifests as a failure much later under normal operating loads."}, {"heading": "Time-in-Service vs Calendar-Based Inspection Intervals", "body": "Inspection programs schedule tasks based on either time-in-service (flight hours, cycles, or landings) or calendar time (days, months, years), and many aircraft use a combination of both, whichever comes first. Time-in-service intervals track actual usage and wear accumulation, appropriate for components that degrade primarily through operational stress such as engine hot-section parts or landing gear cycling. Calendar-based intervals address degradation that occurs regardless of usage, such as elastomer seal aging, corrosion progression, or battery self-discharge, which continue even while an aircraft sits idle. Mechanics tracking compliance must maintain accurate records of both hours/cycles and calendar dates for each applicable inspection item, since an aircraft that flies infrequently may become due for a calendar-based inspection well before it accumulates the equivalent flight hours, and missing this distinction is a common source of inspection program non-compliance."}, {"heading": "Continuous Airworthiness Maintenance Program (CAMP) Structure", "body": "Continuous Airworthiness Maintenance Programs (CAMPs), used primarily by Part 121 and larger Part 135 operators, replace the simpler annual/100-hour inspection model with a comprehensive, ongoing maintenance program that schedules individual tasks (rather than one comprehensive inspection event) at intervals tailored to each specific task's failure characteristics and criticality, informed by reliability data and manufacturer maintenance planning documents. CAMPs are built around a Maintenance Review Board (MRB) report or Maintenance Steering Group (MSG-3) analysis performed during aircraft type certification, which systematically evaluates each system and structural area to determine appropriate task types (such as scheduled inspection, on-condition monitoring, or hard-time replacement) and intervals based on failure consequence severity and detectability. Under a CAMP, individual maintenance tasks are distributed across different check levels (such as A-checks, C-checks, and D-checks on transport aircraft) that group tasks by required access level and typical interval, rather than requiring the entire aircraft to be inspected comprehensively at a single fixed interval as under simpler inspection programs. Operators maintaining a CAMP must have an FAA-approved program description and are subject to ongoing oversight of program effectiveness, including reliability tracking that can result in interval adjustments if in-service data reveals a task is being performed more or less frequently than warranted by actual component performance."},
    {"heading": "Inspection Interval Escalation and De-escalation Based on Fleet Data", "body": "Scheduled inspection intervals are not necessarily fixed for the life of an aircraft type; manufacturers and operators can adjust, escalate or de-escalate, inspection intervals based on accumulated fleet reliability and inspection finding data, subject to regulatory approval of the revised program. Interval escalation, extending the time or cycles between a given inspection, is typically supported when fleet-wide inspection history shows a consistently low finding rate for the item in question across a sufficiently large sample of aircraft and accumulated time, indicating the item degrades more slowly than the original conservative interval assumed; escalation must be approved through the applicable reliability program or manufacturer service bulletin process and cannot simply be adopted unilaterally by an individual operator without proper substantiation and approval. Conversely, de-escalation, shortening an inspection interval, may be mandated if fleet data reveals a higher-than-expected finding rate, an unanticipated failure mode, or a specific fleet campaign following an in-service event, and can be implemented through an airworthiness directive or manufacturer alert service bulletin requiring more frequent inspection until the underlying issue is understood or corrected. Operators participating in a reliability program contribute their own fleet's inspection and discrepancy data to this broader analysis process, meaning individual operator maintenance and inspection documentation quality directly affects the accuracy of fleet-wide escalation and de-escalation decisions across the entire aircraft type's operator community."},
    {"heading": "Airworthiness Directive Compliance Tracking and Repetitive AD Management", "body": "Airworthiness Directives, which are legally enforceable regulations requiring specific inspections, modifications, or operating limitations on aircraft, engines, propellers, or appliances when an unsafe condition is found to exist, fall into two broad categories for maintenance tracking purposes: one-time ADs that require a single action and are then closed, and repetitive ADs that require recurring inspection or maintenance at specified intervals for the life of the article, the latter of which must be actively tracked across the aircraft's entire service life. Repetitive AD management requires the operator or repair station to maintain a current status list that identifies each open repetitive AD, when it was last complied with, what the compliance interval is, and when the next compliance action is due, since missing a repetitive AD compliance deadline makes the aircraft unairworthy even if no physical problem exists and all other maintenance is current. When an aircraft changes ownership or enters a new maintenance program, establishing the compliance status of all applicable ADs is a critical first step that may require research through logbook records, previous repair station work orders, and sometimes the manufacturer's records service when logbook documentation is incomplete, since the new operator inherits all existing AD compliance obligations and assuming a previous operator's records are complete without verification is a known source of AD non-compliance discoveries. AD applicability determination requires reading the AD carefully and matching its applicability clause, which typically specifies by aircraft type certificate, engine model, serial number range, or part number, against the specific hardware installed on the aircraft being maintained, and technicians should note that applicability to an aircraft type does not necessarily mean applicability to every individual aircraft of that type, since serial number range restrictions, retrofit status, or specific configuration criteria can exclude certain individual aircraft from a given AD's scope. Compliance method selection, where an AD offers multiple means of compliance such as a one-time terminating action versus continuing periodic inspection, should be documented with the specific compliance method used, since different compliance methods carry different subsequent requirements and future maintenance personnel must know which method was chosen to determine what is required going forward."}],
        "quiz": [ {"q": "What analytical foundation is a Continuous Airworthiness Maintenance Program (CAMP) typically built around?", "choices": ["A single fixed annual inspection interval applied uniformly to all systems", "A Maintenance Review Board report or MSG-3 analysis that determines task types and intervals based on failure consequence and detectability", "CAMPs require no systematic analytical foundation", "CAMPs are only used for reciprocating engine aircraft"], "answer": 1}, {"q": "Why do some aircraft inspection items use calendar-based intervals instead of flight-hour intervals?", "choices": ["Calendar intervals are always more convenient for scheduling", "Some degradation, like seal aging or corrosion, continues even when the aircraft is not flown", "Flight hours are impossible to track accurately", "Calendar-based intervals are required by all regulations universally"], "answer": 1}, {"q": "Why are event-triggered special inspections (e.g., after a hard landing) still necessary even if the aircraft appears to fly normally afterward?", "choices": ["They are optional and rarely necessary", "Overstress damage can be internal or below the visible threshold and may fail later under normal loads", "Special inspections are only for cosmetic damage", "The aircraft flying fine guarantees no damage occurred"], "answer": 1, "explain": "Overstress damage from events like hard landings can be hidden or internal, and normal-appearing flight afterward does not rule out damage that could fail later."},
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
            },
    {"q": "What typically supports an inspection interval escalation (lengthening the interval) for a scheduled maintenance item?", "choices": ["A single operator's opinion that the interval is too short", "Fleet-wide inspection history showing a consistently low finding rate across a sufficiently large sample of aircraft and time", "Escalation requires no data or approval process", "Escalation can only be applied to brand new aircraft types with no service history"], "answer": 1},
    {"q": "Why must an operator maintain an active tracking list specifically for repetitive ADs rather than treating them as closed after initial compliance?", "choices": ["Repetitive ADs require recurring action at specified intervals throughout the aircraft's life, and missing a compliance deadline makes the aircraft unairworthy even when all other maintenance is current", "All ADs become permanently closed after the first compliance action is recorded", "Repetitive AD tracking is optional for aircraft operated under general aviation rules", "AD compliance intervals are automatically extended whenever an aircraft changes ownership"], "answer": 0}
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
        , {"heading": "Finishing Coats and UV Protection", "body": "After dope application and fabric tautening, finishing coats including aluminum pigmented dope or UV-blocking topcoats protect the fabric from ultraviolet degradation, which is the leading cause of premature fabric failure independent of mechanical wear. Silver or aluminum dope reflects UV radiation, while color topcoats provide the final aesthetic and additional UV barrier. Manufacturers specify minimum numbers of coats and dry film thickness, and applying insufficient UV protection can cut fabric service life dramatically even though the fabric appears sound. Punch testing during inspections should always be paired with a visual check of finish coat condition and chalking."}, {"heading": "Fabric Repair Patch Techniques", "body": "Small fabric damage such as tears or punctures can often be repaired with a doped-on fabric patch rather than requiring a full recover, provided the damage does not exceed the size limits specified in the applicable STC or manufacturer data. Patch material must match the original fabric weight and weave, with edges pinked or heat-sealed to prevent fraying, and the patch is typically oversized to extend well beyond the damage before doping in place with matching dope coats. Patches must be documented in the aircraft records with the STC or data reference used, the size and location of the repair, and the technician's certificate number, since undocumented fabric repairs are a common inspection discrepancy."}, {"heading": "Fabric Covering Regulatory Requirements and STC Compliance", "body": "Fabric covering work must be performed using an approved covering process, whether that is the original type-certificated process or a Supplemental Type Certificate (STC) covering system such as those from Poly-Fiber, Ceconite, or Stits, and mechanics must follow the specific manufacturer's instructions for that STC exactly since mixing components or techniques from different systems can compromise the finished product. The STC documentation specifies approved fabric weights, adhesives, dope formulations, and application sequences, and deviating from these approved processes without additional engineering approval can render the aircraft's airworthiness certificate invalid. Mechanics must maintain accurate records of which covering system was used, including batch numbers of materials where required, since this traceability is essential for future repairs or recovering work to remain compliant with the original STC. Any repair to fabric-covered structure should use materials and methods compatible with the original covering system to avoid chemical incompatibility between old and new dope or adhesive layers."}, {"heading": "Fabric Tautness Assessment and Rib Lacing Tension", "body": "Proper fabric covering tautness, achieved through the shrinking action of dope application during the finishing process, must be verified using a tautness testing tool (such as a Poly-Fiber Tautness Tester or similar calibrated device) that measures fabric tension by deflection under a known applied force, since fabric that is too loose can flutter or billow in flight, potentially causing aerodynamic disturbance or accelerated wear, while excessively tight fabric can create excessive stress on the underlying structure or rib lacing. Rib lacing, which secures fabric to wing and control surface ribs, requires specific lacing patterns, cord type, and knot/tie methods specified by the covering process's approved instructions, and lacing that is too loose allows the fabric to shift or billow between ribs while lacing that is too tight can distort the rib or fabric shape. Rib lacing anti-chafe tape or reinforcing patches at lacing points protect both the fabric and the lacing cord itself from wear caused by the repeated small movements and stress concentration at each lacing point over the aircraft's operational life. Periodic reinspection of fabric tautness and rib lacing condition, not just at the initial covering job, is necessary since fabric tension can change over time due to environmental exposure, UV degradation of the fabric or finish, and normal aging of the dope finish system."},
    {"heading": "Fabric Covering Envelope System Selection and Compatibility", "body": "Modern fabric covering relies on complete envelope systems, such as those certified under a Supplemental Type Certificate, where the fabric material, cements, tapes, finishing tapes, and topcoat products are all formulated to be chemically and mechanically compatible with one another. Mixing components from different manufacturers' systems, even if each individual product seems similar, risks solvent incompatibility that can cause adhesive failure, fabric degradation, or finish lifting months or years after application. The technician must identify the STC or process specification governing the aircraft's covering and use only the approved materials list for that system, documenting the specific product names and batch or lot numbers in the aircraft records. Polyester fabrics, the most common modern covering material, are heat-shrunk in stages using a calibrated iron or heat gun, with the manufacturer's specified temperature ranges strictly observed since overheating can degrade fiber strength while underheating leaves the fabric loose and prone to drumming. Rib lacing or rib stitching, where used instead of adhesive rib attachment, must follow the specified cord type, knot pattern, and spacing from the structural repair manual, since incorrect lacing spacing can allow fabric to billow excessively between ribs under aerodynamic load. Ultraviolet-blocking topcoats are not merely cosmetic; they are a required protective layer that prevents UV degradation of the fabric itself, and coverage gaps in the topcoat create localized weak points that can lead to premature fabric failure."}],
        "quiz": [ {"q": "Why must fabric covering tautness be measured with a calibrated tautness tester rather than judged by touch or visual appearance alone?", "choices": ["Tautness has no effect on aircraft performance or fabric life", "A calibrated tool provides an objective measurement, since fabric that is too loose can flutter in flight while excessively tight fabric can stress the underlying structure", "Visual and touch assessment is always more accurate than instrumented measurement", "Tautness testing is only relevant during initial covering, never for reinspection"], "answer": 1}, {"q": "Why must mechanics strictly follow a single STC covering system's specified materials and procedures when covering a fabric aircraft?", "choices": ["Because mixing components from different systems has no effect on safety", "Because mixing materials or techniques from different STC systems can compromise the finished covering and invalidate airworthiness compliance", "Because the FAA requires only one brand exist", "Because fabric covering has no regulatory requirements"], "answer": 1}, {"q": "What must fabric repair patch material match from the original covering?", "choices": ["Color only", "Fabric weight and weave", "Nothing, any fabric works", "Thickness only, not weave"], "answer": 1, "explain": "Patch fabric must match the original weight and weave to maintain consistent strength and proper dope adhesion across the repair."}, {"q": "What is the leading cause of premature fabric covering failure aside from mechanical damage?", "choices": ["Excessive humidity only", "Ultraviolet radiation degradation", "Cabin pressurization cycles", "Engine vibration"], "answer": 1, "explain": "UV radiation breaks down fabric fibers over time; aluminum/silver dope and UV-blocking topcoats are applied specifically to protect against this degradation."},
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
            },
    {"q": "Why is mixing fabric covering components from different manufacturers' STC systems considered risky?", "choices": ["The products may be chemically or mechanically incompatible, risking adhesive failure or finish lifting", "It is always cheaper to use a single manufacturer's products", "Regulations explicitly forbid owning products from more than one manufacturer", "Mixed systems automatically void the aircraft's airworthiness certificate"], "answer": 0}
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
        , {"heading": "Setting Trend Monitoring Alert and Action Limits", "body": "Effective condition monitoring programs establish two-tier limits: alert limits that trigger increased monitoring frequency, and action limits that require maintenance intervention, both derived from statistical analysis of the specific engine's historical trend data rather than generic fleet-wide values alone. Setting limits too tight generates excessive false alarms that erode technician confidence in the program, while limits set too loose miss developing problems until they become urgent. Many operators use a rate-of-change threshold in addition to absolute value limits, since a rapidly increasing trend approaching but not yet exceeding the absolute limit can indicate a developing fault requiring attention sooner than the absolute limit alone would trigger."}, {"heading": "Exceedance Reporting and Engine Health Trend Software", "body": "Engine exceedance events, such as an overtemperature, overspeed, or overtorque condition during flight, are automatically flagged by engine monitoring systems and must be reported and evaluated per the engine manufacturer's exceedance limits and required inspection actions, which vary based on how far and how long the limit was exceeded. Modern engine health monitoring software aggregates trend data across an entire fleet, using algorithms to detect subtle parameter drift, such as a gradual rise in exhaust gas temperature margin loss, that might not trigger an individual exceedance but indicates developing deterioration warranting proactive maintenance. This fleet-wide data also enables comparison of an individual engine's trends against its peers, helping distinguish between normal engine-to-engine variation and a genuine developing fault. Mechanics and reliability engineers use exceedance reports and trend software output together, since an isolated exceedance may require immediate borescope inspection while gradual trend drift may only require closer monitoring or scheduling maintenance at a more convenient interval."},
    {"heading": "Magnetic Chip Detector Function and Inspection", "body": "Magnetic chip detectors (chip detectors or MCDs) are magnetic plugs installed in the oil system, often at the sump drain or a scavenge line, that attract and hold ferrous metal particles carried in the oil, providing a simple, direct physical sample of wear debris that complements oil analysis and filter inspection. Some chip detectors include an electrical circuit that illuminates a cockpit warning light when accumulated debris bridges a gap between electrodes, giving the flight crew an immediate in-flight indication of a developing mechanical problem rather than waiting for a scheduled inspection. At scheduled removal, the quantity, size, and character of debris found on the detector (fine gray fuzz versus larger metallic chips or flakes) is assessed against normal wear expectations, since fine debris is often normal break-in or minor wear while larger chips or flakes are a strong indicator of a developing bearing or gear failure requiring further investigation before further flight."},
    {"heading": "Statistical Process Control Methods Applied to Engine Trend Data", "body": "Engine condition trend monitoring benefits from statistical process control techniques that distinguish genuine developing faults from normal operational variability and instrumentation noise. Rather than reacting to any single data point that deviates from baseline, the technician evaluates whether a parameter has moved outside statistically established control limits, typically expressed as a number of standard deviations from the historical mean for that engine at similar operating conditions. A single exhaust gas temperature spike during an unusually hot day or high-power takeoff may fall within normal scatter, while a sustained upward trend across multiple consecutive flights, even if each individual reading is modest, indicates a real underlying change such as bleed leakage, seal wear, or fouling. Control charts plotting parameters like EGT margin, oil consumption rate, or vibration amplitude over time allow the technician to visually distinguish random variation from a trend requiring investigation. Establishing a valid baseline requires normalizing data for conditions such as outside air temperature, altitude, and power setting, since raw uncorrected data from varying conditions can mask or exaggerate real trends. When a parameter crosses a control limit, the appropriate response is not necessarily immediate engine removal but rather increased monitoring frequency, targeted borescope inspection, or oil analysis to identify root cause before the trend progresses to an operational limit."}],
        "quiz": [ {"q": "What distinguishes a gradual EGT margin trend drift from a reported exceedance event in engine condition monitoring?", "choices": ["They are identical and require the same response", "An exceedance is an immediate limit violation requiring specified action, while gradual trend drift indicates developing deterioration that may only need closer monitoring", "Trend drift is never meaningful data", "Exceedances are only tracked for reciprocating engines"], "answer": 1}, {"q": "Why do effective trend monitoring programs use rate-of-change thresholds in addition to absolute limits?", "choices": ["Rate-of-change thresholds are purely cosmetic", "A rapidly increasing trend can indicate a developing fault before the absolute limit is reached", "Absolute limits are always sufficient alone", "Rate-of-change thresholds replace the need for baselines"], "answer": 1, "explain": "A rapidly changing trend, even below the absolute action limit, can signal a developing problem that needs attention sooner than waiting for the absolute limit to be exceeded."},
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
            },
    {"q": "What distinguishes a chip detector finding of fine gray fuzz from a finding of larger metallic chips or flakes?", "choices": ["Both findings always indicate an identical level of urgency", "Fine fuzz is often normal wear or break-in debris, while larger chips or flakes strongly indicate a developing bearing or gear failure", "Chip detectors cannot distinguish debris size or character", "Fine fuzz is more serious than larger chips because it is harder to see"], "answer": 1},
    {"q": "Why does trend monitoring analysis rely on control limits rather than reacting to any single deviating data point?", "choices": ["To distinguish genuine developing faults from normal operational variability and instrumentation noise", "Because single data points are always recorded incorrectly by the instrumentation", "Because regulations prohibit analyzing individual flight data", "Because control limits eliminate the need for baseline normalization"], "answer": 0}
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

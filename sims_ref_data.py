"""Aviation Maintenance Academy - Sims + Reference Library data."""

# Interactive lab calculators. Rendering/logic lives in avia_features.js keyed by id.
SIMS = [
    {"id":"wb",       "title":"Weight & Balance", "icon":"&#x2696;",  "cat":"General",    "desc":"Add loading stations, compute CG and check the envelope."},
    {"id":"ohm",      "title":"Ohm's Law & Power","icon":"&#x26A1;",  "cat":"Electrical", "desc":"Solve any two of Voltage, Current, Resistance, Power."},
    {"id":"disp",     "title":"Cylinder Displacement","icon":"&#x1F527;","cat":"Powerplant","desc":"Compute engine displacement from bore, stroke, cylinders."},
    {"id":"cr",       "title":"Compression Ratio","icon":"&#x1F6E2;", "cat":"Powerplant", "desc":"Compute CR from cylinder + clearance volume."},
    {"id":"gas",      "title":"Gas Law Solver",   "icon":"&#x1F4A8;", "cat":"General",    "desc":"Boyle, Charles, and Combined gas-law solver (absolute temp)."},
    {"id":"bend",     "title":"Sheet Metal Bend", "icon":"&#x1F4D0;", "cat":"Airframe",   "desc":"Bend allowance, setback, and bend deduction for a layout."},
    {"id":"diffcomp", "title":"Differential Compression","icon":"&#x1F52C;","cat":"Powerplant","desc":"Interpret a cylinder leak-down reading and locate the leak."},
]

# Reference cheat-sheet cards. Grouped by cat; body is HTML.
REFERENCE = [
    {"cat":"Formulas","title":"Ohm's Law Wheel","body":"<b>E = I x R</b> &middot; <b>P = I x E</b> &middot; P = I&sup2;R = E&sup2;/R. Series: Rt = R1+R2+... Parallel: 1/Rt = 1/R1+1/R2+..."},
    {"cat":"Formulas","title":"Engine Math","body":"Displacement = (pi/4) x bore&sup2; x stroke x #cyl. Compression Ratio = V(BDC)/V(TDC). BHP = (Torque x RPM)/5252."},
    {"cat":"Formulas","title":"Weight & Balance","body":"Moment = Weight x Arm. CG = total moment / total weight. Useful load = max weight - empty weight."},
    {"cat":"Formulas","title":"Gas Laws","body":"Boyle: P1V1 = P2V2. Charles: V1/T1 = V2/T2. Combined: P1V1/T1 = P2V2/T2. Always use absolute temperature (K or R)."},
    {"cat":"Formulas","title":"Sheet Metal","body":"Setback = K x (radius + thickness), K=1 for 90 deg. Bend Allowance = (0.01743 x R + 0.0078 x T) x degrees. Min bend radius from alloy/temper chart."},
    {"cat":"Hardware","title":"Rivet Alloy Codes","body":"<b>A</b>=1100 &middot; <b>AD</b>=2117-T3 (most common, drive as-is) &middot; <b>D</b>=2017 &middot; <b>DD</b>=2024-T4 (ice-box) &middot; <b>B</b>=5056 (magnesium). Head: AN470 universal, AN426 100-deg flush."},
    {"cat":"Hardware","title":"Aluminum Alloys","body":"2024-T3 fatigue/skins. 7075-T6 highest strength/spars. 6061-T6 corrosion-resistant/weldable. Alclad = pure-Al cladding for corrosion."},
    {"cat":"Hardware","title":"Bolt / Thread Basics","body":"AN/MS/NAS. Grip must match joint thickness (1-3 threads showing). AN fittings = 37-deg flare (never mix with 45-deg auto). Positive locking required: safety wire, cotter pin, self-locking nut."},
    {"cat":"Fluids","title":"Hydraulic Fluids","body":"MIL-H-5606 = red mineral. MIL-H-83282 = red fire-resistant mineral. Skydrol = purple phosphate-ester (transport, corrosive, PPE). NEVER mix types - destroys seals."},
    {"cat":"Fluids","title":"Fuel Colors","body":"Avgas 80 = red. 100LL = blue. 100 = green. Jet-A = clear/straw. Confirm grade before fueling; check sumps for water."},
    {"cat":"NDT","title":"NDT Method Picker","body":"Dye penetrant: surface cracks, non-porous. Magnetic particle: ferrous only, surface/near-surface. Eddy current: conductive, surface/subsurface. Ultrasonic: internal/thickness. Radiography: internal, needs safety."},
    {"cat":"Powerplant","title":"Differential Compression","body":"Air out exhaust = exhaust valve. Air out intake/carb = intake valve. Air out breather/oil filler = worn rings. Typical minimum 60/80 (check TCDS/mfr)."},
    {"cat":"Powerplant","title":"Turbine Start Faults","body":"Hot start = EGT/ITT over limit. Hung start = lights but won't reach idle. No start = no light-off. Watch N1/N2 rise and fuel scheduling."},
    {"cat":"Powerplant","title":"Magneto Check","body":"Excessive RPM drop = fouled plugs / faulty mag / bad timing. No drop = grounding (P-lead) fault - hot mag hazard. RPM rise on one mag = over-rich or plug issue."},
    {"cat":"Regs","title":"Key CFR Parts","body":"Part 43 = maintenance/preventive/alteration. Part 65 = mechanic certification. Part 91 = general operating rules. 43.9 = records for maint. 43.11 = inspection records. Form 337 = major repair/alteration."},
    {"cat":"Regs","title":"43.9 Record Entry","body":"Required: description of work, date completed, name of person doing work, signature + certificate number + kind of certificate held. RTS approval = return to service."},
    {"cat":"Safety","title":"Fire Class & Extinguisher","body":"A = ordinary combustibles. B = flammable liquids. C = electrical. D = combustible metals (magnesium!). Match the class or make it worse."},
    {"cat":"Safety","title":"Dirty Dozen","body":"Communication, complacency, knowledge, distraction, teamwork, fatigue, resources, pressure, assertiveness, stress, awareness, norms - the 12 human-factors error precursors."},
    {"cat":"General","title":"DME Exam Day Checklist","body":"<b>Bring:</b> Government photo ID, IACRA confirmation number / Airman Knowledge Test report showing passing scores (valid 24 months), completed 8610-2 application, logbook entries proving experience (or 147 school graduation certificate), and payment for the DME/DAR fee. <b>Also bring:</b> your own tools for the practical portion (check with your DME on required list), safety glasses, coveralls, and any approved data / AC 43.13-1B you plan to reference. <b>Before you go:</b> confirm the appointment time/location 24-48hrs ahead, get a full night's sleep, and arrive 15+ minutes early. <b>During the Oral:</b> think out loud, cite your source (handbook/AC/manual) for every answer, and it's OK to look references up - examiners want to see you know WHERE to find the answer, not just memorize it. <b>During the Practical:</b> narrate what you're doing and why as you work; treat every task like a real job with proper documentation."},
]

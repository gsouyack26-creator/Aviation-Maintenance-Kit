"""Aviation Maintenance Academy - Wave 6 sims/reference pack.
Adds 2 new sims: Hydraulic Force & Pressure (Pascal's Law), Oil Consumption Rate.
Merged in build_aviation_academy.py.
"""

EXT12_SIMS = [
    {"id": "hydforce", "title": "Hydraulic Force & Pressure (Pascal's Law)", "icon": "&#x1F527;", "cat": "Airframe",
     "desc": "Compute output force, pressure, or piston area in a hydraulic system using Pascal's Law and mechanical advantage between two pistons."},
    {"id": "oilconsum", "title": "Oil Consumption Rate Estimator", "icon": "&#x1FAA3;", "cat": "Powerplant",
     "desc": "Estimate engine oil consumption rate in quarts per hour from oil added and elapsed flight/run time."},
]

EXT12_REFERENCE = [
    {"cat": "Formulas", "title": "Pascal's Law & Hydraulic Force", "body": "Pressure is transmitted equally throughout a confined fluid: P = F / A. Force output = Pressure x Area. Mechanical advantage between two pistons = A2 / A1, so F2 = F1 x (A2 / A1). A small input force on a small piston can produce a large output force on a larger piston, at the cost of piston travel distance."},
    {"cat": "Formulas", "title": "Oil Consumption Rate", "body": "Oil consumption rate (qt/hr) = quarts of oil added / hours of operation since last servicing. Compare against the engine manufacturer's normal consumption limits in the type certificate data sheet or maintenance manual; a rate above the published limit may indicate worn rings, seals, or a leak."},
    {"cat": "Safety", "title": "Hydraulic System Precautions", "body": "Hydraulic fluid under pressure can penetrate skin and cause serious injury - never search for leaks with bare hands. Always relieve system pressure per the maintenance manual before opening lines or components, and use only the fluid type specified (e.g., MIL-PRF-5606 vs. MIL-PRF-83282/87257) - mixing incompatible fluid types can damage seals."},
    {"cat": "Safety", "title": "Interpreting Oil Consumption Trends", "body": "A single high reading can be a fluke, but a steadily rising oil consumption trend across several flights/inspections is a strong early indicator of internal wear (rings, cylinder walls, turbine seals) and should trigger a borescope inspection, oil filter/screen check for metal, and oil analysis before the trend worsens into a forced landing or in-flight shutdown risk."},
]

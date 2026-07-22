"""Aviation Maintenance Academy - Wave 7 sims/reference pack.
Adds 2 new sims: Cabin Pressurization Differential, Wire Ampacity/Voltage Drop Check.
Merged in build_aviation_academy.py.
"""

EXT14_SIMS = [
    {"id": "cabindiff", "title": "Cabin Differential Pressure", "icon": "&#x1F6EB;", "cat": "Airframe",
     "desc": "Compute cabin differential pressure from cabin altitude and aircraft altitude, and check it against a structural limit."},
    {"id": "wireamp", "title": "Wire Ampacity Check", "icon": "&#x1F50C;", "cat": "General",
     "desc": "Compare a circuit's expected current draw against a wire's rated ampacity to flag undersized wiring."},
]

EXT14_REFERENCE = [
    {"cat": "Formulas", "title": "Cabin Differential Pressure", "body": "Differential pressure = cabin pressure - outside ambient pressure. Standard atmosphere approximation: pressure (inHg) drops roughly 1 inHg per 1,000 ft up to about 10,000 ft. Compare the computed differential against the aircraft's maximum structural differential pressure limit."},
    {"cat": "Formulas", "title": "Wire Ampacity Margin", "body": "Ampacity margin = rated ampacity - expected circuit current. A positive margin means the wire is adequately sized; a small or negative margin indicates the wire may be undersized for the load and should be upsized or the load reduced, per the applicable wire chart."},
    {"cat": "Safety", "title": "Pressurization Structural Limits", "body": "Exceeding the maximum cabin differential pressure can overstress the fuselage pressure vessel. Flight crews and maintenance must respect published limits, and any pressurization system discrepancy (erratic outflow valve, unreliable controller) should be resolved before further pressurized flight."},
    {"cat": "Safety", "title": "Undersized Wiring Hazards", "body": "An undersized wire running near or above its ampacity limit can overheat, degrade insulation, and become an in-flight fire hazard. Always verify wire gauge against the manufacturer's ampacity chart for the specific bundle size, altitude, and insulation type - never assume a wire is adequate based on gauge alone without checking the chart."},
]

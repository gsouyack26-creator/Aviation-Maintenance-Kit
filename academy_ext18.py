"""Aviation Maintenance Academy - Wave 9 sims/reference pack.
Adds 2 new sims: Jack Load Distribution, Turbine EGT Margin Tracker.
Merged in build_aviation_academy.py.
"""

EXT18_SIMS = [
    {"id": "jackload", "title": "Jack Load Distribution", "icon": "\U0001F3D7", "cat": "General",
     "desc": "Estimate the load on each jack point given aircraft weight, CG position, and jack point locations for a simple 3-point jacking setup."},
    {"id": "egtmargin", "title": "Turbine EGT Margin Tracker", "icon": "\U0001F4C8", "cat": "Powerplant",
     "desc": "Compute the margin between current EGT and the redline limit, and flag a shrinking margin trend."},
]

EXT18_REFERENCE = [
    {"cat": "Formulas", "title": "Simple Jack Load Estimate", "body": "For a basic 3-point jacking setup (nose + two main gear points), approximate load sharing can be estimated from aircraft weight and CG position relative to the jack points, similar to a weight-and-balance moment calculation. Always verify against the aircraft-specific jacking procedure rather than relying on a simplified estimate alone."},
    {"cat": "Formulas", "title": "EGT Margin", "body": "EGT margin = redline EGT limit - current EGT reading (at a comparable, stabilized power setting). A shrinking margin over time at the same power setting is a classic indicator of gradual hot-section deterioration and should prompt closer monitoring or inspection."},
    {"cat": "Safety", "title": "Jacking Stability Precautions", "body": "Never leave a jacked aircraft unattended without stabilizing tripod jacks or locks as specified, and always jack on a level, hard, wind-protected surface within the weight/CG limits specified by the manual - overloading a single jack point or jacking outside CG limits risks a serious tip-over."},
    {"cat": "Safety", "title": "Responding to Shrinking EGT Margin", "body": "A shrinking EGT margin trend at consistent power settings should prompt borescope inspection, oil analysis, and review of recent operating history (hot starts, FOD events) - continuing to operate with an eroding margin risks an in-flight EGT limit exceedance or hot-section failure."},
]

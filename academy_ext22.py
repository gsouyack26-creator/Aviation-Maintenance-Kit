"""Aviation Maintenance Academy - Wave 11 sims/reference pack.
Adds 2 new sims: Turbo Overboost Margin, Fuel Quantity Density Correction.
Merged in build_aviation_academy.py.
"""

EXT22_SIMS = [
    {"id": "boostmargin", "title": "Turbo Overboost Margin", "icon": "\U0001F4A8", "cat": "Powerplant",
     "desc": "Compare current manifold pressure against the redline limit to estimate overboost margin and flag unsafe operation."},
    {"id": "fueldensity", "title": "Fuel Quantity Density Correction", "icon": "\u26FD", "cat": "Airframe",
     "desc": "Convert a fuel volume reading (gallons) to mass (pounds) using actual fuel density, useful for weight-and-balance cross-checks against volume-based gauges."},
]

EXT22_REFERENCE = [
    {"cat": "Formulas", "title": "Overboost Margin", "body": "Overboost margin = manifold pressure redline limit - current manifold pressure reading (at the same altitude/power condition). A shrinking or negative margin indicates the wastegate or its controller may not be functioning correctly, and continued operation risks detonation and engine damage."},
    {"cat": "Formulas", "title": "Fuel Volume to Mass Conversion", "body": "Fuel weight (lbs) = fuel volume (gallons) x fuel density (lbs/gallon). Aviation gasoline is commonly approximated near 6.0 lbs/gallon and Jet A near 6.7-6.8 lbs/gallon at standard temperature, but actual density varies with temperature - always use the actual measured or provided density for accurate weight and balance calculations."},
    {"cat": "Safety", "title": "Turbocharger Shutdown Cooldown", "body": "After sustained high-power operation, allow an idle cooldown period before shutting the engine down completely, when practical per the aircraft/engine manufacturer's procedure, to reduce the risk of oil coking in the hot turbocharger bearing housing from oil starvation at shutdown."},
    {"cat": "Safety", "title": "Emergency Equipment Expiration Tracking", "body": "Maintain a dedicated tracking log for all emergency equipment expiration and inspection dates (extinguisher hydrostatic tests, oxygen generator/cylinder dates, ELT battery dates, slide/raft repack intervals) separate from routine airframe inspection tracking, since these items can lapse independent of flight hours and are easy to overlook."},
]

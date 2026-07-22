"""Aviation Maintenance Academy - Wave 5 sims/reference pack.
Adds 2 new sims: Load Factor & Turn Stall Speed, Specific Fuel Consumption.
Merged in build_aviation_academy.py.
"""

EXT10_SIMS = [
    {"id": "loadfactor", "title": "Load Factor & Turn Stall Speed", "icon": "&#x1F504;", "cat": "General",
     "desc": "Compute load factor (G) in a level turn and the resulting increase in stall speed."},
    {"id": "sfc", "title": "Specific Fuel Consumption Estimator", "icon": "&#x26FD;", "cat": "Powerplant",
     "desc": "Estimate specific fuel consumption (SFC) from fuel flow and power/thrust output."},
]

EXT10_REFERENCE = [
    {"cat": "Formulas", "title": "Load Factor in a Level Turn", "body": "n = 1 / cos(bank angle). At 60 deg bank, n = 2.0 (2 G's). Stall speed increases with the square root of load factor: Vs(turn) = Vs1 x sqrt(n). A 60 deg bank turn increases stall speed by about 41%."},
    {"cat": "Formulas", "title": "Specific Fuel Consumption (SFC)", "body": "BSFC (piston, lb/hp/hr) = fuel flow (lb/hr) / brake horsepower. TSFC (turbine, lb/lb-thrust/hr) = fuel flow (lb/hr) / thrust (lb). Lower SFC = more fuel-efficient for the power/thrust produced."},
    {"cat": "Safety", "title": "Accelerated Stalls", "body": "Load factor increases stall speed in any maneuver that isn't 1G level flight - steep turns, pull-ups, and turbulence all raise the effective stall speed. An 'accelerated stall' can occur well above the normal 1G stall speed if the pilot exceeds the critical angle of attack during a high-G maneuver."},
    {"cat": "Safety", "title": "Fuel Planning Margins", "body": "SFC is a snapshot at one power/thrust setting - actual fuel burn varies with altitude, temperature, and power setting throughout a flight. Always use POH/AFM fuel-flow charts (not a single SFC number) for real flight planning, with adequate reserves per regulation."},
]

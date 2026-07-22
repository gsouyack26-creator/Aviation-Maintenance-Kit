"""Aviation Maintenance Academy - Wave 8 sims/reference pack.
Adds 2 new sims: Battery Capacity Check, Mixture Leaning Estimator.
Merged in build_aviation_academy.py.
"""

EXT16_SIMS = [
    {"id": "battcap", "title": "Battery Capacity Check", "icon": "\U0001F50B", "cat": "General",
     "desc": "Compute a battery's remaining capacity percentage from a discharge test and compare it to the serviceability threshold."},
    {"id": "mixlean", "title": "Mixture Leaning Estimator", "icon": "\u26FD", "cat": "Powerplant",
     "desc": "Estimate the recommended fuel-air mixture lean percentage based on density altitude."},
]

EXT16_REFERENCE = [
    {"cat": "Formulas", "title": "Battery Capacity Check", "body": "Capacity % = (measured discharge amp-hours / rated amp-hours) x 100. A common general guideline is that a battery should retain at least 80% of rated capacity to remain serviceable, though exact limits vary by battery type and manufacturer - always check the applicable maintenance manual."},
    {"cat": "Formulas", "title": "Mixture Leaning vs. Density Altitude", "body": "As density altitude increases, air density drops and less oxygen is available per unit volume, so the fuel-air mixture should be leaned to maintain an efficient ratio. Many manufacturers recommend leaning starting around 3,000-5,000 ft density altitude, with the precise procedure specified in the POH/AFM."},
    {"cat": "Safety", "title": "Battery Servicing Hazards", "body": "Battery servicing exposes technicians to corrosive electrolyte (lead-acid) and combustible hydrogen gas released during charging. Use proper PPE, ensure good ventilation, and never assume a discharged battery is safe to handle without checking for damage, swelling, or leakage first."},
    {"cat": "Safety", "title": "Mixture Mismanagement Risks", "body": "An improperly rich mixture at altitude wastes fuel and can foul spark plugs; an improperly lean mixture can cause excessive cylinder head temperatures and potential engine damage. Always follow the POH/AFM leaning procedure and monitor engine instruments (EGT/CHT) rather than leaning by feel alone."},
]

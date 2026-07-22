"""Aviation Maintenance Academy - Wave 3 sims/reference pack.
Adds 2 new sims: battery C-rating calculator, stall speed w/ load factor.
Merged in build_aviation_academy.py.
"""

EXT6_SIMS = [
    {"id": "battery", "title": "Battery Capacity & C-Rate", "icon": "&#x1F50B;", "cat": "General",
     "desc": "Compute discharge current, run time, and C-rate for aircraft batteries."},
    {"id": "stallv", "title": "Stall Speed & Load Factor", "icon": "&#x2708;", "cat": "Airframe",
     "desc": "Compute stall speed change with bank angle / load factor (n)."},
]

EXT6_REFERENCE = [
    {"cat": "Formulas", "title": "Battery C-Rate", "body": "C-Rate expresses charge/discharge current relative to capacity: Current (A) = C-Rate x Capacity (Ah). A 1C discharge on a 40 Ah battery = 40 A. Run time (hr) &asymp; Capacity (Ah) / Discharge Current (A), derated for real-world efficiency losses and temperature."},
    {"cat": "Formulas", "title": "Load Factor & Stall Speed", "body": "Load factor n = 1 / cos(bank angle) in a coordinated level turn. Stall speed increases with the square root of load factor: Vs(new) = Vs(1g) x sqrt(n). A 60&deg; bank level turn doubles load factor (n=2), raising stall speed ~41%."},
    {"cat": "Safety", "title": "Battery Safety", "body": "Ni-Cd thermal runaway, lead-acid gassing/venting, and Li-ion fire risk all demand correct charger settings, ventilation, and case inspection. Never exceed manufacturer max discharge C-rate - excess heat degrades cells and can cause failure."},
    {"cat": "Safety", "title": "Accelerated Stalls", "body": "Stalls can occur at any airspeed and any attitude if the critical angle of attack is exceeded - steep turns, abrupt pull-ups, and turbulence penetration are common accelerated-stall scenarios. Load factor multiplies stall speed, shrinking the margin above Vs quickly."},
]

"""Aviation Maintenance Academy - Wave 4 sims/reference pack.
Adds 2 new sims: True Airspeed calculator, Propeller RPM/blade-tip-speed calculator.
Merged in build_aviation_academy.py.
"""

EXT8_SIMS = [
    {"id": "tas", "title": "True Airspeed Calculator", "icon": "&#x1F4A8;", "cat": "General",
     "desc": "Estimate true airspeed from calibrated airspeed, pressure altitude, and temperature."},
    {"id": "proprpm", "title": "Propeller Tip Speed & RPM Limit", "icon": "&#x1F300;", "cat": "Powerplant",
     "desc": "Compute propeller blade tip speed and check against the transonic tip-speed caution zone."},
]

EXT8_REFERENCE = [
    {"cat": "Formulas", "title": "True Airspeed (Rule of Thumb)", "body": "TAS &asymp; CAS + (2% x CAS per 1,000 ft of pressure altitude), adjusted further for non-standard temperature. For precise work use a flight computer or POH tables - this is a rough estimate only, most accurate below ~10,000 ft and moderate speeds."},
    {"cat": "Formulas", "title": "Propeller Tip Speed", "body": "Tip speed (ft/min) = pi x Diameter (ft) x RPM. Convert to Mach by dividing tip speed (ft/sec) by local speed of sound (~1,116 ft/sec at sea level standard day). Tip speeds approaching Mach 1 cause a sharp rise in noise and drag (efficiency loss) - most propellers are designed to stay well below this."},
    {"cat": "Safety", "title": "High-Speed Propeller Effects", "body": "As blade tip speed approaches the speed of sound, shockwave formation increases drag sharply, spikes noise levels, and can induce blade vibration/stress - a major reason propeller RPM and diameter are limited by design, and why reduction gearboxes are used on many turboprops to keep the propeller itself turning slower than the engine core."},
    {"cat": "Safety", "title": "Airspeed Indicator Errors", "body": "Indicated airspeed differs from calibrated (instrument/position error), true (density altitude), and groundspeed (wind) - always know which airspeed value a checklist or limitation refers to. Never mix CAS-based limitations with true airspeed readings without proper conversion."},
]

"""Aviation Maintenance Academy - Wave 10 sims/reference pack.
Adds 2 new sims: Bonding Resistance Checker, Fabric Tension/Strength Estimator.
Merged in build_aviation_academy.py.
"""

EXT20_SIMS = [
    {"id": "bondres", "title": "Bonding Resistance Checker", "icon": "\U0001F50C", "cat": "Airframe",
     "desc": "Enter a measured bonding resistance and compare it against typical pass/fail thresholds for general structure versus fuel-system bonding."},
    {"id": "fabtest", "title": "Fabric Strength Margin", "icon": "\U0001FA79", "cat": "Airframe",
     "desc": "Compare a punch-tester fabric strength reading against the minimum required strength to determine remaining margin before re-covering is required."},
]

EXT20_REFERENCE = [
    {"cat": "Formulas", "title": "Bonding Resistance Thresholds", "body": "General structure bonding resistance is typically acceptable up to a few tenths of an ohm depending on manufacturer data, while fuel-system bonding near tanks and fuel lines demands much tighter thresholds, often under 0.003 ohm, because arcing near fuel vapors is an explosion hazard. Always use the aircraft-specific maintenance manual value rather than a generic threshold."},
    {"cat": "Formulas", "title": "Fabric Strength Margin", "body": "Fabric strength margin = measured punch-tester reading (lbs) - minimum required strength (lbs) for the aircraft's certification category. A positive margin means the fabric is still airworthy; a zero or negative margin means the aircraft must be re-covered before further flight regardless of visual appearance."},
    {"cat": "Safety", "title": "Welding Fire and Gas Safety", "body": "Oxy-acetylene welding requires strict gas cylinder safety: acetylene cylinders must always be stored and used upright, never exceed 15 psi acetylene working pressure, and flashback arrestors/check valves should be installed on both oxygen and acetylene lines to prevent a flashback from traveling into the cylinder or regulator, which can cause a violent explosion."},
    {"cat": "Safety", "title": "AD Compliance Tracking Discipline", "body": "Missed or improperly documented Airworthiness Directive compliance is a common source of airworthiness disputes and enforcement action. Maintain a dedicated AD compliance log cross-referenced to the aircraft logbooks, and re-verify AD applicability against the current AD list at every annual inspection, since new ADs are issued continuously."},
]

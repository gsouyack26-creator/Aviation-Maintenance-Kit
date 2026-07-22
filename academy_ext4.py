# -*- coding: utf-8 -*-
"""Aviation Maintenance Academy - Content Expansion Pack 4 (Wave 2 sims/reference)
2 new sims + reference cards. Merged in build_aviation_academy.py like academy_ext2.py.
"""

EXT4_SIMS = [
  {"id":"fuelplan", "title":"Fuel Endurance Planner", "icon":"&#x26FD;", "cat":"Powerplant", "desc":"Compute flight endurance and range from usable fuel and burn rate."},
  {"id":"rivspace",  "title":"Rivet Spacing Checker", "icon":"&#x1F4CF;", "cat":"Airframe",   "desc":"Check rivet pitch and edge distance against standard minimums for a given diameter."}
]

EXT4_REFERENCE = [
  {"cat":"Formulas","title":"Fuel Endurance","body":"Endurance (hr) = Usable Fuel (gal) / Burn Rate (gal/hr). Range (nm) &asymp; Endurance x Groundspeed. Always plan a reserve (commonly 30-45 min VFR/IFR per part/ops rules) - never plan to the last drop."},
  {"cat":"Formulas","title":"Rivet Spacing Minimums","body":"Minimum edge distance &asymp; 2x rivet diameter. Minimum pitch (row spacing along a line) &asymp; 3x rivet diameter (typical general guidance - always confirm against the specific structural repair manual for the actual aircraft)."},
  {"cat":"Electrical","title":"Alternator vs Generator Quick Compare","body":"Generator: DC output directly, heavier, brushes carry full output current, poor low-RPM output. Alternator: AC internally rectified to DC, lighter, brushes carry only field current, good output at low RPM."},
  {"cat":"Regs","title":"A&P Eligibility Paths","body":"Path 1: Part 147 school graduate (structured curriculum). Path 2: 30 months documented hands-on experience (or military equivalency). Both require passing General + Airframe and/or Powerplant written/oral/practical tests."},
  {"cat":"Powerplant","title":"Overhaul Terminology","body":"<b>Overhauled</b> = inspected/reworked to service limits. <b>Rebuilt/zero-timed</b> = manufacturer/agent only, new/service-limit parts, logbook reset to zero. <b>Repaired</b> = fixed a specific defect, not a full overhaul."},
  {"cat":"Airframe","title":"Composite Damage Classification","body":"Cosmetic (no repair needed) &rarr; Repairable per SRM (follow ply schedule/cure exactly) &rarr; Requires engineering disposition/OEM approval (major structural damage beyond standard repair limits)."},
  {"cat":"Safety","title":"Ice Protection System Types","body":"Pneumatic boots (cyclic inflate/deflate), bleed-air thermal (turbine engines, continuous), electrothermal (props/pitot/windshields, cyclic or continuous). Match protection type to the aircraft - never assume a system is anti-ice vs de-ice without checking the AFM."},
  {"cat":"Hardware","title":"Life-Limited vs Time-Continued","body":"Life-limited: hard replacement at a specified time/cycle no matter the condition (e.g., certain crankshafts, turbine disks). Time-continued: stays in service indefinitely as long as inspection shows it's serviceable - no fixed cap."}
]

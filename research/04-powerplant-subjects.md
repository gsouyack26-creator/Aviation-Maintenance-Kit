# 04 — Powerplant Subjects (FAA-H-8083-32B knowledge base)

> Everything about the engine and propeller. Source of record: **AMTH – Powerplant**,
> free from the FAA. [[E1]](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation)

---

## P-1. Reciprocating Engines
- **Operating principle — 4-stroke Otto cycle:** intake → compression → power → exhaust
  (one power stroke per **2** crankshaft revolutions per cylinder).
- **Configurations:** horizontally-opposed (most GA — Lycoming/Continental), radial,
  in-line, V-type. **Firing order** designed for smooth balance (e.g., opposed 6:
  1-4-5-2-3-6).
- **Compression ratio** = cylinder volume BDC ÷ volume TDC (typ. 7:1–8.7:1). Higher CR →
  more power but needs higher-octane fuel (detonation risk).
- **Key parts:** crankcase, crankshaft, connecting rods, pistons/rings, cylinders,
  valves (intake/exhaust), camshaft/lifters, accessory case.
- **Valve timing & overlap;** valve clearance/lash; hydraulic lifters.

## P-2. Turbine Engines
- **Brayton cycle:** intake → compression → combustion (constant pressure) → expansion/exhaust.
- **Sections:** inlet, **compressor** (axial/centrifugal), diffuser, **combustor**,
  **turbine**, exhaust/nozzle. Accessory gearbox.
- **Types:** **turbojet** (pure thrust), **turbofan** (bypass — most airliners),
  **turboprop** (drives a prop via reduction gear), **turboshaft** (helicopters/APUs).
- **Thrust vs. power;** EPR, N1/N2 spools, EGT/ITT limits, **hot section** vs. cold section.
- Materials: nickel superalloys, single-crystal turbine blades, thermal-barrier coatings.

## P-3. Engine Construction & Materials
- Cast/forged/machined components; bearings (plain, ball, roller); seals; fits &
  clearances; magnaflux/zyglo inspection of ferrous/non-ferrous parts.

## P-4. Induction Systems
- **Reciprocating:** air filter, carburetor heat / **alternate air**, intake manifold,
  **turbocharging/supercharging** (density altitude, wastegate, intercooler).
- **Carburetor icing** — throttle/venturi cooling can ice even in warm weather.
- **Turbine inlet:** anti-ice, FOD screens, pressure recovery.

## P-5. Engine Fuel & Fuel Metering
- **Float-type & pressure carburetors;** mixture control (idle cutoff), economizer,
  accelerating pump.
- **Fuel injection** (continuous-flow Bendix/Continental) — flow divider, nozzles.
- **Turbine fuel systems:** fuel control unit (FCU), **FADEC** (full-authority digital
  engine control), fuel nozzles/manifold, fuel-heat.
- Mixture, EGT and leaning; vapor lock; fuel-flow instrumentation.

## P-6. Ignition & Starting Systems
- **Reciprocating: magnetos** (self-contained, engine-driven; **dual mags** for
  redundancy & better combustion). **Impulse coupling / Shower of Sparks** for starting.
- **Magneto-to-engine timing** and **internal (E-gap) timing** — a core practical task.
- Harness, **spark plugs** (massive/fine-wire; gap, reach, heat range, rotation & cleaning).
- **Turbine ignition:** high-energy capacitor-discharge igniters (only for start &
  continuous-ignition modes). Starters: electric, air/pneumatic, starter-generator.

## P-7. Exhaust & Reverser Systems
- Recip: exhaust stacks, collectors, **heat-exchanger muffs** (cabin heat / CO leak checks),
  turbo coupling. Turbine: exhaust cone, **thrust reversers**, mufflers/augmentors.

## P-8. Lubrication Systems
- Functions: lubricate, cool, clean, seal, cushion, protect.
- **Wet-sump** (opposed engines) vs. **dry-sump** (radial/turbine — external tank + scavenge pumps).
- Components: oil pump, filter/screen, oil cooler, pressure & scavenge, thermostatic
  bypass, **oil pressure/temp** gauges. **Oil grades** (mineral vs. ashless-dispersant;
  turbine synthetics). **Oil analysis (SOAP)** & filter debris inspection for wear.

## P-9. Cooling Systems
- Recip: **air-cooled** (cylinder fins, baffles, cowl flaps) — proper baffle seals are
  critical; a few liquid-cooled. Turbine: air cooling of hot section, bleed-air cooling.

## P-10. Propellers
- **Fixed-pitch, ground-adjustable, controllable/constant-speed, feathering, reversing.**
- **Constant-speed:** governor + hub uses oil pressure vs. counterweights/springs/N₂ to
  change blade angle to hold selected RPM. **Feathering** (min drag on shutdown),
  **reverse** (braking).
- Terms: blade angle, pitch, geometric vs. effective pitch (slip), blade station.
- Inspection: nicks/cracks (stop-drill & dress per manual — stress-critical), track &
  balance (static/dynamic), hub/blade AD compliance, prop strike/sudden-stoppage inspection.

## P-11. Engine Instruments
- **Tachometer (RPM), Manifold Pressure (MP), EGT, CHT, oil temp/press, fuel flow/press**;
  turbine: **N1/N2, ITT/EGT, torque, fuel flow**. Ranges & markings; troubleshooting sending units.

## P-12. Engine Fire Protection
- Detection (loop/thermal), extinguishing bottles, fuel/hydraulic **firewall shutoff
  valves**, and test procedures (shared with airframe fire systems).

## P-13. Engine Removal & Replacement (R&R)
- **QECA (quick engine change assembly)**, mount inspection, hoisting, hose/line/wire
  disconnect logging, preservation of stored engines, ground run & leak check on install.

## P-14. Inspection, Maintenance & Troubleshooting
- **Recip:** compression testing (**differential** — reads e.g. 76/80; where the air
  escapes tells you the fault: exhaust valve, intake valve, rings), borescope, spark-plug
  reading, magneto checks (RPM drop), oil-consumption trends.
- **Turbine:** borescope hot section, EGT/vibration trend monitoring, FOD, hot-start /
  hung-start diagnosis, compressor wash.
- **Troubleshooting logic:** symptom → likely systems → isolate with data → verify fix.

## P-15. Engine Overhaul
- **TBO (time between overhaul)**, disassembly, cleaning, dimensional inspection vs.
  service limits, replacement of life-limited parts, reassembly to torque specs, test-cell
  or ground run-in, documentation & return to service.

---

## Key formulas / rules cheat-sheet (powerplant)
| Quantity | Formula / rule |
|---|---|
| Compression ratio | V(BDC) ÷ V(TDC) |
| Power strokes | 1 per cylinder per 720° (4-stroke) |
| Brake HP | BHP = (Torque·RPM)/5252 |
| Indicated vs Brake HP | BHP = IHP − FHP (friction) |
| Mech. efficiency | BHP ÷ IHP |
| Differential compression | reading X/80; investigate if < ~60/80 or per mfr |

## Free resources for this area
| Resource | Covers | URL | Cost |
|---|---|---|---|
| AMTH – Powerplant (FAA-H-8083-32B) | All of the above | [[E1]](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation) | Free |
| AC 43.13-1B (engine/prop chapters) | Accepted methods | [[E2]](https://www.faa.gov/regulations_policies/advisory_circulars) | Free |

## References
- [[E1]](https://www.faa.gov/regulations_policies/handbooks_manuals/aviation) FAA Handbooks (AMTH Powerplant) — *verified*
- [[E2]](https://www.faa.gov/regulations_policies/advisory_circulars) FAA Advisory Circulars

# Module 5 — Powerplant: Reciprocating Engines
*Read alongside AMTH Powerplant (FAA-H-8083-32B).*

## Learning Objectives
- Explain the 4-stroke cycle and reciprocating-engine construction.
- Describe induction, fuel metering, ignition, lubrication, cooling.
- Understand propellers and perform key inspections (compression, mag check).

## Lesson 5.1 — Operating Principle
- **4-stroke Otto cycle:** intake → compression → power → exhaust; **one power stroke per
  2 crank revolutions** per cylinder.
- **Configurations:** horizontally-opposed (most GA), radial, in-line, V. **Firing order**
  for balance (opposed-6 example: 1-4-5-2-3-6).
- **Compression ratio = V_BDC / V_TDC** (typ. 7:1–8.7:1); higher CR needs higher octane
  (detonation/pre-ignition risk).

## Lesson 5.2 — Construction
Crankcase, crankshaft, connecting rods, pistons/rings, cylinders, valves, camshaft/lifters,
accessory case. Valve timing & overlap; valve lash.

## Lesson 5.3 — Induction & Fuel Metering
- Air filter, **carb heat / alternate air**, manifold; **turbo/supercharging** (wastegate,
  intercooler). **Carburetor icing** can occur even in warm, humid air.
- **Float & pressure carburetors;** mixture control (idle cutoff), accelerating pump,
  economizer. **Fuel injection** (continuous-flow): flow divider + nozzles.

## Lesson 5.4 — Ignition & Starting
- **Magnetos** (engine-driven, self-powered; **dual** for redundancy + better combustion).
  **Impulse coupling / Shower of Sparks** aids starting.
- **Magneto timing:** internal **E-gap** timing + **mag-to-engine** timing (a core task).
- **Spark plugs:** massive vs. fine-wire; gap, reach, heat range, rotation, cleaning.

## Lesson 5.5 — Lubrication & Cooling
- Functions: lubricate, cool, clean, seal, cushion, protect.
- **Wet-sump** (opposed) vs. **dry-sump** (radial; external tank + scavenge). Pump, filter,
  oil cooler, thermostatic bypass. **Oil grades:** mineral vs. **ashless-dispersant (AD)**.
- **Oil analysis (SOAP)** & filter debris = early wear detection.
- **Air cooling:** cylinder fins, **baffles & cowl flaps** — intact baffle seals are critical.

## Lesson 5.6 — Propellers
- Fixed-pitch, ground-adjustable, **constant-speed**, feathering, reversing.
- **Constant-speed:** governor uses oil pressure vs. counterweights/springs/N₂ to change
  blade angle and hold RPM. **Feather** (min drag), **reverse** (braking).
- Terms: blade angle, pitch, slip, blade station. **Nicks = stress risers**: dress/stop
  per manual (stress-critical); **track & balance**; **prop-strike/sudden-stoppage inspection**.

## Lesson 5.7 — Inspection & Troubleshooting
- **Differential compression test:** reads e.g. **72/80**; listen where air escapes —
  exhaust (exhaust valve), intake (intake valve), crankcase breather/oil filler (rings).
- Borescope cylinders; **spark-plug reading** (fouling/heat); **magneto check** (RPM drop
  within limits; excessive drop or none = a fault); oil-consumption trends.

## Key Formulas
| Quantity | Formula |
|---|---|
| Compression ratio | V_BDC / V_TDC |
| Power strokes | 1 / cylinder / 720° |
| Brake HP | BHP = (Torque·RPM)/5252 |
| BHP relation | BHP = IHP − FHP |
| Mech. efficiency | BHP ÷ IHP |

## Hands-On Labs
1. **Cycle model:** trace the 4 strokes on a cutaway/animation; identify valve overlap.
2. **Differential compression (sim/trainer):** run a test, get 68/80, and locate the leak by sound.
3. **Mag check logic:** given a run-up RPM drop table, decide pass/fail and likely fault.
4. **Prop inspection:** find & (describe) dressing a small leading-edge nick per limits.

## Self-Check Quiz
1. How many crankshaft revolutions per power stroke (per cylinder) in a 4-stroke?
2. If torque=300 lb-ft at 2700 RPM, what is BHP?
3. On a differential compression test, air out the exhaust pipe indicates what?
4. Why are dual magnetos used?
5. What changes on a constant-speed prop to hold RPM?

<details><summary>Answers</summary>
1. Two (720°). 2. BHP=(300×2700)/5252 ≈ 154 HP. 3. Leaking exhaust valve. 4. Redundancy
plus more complete combustion (two sparks). 5. Blade angle (pitch), via the governor.
</details>

## Free Resources
- AMTH Powerplant: https://www.faa.gov/regulations_policies/handbooks_manuals/aviation
- AC 43.13-1B (engine/prop): https://www.faa.gov/regulations_policies/advisory_circulars

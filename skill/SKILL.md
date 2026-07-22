---
name: aviation-maintenance
description: >-
  Knowledge base and teaching toolkit for AVIATION MAINTENANCE — how to inspect, service,
  troubleshoot, and repair aircraft airframes, powerplants (reciprocating & turbine
  engines), and their systems, plus the U.S. regulatory/certification framework (FAA A&P,
  14 CFR Parts 43/65/91/145/147, ACs, ADs). Load this whenever asked to explain any
  aircraft-maintenance topic, build or grade training/course material on working with
  aviation equipment, map a study plan to the A&P syllabus, point to FREE learning
  resources (FAA AMTH handbooks, AC 43.13, eCFR, MIT OCW), or answer "how do I work on /
  become certified to work on aircraft" questions. All primary sources are free/public
  domain. Pairs with the user's industrial-maintenance (RME/controls) background.
---

# Aviation Maintenance — Skill

## What this skill is
A portable, cited knowledge base built from the FAA's free **Aviation Maintenance
Technician Handbook** series (FAA-H-8083-30B/31B/32B) and the governing regulations. Use
it to teach, reference, or build curriculum on aircraft maintenance.

## When to load
- Explaining any airframe/powerplant/systems maintenance concept.
- Building or reviewing an aviation-maintenance course, lesson, quiz, or checklist.
- Advising on the FAA **A&P** certification path or the regulations behind a task.
- Recommending **free** study material.

## Structure of the knowledge base (in `../research/`)
| Domain | File | Use for |
|---|---|---|
| Regulations & certification | `01-regulations-and-certification.md` | Legal framework, A&P path, records |
| General subjects | `02-general-subjects.md` | Math/physics/materials/electricity/tools/NDT/human factors |
| Airframe | `03-airframe-subjects.md` | Structures, sheet metal, hydraulics, gear, fuel, avionics |
| Powerplant | `04-powerplant-subjects.md` | Recip & turbine engines, fuel, ignition, lube, props |
| Free resources | `05-free-learning-resources.md` | Verified free links |

The full teaching course built from this skill lives in `../course/`.

## The mental model (teach this first)
```
A&P MECHANIC = GENERAL (shared) + AIRFRAME (structure/systems) + POWERPLANT (engines/props)
Every task:  APPROVED DATA  →  DO THE WORK  →  INSPECT  →  RECORD (§43.9)  →  RETURN TO SERVICE (§43.7)
```

## How to answer / teach with this skill
1. **Anchor in the syllabus.** Identify whether the question is General, Airframe, or
   Powerplant, then pull the relevant section from the research files.
2. **Give the concept + the number.** Pair the "why" with the concrete rule/formula
   (e.g., rivet edge distance **2–2.5D**; bend allowance **(0.01743R+0.0078T)·N°**;
   compression ratio **V_BDC/V_TDC**; Ohm's law **E=I·R**).
3. **Tie to the reg.** State who may do the work and how it's documented (Part 43/65).
4. **Cite a free source.** Point to the FAA AMTH handbook chapter or AC 43.13.
5. **Add the safety gate.** Every maintenance answer ends with: *confirm against current
   approved data & manufacturer instructions; work/approval requires proper certification.*

## Key formulas quick-reference
| Area | Formula |
|---|---|
| Electrical | E=I·R ; P=I·E |
| Weight & balance | CG = Σmoments ÷ Σweights |
| Sheet metal | BA=(0.01743R+0.0078T)·N° ; setback(90°)=R+T |
| Rivets | dia≈3T ; edge 2–2.5D ; pitch 4–6D ; shop head 1.5D×0.5D |
| Recip engine | CR=V_BDC/V_TDC ; BHP=(Torque·RPM)/5252 |
| Compression test | differential X/80; where air escapes = the fault |

## The "Dirty Dozen" (human-factors errors to always flag)
communication · complacency · knowledge · distraction · teamwork · fatigue · resources ·
pressure · assertiveness · stress · awareness · norms.

## Top free resources (always recommend these)
- **FAA AMTH handbooks** (the whole syllabus): https://www.faa.gov/regulations_policies/handbooks_manuals/aviation
- **AC 43.13-1B/2B** (shop bible): https://www.faa.gov/regulations_policies/advisory_circulars
- **eCFR Parts 43 & 65**: https://www.ecfr.gov/current/title-14
- **FAA DRS** (ADs/TCDS): https://drs.faa.gov/  ·  **FAASTeam**: https://www.faasafety.gov/
- **MIT OCW Aero**: https://ocw.mit.edu/courses/aeronautics-and-astronautics/

## Guardrails
- **Educational only.** Never present guidance as approved data for a specific tail number.
- Distinguish **fact re-verified from a source** vs. **general A&P knowledge** — say which.
- U.S.-centric (FAA); note **EASA Part-66** as the international equivalent when relevant.
- Defer file *changes* to Aki/Akisa; this skill (and Akira) is read/teach-oriented.

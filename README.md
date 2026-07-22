# ✈️ Aviation Maintenance Kit

A free, self-contained package for learning how to work on aviation equipment — built
2026-07-15 from the FAA's public-domain **Aviation Maintenance Technician Handbook** series
and the governing U.S. regulations.

## Contents
```
Aviation-Maintenance-Kit/
├── README.md                ← you are here
├── research/                ← the raw, cited knowledge base (free sources)
│   ├── 00-index.md
│   ├── 01-regulations-and-certification.md
│   ├── 02-general-subjects.md
│   ├── 03-airframe-subjects.md
│   ├── 04-powerplant-subjects.md
│   └── 05-free-learning-resources.md
├── skill/                   ← reusable teaching skill
│   └── SKILL.md   (name: aviation-maintenance)
└── course/                  ← 8-module educational course
    ├── README.md            ← syllabus & how-to
    └── module-00 … module-07
```

## How the three parts relate
1. **research/** — everything gathered, cited to free sources (mostly FAA/eCFR).
2. **skill/SKILL.md** — packages that knowledge so an assistant can teach/answer from it.
   To activate it as an Aki skill, copy the `skill/` folder to a skills directory (e.g.
   `~/.aki/user_preference/<profile>/skills/aviation-maintenance/`).
3. **course/** — a ready-to-run learning path built from the skill: 8 modules with
   objectives, lessons, formulas, hands-on labs, quizzes, and a capstone.

## Start here
- **To learn:** open `course/README.md` and begin at Module 0.
- **To reference a topic:** browse `research/`.
- **To download the source textbooks (free):**
  https://www.faa.gov/regulations_policies/handbooks_manuals/aviation

## Sourcing & honesty note
Primary references (FAA handbooks page, eCFR Parts 43/65/147, MIT OCW, FAASTeam, DRS,
EASA, Coursera, Alison, AgentJayZ) were fetched and confirmed reachable during research.
Subject-matter content is synthesized from the standard A&P syllabus and well-established
maintenance knowledge; specifics (dimensions, limits, procedures) must always be confirmed
against **current** FAA handbooks and manufacturer approved data before real work.

> ⚠️ **Educational only** — not a substitute for FAA certification, approved data, or a
> Part 147 program. Real aircraft maintenance must be performed/approved by appropriately
> certificated personnel.

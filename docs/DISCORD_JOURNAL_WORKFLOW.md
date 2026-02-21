# Discord Journal Workflow (Pepper)

## Goal
- Run Discord check-ins across morning, midday, and evening.
- Convert replies into structured day-part journal files.
- Apply modifier-trigger coaching logic without changing score math.
- Commit and push each completed check-in entry.

## System source
- Canonical map: `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- SLA/escalation policy: `docs/COACHING_CRON_SYSTEM.md`

## Journal files (per local day, America/New_York)
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-evening.md`
- Weekly file: `weekly/YYYY-[W]WW.md`

## End-to-end flow
1. Pepper sends the matching day-part questions in Discord.
2. Austin replies in freeform text.
3. Pepper asks follow-ups only for missing required fields.
4. Pepper computes the coaching output from Austin's narrative:
   - Morning/midday: concise coaching read + next actions.
   - Evening: computed scorecard + why + insightful read + tomorrow plan.
5. Pepper redacts sensitive medical details.
6. Pepper formats content with the matching template.
7. Pepper writes or updates day-part file in `journals/`.
8. Pepper commits and pushes.

## Source templates
- Questions: `templates/morning-checkin-questions.md`, `templates/midday-checkin-questions.md`, `templates/evening-recap-questions.md`
- Entries: `templates/morning-checkin.md`, `templates/midday-checkin.md`, `templates/evening-recap.md`
- Weekly: `templates/weekly-review.md`, `templates/weekly-recap.md`

## Prompt execution rules (anti-overwhelm)
- Ask required fields first.
- Ask optional fields as one optional line only.
- Keep each check-in question set answerable in under 90 seconds.
- If something is missing, ask only for the missing required field.

## Standard training mode enum (use everywhere)
- `Masters Swim` (`Train:MastersSwim`)
- `Gym LP` (`Train:GymLP`)
- `Home Strength (KB+Pullup+Rings)` (`Train:HomeStrength`)
- `HIIT Only (Chris Heria style)` (`Train:HIITOnly`)
- `Minimum Day` (`Train:MinimumDay`)
- `Recovery` (`Train:Recovery`)

## Fallback ladder (A/B/C)
- `A = Home Strength 25-35 min`
- `B = HIIT 10-15 min`
- `C = Minimum Day 8-12 min`

## Pre-swim-night training guidance (Sun/Tue/Thu)
- Avoid late hard HIIT.
- If evening is tight, favor `A` or `C`.

## Scoring model (only model)
- `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`
- Modifier facets are coaching triggers only and do not add score points.
- Operational floor: `6/10+`
- Austin target: `7/10+` average (with push toward `8/10+`).

## Required fields matrix (no tables)
- Morning required:
- Readiness color, energy, wake window hit, sleep quality.
- Guardrails (caffeine cutoff, last meal cutoff, wind-down).
- Nutrition + training mode token (`Train:<mode>`) + fallback rung (`A/B/C`).
- Hydration 1L-by-noon plan.
- Stress + 10-minute reset plan.
- Meaningful connection plan (10+ minutes, yes/no).
- Pain (0-10) + location + red-flag symptom (yes/no).
- Biggest risk + if-then + one non-negotiable.
- Morning optional:
- One optional line: awakenings, mood/readiness, schedule constraints.
- Midday required:
- Readiness color + energy.
- Stress + reset done/scheduled.
- Hydration (urine color + 1L by noon yes/no).
- Guardrails on-track, nutrition on-track, training mode/status.
- Connection status (done/planned/missed).
- Pain (0-10) + location + red-flag symptom (yes/no).
- One next action with time.
- Midday optional:
- One optional line: focus/hunger note, calendar pressure, other context.
- Evening required:
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency + connection completion.
- Peak pain (0-10) + location + red-flag symptom (yes/no).
- Reflection: what happened (2), what worked (1), friction (1), one change tomorrow.
- Evening optional:
- One optional line: alcohol/cannabis or extra context.

## Trigger handling (short)
- Readiness Yellow: `Yellow` >=2 consecutive check-ins or energy <=2 -> fallback ladder (`A` then `B` then `C`) + bedtime protection for 24h.
- Readiness Red: any `Red` or energy =1 -> recovery-only day and no high-intensity training.
- Stress: stress >=4 -> do 10-minute reset within 60 minutes; if still >=4 next check-in, shift to Busy Day mode.
- Hydration miss: dark urine or missed 1L by noon; if >=2 misses in a week, enforce AM + pre-noon hydration blocks.
- Connection miss: missed 10+ minute meaningful connection for 2 consecutive days -> schedule next-day block before 6pm.
- Pain/red-flag: red-flag yes or pain >=7 -> urgent escalation now. Pain 4-6 >48h (or pain >=3 for 3+ days) -> clinician-soon escalation.

## Unknown rule and follow-up logic
- `Unknown` allowed only if explicitly stated by Austin with a reason.
- Store as `Unknown - <reason>`.
- Missing required value without explicit unknown -> ask follow-up now.
- Required value marked `Unknown` -> force follow-up at next check-in.
- Optional fields never block file creation.

## Commit message conventions
- Morning:
- `git add journals/YYYY-MM-DD-morning.md`
- `git commit -m "journal: YYYY-MM-DD morning check-in"`
- Midday:
- `git add journals/YYYY-MM-DD-midday.md`
- `git commit -m "journal: YYYY-MM-DD midday check-in"`
- Evening:
- `git add journals/YYYY-MM-DD-evening.md`
- `git commit -m "journal: YYYY-MM-DD evening recap"`
- Weekly:
- `git add weekly/YYYY-[W]WW.md`
- `git commit -m "journal: YYYY-[W]WW weekly recap"`

## Safety and redaction
- Do not store sensitive medical details.
- Redact before writing:
- Medication names or doses -> `[medication redacted]`
- Diagnoses or conditions -> `[health detail redacted]`
- Lab or vitals numbers -> `[health metric redacted]`
- Doctor, clinic, or patient IDs -> `[personal health info redacted]`

## Date and timezone conventions
- Date format: `YYYY-MM-DD`.
- Timezone: Austin local timezone `America/New_York` unless changed.
- File date is local date of the check-in message.
- If message date is ambiguous after midnight, ask for explicit date.

## Minimum execution standard
- Every active day ends with an evening recap file.
- Morning is required.
- Midday is expected; if missed, recover at evening recap.
- Weekly recap is required once per week.
- Every check-in file includes a Pepper coaching response block.
- Evening recap includes Pepper-computed scores + why + insightful read + tomorrow plan.

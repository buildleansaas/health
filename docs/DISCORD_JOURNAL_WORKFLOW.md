# Discord Journal Workflow (Pepper)

## Goal
- Run Discord check-ins in a 2-touch loop: daytime + evening.
- Convert replies into structured daily journal files.
- Apply modifier-trigger coaching logic without changing score math.
- Commit and push each completed touch entry.

## System source
- Canonical map: `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- Context-aware algorithm: `docs/CONTEXT_AWARE_CHECKINS.md`
- SLA/escalation policy: `docs/COACHING_CRON_SYSTEM.md`
- Preference profile: `profiles/austin-preferences.yaml`
- Meal logistics playbook: `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`

## Journal files (per local day, America/New_York)
- Canonical outputs:
- `journals/YYYY-MM-DD-daytime.md`
- `journals/YYYY-MM-DD-evening.md`
- Legacy history compatibility (read/backfill only):
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- Weekly file: `weekly/YYYY-[W]WW.md`

## End-to-end flow
1. Pepper reads context (today + yesterday files, prior coach notes, unresolved follow-ups, preference profile) and generates `3-6` targeted prompts for the current touch.
2. Austin replies in freeform text.
3. Pepper asks follow-ups only for missing required fields.
4. Pepper captures durable preference updates in `profiles/austin-preferences.yaml` when Austin changes cadence/tone/rules.
5. Pepper computes coaching output from Austin's narrative:
   - Daytime: concise coaching read + remainder-of-day actions, using prior-evening tomorrow plan as baseline when available and adjusting for reality-day changes.
   - Evening: execution recap + computed scorecard + why + insightful read + explicit output 1 (tomorrow preview top actions) + explicit output 2 (full tomorrow execution plan tailored to schedule constraints) + before-bed goal.
6. Pepper redacts sensitive medical details.
7. Pepper formats content with the matching template.
8. Pepper writes or updates touch file in `journals/`.
9. Pepper commits and pushes.

## Source templates
- Active question guides: `templates/daytime-checkin-questions.md`, `templates/evening-recap-questions.md`
- Active entry templates: `templates/daytime-checkin.md`, `templates/evening-recap.md`
- Legacy/deprecated (historical/backfill only):
- `templates/morning-checkin.md`, `templates/midday-checkin.md`, `templates/afternoon-checkin.md`
- `templates/morning-checkin-questions.md`, `templates/midday-checkin-questions.md`, `templates/afternoon-checkin-questions.md`
- Weekly: `templates/weekly-review.md`, `templates/weekly-recap.md`

## Prompt execution rules (anti-overwhelm)
- First read context per `docs/CONTEXT_AWARE_CHECKINS.md`.
- Ask `3-6` targeted prompts, not static forms.
- Prioritize required fields tied to unresolved friction and current risk.
- Ask optional fields as one optional line only.
- Keep each touch answerable in under 90 seconds.
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

## Meal logistics defaults (coaching-only)
- Apply day-type split from `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`:
- `MWF`: early masters + in-town work; breakfast/lunch execution is high-priority.
- `Tue/Thu`: later start + pool work + home around `7:30pm`; avoid lunch-to-pool under-fueling.
- Default constraints:
- No microwave preferred.
- Fridge access in town available.
- Fast-food fallback chains: Chick-fil-A, McDonald's, Chipotle.

## Scoring model (only model)
- `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`
- Modifier facets are coaching triggers only and do not add score points.
- Operational floor: `6/10+`
- Austin target: `7/10+` average (with push toward `8/10+`).

## Required fields matrix (no tables)
- Daytime required:
- Carryover block when needed (prior evening missed, unresolved unknowns, open follow-ups).
- Prior evening tomorrow-plan baseline (when present) + reality-day adjustments.
- Readiness color + energy + stress now.
- Hydration status, nutrition/training status, and training mode token + fallback rung.
- Schedule constraints and biggest friction.
- One concrete remainder-of-day plan with times (updated from baseline when needed).
- Top risk + if-then fallback.
- Daytime optional:
- One optional line: extra context or schedule nuance.
- Evening required:
- Execution recap vs daytime plan.
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency + connection completion.
- Meal logistics outcomes: breakfast/lunch execution + fallback chain use + no-microwave adherence.
- Peak pain (0-10) + location + red-flag symptom (yes/no).
- Reflection: what happened (2), what worked (1), friction (1), one change tomorrow.
- Tomorrow schedule/context from Austin (hard windows, constraints, likely friction).
- Explicit output 1: tomorrow preview (top 1-3).
- Explicit output 2: full tomorrow execution plan tailored to schedule/context (morning/daytime/evening blocks + fallback).
- One before-bed goal with timing.
- Evening optional:
- One optional line: alcohol/cannabis or extra context.

## Trigger handling (short)
- Readiness Yellow: `Yellow` >=2 consecutive touches or energy <=2 -> fallback ladder (`A` then `B` then `C`) + bedtime protection for 24h.
- Readiness Red: any `Red` or energy =1 -> recovery-only day and no high-intensity training.
- Stress: stress >=4 -> do 10-minute reset within 60 minutes; if still >=4 at next touch, shift to Busy Day mode.
- Hydration miss: dark urine or missed 1L by noon; if >=2 misses in a week, enforce AM + pre-noon hydration blocks.
- Connection miss: missed 10+ minute meaningful connection for 2 consecutive days -> schedule next-day block before 6pm.
- Pain/red-flag: red-flag yes or pain >=7 -> urgent escalation now. Pain 4-6 >48h (or pain >=3 for 3+ days) -> clinician-soon escalation.
- Meal logistics miss: breakfast `No` or lunch `No` on >=2 workdays/week, or any `Impulsive` fast-food event -> enforce next-day traffic-proof defaults and pre-commit one fallback order.

## Unknown rule and follow-up logic
- `Unknown` allowed only if explicitly stated by Austin with a reason.
- Store as `Unknown - <reason>`.
- Missing required value without explicit unknown -> ask follow-up now.
- Required value marked `Unknown` -> force follow-up at next touch.
- Optional fields never block file creation.

## Commit message conventions
- Daytime:
- `git add journals/YYYY-MM-DD-daytime.md`
- `git commit -m "journal: YYYY-MM-DD daytime check-in"`
- Evening:
- `git add journals/YYYY-MM-DD-evening.md`
- `git commit -m "journal: YYYY-MM-DD evening recap"`
- Weekly:
- `git add weekly/YYYY-[W]WW.md`
- `git commit -m "journal: YYYY-[W]WW weekly recap"`
- Legacy backfill entries keep the legacy part name in commit message when used.

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
- Every active day has a daytime check-in file.
- Every active day ends with an evening recap file.
- Weekly recap is required once per week.
- Every touch file includes a Pepper coaching response block.
- Evening recap includes Pepper-computed scores + why + insightful read + explicit tomorrow preview + full tomorrow execution plan (morning/daytime/evening + fallback) + before-bed goal.
- Material user updates between touches should be appended to the active daily journal file before end of day.

# Coaching Integration Plan (Sleep + Nutrition + Training + Modifier Facets)

## Goal
- Run one integrated daily coaching system that stays low friction.
- Keep scoring fixed to sleep + nutrition + training.
- Use readiness/stress/hydration/connection/risk as coaching modifiers and intervention triggers.

## Guiding rules
- Track three scored domains daily: sleep, nutrition, training.
- Track five modifier facets daily: readiness, stress/reset, hydration, connection, risk/safety.
- Track meal logistics adherence as a nutrition execution modifier: breakfast/lunch plan execution, no-microwave preference, and fallback intent.
- Prioritize adherence trend over single-day perfection.
- Keep coaching language non-diagnostic and practical.
- Generate context-aware prompts at each check-in; do not use static forms.

## Meal logistics source and scope
- Meal logistics source doc: `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`.
- Scope: breakfast + lunch execution while in town (`MWF` vs `Tue/Thu` constraints).
- Constraints: no microwave preferred, fridge access available, fast-food fallback chains pre-defined.
- Rule: meal logistics data drives prompts, planning, and intervention triggers only; score formula is unchanged.

## Context-aware check-in generation
- Before each check-in, read today + yesterday day-part files, prior coach notes, unresolved follow-ups, and `profiles/austin-preferences.yaml`.
- Ask `3-6` targeted prompts based on active risk, open friction, prior commitments, and recent wins.
- Preserve required captures by day-part with focused follow-up for missing required fields only.
- Keep prompts concise and answerable in under 90 seconds.

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

## Daily check-ins
- Morning check-in:
- Capture readiness color + energy, sleep state, and guardrails.
- Set nutrition + training mode (`Train:<mode>`) + fallback rung (`A/B/C`).
- Set breakfast and lunch logistics plan for today's day type (`MWF` or `Tue/Thu`) including fallback chain/order if schedule compresses.
- Set hydration 1L-by-noon plan, stress reset plan, connection plan.
- Capture pain/location/red-flag status.
- Midday check-in:
- Re-rate readiness, energy, stress, hydration sufficiency.
- Confirm guardrails, nutrition, training mode/status, and connection status.
- Confirm breakfast execution status and lunch execution plan/status (`Yes/Partial/No`) and whether fallback was intentional.
- Re-check pain/location/red-flag and set one next action.
- Afternoon check-in:
- Re-check energy, stress/reset, hydration progress, and nutrition drift.
- Confirm training mode/status and pain/location/red-flag status.
- Re-check lunch execution and no-microwave adherence; set traffic-proof action if evening constraints tighten.
- Capture biggest friction and one concrete action with time.
- Evening recap:
- Score sleep, nutrition, training, and total.
- Log modifier outcomes (readiness trend, stress reset, hydration, connection, pain/red-flag).
- Log meal logistics outcomes: breakfast/lunch execution, fallback chain use (`Intentional/Impulsive/None`), no-microwave adherence.
- Capture what happened, what worked, friction, and one change for tomorrow.

## Daily cadence (America/New_York)
- Morning: within 15-90 minutes of wake.
- Midday: around late morning to midday.
- Afternoon: late-afternoon course-correct check-in.
- Evening: end of day or 60-120 minutes pre-bed.
- If midday is missed, recover at afternoon.
- If afternoon is missed, recover at evening recap.

## Intervention triggers (explicit and short)
- Readiness Yellow threshold: `Yellow` for >=2 consecutive check-ins or energy <=2.
- Readiness Red threshold: any `Red` or energy =1.
- Stress threshold: stress >=4/5.
- Hydration miss threshold: dark urine or missed 1L by noon; repeated if >=2 days/week.
- Connection miss threshold: no 10+ minute meaningful connection for 2 consecutive days.
- Pain/red-flag threshold: red-flag yes or pain >=7 immediately; pain 4-6 persisting >48h (or pain >=3 for 3+ days).
- Meal logistics miss threshold: breakfast `No` or lunch `No` on >=2 workdays/week, or any `Impulsive` fast-food event.

## Trigger actions
- Yellow readiness: fallback ladder (`A` then `B` then `C`) + protect bedtime for 24h.
- Red readiness: recovery-only day; no high-intensity work.
- Stress >=4: complete 10-minute reset within 60 minutes.
- Hydration misses repeated: lock AM + pre-noon water blocks.
- Connection misses repeated: schedule next-day connection block before 6pm.
- Pain/red-flag threshold met: run clinician/urgent escalation protocol from `docs/COACHING_CRON_SYSTEM.md`.
- Meal logistics threshold met: enforce next-day traffic-proof defaults from `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md` and pre-commit one fallback order per likely chain.

## Fallback modes
- Busy day mode:
- Sleep: caffeine cutoff + wind-down minimum.
- Nutrition: two protein feedings + hydration floor.
- Training: use fallback ladder (`A/B/C`) based on available time.
- Minimum viable day mode:
- Fixed wake window.
- Caffeine cutoff respected.
- `C` (`Minimum Day 8-12 min`) + one protein-forward meal.

## Adherence scoring (only model)
- `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`
- New facets are modifiers/triggers only and add zero score points.
- Sleep `0-4` anchors:
- Wake window hit.
- Caffeine cutoff met.
- Last meal cutoff met.
- Wind-down + sleep-environment target met.
- Nutrition `0-3` anchors:
- Protein anchors met.
- Hydration/fueling consistency met.
- Whole-food pattern/seed-oil avoidance target met.
- Training `0-3` anchors:
- Planned training mode completed (or fallback `A/B/C` completed).
- Daily movement baseline completed.
- Recovery block completed.

## Anti-all-or-nothing rules
- Operational floor: `6/10+` keeps continuity.
- Austin target: `7/10+` average (with push toward `8/10+`).
- Missing one anchor does not void the day.
- Use salvage actions instead of quitting the day.
- Evaluate trends weekly, not emotionally in-day.

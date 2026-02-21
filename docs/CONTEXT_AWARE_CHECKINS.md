# Context-Aware Check-Ins (Pepper)

## Purpose
- Replace static forms with concise, personalized check-ins.
- Keep journaling integrity by still capturing all required fields by day-part.
- Use recent context so each prompt reflects current priorities, progress, and open risks.

## Inputs to read before each check-in
- `profiles/austin-preferences.yaml`
- Today journal files that exist so far:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- `journals/YYYY-MM-DD-evening.md`
- Yesterday journal files:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- `journals/YYYY-MM-DD-evening.md`
- Prior coach notes inside the recent day-part files.
- Open follow-ups from missing required fields or `Unknown - <reason>` values.

## Context extraction algorithm
1. Build a short state snapshot from inputs.
2. Extract unresolved friction:
- Repeated blockers.
- Missed actions from prior check-ins.
- Missed check-ins or incomplete recoveries.
3. Extract prior commitments:
- Non-negotiable, if-then plan, and planned next action.
- Training mode and fallback rung (`A/B/C`).
- Hydration, reset, and connection plans.
4. Extract risk signals:
- Sleep guardrail drift.
- Hydration misses.
- Training risk or pain trend.
- Stress escalation and red-flag status.
5. Extract wins to reinforce:
- Completed commitments.
- Positive trend changes.
6. Rank top priorities for this check-in:
- First: unresolved risk or missing required capture.
- Second: highest-impact next action.
- Third: reinforcement to sustain momentum.

## Question budget and composition
- Ask `3-6` targeted prompts per check-in.
- Prioritize required captures tied to current risk.
- Bundle related fields only when clarity improves.
- Keep the message concise and answerable in under 90 seconds.

## Required captures for journaling integrity
- Morning:
- Readiness color, energy, wake window hit, sleep quality.
- Caffeine cutoff, last meal cutoff, wind-down start.
- Nutrition plan + training mode token + fallback rung.
- Hydration 1L-by-noon plan.
- Stress + reset plan.
- Meaningful connection plan.
- Pain (0-10) + location + red-flag symptom.
- Biggest risk + if-then + one non-negotiable.
- Midday:
- Readiness color + energy.
- Stress + reset done/scheduled.
- Hydration status (urine color + 1L by noon yes/no).
- Guardrails status, nutrition status, training mode/status.
- Meaningful connection status.
- Pain (0-10) + location + red-flag symptom.
- One next action with time.
- Afternoon:
- Energy + stress + reset status.
- Hydration progress + quick nutrition update.
- Training mode/status + pain/location/red-flag check.
- Biggest friction + one concrete action with time.
- Evening:
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency + meaningful connection completion.
- Peak pain (0-10) + location + red-flag symptom.
- Reflection: what happened, what worked, friction, one change for tomorrow.

## Follow-up logic for missing required data
- Missing required field: ask one immediate follow-up for only that field.
- `Unknown` allowed only when explicitly stated with a reason.
- Store unknown as `Unknown - <reason>`.
- Carry `Unknown` required fields into the next check-in follow-up queue.
- Optional context never blocks journaling.

## Personalization guardrails
- No overload: never exceed six prompts.
- No repetitive boilerplate: do not re-ask settled items unless status changed.
- Keep prompts specific to Austin's recent language, commitments, and friction.
- Keep coaching concise, practical, and non-diagnostic.
- Include at least one reinforcement cue when a real win exists.

## Output standard
- Send one concise Discord message with targeted prompts.
- After reply, return concise coaching read + top 1-3 actions.
- Write/update the day-part journal file once required captures are complete or correctly marked as unknown.

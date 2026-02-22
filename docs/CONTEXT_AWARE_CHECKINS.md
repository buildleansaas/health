# Context-Aware Check-Ins (Pepper)

## Purpose
- Replace static forms with concise, personalized check-ins.
- Keep journaling integrity while running a 2-touch daily loop.
- Use recent context so each prompt reflects current priorities, progress, and open risks.

## Inputs to read before each touch
- `profiles/austin-preferences.yaml`
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`
- Today journal files that exist so far:
- `journals/YYYY-MM-DD-daytime.md`
- `journals/YYYY-MM-DD-evening.md`
- Legacy compatibility reads when present:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- Yesterday journal files:
- `journals/YYYY-MM-DD-evening.md`
- `journals/YYYY-MM-DD-daytime.md`
- Legacy compatibility reads when present:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- Prior coach notes inside recent files.
- Open follow-ups from missing required fields or `Unknown - <reason>` values.

## Context extraction algorithm
1. Build a short state snapshot from inputs.
2. Build carryover queue for daytime:
- Include if prior evening was missed.
- Include unresolved required fields marked `Unknown - <reason>`.
- Include open follow-ups not yet closed.
3. Extract unresolved friction:
- Repeated blockers.
- Missed actions from prior touch.
- Missed touches or incomplete recoveries.
- Breakfast/lunch execution misses and impulsive fast-food events.
4. Extract prior commitments:
- Remainder-of-day plan commitments and non-negotiables.
- Training mode + fallback rung (`A/B/C`).
- Hydration, reset, and connection commitments.
5. Extract risk signals:
- Sleep guardrail drift.
- Hydration misses.
- Training risk or pain trend.
- Stress escalation and red-flag status.
6. Extract wins to reinforce:
- Completed commitments.
- Positive trend changes.
7. Rank top priorities for this touch:
- First: unresolved risk or missing required capture.
- Second: highest-impact next action.
- Third: reinforcement to sustain momentum.

## Question budget and composition
- Ask `3-6` targeted prompts per touch.
- Prioritize required captures tied to active risk.
- Bundle related fields only when clarity improves.
- Keep the message concise and answerable in under 90 seconds.

## Required captures for journaling integrity
- Daytime:
- Carryover resolution block when needed (prior evening missed, open unknowns, open follow-ups).
- Readiness color + energy + stress.
- Hydration status and nutrition/training status.
- Training mode token (`Train:<mode>`) + fallback rung (`A/B/C`) for remaining day.
- Schedule constraints + biggest friction.
- Remainder-of-day execution plan with timing sequence.
- Top risk + if-then fallback.
- Evening:
- Execution recap against daytime plan.
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency + meaningful connection completion.
- Meal logistics outcomes: breakfast/lunch execution, fallback use (`Intentional/Impulsive/None`), no-microwave adherence.
- Peak pain (0-10) + location + red-flag symptom.
- Reflection: what happened, what worked, friction, one change for tomorrow.
- Tomorrow preview (top 1-3 actions).
- One before-bed goal with timing.

## Follow-up logic for missing required data
- Missing required field: ask one immediate follow-up for only that field.
- `Unknown` allowed only when explicitly stated with a reason.
- Store unknown as `Unknown - <reason>`.
- Carry `Unknown` required fields to the next touch follow-up queue.
- Carry unresolved daytime unknowns into evening the same day.
- Carry unresolved evening unknowns into next-day daytime.
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
- Write/update canonical daily file once required captures are complete or correctly marked as unknown:
- `journals/YYYY-MM-DD-daytime.md`
- `journals/YYYY-MM-DD-evening.md`

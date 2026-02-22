# Daytime Check-In Prompt Guide (Internal)

This file is an internal generation guide. Do not send it as a fixed user-facing form.

## First read context
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`
- `profiles/austin-preferences.yaml`
- Today daytime/evening files if present.
- Yesterday evening/daytime files.
- Legacy files when present: morning/midday/afternoon.
- Prior coach notes, unresolved follow-ups, and unknown carryovers.

## Ask targeted questions
- Ask `3-6` prompts tailored to current context.
- Priority order:
1. Carryover from prior evening if needed.
2. Current readiness/energy/stress and active risk.
3. Hydration/nutrition/training status + mode token/fallback rung.
4. Schedule constraints and biggest friction.
5. Concrete remainder-of-day plan with times.
- Include one reinforcement cue when a clear win exists.
- Keep the message concise, plain English, one Discord message.

## Carryover inclusion rules
- Include carryover prompt only when one of these is true:
- Prior evening touch was missed.
- There is an unresolved required field marked `Unknown - <reason>`.
- There is an open required follow-up from recent files.

## Ensure required captures before journaling
- Carryover block when applicable.
- Readiness color + energy + stress.
- Hydration status + nutrition/training status.
- Training mode token (`Train:<mode>`) + fallback rung (`A/B/C`).
- Schedule constraints + biggest friction.
- Remainder-of-day execution plan with timing sequence.
- Top risk + if-then fallback.
- If required data is missing, ask only for that missing field before journaling.

After Austin replies:
- Pepper returns a short coaching read + top 1-3 actions.
- Pepper writes/updates `journals/YYYY-MM-DD-daytime.md` and commits.

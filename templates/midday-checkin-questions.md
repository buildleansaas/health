# Midday Check-In Prompt Guide (Internal)

This file is an internal generation guide. Do not send it as a fixed user-facing form.

## First read context
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`
- `profiles/austin-preferences.yaml`
- Today morning/midday files if present.
- Yesterday morning/midday/afternoon/evening files.
- Prior coach notes, open follow-ups, and unresolved morning commitments.

## Ask targeted questions
- Ask `3-6` prompts tailored to midday drift and remaining day constraints.
- Prioritize missing required captures, hydration/training/sleep guardrail risk, and unresolved friction.
- Include one meal-logistics nudge that checks breakfast execution and protects lunch timing before afternoon constraints.
- Include one reinforcement cue when a commitment was completed.
- Keep wording concise and practical.

## Ensure required captures before journaling
- Readiness color + energy.
- Stress + reset done/scheduled.
- Hydration status (urine color + 1L by noon yes/no).
- Sleep guardrails on track, nutrition on track, training mode/status.
- Breakfast execution (`Yes/Partial/No`) + lunch plan/status + fallback use (`Intentional/Impulsive/None` if used).
- Meaningful connection status (done/planned/missed).
- Pain (0-10) + location + red-flag symptom (yes/no).
- One next action with time.
- Optional line only if needed: focus/hunger/calendar pressure.
- If required data is missing, ask only for that missing field before journaling.

Pre-swim nights (Sun/Tue/Thu): avoid late hard HIIT; favor `A` or `C` if evening is tight.

After Austin replies:
- Pepper returns a short coaching read + top 1-3 actions for the rest of the day.
- Pepper writes/updates `journals/YYYY-MM-DD-midday.md` and commits.

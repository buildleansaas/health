# Afternoon Check-In Prompt Guide (Internal)

This file is an internal generation guide. Do not send it as a fixed user-facing form.

## First read context
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`
- `profiles/austin-preferences.yaml`
- Today morning/midday/afternoon files if present.
- Yesterday morning/midday/afternoon/evening files.
- Prior coach notes, unresolved midday actions, and open follow-ups.

## Ask targeted questions
- Ask `3-6` prompts tuned for late-day course correction.
- Prioritize unresolved friction, hydration/training risk, and what still needs to happen before evening.
- Include one logistics nudge on lunch completion, no-microwave adherence, and dinner timing risk if traffic/work runs late.
- Keep language concise and action-oriented.
- Avoid re-asking completed items unless status changed.

## Ensure required captures before journaling
- Energy + stress + reset status.
- Hydration progress + quick nutrition update.
- Lunch execution (`Yes/Partial/No`) + no-microwave adherence (`Yes/No`, reason if `No`).
- Training mode/status + pain (0-10) + location + red-flag symptom (yes/no).
- Biggest friction + one concrete action with time.
- Optional line only if needed: mood/focus/context.
- If required data is missing, ask only for that missing field before journaling.

After Austin replies:
- Pepper returns a short coaching read + top 1-3 actions to finish strong.
- Pepper writes/updates `journals/YYYY-MM-DD-afternoon.md` and commits.

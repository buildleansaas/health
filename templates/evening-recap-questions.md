# Evening Recap Prompt Guide (Internal)

This file is an internal generation guide. Do not send it as a fixed user-facing form.

## First read context
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md`
- `profiles/austin-preferences.yaml`
- Today daytime/evening files if present.
- Yesterday evening file for trend and unresolved carryover.
- Legacy files when present: morning/midday/afternoon.
- Prior coach notes and unresolved follow-ups.

## Ask targeted questions
- Ask `3-6` prompts focused on score-critical gaps, execution reality, and tomorrow setup.
- Prioritize required captures first.
- Include one direct prompt for execution recap vs daytime plan.
- Include one targeted meal-logistics reflection prompt (breakfast/lunch execution and fallback quality).
- Include one direct prompt for tomorrow preview + before-bed goal.
- Reinforce clear wins before correction when possible.
- Keep the message concise and practical.

## Ensure required captures before journaling
- Execution recap vs daytime plan.
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency + meaningful connection completion.
- Meal logistics outcomes: breakfast/lunch execution, fallback use (`Intentional/Impulsive/None`), no-microwave adherence.
- Peak pain (0-10) + location + red-flag symptom (yes/no).
- Reflection: what happened, what worked, friction, one change for tomorrow.
- Tomorrow preview (top 1-3 actions).
- One before-bed goal with timing.
- Optional line only if needed: alcohol/cannabis or extra context.
- If required data is missing, ask only for that missing field before journaling.

After Austin replies:
- Pepper computes scores using only: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
- Pepper returns: why (wins + score drag), insightful read, tomorrow top 1-3 actions, and before-bed lock-in.
- Pepper writes/updates `journals/YYYY-MM-DD-evening.md` and commits.

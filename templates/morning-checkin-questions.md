# Morning Check-In Prompt Guide (Internal)

This file is an internal generation guide. Do not send it as a fixed user-facing form.

## First read context
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `profiles/austin-preferences.yaml`
- Today files already written for the current date.
- Yesterday morning/midday/afternoon/evening files.
- Prior coach notes and unresolved follow-up items.

## Ask targeted questions
- Ask `3-6` prompts tailored to current context.
- Prioritize unresolved friction, prior commitments, and morning risk signals.
- Include reinforcement when a clear win exists.
- Keep the message concise, plain English, one Discord message.

## Ensure required captures before journaling
- Readiness color, energy, wake window hit, sleep quality.
- Caffeine cutoff, last meal cutoff, wind-down start.
- Nutrition plan + training mode (`Train:<mode>`) + fallback rung (`A/B/C`).
- Hydration 1L-by-noon plan.
- Stress + reset plan.
- Meaningful connection plan.
- Pain (0-10) + location + red-flag symptom (yes/no).
- Biggest risk + if-then + one non-negotiable.
- Optional line only if needed: awakenings, mood, schedule constraints.
- If required data is missing, ask only for that missing field before journaling.

After Austin replies:
- Pepper returns a short coaching read + top 1-3 actions.
- Pepper writes/updates `journals/YYYY-MM-DD-morning.md` and commits.

# System Source of Truth (Austin Coaching)

## Canonical active workflow
- `docs/CONTEXT_AWARE_CHECKINS.md` is the canonical algorithm for context-aware prompt generation and follow-up logic.
- `docs/COACHING_CRON_SYSTEM.md` is the operating source for check-in cadence, SLA, thresholds, and escalation.
- `docs/DISCORD_JOURNAL_WORKFLOW.md` is the source for Discord-to-journal execution details.
- `docs/COACHING_INTEGRATION_PLAN.md` is the behavior framework for scored domains + modifier facets.
- `docs/AUSTIN_GOAL_SETUP_2026-02-20.md` is the active goal and weekly structure.
- `docs/AUSTIN_MEAL_PREP_PLAYBOOK.md` is the meal logistics source for weekday breakfast/lunch execution defaults.
- `scripts/new-journal-entry-from-text.md` is the canonical parser/formatter prompt spec.
- `profiles/austin-preferences.yaml` is the canonical preference profile for cadence, tone, and coaching defaults.

## Canonical check-in mode
- Context-aware coaching is the default mode.
- Before each check-in, read today + yesterday day-part files, prior coach notes, unresolved follow-ups, and the preference profile.
- Send `3-6` targeted prompts based on current risk, commitments, friction, and wins.
- Do not send static fixed forms.
- Preserve journaling integrity by collecting all required captures with focused follow-up for missing required fields.

## Canonical active templates
- `templates/morning-checkin.md`
- `templates/midday-checkin.md`
- `templates/afternoon-checkin.md`
- `templates/evening-recap.md`
- `templates/weekly-review.md`
- `templates/weekly-recap.md`
- Question sets: `templates/morning-checkin-questions.md`, `templates/midday-checkin-questions.md`, `templates/afternoon-checkin-questions.md`, `templates/evening-recap-questions.md`

## Canonical scoring model (only model)
- Daily total: `0-10`
- Sleep: `0-4`
- Nutrition: `0-3`
- Training: `0-3`
- Formula: `total = sleep + nutrition + training`

## Canonical modifier facets (coaching only, not score points)
- Recovery readiness: Green/Yellow/Red + energy.
- Stress + 10-minute reset.
- Hydration sufficiency: urine color + 1L by noon.
- Social connection: meaningful 10+ minute connection yes/no.
- Risk/safety: pain 0-10 + location + red-flag symptom yes/no.

## Trigger and escalation source
- Operational thresholds and scripts: `docs/COACHING_CRON_SYSTEM.md`.
- Behavior framework: `docs/COACHING_INTEGRATION_PLAN.md`.
- User-specific defaults: `docs/AUSTIN_GOAL_SETUP_2026-02-20.md`.

## Workflow boundary
- Active execution is four daily day-part check-ins (morning/midday/afternoon/evening) plus weekly recap in `America/New_York` local date boundaries.
- Do not modify the scoring formula when adding or adjusting modifier facets.

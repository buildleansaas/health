# System Source of Truth (Austin Coaching)

## Canonical active workflow
- `docs/COACHING_CRON_SYSTEM.md` is the operating source for check-in cadence, SLA, and escalation.
- `docs/DISCORD_JOURNAL_WORKFLOW.md` is the source for Discord-to-journal execution details.
- `docs/COACHING_INTEGRATION_PLAN.md` is the behavior framework for sleep + nutrition + training.
- `docs/AUSTIN_GOAL_SETUP_2026-02-20.md` is the active goal and weekly structure.
- `scripts/new-journal-entry-from-text.md` is the canonical parser/formatter prompt spec.

## Canonical active templates
- `templates/morning-checkin.md`
- `templates/midday-checkin.md`
- `templates/evening-recap.md`
- `templates/weekly-review.md`
- `templates/weekly-recap.md`
- Question sets: `templates/morning-checkin-questions.md`, `templates/midday-checkin-questions.md`, `templates/evening-recap-questions.md`

## Canonical scoring model (only model)
- Daily total: `0-10`
- Sleep: `0-4`
- Nutrition: `0-3`
- Training: `0-3`
- Formula: `total = sleep + nutrition + training`

## Deprecated and historical files
- Deprecated templates: `templates/daily-recap.md`, `templates/daily-recap-questions.md`, `templates/daily-scorecard.md`
- Historical reference only: `reports/2026-02-19-sleep-bible.md`

## Migration note (from legacy sleep-only)
- Legacy system used one end-of-day sleep recap and `0-7` sleep score.
- Active system is day-part journaling with integrated domains:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-evening.md`
- Do not create new `daily-recap` or sleep-only scorecard entries.

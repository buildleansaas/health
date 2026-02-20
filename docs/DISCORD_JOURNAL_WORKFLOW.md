# Discord Journal Workflow (Pepper)

## Goal
- Run Discord check-ins across morning, midday, and evening.
- Convert replies into structured day-part journal files.
- Commit and push each completed check-in entry.

## System source
- Canonical map: `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- SLA/escalation policy: `docs/COACHING_CRON_SYSTEM.md`

## Journal files (per local day)
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-evening.md`
- Weekly file: `weekly/YYYY-[W]WW.md`

## End-to-end flow
1. Pepper sends the matching day-part questions in Discord.
2. Austin replies in freeform text.
3. Pepper asks follow-ups only for missing required fields.
4. Pepper redacts sensitive medical details.
5. Pepper formats content with the matching template.
6. Pepper writes or updates day-part file in `journals/`.
7. Pepper commits and pushes.

## Source templates
- Questions: `templates/morning-checkin-questions.md`, `templates/midday-checkin-questions.md`, `templates/evening-recap-questions.md`
- Entries: `templates/morning-checkin.md`, `templates/midday-checkin.md`, `templates/evening-recap.md`
- Weekly: `templates/weekly-review.md`, `templates/weekly-recap.md`

## Scoring model (only model)
- `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`
- Operational floor: `6/10+`
- Austin target: `7/10+` average (with push toward `8/10+`).

## Required fields matrix (no tables)
- Morning required:
- Wake window hit, sleep quality, morning energy.
- Caffeine cutoff, last meal cutoff, wind-down start.
- Nutrition anchors, training plan, training fallback.
- Biggest risk, if-then response, one non-negotiable.
- Morning optional:
- Night awakenings, mood/readiness, schedule/stress notes.
- Midday required:
- Energy, stress.
- Sleep guardrails on track, nutrition anchors on track, training status.
- One sleep adjustment, one nutrition adjustment, one training/recovery adjustment.
- Accountability action with timing.
- Midday optional:
- Focus, hunger/cravings, calendar/social notes.
- Evening required:
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- What happened (2-3 bullets), what worked (at least 1 bullet), friction (at least 1 bullet), one change for tomorrow.
- Evening optional:
- Symptoms/recovery notes, alcohol/cannabis, stress load.

## Unknown rule and follow-up logic
- `Unknown` allowed only if explicitly stated by Austin with a reason.
- Store as `Unknown - <reason>`.
- Missing required value without explicit unknown -> ask follow-up now.
- Required value marked `Unknown` -> force follow-up at next check-in.
- Optional fields never block file creation.

## Commit message conventions
- Morning:
- `git add journals/YYYY-MM-DD-morning.md`
- `git commit -m "journal: YYYY-MM-DD morning check-in"`
- Midday:
- `git add journals/YYYY-MM-DD-midday.md`
- `git commit -m "journal: YYYY-MM-DD midday check-in"`
- Evening:
- `git add journals/YYYY-MM-DD-evening.md`
- `git commit -m "journal: YYYY-MM-DD evening recap"`
- Weekly:
- `git add weekly/YYYY-[W]WW.md`
- `git commit -m "journal: YYYY-[W]WW weekly recap"`

## Safety and redaction
- Do not store sensitive medical details.
- Redact before writing:
- Medication names or doses -> `[medication redacted]`
- Diagnoses or conditions -> `[health detail redacted]`
- Lab or vitals numbers -> `[health metric redacted]`
- Doctor, clinic, or patient IDs -> `[personal health info redacted]`

## Date and timezone conventions
- Date format: `YYYY-MM-DD`.
- Timezone: Austin local timezone `America/New_York` unless changed.
- File date is local date of the check-in message.
- If message date is ambiguous after midnight, ask for explicit date.

## Minimum execution standard
- Every active day ends with an evening recap file.
- Morning is required.
- Midday is expected; if missed, recover at evening recap.
- Weekly recap is required once per week.

# Discord Journal Workflow (Pepper)

## Goal
- Run Discord check-ins with Austin across the day.
- Convert replies into structured journal files per day-part.
- Commit and push each completed check-in entry.
- Coach against integrated sleep + nutrition + training adherence.

## Journal files (per local day)
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-evening.md`
- Weekly file: `weekly/YYYY-[W]WW.md`

## End-to-end flow
1. Pepper sends the matching questions file in Discord.
2. Austin replies in freeform text.
3. Pepper asks follow-ups only for missing required fields.
4. Pepper redacts sensitive medical details.
5. Pepper formats content with the matching template.
6. Pepper writes or updates day-part file in `journals/`.
7. Pepper commits and pushes.

## Source templates
- Morning questions: `templates/morning-checkin-questions.md`
- Midday questions: `templates/midday-checkin-questions.md`
- Evening questions: `templates/evening-recap-questions.md`
- Morning entry: `templates/morning-checkin.md`
- Midday entry: `templates/midday-checkin.md`
- Evening entry: `templates/evening-recap.md`
- Weekly review: `templates/weekly-review.md`
- Weekly recap: `templates/weekly-recap.md`

## Scoring model
- Daily total: `0-10`
- Sleep: `0-4`
- Nutrition: `0-3`
- Training: `0-3`
- `6/10+` is a successful day.

## Follow-up logic (ask only what is missing)
- Missing required score/value: ask only for that value.
- Missing reflection bullets: ask only for missing bullet count.
- Missing one action/change: ask for one concrete action.
- Optional notes missing: do not block file creation.
- If midday is missed, continue and complete evening recap.

## Commit message conventions
- Morning check-in:
- `git add journals/YYYY-MM-DD-morning.md`
- `git commit -m "journal: YYYY-MM-DD morning check-in"`
- Midday check-in:
- `git add journals/YYYY-MM-DD-midday.md`
- `git commit -m "journal: YYYY-MM-DD midday check-in"`
- Evening recap:
- `git add journals/YYYY-MM-DD-evening.md`
- `git commit -m "journal: YYYY-MM-DD evening recap"`
- Weekly recap/review:
- `git add weekly/YYYY-[W]WW.md`
- `git commit -m "journal: YYYY-[W]WW weekly recap"`
- Batch option for multiple files:
- `git commit -m "journal: YYYY-MM-DD check-ins (morning/midday/evening)"`

## Safety and redaction
- Do not store sensitive medical details.
- Redact before writing:
- Medication names or doses -> `[medication redacted]`
- Diagnoses or conditions -> `[health detail redacted]`
- Lab or vitals numbers -> `[health metric redacted]`
- Doctor, clinic, or patient IDs -> `[personal health info redacted]`
- Keep entries behavioral and coaching-focused.

## Date and timezone conventions
- Date format: `YYYY-MM-DD` (ISO).
- Timezone: Austin local timezone (`America/New_York` unless changed).
- File date is local date of the check-in message.
- Morning check-in can reference last night, but file stays on current morning date.
- If message is after midnight and ambiguous, ask for explicit date.

## Minimum execution standard
- Every active day should end with an evening recap file.
- Morning check-in is required.
- Midday check-in is expected; if missed, recover at evening recap.
- Weekly recap is required once per week.

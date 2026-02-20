# Coaching Cron System (Pepper)

## Purpose
- Run structured integrated check-ins (sleep + nutrition + training) with low friction.
- Capture coaching data in day-part journal files.
- Keep entries concise, behavioral, and privacy-safe.

## Source of truth docs
- `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- `docs/DISCORD_JOURNAL_WORKFLOW.md`
- `docs/COACHING_INTEGRATION_PLAN.md`

## Modes
- Full mode: morning + midday + evening check-ins.
- Busy day mode: shorter prompts, same three check-ins.
- Minimum viable day mode: keep floor habits and finish evening recap.

## Check-in windows (local time)
- Morning: within 15-90 minutes of wake.
- Midday: near wake-day midpoint.
- Evening: end of day or 60-120 minutes pre-bed.

## Check-in SLA policy
- Initial prompt window:
- Send first prompt at start of each check-in window.
- Reminder timing:
- Reminder 1 at +30 minutes if no response.
- Reminder 2 at +90 minutes if no response.
- Missed-state threshold:
- Mark check-in missed when no response by window end + 2 hours.
- Recovery behavior:
- If morning is missed, midday starts with a 2-line recovery prompt plus outstanding required follow-ups.
- If midday is missed, evening recap includes a short recovery catch-up before scoring.
- If evening is missed, next morning starts with prior-day mini recap then normal morning check-in.

## Required fields matrix (no tables)
- Morning required:
- Wake window hit, sleep quality, morning energy.
- Caffeine cutoff, last meal cutoff, wind-down start.
- Nutrition anchors, training plan, training fallback.
- Biggest risk, if-then response, one non-negotiable.
- Morning optional:
- Night awakenings, mood/readiness, schedule/stress notes.
- Midday required:
- Energy and stress now.
- Sleep guardrails on track status.
- Nutrition anchors on track status.
- Training status.
- One sleep adjustment, one nutrition adjustment, one training/recovery adjustment.
- Accountability action with timing.
- Midday optional:
- Focus, hunger/cravings, calendar/social notes.
- Evening required:
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- What happened (2-3 bullets), what worked (at least 1 bullet), friction (at least 1 bullet), one change for tomorrow.
- Evening optional:
- Symptoms/recovery notes, alcohol/cannabis, stress load.

## Unknown rule
- `Unknown` is allowed only when Austin explicitly says it is unknown and gives a reason.
- Write as `Unknown - <reason>`.
- Do not auto-fill unknown for missing data.
- If a required field is `Unknown`, create a forced follow-up in the next check-in.

## What Pepper does
- Sends matching question set in Discord.
- Parses freeform replies into concise structured bullets.
- Asks follow-ups only for missing required fields.
- Redacts sensitive health details before writing.
- Writes or updates day-part files:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-evening.md`
- Commits and pushes with day-part commit messages.

## Scoring and anti-all-or-nothing rules
- Use only this model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
- Operational floor: `6/10+` keeps the streak alive.
- Austin target: `7/10+` average (with push toward `8/10+`).
- Missing one anchor does not void the day.
- Use fallback actions instead of quitting the day.
- Track weekly trend, not single-day perfection.

## Escalation
- Coaching escalation:
- If one check-in is missed, run recovery behavior on next check-in.
- If two check-ins are missed in a row, send restart prompt with one easy action.
- If adherence is below `6/10` for 3 consecutive days, run Busy Day mode for 48 hours.
- If 7-day average is below `7/10`, keep goals unchanged and reduce friction instead of adding new goals.
- Health-risk escalation scripts:
- Tier 1 monitor trigger: mild short-lived flag without acute danger.
- Tier 1 message template:
- `Noted. Let's monitor this for 48 hours. Keep tonight simple: caffeine cutoff, wind-down, and target bedtime.`
- Tier 2 clinician-soon trigger: persistent or worsening red flags for 3+ days.
- Tier 2 message template:
- `This pattern should be reviewed by a licensed clinician soon. Please book an appointment this week. I will keep coaching behaviors here.`
- Tier 3 urgent/crisis trigger: chest pain, breathing distress, suicidality, or immediate safety concern.
- Tier 3 message template:
- `This may be urgent. Contact local emergency services now or go to the nearest ER. If you might harm yourself or someone else, call or text 988 now. Reply when you are safe.`

## Date conventions
- Use ISO date format: `YYYY-MM-DD`.
- Use Austin local timezone for day boundaries: `America/New_York` unless changed.
- File date is the local date of the check-in message.
- If message date is ambiguous after midnight, ask for explicit date before writing.

## Privacy and redaction
- Do not store sensitive medical details.
- Redact before writing:
- Medication names or doses -> `[medication redacted]`
- Diagnoses or conditions -> `[health detail redacted]`
- Lab or vitals numbers -> `[health metric redacted]`
- Doctor, clinic, or patient IDs -> `[personal health info redacted]`
- Keep stored content behavioral: routines, adherence, stress, energy, friction, and next action.

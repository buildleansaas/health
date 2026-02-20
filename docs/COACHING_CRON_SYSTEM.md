# Coaching Cron System (Pepper)

## Purpose
- Run structured integrated check-ins (sleep + nutrition + training) with low friction.
- Capture coaching modifiers (readiness, stress/reset, hydration, connection, risk/safety) without changing score math.
- Keep entries concise, behavioral, and privacy-safe.

## Source of truth docs
- `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- `docs/DISCORD_JOURNAL_WORKFLOW.md`
- `docs/COACHING_INTEGRATION_PLAN.md`

## Modes
- Full mode: morning + midday + evening check-ins.
- Busy day mode: shorter prompts, same three check-ins.
- Minimum viable day mode: keep floor habits and finish evening recap.

## Check-in windows (local time, America/New_York)
- Morning: within 15-90 minutes of wake.
- Midday: near wake-day midpoint.
- Evening: end of day or 60-120 minutes pre-bed.

## Check-in SLA policy
- Initial prompt window: send first prompt at start of each check-in window.
- Reminder timing: reminder 1 at +30 minutes, reminder 2 at +90 minutes if no response.
- Missed-state threshold: mark check-in missed when no response by window end + 2 hours.
- Recovery behavior:
- If morning is missed, midday starts with a 2-line recovery prompt plus outstanding required follow-ups.
- If midday is missed, evening recap includes a short recovery catch-up before scoring.
- If evening is missed, next morning starts with prior-day mini recap then normal morning check-in.

## Prompt design standard
- Ask required fields first.
- Ask optional fields as one optional line only.
- Keep each check-in question set answerable in under 90 seconds.

## Required fields matrix (no tables)
- Morning required:
- Readiness color, energy, wake window hit, sleep quality.
- Sleep guardrails (caffeine cutoff, last meal cutoff, wind-down start).
- Nutrition + training plan/fallback.
- Hydration 1L-by-noon plan.
- Stress + 10-minute reset plan.
- Meaningful connection plan (10+ minutes, yes/no).
- Risk check: pain (0-10) + location + red-flag symptom (yes/no).
- Biggest risk + if-then + one non-negotiable.
- Morning optional:
- One optional line: awakenings, mood/readiness, schedule constraints.
- Midday required:
- Readiness color and energy.
- Stress + reset done/scheduled.
- Hydration sufficiency (urine color + 1L by noon yes/no).
- Guardrails on-track, nutrition on-track, training status.
- Meaningful connection status (done/planned/missed).
- Risk check: pain (0-10) + location + red-flag symptom (yes/no).
- One next action with time.
- Midday optional:
- One optional line: focus/hunger note, calendar pressure, other context.
- Evening required:
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency and connection completion.
- Risk/safety: peak pain (0-10) + location + red-flag symptom (yes/no).
- Reflection: what happened (2), what worked (1), friction (1), one change for tomorrow.
- Evening optional:
- One optional line: alcohol/cannabis or extra context.

## Unknown rule
- `Unknown` is allowed only when Austin explicitly says it is unknown and gives a reason.
- Write as `Unknown - <reason>`.
- Do not auto-fill unknown for missing data.
- If a required field is `Unknown`, create a forced follow-up in the next check-in.

## What Pepper does
- Sends the matching question set in Discord.
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
- New facets are coaching modifiers/triggers only; they do not add score points.
- Operational floor: `6/10+` keeps the streak alive.
- Austin target: `7/10+` average (with push toward `8/10+`).
- Missing one anchor does not void the day.
- Use fallback actions instead of quitting the day.
- Track weekly trend, not single-day perfection.

## Modifier trigger rules (short, explicit)
- Readiness Yellow threshold: `Yellow` for >=2 consecutive check-ins or energy <=2 -> fallback training + bedtime protection for next 24h.
- Readiness Red threshold: any `Red` or energy =1 -> recovery-only day, no high-intensity training.
- Stress threshold: stress >=4/5 -> run 10-minute reset within 60 minutes; if still >=4 at next check-in, switch to Busy Day mode.
- Hydration misses: dark urine or missed 1L by noon -> same-day hydration recovery; if >=2 misses in a week, enforce fixed AM + pre-noon water blocks.
- Connection misses: no meaningful 10+ minute connection for 2 consecutive days -> schedule next-day connection block before 6pm.
- Pain/red-flag escalation: red-flag yes or pain >=7 -> urgent escalation now. Pain 4-6 for >48h (or pain >=3 for 3+ days) -> clinician-soon escalation.

## Escalation scripts
- Coaching escalation:
- If one check-in is missed, run recovery behavior on next check-in.
- If two check-ins are missed in a row, send restart prompt with one easy action.
- If adherence is below `6/10` for 3 consecutive days, run Busy Day mode for 48 hours.
- If 7-day average is below `7/10`, keep goals unchanged and reduce friction instead of adding new goals.
- Health-risk escalation scripts:
- Tier 1 monitor trigger: mild short-lived pain (`1-3`) without red-flag symptoms.
- Tier 1 message template:
- `Noted. Let's monitor this for 48 hours. Keep tonight simple: caffeine cutoff, wind-down, and target bedtime.`
- Tier 2 clinician-soon trigger: pain `4-6` persisting >48h, pain `>=3` for 3+ days, or worsening function.
- Tier 2 message template:
- `This pattern should be reviewed by a licensed clinician soon. Please book an appointment this week. I will keep coaching behaviors here.`
- Tier 3 urgent/crisis trigger: red-flag symptom yes, pain `>=7`, chest pain, breathing distress, suicidality, or immediate safety concern.
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

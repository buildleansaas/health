# Coaching Cron System (Pepper)

## Purpose
- Run context-aware integrated check-ins with low friction.
- Capture coaching modifiers (readiness, stress/reset, hydration, connection, risk/safety) without changing score math.
- Keep entries concise, behavioral, and privacy-safe.

## Source of truth docs
- `docs/SYSTEM_SOURCE_OF_TRUTH.md`
- `docs/CONTEXT_AWARE_CHECKINS.md`
- `docs/DISCORD_JOURNAL_WORKFLOW.md`
- `docs/COACHING_INTEGRATION_PLAN.md`

## Canonical prompt mode
- Context-aware mode is default for both daily touches.
- Before each touch, read context from today + yesterday files, prior coaching notes, unresolved follow-ups, and `profiles/austin-preferences.yaml`.
- Generate `3-6` targeted prompts instead of fixed forms.
- Preserve required captures through focused follow-up on missing required data.

## Modes
- Standard mode: daytime + evening touches.
- Busy day mode: shorter prompts, same two touches.
- Minimum viable day mode: keep floor habits and finish evening recap.

## Standard training mode enum (use everywhere)
- `Masters Swim` (`Train:MastersSwim`)
- `Gym LP` (`Train:GymLP`)
- `Home Strength (KB+Pullup+Rings)` (`Train:HomeStrength`)
- `HIIT Only (Chris Heria style)` (`Train:HIITOnly`)
- `Minimum Day` (`Train:MinimumDay`)
- `Recovery` (`Train:Recovery`)

## Fallback ladder (A/B/C)
- `A = Home Strength 25-35 min`
- `B = HIIT 10-15 min`
- `C = Minimum Day 8-12 min`

## Pre-swim-night training guidance (Sun/Tue/Thu)
- Avoid late hard HIIT.
- If evening is tight, favor `A` or `C`.

## Check-in windows (local time, America/New_York)
- Daytime: target `11:30`, window `10:30-14:30`.
- Evening: target `20:30`, window `19:30-22:30` (or 60-120 minutes pre-bed).

## Check-in SLA policy
- Initial prompt: send first prompt at target time.
- Reminder timing: reminder 1 at `+30 minutes`, reminder 2 at `+90 minutes` if no response.
- Missed-state threshold: mark touch missed when no response by window end + 2 hours.
- Recovery behavior:
- If daytime is missed, evening starts with a short catch-up block before recap/scoring.
- If evening is missed, next daytime starts with prior-night carryover and immediate day plan.
- If both touches are missed, next daytime sends restart prompt + one easy action.

## Prompt design standard
- Read context first (`docs/CONTEXT_AWARE_CHECKINS.md`).
- Ask `3-6` targeted prompts that prioritize required fields with active risk.
- Ask optional fields as one optional line only.
- Keep each touch answerable in under 90 seconds.
- Do not send repetitive boilerplate when a field is already known and unchanged.

## Required fields matrix (no tables)
- Daytime required:
- Carryover block when needed (prior evening missed, unresolved unknowns, or open follow-ups).
- Prior evening tomorrow-plan baseline (when present) + reality-day changes.
- Readiness color + energy + stress now.
- Hydration status and nutrition/training status.
- Training mode token (`Train:<mode>`) + fallback rung (`A/B/C`) for remaining day.
- Schedule constraints and biggest friction.
- Concrete remainder-of-day execution plan with timing sequence (updated from baseline when needed).
- Top risk + if-then fallback.
- Daytime optional:
- One optional line: mood/readiness note, extra context, or schedule nuance.
- Evening required:
- Execution recap against daytime plan (what completed, what slipped, why).
- Sleep score (`0-4`), nutrition score (`0-3`), training score (`0-3`), total score (`0-10`).
- Readiness trend, peak stress + reset completion.
- Hydration sufficiency and connection completion.
- Risk/safety: peak pain (0-10) + location + red-flag symptom (yes/no).
- Reflection: what happened (2), what worked (1), friction (1), one change for tomorrow.
- Tomorrow schedule/context capture from Austin (hard windows, constraints, likely friction).
- Explicit output 1: tomorrow preview (top 1-3 actions).
- Explicit output 2: full tomorrow execution plan (morning/daytime/evening blocks + fallback), tailored to tomorrow schedule/context.
- One before-bed goal with timing.
- Evening optional:
- One optional line: alcohol/cannabis or extra context.

## Unknown rule
- `Unknown` is allowed only when Austin explicitly says it is unknown and gives a reason.
- Write as `Unknown - <reason>`.
- Do not auto-fill unknown for missing data.
- If a required field is `Unknown`, create a forced follow-up in the next touch.

## What Pepper does
- Builds a context-aware prompt for the current touch in Discord.
- Parses freeform replies into concise structured bullets.
- Asks follow-ups only for missing required fields.
- Captures durable user preference changes in `profiles/austin-preferences.yaml`.
- Computes coaching output at each touch:
  - Daytime: coaching read + remainder-of-day next actions.
  - Evening: computed scorecard + why + insightful read + explicit output 1 (tomorrow preview top actions) + explicit output 2 (full tomorrow execution plan with morning/daytime/evening blocks + fallback) + before-bed goal lock-in.
- Redacts sensitive health details before writing.
- Writes or updates canonical daily files:
- `journals/YYYY-MM-DD-daytime.md`
- `journals/YYYY-MM-DD-evening.md`
- Keeps legacy compatibility for historical context reads:
- `journals/YYYY-MM-DD-morning.md`
- `journals/YYYY-MM-DD-midday.md`
- `journals/YYYY-MM-DD-afternoon.md`
- Commits and pushes with touch-specific commit messages.
- For material user updates between touches, updates the active daily journal file and commits a follow-up note.

## Scoring and anti-all-or-nothing rules
- Use only this model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
- New facets are coaching modifiers/triggers only; they do not add score points.
- Operational floor: `6/10+` keeps the streak alive.
- Austin target: `7/10+` average (with push toward `8/10+`).
- Missing one anchor does not void the day.
- Use fallback actions instead of quitting the day.
- Track weekly trend, not single-day perfection.

## Modifier trigger rules (short, explicit)
- Readiness Yellow threshold: `Yellow` for >=2 consecutive touches or energy <=2 -> fallback ladder (`A` then `B` then `C`) + bedtime protection for next 24h.
- Readiness Red threshold: any `Red` or energy =1 -> recovery-only day, no high-intensity training.
- Stress threshold: stress >=4/5 -> run 10-minute reset within 60 minutes; if still >=4 at next touch, switch to Busy Day mode.
- Hydration misses: dark urine or missed 1L by noon -> same-day hydration recovery; if >=2 misses in a week, enforce fixed AM + pre-noon water blocks.
- Connection misses: no meaningful 10+ minute connection for 2 consecutive days -> schedule next-day connection block before 6pm.
- Pain/red-flag escalation: red-flag yes or pain >=7 -> urgent escalation now. Pain 4-6 for >48h (or pain >=3 for 3+ days) -> clinician-soon escalation.

## Escalation scripts
- Coaching escalation:
- If one touch is missed, run recovery behavior on next touch.
- If both touches are missed in one day, send restart prompt with one easy action.
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

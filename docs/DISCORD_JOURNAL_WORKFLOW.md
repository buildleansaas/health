# Discord Journal Workflow (Pepper)

## Goal
Run a daily Discord recap with Austin, convert replies into `journals/YYYY-MM-DD.md`, then commit and push.

## End-to-End Flow
1. Pepper sends recap questions in Discord (use `templates/daily-recap-questions.md`).
2. Austin replies in freeform text.
3. Pepper checks for missing fields and asks targeted follow-ups.
4. Pepper redacts sensitive medical details.
5. Pepper formats content using `templates/daily-recap.md`.
6. Pepper writes/updates `journals/YYYY-MM-DD.md`.
7. Pepper commits and pushes:
   - `git add journals/YYYY-MM-DD.md`
   - `git commit -m "journal: YYYY-MM-DD daily recap"`
   - `git push`

## Follow-Up Logic (Ask Only What Is Missing)
- Missing scorecard item: ask only for that item as yes/no or short text.
- Fewer than 3 "What happened" bullets: ask for the missing bullets.
- Missing "What worked": ask for 1-2 wins.
- Missing friction: ask for 1-2 blockers.
- Missing "One change for tonight": ask for one concrete action.
- Optional notes missing: do not block journal creation.

Use short follow-up phrasing:
- "Quick fill: did you hit caffeine cutoff (>=8h pre-bed)?"
- "Give me one blocker from today."
- "What is the one change for tonight?"

## Safety and Redaction
Do not store sensitive medical details. Keep entries behavioral and coaching-focused.

Redact before writing:
- Medication names/doses -> `[medication redacted]`
- Diagnoses/conditions -> `[health detail redacted]`
- Lab/vitals numbers -> `[health metric redacted]`
- Doctor/clinic/patient IDs -> `[personal health info redacted]`

Allowed examples:
- "Energy was low"
- "Stress high after work"
- "Woke up twice"

## Date, Filename, and Timezone Conventions
- Date format: `YYYY-MM-DD` (ISO).
- Filename: `journals/YYYY-MM-DD.md`.
- Use Austin's local timezone for day boundaries (Austin is `America/New_York` unless he says otherwise).
- Default behavior: **assume we are logging “the day that just ended.”**
- Only ask to clarify the date if it’s after midnight, travel/jet lag, or the message is ambiguous.
- One journal file per local day.

## Example
Discord conversation:
- Pepper: "Quick recap: scorecard, what happened (3 bullets), what worked, friction, one change."
- Austin: "Score 5/7. Missed wind-down and late meal. Morning light done. Busy day, long call, gym. Worked: no caffeine after 2pm. Friction: late dinner. Change: prep dinner earlier."
- Pepper follow-up: "Sleep quality >=4/5?"
- Austin: "3/5."

Resulting file `journals/2026-02-19.md`:

```md
# Daily Recap (Sleep System)

Date: 2026-02-19

## The 7-point score (0–7)
- Wake time hit (+/-30m): Yes
- Morning light (10–30m outdoors): Yes
- Caffeine cutoff (>=8h pre-bed): Yes
- Last meal (>=90m pre-bed): No
- Room: cool/dark/quiet: Yes
- Wind-down done (60m): No
- Sleep quality >=4/5: No (3/5)

## What happened (3 bullets)
- Busy workday with one long call.
- Got gym session done.
- Dinner ran late.

## What worked (1–2 bullets)
- No caffeine after 2pm.

## What sucked / friction (1–2 bullets)
- Late dinner made wind-down harder.

## One change for tonight (ONE thing)
- Prep dinner earlier so last meal is >=90m before bed.

## Notes (optional)
- Training: Gym.
- Alcohol/cannabis:
- Stress: High during work call.
```

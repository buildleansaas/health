# Morning Check-In (Integrated System)

Date:
Check-in: Morning
Timezone: America/New_York

Scoring model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
Modifier facets (not score points): readiness, stress/reset, hydration, connection, risk/safety.
Training mode enum: `Gym LP`, `Home Strength (KB+Pullup+Rings)`, `HIIT Only (Chris Heria style)`, `Minimum Day`, `Recovery`.
Mode token format: `Train:GymLP|Train:HomeStrength|Train:HIITOnly|Train:MinimumDay|Train:Recovery`.
Fallback ladder: `A = Home Strength 25-35 min`, `B = HIIT 10-15 min`, `C = Minimum Day 8-12 min`.
Pre-swim nights (Sun/Tue/Thu): avoid late hard HIIT; if evening is tight, favor `A` or `C`.

## Required (fast)
- Recovery readiness (Green/Yellow/Red):
- Energy (1-5):
- Wake window hit (+/-30m):
- Sleep quality (1-5):
- Sleep guardrails today (caffeine cutoff / last meal cutoff / wind-down start):
- Nutrition anchors + training mode token + fallback rung (A/B/C) (1 line):
- Hydration kickoff: 1L by noon plan (yes/no + plan):
- Stress now (1-5) + 10-min reset time:
- Meaningful connection planned (10+ min) (yes/no + who):
- Risk check: pain (0-10), location, red-flag symptom (yes/no):
- Biggest risk + if-then:
- One non-negotiable:

## Optional
- Optional: awakenings count, mood/readiness note, schedule constraint.

Unknown format: `Unknown - reason` (only if explicitly stated).

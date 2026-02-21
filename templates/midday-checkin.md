# Midday Check-In (Integrated System)

Date:
Check-in: Midday
Timezone: America/New_York

Scoring model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
Modifier facets (not score points): readiness, stress/reset, hydration, connection, risk/safety.
Training mode enum: `Masters Swim`, `Gym LP`, `Home Strength (KB+Pullup+Rings)`, `HIIT Only (Chris Heria style)`, `Minimum Day`, `Recovery`.
Mode token format: `Train:MastersSwim|Train:GymLP|Train:HomeStrength|Train:HIITOnly|Train:MinimumDay|Train:Recovery`.
Fallback ladder: `A = Home Strength 25-35 min`, `B = HIIT 10-15 min`, `C = Minimum Day 8-12 min`.
Pre-swim nights (Sun/Tue/Thu): avoid late hard HIIT; if evening is tight, favor `A` or `C`.

## Required (fast)
- Recovery readiness now (Green/Yellow/Red):
- Energy now (1-5):
- Stress now (1-5) + 10-min reset done/scheduled:
- Hydration sufficiency: urine color + 1L by noon hit (yes/no):
- Sleep guardrails on track (yes/no):
- Nutrition anchors on track (yes/no):
- Training status (Train token + done / pending / fallback A/B/C):
- Meaningful connection status (10+ min) (done / planned / missed):
- Risk check: pain (0-10), location, red-flag symptom (yes/no):
- One next action + time:

## Optional
- Optional: focus/hunger note, calendar pressure, other context.

## Pepper Coach Response (required)
- Midday coaching read (1-2 lines):
- Next 1-3 actions for the rest of today:
  1)
  2)
  3)

Unknown format: `Unknown - reason` (only if explicitly stated).

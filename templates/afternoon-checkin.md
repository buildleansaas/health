# Afternoon Check-In (Integrated System)

Date:
Check-in: Afternoon
Timezone: America/New_York

Scoring model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
Modifier facets (not score points): readiness, stress/reset, hydration, connection, risk/safety.
Training mode enum: `Masters Swim`, `Gym LP`, `Home Strength (KB+Pullup+Rings)`, `HIIT Only (Chris Heria style)`, `Minimum Day`, `Recovery`.
Mode token format: `Train:MastersSwim|Train:GymLP|Train:HomeStrength|Train:HIITOnly|Train:MinimumDay|Train:Recovery`.
Fallback ladder: `A = Home Strength 25-35 min`, `B = HIIT 10-15 min`, `C = Minimum Day 8-12 min`.

## Required (fast)
- Energy now (1-5):
- Stress now (1-5) + reset done/scheduled:
- Hydration progress so far (estimated liters + on-track yes/no):
- Nutrition update since midday (short):
- Training status now (done / pending / fallback / recovery):
- Training type now (Train token):
- Risk check: pain (0-10), location, red-flag symptom (yes/no):
- Biggest friction this afternoon:
- One concrete action + time for next 2-3 hours:

## Optional
- Optional: mood/focus/context.

## Pepper Coach Response (required)
- Afternoon coaching read (1-2 lines):
- Next 1-3 actions to finish strong:
  1)
  2)
  3)

Unknown format: `Unknown - reason` (only if explicitly stated).

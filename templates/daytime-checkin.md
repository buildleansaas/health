# Daytime Check-In (Integrated System)

Date:
Check-in: Daytime
Timezone: America/New_York

Scoring model (unchanged): `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
Modifier facets (not score points): readiness, stress/reset, hydration, connection, risk/safety.
Training mode enum: `Masters Swim`, `Gym LP`, `Home Strength (KB+Pullup+Rings)`, `HIIT Only (Chris Heria style)`, `Minimum Day`, `Recovery`.
Mode token format: `Train:MastersSwim|Train:GymLP|Train:HomeStrength|Train:HIITOnly|Train:MinimumDay|Train:Recovery`.
Fallback ladder: `A = Home Strength 25-35 min`, `B = HIIT 10-15 min`, `C = Minimum Day 8-12 min`.

## 1) Carryover + Prior-Night Plan Baseline (required when applicable)
- Prior evening tomorrow-plan baseline available (yes/no):
- Baseline summary from prior evening:
- Reality-day changes since last night (schedule, energy, friction):
- Prior evening missed or unresolved follow-up present (yes/no):
- Carryover items to resolve now:
- Carryover/baseline update resolved in this touch (yes/no + note):

## 2) Current Status Snapshot (required)
- Recovery readiness now (Green/Yellow/Red):
- Energy now (1-5):
- Stress now (1-5) + 10-min reset done/scheduled:
- Hydration status right now (quick):
- Nutrition status right now (quick):
- Training status now (Train token + planned/pending/fallback/recovery):

## 3) Schedule Constraints (required)
- Hard constraints for rest of day:
- Biggest friction right now:

## 4) Remainder-of-Day Execution Plan (required)
- Ordered plan with timing:
  1)
  2)
  3)

## 5) Top Risk + Fallback (required)
- Top risk that could break execution:
- If-then fallback:
- Fallback rung for today (`A/B/C`):

## 6) Pepper Coach Response (required)
- Daytime coaching read (1-2 lines):
- Next 1-3 actions for remainder of day (baseline-adjusted):
  1)
  2)
  3)

Unknown format: `Unknown - reason` (only if explicitly stated).

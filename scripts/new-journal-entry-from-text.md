# Prompt Spec: New Journal Entry From Raw Text (Day-Part)

Paste this into Codex and replace placeholders.

```text
You are formatting a day-part journal entry for this repo.

Inputs:
- Date (local): {{YYYY-MM-DD}}
- Check-in part: {{daytime|evening|morning|midday|afternoon}}
- Timezone: {{IANA timezone}}
- Raw Discord answers:
{{PASTE_RAW_TEXT}}

Context to read before parsing:
- docs/CONTEXT_AWARE_CHECKINS.md
- profiles/austin-preferences.yaml
- Today day-part files that already exist.
- Yesterday evening/daytime files.
- Legacy history files if present: morning/midday/afternoon.
- Prior coach notes and unresolved follow-ups.

Rules:
1) Canonical check-in parts are `daytime` and `evening`.
2) Legacy aliases `morning|midday|afternoon` are accepted for historical/backfill parsing compatibility.
3) Normalize part for canonical output unless explicit legacy backfill is requested:
   - `daytime` -> canonical `daytime`
   - `evening` -> canonical `evening`
   - `morning|midday|afternoon` -> canonical `daytime`
4) Select template by normalized canonical part:
   - daytime -> templates/daytime-checkin.md
   - evening -> templates/evening-recap.md
5) Output filename must be canonical by default:
   - journals/{{YYYY-MM-DD}}-daytime.md
   - journals/{{YYYY-MM-DD}}-evening.md
6) If explicit historical backfill says to keep legacy part name, use matching deprecated legacy template/file name:
   - morning -> templates/morning-checkin.md -> journals/{{YYYY-MM-DD}}-morning.md
   - midday -> templates/midday-checkin.md -> journals/{{YYYY-MM-DD}}-midday.md
   - afternoon -> templates/afternoon-checkin.md -> journals/{{YYYY-MM-DD}}-afternoon.md
7) Context-aware ingestion notes:
   - Use recent context to resolve references like "same as earlier", "still pending", or "did it".
   - Preserve unresolved friction and prior commitments when they are updated in raw answer.
   - Do not invent details that are not present in raw text or explicit recent context.
8) Required-field behavior:
   - If a required field is missing, ask a follow-up question for only that missing field.
   - Do not ask about optional fields.
9) Unknown handling:
   - `Unknown` is allowed only if Austin explicitly says unknown and gives a reason.
   - Write as `Unknown - <reason>`.
   - Do not auto-fill Unknown for missing fields.
   - If a required field is `Unknown`, include it in "Next-check-in follow-up".
10) Redact sensitive medical info:
   - meds/doses -> [medication redacted]
   - diagnoses/conditions -> [health detail redacted]
   - lab/vitals -> [health metric redacted]
11) Keep wording concise and behavioral.
12) Recognize training mode enum from raw text:
   - Canonical display values:
     - `Masters Swim`
     - `Gym LP`
     - `Home Strength (KB+Pullup+Rings)`
     - `HIIT Only (Chris Heria style)`
     - `Minimum Day`
     - `Recovery`
   - Canonical quick tokens:
     - `Train:MastersSwim`
     - `Train:GymLP`
     - `Train:HomeStrength`
     - `Train:HIITOnly`
     - `Train:MinimumDay`
     - `Train:Recovery`
   - Accept loose variants and map to canonical:
     - `masters`, `masters swim`, `swim practice`, `swim team` -> `Masters Swim`
     - `gym`, `lp`, `greyskull`, `phrak` -> `Gym LP`
     - `home strength`, `kb`, `kettlebell`, `pullup`, `rings` -> `Home Strength (KB+Pullup+Rings)`
     - `hiit`, `chris heria`, `heria` -> `HIIT Only (Chris Heria style)`
     - `minimum`, `minimum day`, `micro` -> `Minimum Day`
     - `recovery`, `rest`, `easy recovery` -> `Recovery`
   - Parse fallback ladder where present:
     - `A = Home Strength 25-35 min`
     - `B = HIIT 10-15 min`
     - `C = Minimum Day 8-12 min`
   - If training is mentioned but mode is ambiguous, ask one follow-up for exact mode token.
13) Always include a Pepper coaching block in the journal output:
   - Daytime: short coaching read + remainder-of-day next 1-3 actions.
   - Evening: computed scores + why + insightful read + tomorrow preview + before-bed goal.
14) Keep scoring model unchanged everywhere:
   - `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.

Required fields by canonical part:
- Daytime (applies to `daytime` and legacy aliases when normalized):
  - carryover block only when needed (prior evening missed, unresolved unknowns, open follow-ups)
  - readiness color + energy + stress
  - hydration status + nutrition/training status
  - training mode token + fallback rung (`A/B/C`)
  - schedule constraints + biggest friction
  - remainder-of-day execution plan with timing sequence
  - top risk + if-then fallback
- Evening:
  - execution recap vs daytime plan
  - sleep score (0-4), nutrition score (0-3), training score (0-3), total score (0-10)
  - readiness trend, peak stress + reset completion
  - hydration sufficiency + meaningful connection completion
  - peak pain (0-10) + location + red-flag symptom
  - reflection: what happened, what worked, friction, one change for tomorrow
  - tomorrow preview (top 1-3 actions)
  - one before-bed goal with timing

Output format:
- First: "Follow-up questions (now)" section (only if required fields are missing).
- Second: "Next-check-in follow-up" section (only if required fields are `Unknown`).
- Third: "Journal markdown" section with final file content.
```

## Rubric (Self-Check Before Final Output)
- Completeness (0-5): required fields handled or follow-up created.
- Fidelity (0-5): no invented facts.
- Actionability (0-5): concrete next action captured.
- Safety (0-5): sensitive health info redacted.
- Format (0-5): correct template and filename behavior.

Minimum acceptable total: 21/25.

# Prompt Spec: New Journal Entry From Raw Text (Day-Part)

Paste this into Codex and replace placeholders.

```text
You are formatting a day-part journal entry for this repo.

Inputs:
- Date (local): {{YYYY-MM-DD}}
- Check-in part: {{morning|midday|afternoon|evening}}
- Timezone: {{IANA timezone}}
- Raw Discord answers:
{{PASTE_RAW_TEXT}}

Context to read before parsing:
- docs/CONTEXT_AWARE_CHECKINS.md
- profiles/austin-preferences.yaml
- Today day-part files that already exist.
- Yesterday morning/midday/afternoon/evening files.
- Prior coach notes and unresolved follow-ups from recent files.

Rules:
1) `afternoon` is a first-class supported check-in part and must always map to its own template/file.
2) Select template by check-in part:
   - morning -> templates/morning-checkin.md
   - midday -> templates/midday-checkin.md
   - afternoon -> templates/afternoon-checkin.md
   - evening -> templates/evening-recap.md
3) Output filename must be:
   - journals/{{YYYY-MM-DD}}-{{part}}.md
4) Context-aware ingestion notes:
   - Use recent context to resolve references like "same as earlier", "still pending", or "did it".
   - Preserve unresolved friction and prior commitments when they are updated in the raw answer.
   - Do not invent details that are not present in raw text or explicit recent context.
5) Required-field behavior:
   - If a required field is missing, ask a follow-up question for only that missing field.
   - Do not ask about optional fields.
6) Unknown handling:
   - `Unknown` is allowed only if Austin explicitly says unknown and gives a reason.
   - Write as `Unknown - <reason>`.
   - Do not auto-fill Unknown for missing fields.
   - If a required field is `Unknown`, include it in "Next-check-in follow-up".
7) Redact sensitive medical info:
   - meds/doses -> [medication redacted]
   - diagnoses/conditions -> [health detail redacted]
   - lab/vitals -> [health metric redacted]
8) Keep wording concise and behavioral.
9) Recognize training mode enum from raw text:
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
10) Always include a Pepper coaching block in the journal output:
   - Morning/midday/afternoon: short coaching read + next 1-3 actions.
   - Evening: computed scores + why + insightful read + tomorrow plan.

Required fields by part:
- Morning:
  - readiness color, energy, wake window hit, sleep quality
  - caffeine cutoff, last meal cutoff, wind-down start
  - nutrition plan, training mode, fallback rung (`A/B/C`)
  - hydration 1L-by-noon plan
  - stress + reset plan
  - meaningful connection plan
  - pain (0-10) + location + red-flag symptom
  - biggest risk + if-then response + one non-negotiable
- Midday:
  - readiness color + energy
  - stress + reset done/scheduled
  - hydration status (urine color + 1L by noon yes/no)
  - guardrails on-track, nutrition on-track, training mode/status
  - meaningful connection status
  - pain (0-10) + location + red-flag symptom
  - one next action with timing
- Afternoon:
  - energy + stress + reset status
  - hydration progress + quick nutrition update
  - training mode/status + pain/location/red-flag risk check
  - biggest friction + one concrete action with timing
- Evening:
  - sleep score (0-4), nutrition score (0-3), training score (0-3), total score (0-10)
  - readiness trend, peak stress + reset completion
  - hydration sufficiency + meaningful connection completion
  - peak pain (0-10) + location + red-flag symptom
  - what happened, what worked, friction, one change for tomorrow

Output format:
- First: "Follow-up questions (now)" section (only if required fields are missing).
- Second: "Next-check-in follow-up" section (only if required fields are `Unknown`).
- Third: "Journal markdown" section with final file content for journals/{{YYYY-MM-DD}}-{{part}}.md.
```

## Rubric (Self-Check Before Final Output)
- Completeness (0-5): required fields handled or follow-up created.
- Fidelity (0-5): no invented facts.
- Actionability (0-5): concrete next action captured.
- Safety (0-5): sensitive health info redacted.
- Format (0-5): correct day-part template and filename.

Minimum acceptable total: 21/25.

# Prompt Spec: New Journal Entry From Raw Text (Day-Part)

Paste this into Codex and replace placeholders.

```text
You are formatting a day-part journal entry for this repo.

Inputs:
- Date (local): {{YYYY-MM-DD}}
- Check-in part: {{morning|midday|evening}}
- Timezone: {{IANA timezone}}
- Raw Discord answers:
{{PASTE_RAW_TEXT}}

Rules:
1) Select template by check-in part:
   - morning -> templates/morning-checkin.md
   - midday -> templates/midday-checkin.md
   - evening -> templates/evening-recap.md
2) Output filename must be:
   - journals/{{YYYY-MM-DD}}-{{part}}.md
3) Required-field behavior:
   - If a required field is missing, ask a follow-up question for only that missing field.
   - Do not ask about optional fields.
4) Unknown handling:
   - `Unknown` is allowed only if Austin explicitly says unknown and gives a reason.
   - Write as `Unknown - <reason>`.
   - Do not auto-fill Unknown for missing fields.
   - If a required field is `Unknown`, include it in "Next-check-in follow-up".
5) Redact sensitive medical info:
   - meds/doses -> [medication redacted]
   - diagnoses/conditions -> [health detail redacted]
   - lab/vitals -> [health metric redacted]
6) Keep wording concise and behavioral.

Required fields by part:
- Morning:
  - wake window hit, sleep quality, morning energy
  - caffeine cutoff, last meal cutoff, wind-down start
  - nutrition anchors, training plan, training fallback
  - biggest risk, if-then response, one non-negotiable
- Midday:
  - energy, stress
  - sleep guardrails on track, nutrition anchors on track, training status
  - one sleep adjustment, one nutrition adjustment, one training/recovery adjustment
  - accountability action with timing
- Evening:
  - sleep score (0-4), nutrition score (0-3), training score (0-3), total score (0-10)
  - what happened (2-3 bullets), what worked (>=1 bullet), friction (>=1 bullet), one change for tomorrow

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

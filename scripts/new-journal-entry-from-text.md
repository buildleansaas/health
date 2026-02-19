# Prompt Spec: New Journal Entry From Raw Text

Paste this into Codex and replace placeholders.

```text
You are formatting a daily journal entry for this repo.

Inputs:
- Date (local): {{YYYY-MM-DD}}
- Timezone: {{IANA timezone}}
- Raw Discord answers:
{{PASTE_RAW_TEXT}}

Rules:
1) Output must match templates/daily-recap.md section structure exactly.
2) Fill unknown fields with blank values; do not invent facts.
3) If critical fields are missing, ask follow-up questions first:
   - Missing scorecard items
   - Missing "What happened" bullets (<3)
   - Missing "What worked"
   - Missing friction
   - Missing one change for tonight
4) Redact sensitive medical info:
   - meds/doses -> [medication redacted]
   - diagnoses/conditions -> [health detail redacted]
   - lab/vitals -> [health metric redacted]
5) Keep wording concise and behavioral.

Output format:
- First: "Follow-up questions" section (only if needed).
- Then: "Journal markdown" section with final file content for journals/{{YYYY-MM-DD}}.md.
```

## Rubric (Self-Check Before Final Output)
- Completeness (0-5): all required sections filled.
- Fidelity (0-5): no invented facts; raw answers preserved.
- Actionability (0-5): one concrete change for tonight.
- Safety (0-5): sensitive medical info redacted.
- Format (0-5): template structure and filename date are correct.

Minimum acceptable total: 21/25.

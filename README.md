# health

Schema-first health data repo for:
- affirmations
- HIIT routines
- workout + affirmation logs

## Quickstart

```bash
./scripts/validate.py
```

Validation checks all JSON/JSONL examples against `schemas/*.schema.json`.

## Intents

- Keep data portable and machine-readable.
- Keep structures minimal but explicit.
- Log events with timezone-aware timestamps.
- Support phrase-based routine lookup (see `docs/phrase-mapping.md`).

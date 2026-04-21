# health

Schema-first health system for:
- morning affirmations
- HIIT routine definitions
- workout and affirmation logs

## Repo structure
- `schemas/` JSON Schemas for database objects
- `data/exercises.json` exercise catalog (with source videos + confidence)
- `data/affirmations.json` affirmation array
- `data/routines/` ready HIIT routines
- `logs/*.example.jsonl` hit/miss + workout log examples
- `docs/phrase-mapping.md` natural phrase -> routine file

## Quickstart

```bash
cd /root/.openclaw/workspace/repos/health
./scripts/validate.py
```

Expected output:

```text
VALIDATION PASSED
```

## HIIT protocol standard
Both packaged routines use your preferred template:
- 8 exercises
- 40s on / 20s off
- 1 round = 8:00
- 2:00 rest between rounds
- default 2 rounds (scale 1-3)

## Research notes
The no-equipment catalog is grounded in Chris Heria bodyweight/calisthenics videos.
Single-kettlebell entries are marked as transfer adaptations from Chris Heria dumbbell-only videos when direct kettlebell-specific uploads were not available in the crawl.

# Telegram HIIT Mini App Blueprint (Topics-Compatible)

## Goal
Run HIIT sessions inside Telegram with:
- routine selection from topic messages ("hiit with no equipment", "hiit with kettlebells")
- Start / Pause / Resume / Skip / Complete controls
- live 40s/20s interval countdown
- session completion post back into the same topic

## Feasibility
Yes, this is possible in Telegram forum topics.

## How it works
1. User sends phrase in topic.
2. Bot detects phrase and replies in the same `message_thread_id` with inline button: **Open HIIT App**.
3. Button launches Telegram Mini App (Web App URL).
4. Mini App runs the timer and controls in-app.
5. On completion, backend logs session + bot posts summary back to same topic.

## Core components
- Telegram Bot (BotFather token)
- Mini App frontend (React/Vite or Next.js)
- Backend API (FastAPI/Node)
- DB (local Postgres on VPS) for exercises, routines, logs

## Topic support details
- Use Bot API `message_thread_id` for forum topics.
- Keep topic id `6228` available in routing payloads.
- Send completion/status messages to the same thread.

## Data mapping
- no equipment routine: `data/routines/no_equipment_full_body_hiit.json`
- kettlebell routine: `data/routines/single_kettlebell_full_body_hiit.json`
- logs: `schemas/workout_log.schema.json`, `schemas/affirmation_log.schema.json`

## MVP feature set
- Phrase trigger parser
- Two routine presets
- Launch screen pickers:
  - exercises per round (6, 8, or 10)
  - number of rounds (1, 2, or 3)
- Session timer engine (40/20, 2:00 between rounds)
- Buttons: Start, Pause, Resume, Next, End
- Completion summary + save log

## Constraints
- Timer runs while Mini App is open. If user fully closes app, timer state must be restored from backend/local storage on reopen.
- Needs HTTPS-hosted Web App URL and valid bot token.

## Fastest launch plan
1. Create dedicated bot via BotFather.
2. Host Mini App frontend + backend on one domain.
3. Connect phrase parser to existing routine JSON files in this repo.
4. Enable posting back into topic `6228`.
5. Test with: "hiit with no equipment" and "hiit with kettlebells".

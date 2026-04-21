# Chris Heria YouTube Exercise Research (No-Equipment + Single-Kettlebell)

## Scope and method
- Target: YouTube content for **Chris Heria** (primary channel `@CHRISHERIA`).
- Collected channel video metadata by parsing YouTube channel pages + continuation API responses.
- Total videos captured from `@CHRISHERIA`: **383** (historical coverage from accessible video grid/continuations).
- For deeper extraction, enriched a sample of workout-relevant videos (watch-page metadata, descriptions, caption/transcript availability checks).

## Coverage achieved
- Channel-level metadata coverage: **383/383 videos discovered in crawl**.
- Transcript/caption coverage for sampled workout videos: **very limited** (most sampled videos had no accessible caption tracks via watch-page payload; transcript API returned none).
- Result: high confidence for exercises explicitly named in video titles; lower confidence where movement-level detail would require captions.

## Key finding (important)
I found **no clearly kettlebell-titled uploads on Chris Heria’s `@CHRISHERIA` channel** in the collected 383-video corpus.

So for single-kettlebell, I built a **transfer set** from Chris Heria dumbbell-only uploads (same movement patterns, adapted to one kettlebell). These are marked medium confidence and explicitly tagged as inferred transfer, not direct kettlebell-title evidence.

## Source set used (title + URL)
### No-equipment direct exercise evidence
- How To Do The Perfect Push Up  
  https://www.youtube.com/watch?v=rruHM_sB2Hc
- Get a BIGGER CHEST With JUST Push Ups  
  https://www.youtube.com/watch?v=zPp-VAi_a24
- What 100 One-Arm Push-Ups A Day Does To Your Body  
  https://www.youtube.com/watch?v=BvZw1tyna-M
- How To Do The Perfect Pull Up  
  https://www.youtube.com/watch?v=iBtL9nX2qOs
- Pull-Ups LVL 1-10 (How To Progress Faster)  
  https://www.youtube.com/watch?v=hByjG7mymdw
- HOW TO MUSCLE UP WITH 3 EASY EXERCISES  
  https://www.youtube.com/watch?v=KGGWP695Zx4
- How To MUSCLE UP In 5 Min FT. Twan  
  https://www.youtube.com/watch?v=QIaWg5nBWE4
- 5 BEST EXERCISES FOR THE DIP BAR  
  https://www.youtube.com/watch?v=1cvGnmDYoXk
- HOW TO HANDSTAND KICK UP  
  https://www.youtube.com/watch?v=XnsM3TLjubY
- HOW TO TUCK PLANCHE  
  https://www.youtube.com/watch?v=M5il8Jpltt8
- How To Full Planche Pushup | 5 Steps  
  https://www.youtube.com/watch?v=LSWwofk03_8
- Do This Plank Routine Every Day | Just 5 Min  
  https://www.youtube.com/watch?v=6ONgwzcQIvQ
- Burpees LVL 1-10 (How To Progress Faster)  
  https://www.youtube.com/watch?v=1IhPhkoBc_M
- Why You Can’t L-Sit Hold (How To Step By Step)  
  https://www.youtube.com/watch?v=Qv6j5gZyBQ8
- How To Front Lever Step By Step  
  https://www.youtube.com/watch?v=5g8-sj-8snc
- How To Human Flag The Easiest Way  
  https://www.youtube.com/watch?v=TF9XhvYh_m8

### Single-kettlebell transfer evidence base (Chris dumbbell uploads)
- Best Dumbbell Exercises You Can Do From Home  
  https://www.youtube.com/watch?v=LBBnoBJeUEY
- Perfect Full Body Home Workout For Beginners (DUMBBELLS ONLY)  
  https://www.youtube.com/watch?v=B0HaGjZW5Cc
- Complete 15 Min Chest & Tricep Workout | Dumbbells Only  
  https://www.youtube.com/watch?v=ceiIEk9CKkg
- BEST BACK & BICEPS WORKOUT FROM HOME | DUMBBELLS ONLY  
  https://www.youtube.com/watch?v=wMgYD0ALT4g
- BEST HOME Leg Workout | Dumbbells Only  
  https://www.youtube.com/watch?v=c8Hlyu71KcE

## Recommended sets

### A) No-equipment 8-exercise set (high confidence)
1. Push-Up  
2. Pull-Up  
3. Dip (parallel bar)  
4. Muscle-Up  
5. Handstand (hold/wall progression)  
6. Plank  
7. Burpee  
8. L-Sit Hold

### B) Single-kettlebell 8-exercise set (medium confidence, inferred transfer)
1. Single-Kettlebell Goblet Squat  
2. Single-Kettlebell Reverse Lunge  
3. Single-Arm Kettlebell Row  
4. Single-Arm Kettlebell Floor Press  
5. Single-Arm Kettlebell Overhead Press  
6. Single-Kettlebell Romanian Deadlift  
7. Single-Kettlebell Thruster  
8. Single-Kettlebell Suitcase Carry

## Caveats
- This is YouTube-surface evidence, not app-exclusive content.
- Movement-level extraction is constrained by missing captions/transcripts on many videos.
- Single-kettlebell set is intentionally labeled inferred because direct kettlebell-titled Chris Heria uploads were not found in this crawl.

## Output files
- Normalized exercise objects with classification and citations:  
  `/root/.openclaw/workspace/tmp/chris-heria-exercises.json`

## Verification (how data was gathered)
- Crawled `@CHRISHERIA/videos` HTML and parsed `ytInitialData`.
- Followed YouTube continuation browse payloads to extend coverage.
- Parsed video titles/URLs and checked watch-page metadata for sampled videos.
- Attempted transcript/caption retrieval on sampled workout videos; retained only evidence-supported exercise claims.

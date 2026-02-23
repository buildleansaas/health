# Coaching 2-Touch Rework Plan

Date: 2026-02-22
Owner: Pepper coaching system
Scope: Planning-only migration from 4 daily check-ins to 2 daily touches

## 1) Current-state diagnosis (what enforces 4x/day today)

The current 4-touch cadence is enforced in multiple layers:

- `profiles/austin-preferences.yaml`
  - `cadence.checkins_per_day: 4`
  - Four fixed windows: `morning`, `midday`, `afternoon`, `evening`.
- `docs/COACHING_CRON_SYSTEM.md`
  - Defines full mode as morning + midday + afternoon + evening.
  - Defines SLA/reminder/recovery behavior for four windows.
  - Writes four day-part files.
- `docs/DISCORD_JOURNAL_WORKFLOW.md`
  - Goal and workflow explicitly run four check-ins.
  - Commit conventions and minimum execution standard require four day-parts.
- `docs/COACHING_INTEGRATION_PLAN.md`
  - Daily check-ins section and cadence section are four-part.
- `docs/SYSTEM_SOURCE_OF_TRUTH.md`
  - Workflow boundary states active execution is four daily day-parts.
- `scripts/new-journal-entry-from-text.md`
  - Check-in part enum is `morning|midday|afternoon|evening`.
  - Template mapping and required fields are part-specific across four touches.
- Templates and question guides (`templates/*checkin*.md`, `templates/*-questions.md`)
  - Separate files exist for morning, midday, afternoon, evening.
- `journals/README.md` and `README.md`
  - Document day-part outputs and active template set.

Important constraint already respected today:

- Scoring model is already canonical and stable: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.

## 2) Target-state design (new 2-touch architecture)

### Canonical daily flow

- Touch 1: `Daytime` (new canonical day-part)
  - Goal: collect key status + unresolved prior-night carryover + current constraints.
  - Output: a concrete, time-bound remainder-of-day execution plan.
  - Journal file: `journals/YYYY-MM-DD-daytime.md`.
- Touch 2: `Night` (implemented as `evening` file for continuity)
  - Goal: execution recap, score computation, journal reflection, tomorrow preview, one before-bed goal.
  - Journal file: `journals/YYYY-MM-DD-evening.md`.

### Required behavior in each touch

- Daytime touch must:
  - Ask `3-6` context-aware prompts.
  - Include prior-night carryover only when needed (night missed, unresolved unknowns, or open follow-ups).
  - Capture status needed to steer the rest of the day.
  - Produce a specific remainder-of-day plan with clear times/sequence.
- Night touch must:
  - Ask `3-6` context-aware prompts.
  - Recap execution against daytime plan.
  - Compute score using unchanged formula.
  - Record reflection + tomorrow preview.
  - Set one explicit before-bed goal.

### Backward compatibility strategy

- Keep all historical files untouched (`morning`, `midday`, `afternoon`, `evening`, and legacy single-file entries).
- Parser and context loader must accept both:
  - New canonical parts: `daytime`, `evening`.
  - Legacy parts: `morning`, `midday`, `afternoon`.
- Weekly and trend logic should treat legacy day-parts as valid historical context without migration rewrite.

## 3) File-by-file change plan (exact files + exact modifications)

| File | Exact modifications |
| --- | --- |
| `docs/COACHING_CRON_SYSTEM.md` | Replace four-touch mode definitions with two-touch mode (`Daytime`, `Night`). Replace check-in windows and recovery rules to two-touch logic. Update required fields matrix to `Daytime` and `Evening/Night`. Update "What Pepper does" output files to `-daytime.md` and `-evening.md`. Keep scoring section unchanged. |
| `docs/CONTEXT_AWARE_CHECKINS.md` | Update input file list to include new `-daytime.md` as canonical plus legacy files for history. Replace required captures by part from morning/midday/afternoon/evening to daytime/evening. Add explicit prior-night carryover queue behavior. Update follow-up carry rules between two touches. |
| `docs/DISCORD_JOURNAL_WORKFLOW.md` | Rewrite goal and end-to-end flow around two touches. Replace journal file list with canonical `daytime` + `evening` (and mention legacy compatibility). Update source template list to include new daytime templates and mark midday/afternoon as legacy. Replace commit message conventions with daytime + evening commits. Update minimum execution standard to two required touches/day. |
| `docs/COACHING_INTEGRATION_PLAN.md` | Replace four daily check-in blocks with two blocks. Daytime block should include status capture + remainder-of-day execution plan. Evening block should include execution recap + score + tomorrow preview + before-bed goal. Update cadence and missed-touch recovery references. |
| `docs/SYSTEM_SOURCE_OF_TRUTH.md` | Update canonical active templates and question sets to daytime/evening. Update workflow boundary from four day-parts to two touches/day. Add one compatibility note that legacy day-parts remain supported for historical parsing. |
| `scripts/new-journal-entry-from-text.md` | Expand/adjust check-in enum and mapping rules: canonical `daytime|evening`, legacy aliases `morning|midday|afternoon` for historical/backfill parsing. Add mapping for `daytime -> templates/daytime-checkin.md`. Update required-field matrix to daytime/evening. Add evening requirement for `before-bed goal`. Keep scoring formula and computation unchanged. |
| `templates/daytime-checkin.md` (new) | Create new journal template with sections for (1) carryover, (2) current status snapshot, (3) schedule constraints, (4) remainder-of-day execution plan, (5) top risk + fallback, (6) Pepper coach response/actions. |
| `templates/daytime-checkin-questions.md` (new) | Create internal prompt guide defining `3-6` daytime prompts, priority order, carryover conditions, and required captures before writing journal. |
| `templates/evening-recap.md` | Keep score sections intact. Add explicit fields: execution recap vs daytime plan, tomorrow preview, one before-bed goal (with timing). Keep existing reflection and modifier checks. |
| `templates/evening-recap-questions.md` | Add prompt requirements to cover daytime-plan execution recap, tomorrow preview, and before-bed goal. Keep scoring capture requirements unchanged. |
| `templates/morning-checkin.md` | Convert to legacy/deprecated template status. Add header note: retained for historical compatibility only; not used in active schedule. |
| `templates/midday-checkin.md` | Convert to legacy/deprecated template status; retained only for historical/backfill use. |
| `templates/afternoon-checkin.md` | Convert to legacy/deprecated template status; retained only for historical/backfill use. |
| `templates/morning-checkin-questions.md` | Convert to legacy/deprecated guide and point to `templates/daytime-checkin-questions.md`. |
| `templates/midday-checkin-questions.md` | Convert to legacy/deprecated guide and point to `templates/daytime-checkin-questions.md`. |
| `templates/afternoon-checkin-questions.md` | Convert to legacy/deprecated guide and point to `templates/daytime-checkin-questions.md`. |
| `templates/daily-recap-questions.md` | Update deprecation pointer to new active question files (`daytime-checkin-questions.md`, `evening-recap-questions.md`). |
| `profiles/austin-preferences.yaml` | Change cadence to `checkins_per_day: 2`. Replace windows with `daytime` and `evening` keys (or `night` alias + `evening` canonical), including exact trigger times. |
| `journals/README.md` | Update canonical daily output list to `-daytime.md` and `-evening.md`. Update template references to daytime/evening templates. Add compatibility note for legacy day-part history. |
| `README.md` | Update active templates and journal outputs to daytime/evening architecture. Add one-line note that legacy 4-touch files remain valid history. |

## 4) Cron schedule changes

Timezone remains `America/New_York`.

Proposed schedule:

- Daytime touch
  - Initial prompt: `11:30`
  - Window: `10:30-14:30`
  - Reminders: `+30m`, `+90m`
  - Missed threshold: window end `+2h`
- Night touch
  - Initial prompt: `20:30`
  - Window: `19:30-22:30` (or 60-120 minutes pre-bed if bed timing differs)
  - Reminders: `+30m`, `+90m`
  - Missed threshold: window end `+2h`

Recovery behavior (2-touch):

- If daytime missed: night touch starts with a short catch-up block before recap/scoring.
- If night missed: next daytime touch begins with prior-night carryover and immediate today plan.
- If both touches missed in one day: next daytime sends restart prompt + one easy action.

## 5) Prompt/template changes

Daytime prompt strategy:

- Keep `3-6` questions.
- Ask only high-leverage items for same-day execution:
  - readiness/energy/stress snapshot,
  - hydration + nutrition status,
  - training intent + fallback rung,
  - key schedule constraints,
  - risk check,
  - one biggest friction.
- Always end with Pepper-generated remainder-of-day plan:
  - explicit sequence,
  - target times,
  - fallback if schedule collapses.

Night prompt strategy:

- Keep `3-6` questions.
- Ask for:
  - execution recap against daytime plan,
  - sleep/nutrition/training scores,
  - modifier outcomes,
  - reflection,
  - tomorrow preview,
  - one before-bed goal.
- Pepper response must include:
  - score rationale,
  - concise read,
  - tomorrow top actions,
  - before-bed lock-in action.

## 6) Journal schema changes (if needed)

Schema change is needed for new canonical daytime file.

New canonical daily files:

- `journals/YYYY-MM-DD-daytime.md` (new)
- `journals/YYYY-MM-DD-evening.md` (existing, updated fields)

Data compatibility approach:

- Do not rewrite old files.
- Context loader reads all available day-parts in this order:
  - for current day: `daytime`, `evening`, then legacy `morning`, `midday`, `afternoon` if present,
  - for prior day: `evening`, `daytime`, then legacy parts.
- Legacy files remain first-class historical evidence for coaching trends.

## 7) Parser and scoring logic impact

Parser impact:

- Update part recognition to support new canonical parts and legacy aliases.
- Update required-field validation rules to two-touch schema.
- Preserve `Unknown - <reason>` behavior exactly.
- Carry unresolved required fields from night to next daytime and daytime to same-night follow-up.

Scoring impact:

- No formula changes.
- Keep exact model: `total 0-10 = sleep 0-4 + nutrition 0-3 + training 0-3`.
- Score computation remains in night touch only.
- Any daytime estimates are advisory only and never persisted as final scores.

## 8) Migration steps in order, with rollback plan

Migration steps:

1. Add new daytime templates (`templates/daytime-checkin.md`, `templates/daytime-checkin-questions.md`).
2. Update evening template/question guide for execution recap + before-bed goal.
3. Update parser spec (`scripts/new-journal-entry-from-text.md`) for new part mapping and required fields.
4. Update cadence/config in `profiles/austin-preferences.yaml` to 2-touch windows.
5. Update source-of-truth and workflow docs (`docs/*.md`, `README.md`, `journals/README.md`).
6. Run dry-run simulations with raw text for:
   - normal day (both touches),
   - missed daytime,
   - missed night,
   - legacy backfill parse using `morning`/`midday`/`afternoon` input.
7. Cut over on a single explicit date (recommended: next local day boundary).
8. Monitor first 7 days for adherence and prompt quality drift.

Rollback plan:

1. Revert to pre-cutover commit.
2. Reset `profiles/austin-preferences.yaml` cadence to 4 windows.
3. Restore four-touch template routing in parser spec.
4. Resume morning/midday/afternoon/evening prompts immediately.
5. Keep any generated `-daytime.md` files as historical artifacts (do not delete).

## 9) Acceptance criteria + test checklist

Acceptance criteria:

- Exactly two daily prompts are scheduled by default.
- Daytime touch produces a specific remainder-of-day plan.
- Night touch computes unchanged scores and writes recap.
- Night touch always captures tomorrow preview + one before-bed goal.
- Historical journal files remain readable and usable for context.
- `Unknown` follow-up behavior still works.
- No scoring changes from existing model.

Test checklist:

- [ ] Config test: `profiles/austin-preferences.yaml` reflects 2-touch cadence.
- [ ] Prompt generation test: daytime output stays within `3-6` targeted questions.
- [ ] Prompt generation test: night output stays within `3-6` targeted questions.
- [ ] Journal write test: creates `journals/YYYY-MM-DD-daytime.md` and `journals/YYYY-MM-DD-evening.md`.
- [ ] Parser test: accepts `daytime` and `evening` parts.
- [ ] Parser compatibility test: accepts legacy `morning|midday|afternoon` parts.
- [ ] Scoring test: score totals still match `sleep + nutrition + training` exactly.
- [ ] Recovery test: missed daytime triggers catch-up at night.
- [ ] Recovery test: missed night triggers prior-night carryover in next daytime.
- [ ] Unknown test: `Unknown - reason` carried to next touch follow-up queue.

## 10) Outcome preview: daily user experience

Example day (America/New_York):

- 11:30 Daytime touch arrives with concise context-aware questions.
- User replies once.
- Pepper returns a practical remainder-of-day execution plan with timing (nutrition, hydration, training, reset, connection, and fallback path), adjusted from prior-night baseline when needed.
- 20:30 Night touch arrives.
- User gives execution recap.
- Pepper computes and explains score, then returns two explicit outputs:
  - Output 1: tomorrow preview (top actions).
  - Output 2: full tomorrow execution plan tailored to tomorrow schedule constraints (morning/daytime/evening blocks + fallback).
- Next-day daytime touch starts from that prior-night plan baseline and adjusts only what changed in reality.

Result: fewer interruptions, same scoring rigor, and a tighter night-to-next-day execution loop.

## 11) Open questions/assumptions to confirm

- Should canonical naming be `daytime + evening` (file stability) or `daytime + night` (language alignment)?
- Confirm exact default trigger times (`11:30` and `20:30` proposed).
- Should daytime touch still be required on weekends/atypical schedules?
- If daytime is missed, should night still compute final score when some daytime required fields are unknown?
- Should legacy morning/midday/afternoon templates be retained indefinitely or sunset after a date?
- Should before-bed goal completion be checked first in next-day daytime touch by default?

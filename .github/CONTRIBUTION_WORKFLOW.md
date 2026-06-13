# Contribution review workflow

How a community suggestion becomes a pin on the map. Two paths — one fully
automatic and free, one for the cases that need judgment.

```
                       ┌─ entity-add issue (anyone) ──────────────────────────┐
                       │   auto-entity.yml — deterministic Python, NO LLM      │
                       │   parse form · geocode (OSM) · validate · open PR     │  ← free, $0 tokens, runs on its own
                       └──────────────────────────────────────────────────────┘
                       ┌─ entity-fix issue, or you comment @claude / label ────┐
                       │   claude-triage.yml — Claude (your Max plan)          │
                       │   reads · validates · opens PR with Review summary    │  ← only you/collaborators trigger it
                       └──────────────────────────────────────────────────────┘
                                              │
                                  You review the PR → merge / close
```

## The two paths

### 1. `auto-entity.yml` — automatic, free, safe (handles `entity-add`)
Any `entity-add` issue (the template applies that label) is processed with **no
language model**: a Python script parses the form, geocodes the city
(OpenStreetMap / a built-in table), builds the entity, runs the schema
validator, and **opens a data-only PR** — or comments on the issue saying
exactly what's missing (no source, bad country, etc.).

- **$0 tokens.** No model runs. Spam can't burn your plan.
- **No prompt-injection surface.** The issue text is only ever treated as data,
  never as instructions, never passed through a shell — so it's safe to run on
  issues from people without repo access.
- Descriptions are taken **verbatim** from the issue (not rewritten). You polish
  on review if you want.
- Escape hatch: add the `no-auto` label to a specific issue to skip this and
  hand it to Claude instead.

### 2. `claude-triage.yml` — Claude, for judgment (handles `entity-fix` and anything you flag)
Runs **only when you/a collaborator** comment `@claude` or add the
`ready-for-claude` label (the action ignores non-write users by default — that's
the safety gate). Use it for:
- `entity-fix` issues (free-text "what's wrong" needs judgment),
- any `add` you'd like Claude to dedupe/verify/polish instead of the auto path.

Auth is your **Claude Pro/Max subscription** (OAuth token, no API billing). It's
tuned to be cheap (~$0.15/issue: greps instead of full-file reads, schema inline
in CLAUDE.md, capped turns).

## Safety boundary (applies to both)
The existing **`validate.yml`** + the deterministic script both enforce
**data-only, schema-valid** changes. Nothing reaches the map without **your
merge**. Code/workflow changes are authored by the maintainer directly.

## One-time setup (maintainer)
1. **Claude GitHub App** installed: <https://github.com/apps/claude> — *(done if Claude path already works)*.
2. Secret **`CLAUDE_CODE_OAUTH_TOKEN`** from `claude setup-token` — *(done)*.
3. *(optional)* connect the repo to **Vercel** → a map **preview on every PR** so you eyeball the new pin before merging.

## Day-to-day
- An `add` suggestion arrives → a PR appears on its own (or a comment asking for the missing bit). You merge/close.
- A `fix` suggestion (or a tricky `add`) → skim it, comment `@claude`, review the PR it opens, merge/close.
- Junk → just close it. The auto path only ever produces a PR for a schema-valid, sourced entry.

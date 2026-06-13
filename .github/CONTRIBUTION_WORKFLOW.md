# Contribution review workflow

How a community suggestion becomes a pin on the map, with a fast maintainer gate.

```
Issue (add / fix template)
        │   maintainer vets it →  comment @claude   OR   add label `ready-for-claude`
        ▼
Claude drafts a DATA-ONLY pull request
        │   validate.yml runs automatically (data-only guard · schema · diff summary)
        ▼
You review the PR  →  merge (approve)  /  close (reject)
        │
        ▼
Sync data/ into the website (qutsur.com/LATAM-quantum-map)
```

## What each piece does

- **Issue templates** (`add-entity.yml`, `fix-entity.yml`) collect structured, sourced input.
- **`claude-triage.yml`** runs Anthropic's `claude-code-action` when you gate an issue
  (`@claude` comment or the `ready-for-claude` label — both restricted to users with write
  access). Claude reads the issue, validates against the schema, edits `data/*.json`, runs
  `scripts/validate_data.py`, and opens a PR whose body starts with a one-glance **Review** block.
- **`validate.yml`** (already in the repo) is the real safety boundary: it fails any PR that
  touches non-data files or breaks the schema, and prints an entity diff summary.
- **`CLAUDE.md`** carries the standing rules (data-only, no invention, dedupe, schema pointer).

## One-time setup (maintainer)

Auth uses the maintainer's **Claude Pro/Max subscription** (no per-token API billing).

1. **Install the Claude GitHub App** on this repo: <https://github.com/apps/claude>
   (or run `claude /install-github-app`).
2. **Generate a subscription token**: run `claude setup-token` locally (requires an active
   Pro/Max plan), then add it as the secret **`CLAUDE_CODE_OAUTH_TOKEN`** in
   Settings → Secrets and variables → Actions. The token is long-lived; refresh it if it expires.
3. **Create the label** `ready-for-claude` (any colour). Optional — `@claude` comments work without it.
4. *(Optional, for a visual review)* connect this repo to **Vercel** as its own static project.
   Vercel then posts a **preview URL on every PR** that renders the map with the proposed pin,
   so you can eyeball it before merging. The repo is plain static (`index.html` + `data/`), so no
   config is needed — just import the repo in Vercel once.

## Day-to-day

- A suggestion arrives as an issue. Skim it.
- Worth it? Comment `@claude` (or add `ready-for-claude`). Claude opens a PR in ~a minute.
- Read the **Review** block at the top of the PR (and the Vercel preview pin, if enabled).
- **Merge** to accept, **close** to reject. That's the whole loop.

Junk or off-topic issues: just close them — Claude never runs unless you gate them.

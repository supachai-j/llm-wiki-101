---
id: concept:lint
type: concept
title: Lint operation
status: active
confidence: 0.9
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# Lint

## Summary

**Lint** = the periodic health check. Identifies contradictions, stale claims, orphaned pages, missing cross-references, and gaps. The wiki's "garbage collector" — without it, the artifact silently rots.

## Claims

- "Periodic health checks identify contradictions, stale claims, orphaned pages, missing cross-references, and data gaps requiring investigation." `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Lint is **invoked deliberately** (manually or scheduled), not on every ingest. Too frequent = noise; too rare = drift compounds. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`

## What lint checks

### Orphans
Pages with no inbound wikilinks and not in `index.md`. Either link them or mark `status: orphan`.

### Broken wikilinks
`[[entity-id]]` targets that don't exist. Repair or remove.

### Contradictions
Two claims on the same subject with opposite content. Propose supersession: more recent / more authoritative source wins; older claim stays in the file marked `status: stale`.

### Stale claims (decay)
Apply confidence decay: `conf_now = conf_last * exp(-Δdays / half_life)`. If `conf_now < 0.2` and untouched for 2× half-life, mark `status: faded`. **Never delete** — the audit trail matters more than tidiness.

### Consolidation candidates
Observations from `raw/` that have been confirmed ≥3 times across independent sources should be promoted from episodic to semantic memory — written into a proper wiki page if not already.

### Quality scoring
Per-page rate (0-1) based on: cites sources? Consistent? Well-structured? Below 0.5 → flag for rewrite.

## Output

A dated audit artefact: `raw/lint-YYYY-MM-DD.md` listing what was found, what was resolved, what was escalated to the human.

## When to lint

| Trigger | Recommended cadence |
|---|---|
| Every N new sources | every 10 ingests |
| Calendar-based | weekly or monthly |
| User-requested | "run lint" any time |
| Pre-publish | before sharing the wiki externally |

## Anti-patterns

- ❌ **Silent deletion** — supersession over deletion, always
- ❌ **Hiding contradictions** — surface them for human resolution
- ❌ **Auto-faded everything stale** — apply decay; don't delete

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- mitigates → [[risk:claim-drift]] `{conf: 0.9}`
- mitigates → [[risk:orphan-pages]] `{conf: 0.95}`

## Changelog

- 2026-05-09 — created

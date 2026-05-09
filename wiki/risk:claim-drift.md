---
id: risk:claim-drift
type: risk
title: Claim drift — when wiki claims diverge from sources
status: active
confidence: 0.9
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
  - raw/2026-05-09-anthropic-context-engineering.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Claim drift

## Summary

**Claim drift** = the wiki gradually saying things its raw sources no longer support. Happens when the LLM rewrites pages without re-reading raw, when sources update upstream, or when pages get reinforced by other pages instead of fresh sources. The number-one failure mode of an unmaintained LLM Wiki.

## Claims

- Lewis et al. flagged "updating their world knowledge" as an unsolved problem in retrieval-augmented systems. `[src: raw/2026-05-09-lewis-rag-paper.md] {conf: 0.85}`
- Anthropic's context-engineering article warns about "context rot" — accumulated state degrades over time without active maintenance. `[src: raw/2026-05-09-anthropic-context-engineering.md] {conf: 0.85}`
- Karpathy's gist names the lint operation specifically as the mitigation: identifies "stale claims" and "data gaps". `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`

## How drift happens

### 1. Re-write without re-read
The LLM updates a page based on its own priors instead of the raw source it cites. Page says "X is Y" but the cited raw source actually says "X is Z" — the citation is fake.

### 2. Source updates upstream
A blog post we ingested gets edited. Our raw file is dated 2024-12-01 and accurately reflects what the source said *then*; the page citing it now contradicts what the source says *now*.

### 3. Cascading reinforcement
Page A cites Page B which cites Page C. Page C originally cited a raw source. Six months later, Page A is being maintained by reinforcement from B (not C, not raw). The trail back to raw evidence has thinned.

### 4. Schema evolution
SCHEMA §2 added a new entity type. Old pages don't conform. Lint flags them; nobody migrates them.

## Mitigations

| Mechanism | What it does |
|---|---|
| **Citation discipline** | Every claim points to a specific raw file — drift becomes detectable |
| **Confidence + decay** | Untouched claims gradually mark themselves `faded` |
| **Lint operation** | Surfaces contradictions, orphans, stale claims |
| **Re-ingest cadence** | Periodically re-read sources that change upstream (mark `re-verified-on`) |
| **Provenance audit** | For each claim on a hot page, verify the cited raw still says it |

## Severity

Drift is rarely catastrophic on day 1. It compounds. After 6 months without lint, a wiki of 50 pages can have 10-20% of claims that no longer match their sources. The artifact still *looks* fine — until someone checks.

## Detection

```bash
# Quick provenance audit (manual)
for page in wiki/*.md; do
  for src in $(grep -oE 'raw/[^]]+' "$page"); do
    [ -f "$src" ] || echo "BROKEN CITATION: $page → $src"
  done
done
```

For deeper drift (citation exists but content moved), spot-check 5 random claims monthly. If 1+ fails verification, full lint sweep is overdue.

## Relationships

- mitigated-by ← [[concept:lint]] `{conf: 0.95}`
- mitigated-by ← [[pattern:citation-discipline]] `{conf: 0.9}`

## Changelog

- 2026-05-09 — created

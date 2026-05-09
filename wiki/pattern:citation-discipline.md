---
id: pattern:citation-discipline
type: pattern
title: Citation discipline — every claim cites a source
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
  - raw/2026-05-09-lewis-rag-paper.md
created: 2026-05-09
updated: 2026-05-09
tiers: procedural
half_life_days: 180
tags: [deck]
---

# Citation discipline

## Summary

The single rule that prevents an LLM-maintained wiki from devolving into hallucination: **every claim cites at least one raw source, with a confidence number**. No floating assertions. If you can't cite it, it doesn't enter the wiki.

## Claims

- Every claim has an inline source marker `[src: raw/...]` and a confidence number. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.9}`
- Lewis et al. flagged "providing provenance" as an open problem in RAG — citation discipline is how LLM Wiki addresses it. `[src: raw/2026-05-09-lewis-rag-paper.md] {conf: 0.85}`

## The format

```markdown
- <Claim statement.> `[src: raw/2026-05-08-source.md] {conf: 0.5}`
- <Claim from multiple sources.> `[src: raw/A.md, raw/B.md] {conf: 0.8}`
```

Each component:
- **Inline marker `[src: ...]`** — points to specific raw file(s)
- **`{conf: 0.5}`** — page-level rollup; first observation = 0.5
- **Multiple sources** = comma-separated → higher initial confidence

## Confidence math

```
First observation:               conf = 0.5
Reinforcement (independent src): conf = 1 - (1 - conf) * 0.6
                                 (asymptotes toward 1.0)
Contradiction:                   open supersession candidate
                                 (don't lower silently)
```

After 1 reinforcement: 0.5 → 0.8
After 2: 0.8 → 0.92
After 3: 0.92 → 0.968

## Why this works

The discipline does three things at once:

1. **Forces grounding** — LLM can't pad pages with priors; every line traces to text in `raw/`
2. **Enables decay** — claims with low confidence and old timestamps mark themselves stale
3. **Reveals contradictions** — when source B contradicts source A, both citations stay; supersession becomes explicit

## Anti-patterns

- ❌ **Inline citation without raw file** — "[src: official docs]" is meaningless. Must point to `raw/<filename>.md`.
- ❌ **One mega-citation at end of page** — defeats the per-claim audit. Cite per claim.
- ❌ **No confidence number** — without it, decay is impossible.
- ❌ **Synthesising claims that exceed sources** — if you can't trace it, don't write it. The LLM is a connector, not an author.

## Lint behaviour

`lint` checks:
- Every claim has `[src:]` marker
- Every cited file actually exists in `raw/`
- Confidence numbers parse and fall in [0, 1]
- No claim has been untouched longer than 2× half-life with `conf < 0.2` (→ mark `status: faded`)

## Relationships

- composes → [[concept:wiki-layer]] `{conf: 0.95}`
- mitigates → [[risk:hallucination]] `{conf: 0.95}`
- mitigates → [[risk:claim-drift]] `{conf: 0.9}`

## Changelog

- 2026-05-09 — created

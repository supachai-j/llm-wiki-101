---
id: concept:llm-wiki
type: concept
title: LLM Wiki — definition + scope
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
  - raw/2026-05-09-anthropic-context-engineering.md
created: 2026-05-09
updated: 2026-05-09
updated_log:
  - 2026-05-09: created
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# LLM Wiki

## Summary

An **LLM Wiki** is a design pattern for persistent, LLM-maintained knowledge bases. Three layers (raw / wiki / schema), three operations (ingest / query / lint), and a philosophy: knowledge **compounds** across sessions rather than being re-derived each query.

## Claims

- "The wiki is a persistent, compounding artifact" — Karpathy. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- The pattern has **three architectural layers**: immutable raw sources, LLM-generated wiki, schema document. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Three primary operations: **ingest, query, lint**. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Anthropic frames this as "structured note-taking" providing "persistent memory with minimal overhead". `[src: raw/2026-05-09-anthropic-context-engineering.md] {conf: 0.9}`
- Humans direct curation; LLMs handle bookkeeping (cross-references, consistency, updates). `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`

## Why "compounding"

Each ingest doesn't just add a new file — it potentially updates many existing wiki pages, strengthening cross-references and reconciling new evidence with old. The artifact gets denser and more interconnected over time. Compare to:

- **RAG** (stateless): every query re-derives context from raw chunks; nothing accumulates between sessions
- **LLM Wiki** (stateful): the wiki itself encodes accumulated synthesis

## Relationships

- composes → [[concept:raw-layer]] `{conf: 0.95}`
- composes → [[concept:wiki-layer]] `{conf: 0.95}`
- composes → [[concept:schema-layer]] `{conf: 0.95}`
- alternative-to → [[concept:rag]] `{conf: 0.85}`
- descends-from → [[principle:zettelkasten]] `{conf: 0.9}`

## Open questions

- [ ] At what scale does the wiki overhead exceed retrieval benefits?
- [ ] How does the pattern degrade when sources become massive (10k+)?

## Changelog

- 2026-05-09 — created from Karpathy gist + Anthropic context-engineering article

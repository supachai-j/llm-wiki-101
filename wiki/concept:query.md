---
id: concept:query
type: concept
title: Query operation
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

# Query

## Summary

**Query** = the operation that retrieves accumulated knowledge to answer a question. Unlike a RAG query (which always re-derives from chunks), a Wiki query first searches the synthesised pages, follows wikilinks, and *optionally files the result back* if it represents a new question worth remembering.

## Claims

- "Users ask questions; the LLM searches wiki pages, synthesizes answers with citations, and optionally files valuable findings back as new wiki pages." `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Queries should produce **citations to specific wiki pages** that contain the supporting claims. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.9}`
- A novel question + good answer is itself a candidate wiki page (`q-<slug>.md` or similar). `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`

## The query workflow

```
1. PARSE
   - Identify entities mentioned in the question

2. RETRIEVE
   - Grep wiki/ for matching entity IDs
   - Read those pages
   - Follow [[wikilinks]] one or two hops

3. SYNTHESISE
   - Compose answer from accumulated claims
   - Cite specific pages: "according to [[concept:llm-wiki]]..."

4. (OPTIONAL) FILE BACK
   - If the question is novel and reusable, save Q+A as wiki/q-<slug>.md
   - Future queries on similar questions can short-circuit
```

## When to file back vs not

| Situation | File back? |
|---|---|
| User asks "what is X?" — X already has a wiki page | ❌ no |
| User asks "how does X relate to Y?" — answer not yet on either page | ✅ yes |
| User asks ephemeral question ("what date is the meeting?") | ❌ no |
| User explores edge case worth preserving | ✅ yes |

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- depends-on → [[concept:wiki-layer]] `{conf: 0.95}`

## Changelog

- 2026-05-09 — created

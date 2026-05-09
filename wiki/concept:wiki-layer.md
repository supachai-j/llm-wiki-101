---
id: concept:wiki-layer
type: concept
title: Wiki layer — the synthesised pages
status: active
confidence: 0.9
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Wiki layer

## Summary

The **wiki layer** holds synthesised entity pages — one concept per file. Pages are written by the LLM (with human review), every claim cites a raw source, every relation links via wikilink. This is where the **understanding** lives.

## Claims

- The LLM-generated wiki is one of the three architectural layers. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Wiki pages are **synthesised**, not copied — they cite raw sources but are written for cross-reference. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.9}`
- Page granularity follows the Zettelkasten principle of atomicity (one concept per page). `[src: raw/2026-05-09-zettelkasten-wikipedia.md] {conf: 0.85}`

## Layout

```
wiki/
├── _TEMPLATE.md            # the standard page template
├── concept:llm-wiki.md
├── concept:rag.md
├── pattern:citation-discipline.md
├── pattern:page-template.md
├── principle:zettelkasten.md
├── risk:claim-drift.md
├── tool:obsidian.md
├── ...
```

Files are named `<entity-type>:<kebab-slug>.md`. The colon-separated naming makes the type visible at a glance.

## Page contents

Every page follows [[pattern:page-template]] — frontmatter, summary, claims with citations, relationships, changelog. See that page for the standard.

## Differences from a regular wiki

| Regular wiki (Wikipedia, Notion) | LLM Wiki layer |
|---|---|
| Free-form pages | Strict template per entity type |
| Manual cross-references | LLM follows + maintains links |
| Citation optional | Citation per-claim mandatory |
| One author edits at a time | LLM updates across pages atomically |
| Stable shape over years | Schema-driven shape, evolving deliberately |

## Differences from RAG retrieval

| RAG | Wiki layer |
|---|---|
| Chunks (200-1000 tokens) | Whole entity pages |
| Embedding-similarity retrieved | Wikilink-traversed (or grep) |
| No internal structure | Frontmatter + sections |
| One source per chunk | Multiple sources per claim |

## Anti-patterns

- ❌ **Pages without citations** — see [[pattern:citation-discipline]]
- ❌ **One mega-page per topic** — split per atomicity
- ❌ **Wikilinks to free-form names** ([[Things I Learned]]) — use entity IDs ([[concept:thing-x]])
- ❌ **Modifying pages without updating frontmatter `updated_log`** — breaks audit trail

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- composes → [[concept:three-layer-architecture]] `{conf: 0.95}`
- depends-on → [[concept:schema-layer]] `{conf: 0.95}`
- enables → [[concept:query]] `{conf: 0.9}`

## Changelog

- 2026-05-09 — created

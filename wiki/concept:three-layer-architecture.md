---
id: concept:three-layer-architecture
type: concept
title: Three-layer architecture (raw / wiki / schema)
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
updated_log:
  - 2026-05-09: created
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# Three-layer architecture

## Summary

LLM Wiki has **three distinct layers**, each with different mutability rules:

| Layer | Contents | Mutability | Authored by |
|---|---|---|---|
| **Raw** | Captured sources verbatim | **Never edited** after capture | Human (curates URLs/docs) |
| **Wiki** | Synthesised entity pages | Updated on every ingest | LLM (with human review) |
| **Schema** | Rules + entity types | Edited rarely, deliberately | Human (the constitution) |

## The three layers

### Raw layer (`raw/`)

Captured primary sources, **immutable**:
```
raw/
├── 2026-05-09-karpathy-llm-wiki-gist.md
├── 2026-05-09-rag-paper.md
└── ...
```

Frontmatter records `source_url`, `ingested_at`, `source_type`. The text itself is verbatim — what the source said when ingested. If the source updates upstream, you re-ingest as a *new* raw file with a new date prefix; you never edit the old one. This preserves the audit trail.

### Wiki layer (`wiki/`)

LLM-generated entity pages — one concept per file:
```
wiki/
├── concept:llm-wiki.md
├── concept:rag.md
├── pattern:citation-discipline.md
└── ...
```

Pages are **synthesised**, not copied. Every claim cites at least one raw source: `[src: raw/...] {conf: 0.5}`. Pages get updated as new sources arrive — confidence rises, claims are reinforced, contradictions surface.

### Schema layer (`SCHEMA.md`)

The constitution. Defines:
- Entity types (concept, pattern, risk, etc.)
- Relation types (composes, depends-on, etc.)
- Confidence rules
- Lint policies
- Privacy rules

The schema is the **discipline** that prevents the LLM from drifting. Without a schema, an LLM-maintained wiki becomes inconsistent within weeks.

## Claims

- Three layers — raw, wiki, schema — each with distinct mutability. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Raw is immutable: "users curate" sources that the LLM "reads" but never edits. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Schema document defines structure and workflows (e.g. CLAUDE.md, AGENTS.md). `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.9}`

## Why three layers (not two)

A two-layer system (raw → wiki) lacks the discipline mechanism. The LLM has no contract for how to write pages, what entities mean, or when to lint. After a few dozen sources, the wiki diverges. The schema layer is what makes this a **maintainable** pattern, not just a one-shot synthesis.

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- depends-on → [[concept:schema-layer]] `{conf: 0.95}` (the schema is the discipline)

## Changelog

- 2026-05-09 — created

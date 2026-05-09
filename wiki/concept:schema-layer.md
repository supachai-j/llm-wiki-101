---
id: concept:schema-layer
type: concept
title: Schema layer (CLAUDE.md / AGENTS.md / SCHEMA.md)
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck]
---

# Schema layer

## Summary

The **schema** is the wiki's constitution — the document that disciplines the LLM's behaviour. Defines entity types, relations, confidence rules, lint policies, privacy rules. Without it, an LLM-maintained wiki diverges within weeks. With it, the artifact stays coherent for years.

## Claims

- "A schema document defining structure and workflows" is one of the three core layers. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Karpathy names CLAUDE.md and AGENTS.md as conventional schema filenames depending on the LLM ecosystem. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`

## What a schema specifies

A complete schema covers:

| Section | What it answers |
|---|---|
| Domain | What this wiki is *for* |
| Entity catalogue | What kinds of pages can exist (concept, pattern, risk, ...) |
| Relation catalogue | How pages link (composes, depends-on, mitigates, ...) |
| Page rules | What every page must contain (frontmatter, citations, etc.) |
| Ingest rules | What happens when a new source arrives |
| Confidence + decay | How claims age |
| Privacy + secrets | What never enters wiki/ or graph/ |
| Lint policy | When + what to check |
| Co-evolution | How the schema itself changes |

This course's `SCHEMA.md` shows all 13 sections in production form.

## Filename conventions

| LLM | Conventional filename |
|---|---|
| Claude Code (Anthropic) | `CLAUDE.md` (often) |
| OpenAI Codex | `AGENTS.md` |
| Vendor-neutral | `SCHEMA.md` |
| Per-skill (LLM Wiki skill) | `SCHEMA.md` (in wiki root) |

The filename matters less than the content. What matters: the LLM reads it before any operation.

## When to update the schema

**Rare and deliberate.** The schema is a constitution, not a config. Update it only when:

- A new entity type emerges that doesn't fit existing types
- A new relation type would meaningfully clarify the graph
- Confidence/decay parameters are demonstrably miscalibrated
- Privacy rules need to change (e.g. legal/compliance shift)

Casual schema edits = drift. Resist them.

## Schema is the discipline mechanism

> "Without a schema, an LLM-maintained wiki becomes inconsistent within weeks."

The LLM is a great writer but a sloppy librarian. The schema is what turns it into a librarian. Without rules, every ingest's vibe varies, page templates diverge, citation styles drift. The schema makes the LLM operate consistently across days, weeks, months.

## Anti-patterns

- ❌ **No schema** — wiki diverges fast
- ❌ **Schema in chat history** — LLM forgets between sessions
- ❌ **Schema that changes weekly** — defeats the constitution role
- ❌ **Schema longer than the wiki** — over-engineered; trim

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- composes → [[concept:three-layer-architecture]] `{conf: 0.95}`
- enables → [[concept:lint]] `{conf: 0.95}` (lint enforces schema)

## Changelog

- 2026-05-09 — created

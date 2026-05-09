---
source_type: web
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
ingested_at: 2026-05-09
title: Karpathy — LLM Wiki (gist)
---

# Karpathy — LLM Wiki

The seed pattern. Andrej Karpathy's design for persistent, LLM-maintained knowledge bases.

## Core architectural layers (3)

Three components:
1. **Immutable raw sources** — user-curated, never edited after capture
2. **LLM-generated wiki** — markdown files the LLM writes and maintains
3. **Schema document** — defines structure and workflows (e.g. `CLAUDE.md` or `AGENTS.md`)

## The three primary operations

### Ingest
> Users add sources; the LLM reads them, discusses takeaways, creates summary pages, updates indexes, and revises relevant entity pages across the wiki.

### Query
> Users ask questions; the LLM searches wiki pages, synthesizes answers with citations, and optionally files valuable findings back as new wiki pages.

### Lint
> Periodic health checks identify contradictions, stale claims, orphaned pages, missing cross-references, and data gaps requiring investigation.

## Navigation files

- **`index.md`** — content-oriented, links and summaries organised by category
- **`log.md`** — chronological, append-only record with parseable date prefixes; tracks ingests, queries, maintenance

## Core philosophy (verbatim quote)

> "The wiki is a persistent, compounding artifact."

Rather than re-deriving knowledge per query (the RAG default), connections, contradictions, and syntheses **accumulate**. Humans direct analysis and curation; LLMs handle maintenance — updating cross-references, maintaining consistency, and bookkeeping across pages.

## Practical applications

- Personal knowledge management (PKM)
- Research deep-dives
- Book annotation
- Business team wikis
- Competitive analysis

## Tooling notes

- Works with **Obsidian** as a viewer (markdown native, graph view, wikilinks)
- **Git** for version control
- LLM-agnostic: works with Claude, Codex, etc.
- Optional CLI tools (e.g. `qmd` mentioned for search)

## Why this matters as a course seed

Karpathy's gist is conceptually rich but practically thin — ~1 page of design principles. The course's job is to operationalise it: schema design choices, lifecycle automation, evaluation, integration patterns. Plus the adjacent academic context (RAG, Zettelkasten) that makes the pattern's novelty visible.

---
id: concept:ingest
type: concept
title: Ingest operation
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# Ingest

## Summary

**Ingest** = the operation that turns a new source into wiki updates. The LLM reads, discusses, summarises, then *revises relevant entity pages across the wiki*. This is where the "compounding" actually happens — a new source rarely creates one new page; it usually touches several.

## Claims

- "Users add sources; the LLM reads them, discusses takeaways, creates summary pages, updates indexes, and revises relevant entity pages across the wiki." `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.95}`
- Ingest is **multi-page** by design — one new source can update 3-10 entity pages. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`
- Successful ingest leaves the wiki **denser and more interconnected**, not just bigger. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`

## The ingest workflow

```
1. CAPTURE
   - User points LLM at a source (URL, doc, transcript, paste)
   - LLM saves verbatim to raw/YYYY-MM-DD-<slug>.md with frontmatter

2. EXTRACT
   - LLM identifies entities mentioned (per SCHEMA's catalogue)
   - For each entity: does it exist? Update. Else create.

3. WRITE / UPDATE
   - For each entity page touched, add new claims with [src: raw/<file>] markers
   - Bump confidence on reinforced claims (formula: conf ← 1 - (1-conf) * 0.6)
   - Open supersession candidates if claims contradict

4. RECONCILE
   - Update index.md (catalogue)
   - Append to log.md (chronological audit)
   - Update graph/edges.jsonl with new relationships

5. SUMMARISE
   - LLM tells the user: pages added, pages modified, contradictions opened
```

## Why this is more than RAG

A RAG-style "ingest" usually means *embedding chunks into a vector store* — additive, no synthesis. The LLM Wiki ingest is **synthetic**: every existing page that touches the topic gets re-evaluated. The artifact isn't just bigger; it's smarter.

## Anti-patterns

- ❌ **Touch only one page** — usually means you missed cross-references. Re-scan.
- ❌ **No citation back to raw** — un-citable claims = drift. Every claim cites or doesn't enter the wiki.
- ❌ **Skipping reconcile** — index.md and log.md drift from reality.
- ❌ **Auto-merging contradictions** — surface them for the human to judge, don't pick silently.

## Relationships

- composes → [[concept:llm-wiki]] `{conf: 0.95}`
- depends-on → [[concept:raw-layer]] `{conf: 0.95}`
- depends-on → [[pattern:citation-discipline]] `{conf: 0.9}`

## Changelog

- 2026-05-09 — created

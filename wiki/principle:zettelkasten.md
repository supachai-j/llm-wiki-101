---
id: principle:zettelkasten
type: principle
title: Zettelkasten — the pre-LLM ancestor
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-zettelkasten-wikipedia.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# Zettelkasten

## Summary

A **Zettelkasten** ("slipbox" in German) is a knowledge management system based on atomic notes, explicit cross-references, and unique IDs. Niklas Luhmann's ~90,000-card system is the canonical example. The LLM Wiki pattern is **the same architecture with an LLM doing the maintenance**.

## Claims

- A Zettelkasten consists of "small items of information stored on Zetteln (German: 'slips'; singular: Zettel), paper slips or cards, that may be linked to each other through subject headings or other metadata such as numbers and tags." `[src: raw/2026-05-09-zettelkasten-wikipedia.md] {conf: 0.95}`
- Niklas Luhmann built a Zettelkasten of "some 90,000 index cards for his research, and credited it for enabling his extraordinarily prolific writing (including about 50 books and 550 articles)". `[src: raw/2026-05-09-zettelkasten-wikipedia.md] {conf: 0.95}`
- The genealogy is direct: paper cards → NoteCards (1980s) → wikis (1990s) → modern PKM (2020s) → LLM Wiki (2024+). `[src: raw/2026-05-09-zettelkasten-wikipedia.md] {conf: 0.9}`

## Three core principles (each maps to LLM Wiki)

### 1. Atomicity
> "Individual notes capture discrete ideas..."

Maps to LLM Wiki: **one concept per page**. Pages with two clearly-separable subjects get split. The 70-year-old principle still holds.

### 2. Cross-referencing
> "Notes employ subject headings or tags that describe key aspects of the note, and they may reference other notes, creating networks of interconnected information."

Maps to LLM Wiki: **wikilinks** `[[entity-id]]` between pages, plus typed edges in `graph/edges.jsonl`.

### 3. Unique identification
> "Numbering, metadata, format, and structure customised to individual methods..."

Maps to LLM Wiki: **stable entity IDs** (`concept:llm-wiki`, `pattern:citation-discipline`) that survive renames and rewrites.

## What's new in LLM Wiki

The architecture is **70 years old**. The novelty is the **maintenance layer**:

| Concern | Zettelkasten (manual) | LLM Wiki |
|---|---|---|
| Atomic notes | Human writes each card | LLM writes pages, human reviews |
| Cross-references | Human inserts links | LLM follows + suggests |
| Consistency check | Human flips through cards | LLM lints |
| Updating on new info | Human re-reads + rewrites | LLM ingest re-touches relevant pages |
| Volume ceiling | ~90k (Luhmann) | effectively unbounded |

A practical Zettelkasten requires hours/week of manual gardening. An LLM Wiki delegates the gardening — the human stays in the curation/judgement role.

## Why this matters

If a student understands Zettelkasten, they understand LLM Wiki. The teaching shortcut is:

> "LLM Wiki = Zettelkasten + an LLM doing the maintenance."

## Relationships

- descended-from → [[concept:llm-wiki]] (well — the other direction: LLM Wiki descends-from Zettelkasten) `{conf: 0.95}`
- composes → [[principle:atomicity]] `{conf: 0.9}`
- composes → [[principle:wikilinks]] `{conf: 0.9}`

## Changelog

- 2026-05-09 — created

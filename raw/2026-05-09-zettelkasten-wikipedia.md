---
source_type: web
source_url: https://en.wikipedia.org/wiki/Zettelkasten
ingested_at: 2026-05-09
title: Zettelkasten — Wikipedia
---

# Zettelkasten

The pre-digital ancestor of LLM Wiki. Niklas Luhmann's note-card system, the conceptual DNA for hypertext, wikis, and (now) LLM-maintained knowledge bases.

## Definition (verbatim)

> "Small items of information stored on Zetteln (German: 'slips'; singular: Zettel), paper slips or cards, that may be linked to each other through subject headings or other metadata such as numbers and tags."

## Core principles

### Atomicity
Individual notes capture **discrete ideas** that "may be numbered hierarchically so that new notes may be inserted at the appropriate place, and contain metadata to allow the note-taker to associate notes with each other."

### Cross-referencing
Notes employ "subject headings or tags that describe key aspects of the note, and they may reference other notes," creating networks of interconnected information.

### Unique identification
"Numbering, metadata, format, and structure" customised to the user. Luhmann's approach assigned "each a unique index number based on a branching hierarchy."

## Niklas Luhmann's system (the famous one)

> "Luhmann, a German sociologist, built up a Zettelkasten of some 90,000 index cards for his research, and credited it for enabling his extraordinarily prolific writing (including about 50 books and 550 articles)."

His index cards were digitised and made available online in 2019. This is the canonical reference for "knowledge accumulation through atomic linked notes."

## Genealogy — Zettelkasten → wikis → LLM Wiki

> "In the 1980s, the card file began to be used as metaphor in the interface of some hypertextual personal knowledge base software applications such as NoteCards. In the 1990s, such software inspired the invention of wikis."

The lineage:
1. Paper note cards (1950s-2000s)
2. NoteCards / hypertext PKM (1980s)
3. Wikis — Ward Cunningham (1995)
4. Modern PKM tools — Roam, Obsidian, Logseq (2020s)
5. **LLM-maintained wikis** — Karpathy et al. (2024-2026)

The atomic notes, explicit linking, and metadata-driven retrieval that define LLM Wiki **descend directly from the index card.**

## Why this matters for the course

Two things:

1. **Validation of the pattern** — atomic + linked + metadata-driven knowledge management has been working for ~70 years before LLMs existed. The novelty is the maintenance layer (LLM doing the bookkeeping), not the architecture.

2. **Proven principles to reuse**:
   - **Atomic notes** → one concept per page (Karpathy: one entity per wiki page)
   - **Unique IDs** → entity IDs in the LLM Wiki schema
   - **Cross-references** → wikilinks `[[entity-id]]`
   - **Append-only structure** → the `log.md` Karpathy specifies

If a student understands Zettelkasten, the LLM Wiki is "Zettelkasten + an LLM doing the gardening." That framing is pedagogically powerful.

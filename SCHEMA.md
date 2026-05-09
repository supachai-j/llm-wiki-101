# SCHEMA — LLM Wiki 101

> Constitution of this wiki. Every Ingest / Query / Lint operation reads this file.

## 1. Domain

This wiki teaches the **LLM Wiki pattern** — a design for persistent, LLM-maintained knowledge bases. Three-layer architecture (raw / wiki / schema), three operations (ingest / query / lint), and the philosophy of "compounding artifact, not re-derived chunks". Audiences: researchers/PKM users (Track A) and engineers building knowledge systems (Track B).

## 2. Entity catalogue

| type | id pattern | gets its own page? | notes |
|---|---|---|---|
| `concept` | `concept:<kebab>` | yes | core ideas (raw layer, wiki layer, schema, ingest, query, lint) |
| `principle` | `principle:<kebab>` | yes | Zettelkasten principles (atomicity, links, IDs, append-only) |
| `pattern` | `pattern:<kebab>` | yes | reusable design patterns (page template, citation discipline, decay) |
| `tool` | `tool:<name>` | yes | Obsidian, Dataview, Git, claude-code |
| `risk` | `risk:<kebab>` | yes | failure modes (claim drift, stale pages, orphaned content) |
| `decision` | `decision:<date>-<slug>` | yes | ADRs (e.g. why markdown over notion) |
| `source` | `source:<kebab>` | no — referenced from raw/ only | upstream URLs |

## 3. Relation catalogue

- `composes` — A is part of B
- `extends` — A is a specialisation of B
- `depends-on` — A cannot function without B
- `descends-from` — historical lineage (LLM Wiki descends-from Zettelkasten)
- `mitigates` — A reduces risk B
- `alternative-to` — A and B solve overlapping problems
- `enables` — A makes B possible
- `cites` — A draws evidence from source B

## 4. Page rules

- One concept per page. If a page grows two clearly-separable subjects, split it.
- YAML frontmatter mandatory. See `wiki/_TEMPLATE.md`.
- Every claim has an inline source marker `[src: raw/...]`.
- Wikilinks use entity IDs: `[[concept:wiki-layer]]`, not `[[Wiki Layer]]`.
- Status: `active` (default), `stale`, `faded`, `orphan`.

## 5. Ingest rules

- Raw source → `raw/YYYY-MM-DD-<slug>.md` untouched.
- Entity extraction runs against §2.
- New page created when entity is "yes" in catalogue _and_ ≥1 non-trivial claim exists.
- Existing page updates: reinforce matching claims, append new ones.

## 6. Confidence and decay

- First observation: `confidence: 0.5`
- Reinforcement (independent source): `conf ← 1 - (1 - conf) * 0.6`
- Contradiction: open supersession candidate.
- Decay half-life:
  - `decision`: 365 days
  - `concept`, `principle`, `pattern`, `risk`: 180 days
  - `tool`: 90 days (tools evolve fast)
  - `source`: not applicable

## 7. Privacy and secrets

Never written to wiki/ or graph/, redacted in raw/ on detection. Standard token: `<REDACTED:apikey|token|pii|secret>`.

For LLM Wiki specifically: **don't leak proprietary sources** into raw/ if they're under NDA. Cite externally only.

## 8. Lint policy

- Lint when ≥10 new sources since last lint, or on user request.
- Orphans with `conf > 0.5` → link from most relevant parent.
- Contradictions → resolve by (most recent authoritative source) > (most sources) > (highest prior confidence).
- Emit `raw/lint-YYYY-MM-DD.md` audit artefact.

## 9. Track structure

- **Track A modules (01-06)** — Foundations. Cite mostly `concept:` + `principle:` pages.
- **Track B modules (07-12)** — Engineering. Cite `pattern:`, `tool:`, `risk:`, `decision:` pages.

## 10. Pre-LLM ancestry stance

This wiki treats Zettelkasten and traditional wikis as **ancestors, not competitors**. The LLM Wiki novelty is the **maintenance layer** (LLM doing bookkeeping), not the architecture. When a claim about LLM Wiki has a Zettelkasten precedent, cite it — credibility accumulates from the lineage.

## 11. RAG positioning

LLM Wiki **complements** RAG; doesn't replace it. When discussing the relationship:
- RAG = stateless retrieval, every query starts fresh
- LLM Wiki = stateful synthesis that compounds
- A production system often uses both: wiki for synthesised understanding, RAG for raw chunk retrieval

Mark this as the canonical framing in any module that touches retrieval.

## 12. Co-evolution

When the LLM hits a case this schema doesn't cover:
1. Do the right thing now.
2. Append note to `raw/schema-todo.md`.
3. Next Lint surfaces it for human promotion.

## 13. Training-deck rules

This wiki feeds two HTML training decks (English + Thai) under `slides/`. When a wiki page is updated with a new "deck-worthy" claim, mark with `tag: deck`.

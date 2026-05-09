# Outline — LLM Wiki 101

_Phase 5 deliverable from `/scaffolding-course-portal` pipeline._
_Written: 2026-05-09 · Author: Supachai Jaturaprom_

12 modules across 2 tracks. Every module cites at least one wiki page.

## Track A — Foundations (modules 01-06)

### Module 01 — What is an LLM Wiki?
- **Wiki cited:** [[concept:llm-wiki]]
- **Outcome:** Understand the pattern in one paragraph; know why "compounding" is the central claim
- **Key claims:** Three layers, three ops, "the wiki is a persistent compounding artifact" (Karpathy)
- **Lab:** none (orientation)

### Module 02 — Why not just RAG?
- **Wiki cited:** [[concept:rag]], [[concept:llm-wiki]]
- **Outcome:** Know when each tool fits; recognise that production often uses both
- **Key claims:** RAG = stateless retrieval; LLM Wiki = stateful synthesis; provenance + updating are RAG's open problems
- **Lab:** Identify 3 questions in your work — classify each as RAG-fit, Wiki-fit, or hybrid

### Module 03 — Ancestry: Zettelkasten and friends
- **Wiki cited:** [[principle:zettelkasten]]
- **Outcome:** See the 70-year lineage; recognise that the architecture is well-validated, only the maintenance layer is new
- **Key claims:** Atomicity + cross-reference + unique IDs descend from Luhmann's index cards through wikis to LLM Wiki
- **Lab:** Sketch your existing notes (Notion/Obsidian/notebook) — count notes, count links, identify atomic vs sprawling notes

### Module 04 — The three layers
- **Wiki cited:** [[concept:three-layer-architecture]], [[concept:raw-layer]], [[concept:wiki-layer]], [[concept:schema-layer]]
- **Outcome:** Internalise that raw is immutable, schema is constitutional, wiki is the synthesised middle
- **Key claims:** Different mutability per layer; the schema is what prevents drift
- **Lab:** Draw the architecture for your own use case — what's "raw" for you? What's a "concept"?

### Module 05 — The page template (citation discipline)
- **Wiki cited:** [[pattern:page-template]], [[pattern:citation-discipline]]
- **Outcome:** Know how every wiki page is structured; know the citation format
- **Key claims:** Every claim cites a source with confidence; multiple citations bump confidence per formula; `{conf: 0.5}` first → asymptotes to 1.0
- **Lab:** Take a paragraph from any source and rewrite it as 3 atomic claims with `[src:]` markers

### Module 06 — Operating an LLM Wiki by hand
- **Wiki cited:** [[concept:ingest]], [[concept:query]], [[concept:lint]]
- **Outcome:** Walk through one ingest, one query, one lint — manually
- **Key claims:** Ingest = multi-page; query = wiki-first then raw; lint = supersession over deletion
- **Lab:** Pick a one-paragraph article. Ingest it manually (write 1-2 wiki pages). Query something. Lint after.

## Track B — Engineering (modules 07-12)

### Module 07 — Schema design choices
- **Wiki cited:** [[concept:schema-layer]]
- **Outcome:** Pick entity types, relations, decay parameters that fit your domain; know what to never put in schema
- **Key claims:** Schema is rare-update; entity catalogue is small + stable; decay half-life varies by entity type
- **Lab:** Customise the SCHEMA template for a domain you care about (e.g. "personal financial decisions", "team incident retros")

### Module 08 — Tooling: Obsidian + Git
- **Wiki cited:** [[tool:obsidian]]
- **Outcome:** Configure Obsidian as a viewer; set up Git for versioning; pick a recommended plugin set
- **Key claims:** Local-first + markdown native = portable; Dataview enables partial lint; Obsidian Git for sync
- **Lab:** Open the course's `wiki/` folder in Obsidian. Install Dataview. Run a Dataview query against frontmatter

### Module 09 — Failure modes (claim drift, orphans, contradictions)
- **Wiki cited:** [[risk:claim-drift]], [[concept:lint]]
- **Outcome:** Recognise the four classes of drift; know mitigations for each; understand why "supersession over deletion"
- **Key claims:** Drift is rarely catastrophic on day 1 — compounds; lint is the maintenance contract; never silently delete
- **Lab:** Run a manual lint pass on a sample wiki — identify orphans, broken citations, stale claims

### Module 10 — Integration with agents (the production angle)
- **Wiki cited:** [[concept:rag]], [[concept:llm-wiki]] (cross-references Anthropic context-engineering article)
- **Outcome:** Position LLM Wiki within agent context engineering; know when to use it vs raw RAG
- **Key claims:** Wiki provides "persistent memory with minimal overhead"; complements just-in-time retrieval; ideal for cross-session compounding
- **Lab:** Sketch how a customer-support bot would use LLM Wiki to learn from each ticket without bloating its context window

### Module 11 — Evaluation: how do I know my wiki is healthy?
- **Wiki cited:** [[concept:lint]], [[risk:claim-drift]]
- **Outcome:** Build a basic eval rubric; know what to check periodically
- **Key claims:** Quality scoring per page; provenance audit (cite still says it?); citation density; orphan rate; freshness percentile
- **Lab:** Define 5 metrics for your wiki; baseline them today; commit to a monthly re-check

### Module 12 — Cheatsheet, deployment, and what to read next
- **Wiki cited:** All
- **Outcome:** One-page reference; know where to take this further
- **Content:** Cheatsheet, links to all 5 sources, recommended next reads (Anthropic context-engineering, Obsidian Dataview, Karpathy's other gists)

---

## Module-to-wiki mapping (Phase 5 quality gate)

| Module | Wiki page(s) cited | Status |
|---|---|---|
| 01 | concept:llm-wiki | ✓ |
| 02 | concept:rag, concept:llm-wiki | ✓ |
| 03 | principle:zettelkasten | ✓ |
| 04 | concept:three-layer-architecture, raw/wiki/schema-layer | ✓ |
| 05 | pattern:page-template, pattern:citation-discipline | ✓ |
| 06 | concept:ingest, concept:query, concept:lint | ✓ |
| 07 | concept:schema-layer | ✓ |
| 08 | tool:obsidian | ✓ |
| 09 | risk:claim-drift, concept:lint | ✓ |
| 10 | concept:rag + Anthropic context-engineering source | ✓ |
| 11 | concept:lint, risk:claim-drift | ✓ |
| 12 | (cheatsheet — cross-references all) | ✓ |

**Phase 5 done when:** every module maps to ≥1 wiki page. ✅ Met.

→ **Phase 5 complete.** Next: Phase 6 (course-en.html long-form).

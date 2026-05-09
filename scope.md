# Scope — LLM Wiki 101

_Phase 1 deliverable from `/scaffolding-course-portal` pipeline._
_Written: 2026-05-09 · Author: Supachai Jaturaprom_
_Seed source: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)_

## Outcome (one sentence)

> **After this course, the reader will be able to design and operate a persistent, LLM-maintained knowledge base — moving their AI workflow from "re-derive every session" to "compounding artifact that gets smarter over time."**

## Audience — two tracks

### Track A — Foundations (modules 01-06, ~20 min)
- **Audience:** Researchers, PKM enthusiasts, knowledge workers using Obsidian/Notion/Roam
- **Focus:** Mental model of the LLM Wiki pattern, why RAG alone isn't enough, how to start
- **No coding required** — concepts and Obsidian-friendly workflow

### Track B — Engineering patterns (modules 07-12, ~25 min)
- **Audience:** Engineers building knowledge systems for teams or production
- **Focus:** Schema design, lifecycle automation, evaluation, integration with agents
- **Code examples** in vendor-neutral pseudo-code

## Format

- **Self-paced reading** primary
- **Reveal.js slides** for live workshops
- **Wiki** as source-of-truth
- **12 modules**, ~45 min full read

## Languages

**Bilingual EN + TH** mirrored 1:1, following the `translating-to-thai-technical` skill rules.

## Sources (Phase 2)

| Source | Why |
|---|---|
| Karpathy "LLM Wiki" gist | The seed pattern — primary |
| Lewis et al. — "Retrieval-Augmented Generation" (2020) | The thing LLM Wiki improves on |
| Sönke Ahrens — "How to Take Smart Notes" (Zettelkasten) | Pre-LLM ancestor of the same idea |
| Obsidian — graph and linking docs | The viewer / tool layer most readers will use |
| Anthropic — agent memory / context engineering | Modern LLM context for the production angle |

## Time budget

| Phase | Estimated |
|---|---|
| 1 — Scope | done (this doc) |
| 2 — Research | ~2 h |
| 3 — Wiki init | ~30 min |
| 4 — Ingest | ~2 h |
| 5 — Outline | ~1 h |
| 6 — Course pages EN | ~3-4 h |
| 7 — Slide deck EN | ~2 h |
| 8 — Bilingual TH mirror | ~3 h |
| 9 — Landing tuning | ~1 h |
| 10 — Deploy | ~30 min |
| 11 — Validate (asset coverage check!) | ~1 h |
| 12 — Promote | ~30 min |

**Total:** ~17 hours bilingual.

## Success criteria

- [ ] A researcher can follow Track A and stand up an Obsidian-based LLM Wiki within an hour
- [ ] An engineer can read Track B and ship a wiki-backed AI assistant for their team
- [ ] Every claim is cited to a primary source in `raw/`
- [ ] Both EN and TH read naturally
- [ ] Phase 11 asset-coverage check passes (every asset reachable from index hero or start-section)

## Out of scope

- **Specific vector DB tutorials** (Pinecone / Chroma / Weaviate) — vendor-specific, drift fast
- **Specific Obsidian plugins** beyond the canonical ones (graph, dataview)
- **Fine-tuning a wiki-aware model** — different topic
- **Multi-tenant SaaS architecture** — too domain-specific

## Done when

- [x] Outcome is one sentence
- [x] Audience defined (two tracks)
- [x] Format chosen
- [x] Time budget mapped
- [x] Out-of-scope explicit

→ **Phase 1 complete.** Next: Phase 2 (research & capture).

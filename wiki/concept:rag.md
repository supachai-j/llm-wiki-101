---
id: concept:rag
type: concept
title: Retrieval-Augmented Generation (RAG) — what LLM Wiki improves on
status: active
confidence: 0.95
sources:
  - raw/2026-05-09-lewis-rag-paper.md
  - raw/2026-05-09-anthropic-context-engineering.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 180
tags: [deck, foundational]
---

# RAG (Retrieval-Augmented Generation)

## Summary

**RAG** combines parametric memory (model weights) with non-parametric memory (external retrievable corpus). Per query, the model retrieves relevant chunks and conditions generation on them. RAG is a baseline; LLM Wiki is what you build *on top of* RAG when you need synthesis to compound across sessions.

## Claims

- RAG combines "pre-trained parametric and non-parametric memory for language generation" — Lewis et al. (2020). `[src: raw/2026-05-09-lewis-rag-paper.md] {conf: 0.95}`
- Parametric memory = model weights (static, hard to update). Non-parametric = explicit, updatable external knowledge. `[src: raw/2026-05-09-lewis-rag-paper.md] {conf: 0.95}`
- The original paper acknowledged that "providing provenance for their decisions and updating their world knowledge remain open research problems". `[src: raw/2026-05-09-lewis-rag-paper.md] {conf: 0.9}`
- Anthropic's framing: RAG retrieves *just-in-time*; LLM Wiki maintains "structured note-taking" that provides "persistent memory with minimal overhead". `[src: raw/2026-05-09-anthropic-context-engineering.md] {conf: 0.9}`

## RAG vs LLM Wiki — the canonical comparison

| Dimension | RAG | LLM Wiki |
|---|---|---|
| State | Stateless per query | Stateful, accumulates |
| Retrieval target | Raw chunks | Synthesised pages |
| Connections | Embedding similarity | Explicit wikilinks |
| Provenance | Chunk → source (loose) | Page → claim → source (tight) |
| Update cost | Re-embed | Re-ingest (touches multiple pages) |
| Compounding | None | High — pages get denser over time |
| Best for | Lookup / per-query QA | Domain mastery / research |

## When RAG is enough

- Need raw chunks, not synthesised understanding
- Knowledge changes faster than wiki can be re-ingested
- Per-query retrieval cost is acceptable
- No need for the model to "know" anything across sessions

## When LLM Wiki adds value

- Engineers building knowledge bases the team needs to learn from
- Researchers who'll spend weeks on a topic
- Onboarding documentation that must converge to a stable shape
- Any domain where **synthesis** matters more than **lookup**

## Production hybrid

Real systems use **both**:
- RAG for raw chunk retrieval (current docs, fresh data)
- LLM Wiki for synthesised understanding (domain knowledge, decisions, lessons)

A query first hits the wiki (cheap, synthesised). If the wiki is silent, fall through to RAG over raw documents (expensive, raw).

## Relationships

- alternative-to → [[concept:llm-wiki]] `{conf: 0.85}`
- composes → [[concept:llm-wiki]] `{conf: 0.6}` (often both used together)

## Changelog

- 2026-05-09 — created

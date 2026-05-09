---
source_type: paper
source_url: https://arxiv.org/abs/2005.11401
ingested_at: 2026-05-09
title: Lewis et al. — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)
---

# Lewis et al. — RAG paper (2020)

The foundational paper for retrieval-augmented generation. The thing LLM Wiki improves on.

## Definition

> "Pre-trained parametric and non-parametric memory for language generation."

- **Parametric memory** = pre-trained seq2seq model (knowledge in weights)
- **Non-parametric memory** = dense vector index of Wikipedia, accessed via neural retriever

## The dual-memory framework

The paper contrasts:
- Knowledge embedded in **model weights** (static, hard to update)
- Knowledge in **explicit external sources** (updatable, citable)

Combining both lets models "access and precisely manipulate knowledge" more effectively than parameter-only systems.

## Key results

- State-of-the-art on open-domain QA tasks (NaturalQuestions, TriviaQA)
- Output is "more specific, diverse and factual" than seq2seq baselines

## Acknowledged limitations (verbatim)

> "Providing provenance for their decisions and updating their world knowledge remain open research problems."

The paper itself flags these as **unsolved** — and these are exactly the problems LLM Wiki tries to address differently:
- **Provenance** → wiki citations to raw sources
- **Updating** → ingest operation reconciles new sources with existing pages

## Why this matters for the course

RAG = **stateless retrieval + generation** (every query starts fresh).
LLM Wiki = **stateful synthesis that compounds** (every query updates the artifact).

The course's mental model rests on this contrast. RAG is the baseline; LLM Wiki is the evolution.

## Citation format

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401.

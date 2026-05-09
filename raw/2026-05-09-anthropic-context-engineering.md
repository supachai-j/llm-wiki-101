---
source_type: web
source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
ingested_at: 2026-05-09
title: Anthropic — Effective context engineering for AI agents
---

# Anthropic — Context engineering for agents

The production-side angle. How LLM Wiki fits into the broader category of "managing what's in the model's context window".

## Core framing

Agents are "LLMs autonomously using tools in a loop", where each interaction depletes an **attention budget**.

> "As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases."

This is called **context rot**. It justifies treating context as a scarce resource — and motivates LLM Wiki: keep the artifact compact, retrieve only what's needed.

## Memory as alternative to pre-loaded context

> "Agents built with the 'just in time' approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools."

This is exactly the LLM Wiki philosophy — the wiki holds the identifiers (entity IDs, file paths, links), and the agent loads pages on demand instead of stuffing everything into context upfront.

> "This mirrors human cognition — we maintain external indexing systems rather than memorizing entire corpuses."

## When to compress vs retrieve

### Compaction
For long-horizon tasks where token count exceeds context windows:

> "Summarises critical architectural decisions, unresolved issues, and implementation details while discarding redundant tool outputs."

Maps to LLM Wiki's **lint operation** — periodically consolidate stale or redundant pages.

### Structured note-taking
> "Agents write notes that get pulled back in later, providing 'persistent memory with minimal overhead.'"

This is **literally the LLM Wiki pattern** as Anthropic describes it — agents writing notes that compound across sessions.

### Hybrid strategies
> "Combine upfront retrieval for speed with autonomous exploration at the agent's discretion, depending on task characteristics."

Maps to LLM Wiki's `query` operation: agent searches the wiki first (fast), retrieves raw sources only if needed (expensive).

## Architectural patterns referenced

1. **Sub-agent architectures** — specialised agents handle focused tasks with clean context windows, returning condensed summaries (1,000-2,000 tokens) to a coordinator
2. **Progressive disclosure** — agents incrementally discover context through exploration rather than exhaustive upfront retrieval
3. **Tool-driven navigation** — well-designed tools enable agents to navigate information landscapes efficiently

All three compose with LLM Wiki:
- Sub-agents read the wiki, write notes back
- Progressive disclosure fits how queries traverse wiki pages
- Tools navigate (grep, read file, follow wikilink)

## Why this matters for the course

The **Engineering track** needs to position LLM Wiki within Anthropic's framing of context engineering. Specifically:

- LLM Wiki is the **persistent layer** in a context-engineering stack
- It complements (doesn't replace) RAG — RAG retrieves chunks; wiki holds synthesised understanding
- It's the right tool for **"knowledge that should compound across sessions"** — not for "session-specific working memory"

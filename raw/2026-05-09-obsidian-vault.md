---
source_type: web
source_url: https://obsidian.md/help/getting-started/getting-started-vault
ingested_at: 2026-05-09
title: Obsidian — Vault concepts
---

# Obsidian — Vault & core concepts

The viewer / tool layer that most LLM Wiki users will adopt. Local-first, file-based, markdown-native.

## What is a Vault?

> "A vault is the foundational unit in Obsidian — essentially a folder of plain markdown files stored locally on your device."

Key word: **plain markdown files**. No proprietary database. No vendor lock-in. Vault is just a folder you can `git init`.

## Core features

### Notes & Wikilinks

> "Your content exists as individual notes that you connect using wikilinks — the `[[note name]]` syntax — creating relationships between ideas without leaving your document."

Wikilinks are the typed edge of the knowledge graph. They render as live cross-references and are how the graph view builds its structure.

### Graph View

> "Visualize your knowledge as an interconnected network, showing how your notes relate to one another across your entire vault."

A force-directed layout of the wikilink graph. Useful for orienting in a large vault and spotting orphan notes (unconnected nodes).

### Plugin Ecosystem

Two tiers:
- **Core plugins** — officially maintained (graph, daily notes, backlinks, tags pane)
- **Community plugins** — created by users (Dataview, Templater, Obsidian Git, etc.)

For LLM Wiki use cases, community-relevant plugins:
- **Dataview** — query notes by frontmatter (similar to LLM Wiki's `lint` capabilities)
- **Obsidian Git** — auto-commit + sync to GitHub
- **Templater** — frontmatter scaffolding (similar to `wiki/_TEMPLATE.md` pattern)

## Philosophy (verbatim)

> "Obsidian emphasizes local-first storage, meaning your notes remain on your device where you maintain complete control."

This aligns precisely with Karpathy's LLM Wiki: the wiki is yours, lives on disk, version-controllable, future-proof.

> "The platform treats your vault as a system where individual notes become more valuable through their relationships — transforming isolated documents into a cohesive knowledge base."

## Why this matters for the course

For the **Foundations track** (researchers, PKM users), Obsidian is the recommended viewer. The course can target Obsidian-specific features (graph, backlinks, Dataview) for visualisation while the LLM does the maintenance.

For the **Engineering track**, Obsidian becomes optional — the wiki is "just markdown files in a git repo," and engineers can use any viewer (CLI, custom UI, VS Code with the markdown preview, etc.).

## Setup quick-reference

```
1. Download Obsidian (free, offline, no signup)
2. "Open folder as vault" → point at your wiki folder
3. Optionally: install Dataview + Obsidian Git
4. Configure CLAUDE.md / AGENTS.md / SCHEMA.md as the LLM's contract
5. Start ingesting raw sources
```

The LLM does the wiki updates (via Claude Code, Cursor, etc.); Obsidian renders them. **They never need to know about each other.**

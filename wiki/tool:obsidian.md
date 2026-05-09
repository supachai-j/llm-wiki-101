---
id: tool:obsidian
type: tool
title: Obsidian — the recommended viewer
status: active
confidence: 0.9
sources:
  - raw/2026-05-09-obsidian-vault.md
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: semantic
half_life_days: 90
tags: [deck, tool]
---

# Obsidian

## Summary

**Obsidian** is the recommended viewer for an LLM Wiki: local-first, markdown-native, free, and supports wikilinks + graph view natively. Critically — it doesn't *own* your data. The vault is just a folder. The LLM writes the wiki; Obsidian renders it.

## Claims

- "A vault is the foundational unit in Obsidian — essentially a folder of plain markdown files stored locally on your device." `[src: raw/2026-05-09-obsidian-vault.md] {conf: 0.95}`
- Wikilink syntax `[[note name]]` matches the LLM Wiki convention. `[src: raw/2026-05-09-obsidian-vault.md] {conf: 0.95}`
- Karpathy's gist names Obsidian as a viewer that works with the pattern. `[src: raw/2026-05-09-karpathy-llm-wiki-gist.md] {conf: 0.85}`
- Obsidian emphasizes "local-first storage, meaning your notes remain on your device where you maintain complete control" — aligns with the LLM Wiki ethos. `[src: raw/2026-05-09-obsidian-vault.md] {conf: 0.95}`

## Why Obsidian fits the pattern

| LLM Wiki convention | Obsidian capability |
|---|---|
| One markdown file per entity | Native (every note = one .md file) |
| Wikilinks `[[entity-id]]` | Native (resolves links, shows backlinks) |
| Frontmatter (YAML) | Native (parsed, used by plugins) |
| Cross-page graph | Graph view core plugin |
| Search across pages | Native + plugins (Dataview for queries) |
| Local + git-friendly | Native (just a folder) |
| Offline-capable | Yes (no cloud dependency) |

Compare to Notion (cloud-only, proprietary), Roam (subscription, lock-in), Logseq (similar to Obsidian but smaller ecosystem). Obsidian is the closest match to "the wiki is just markdown files in a folder."

## Recommended plugin set for LLM Wiki users

| Plugin | Purpose |
|---|---|
| Graph view (core) | Visualise the wiki's knowledge graph |
| Backlinks (core) | See what links to current page (orphan detection) |
| Outline (core) | Per-page navigation |
| **Dataview** (community) | Query notes by frontmatter — partial lint |
| **Templater** (community) | Frontmatter scaffolding (similar to `wiki/_TEMPLATE.md`) |
| **Obsidian Git** (community) | Auto-commit + sync to GitHub |

## Setup quick-reference

```
1. Download Obsidian (free, offline)
2. "Open folder as vault" → point at your wiki folder
3. Install Dataview + Obsidian Git
4. Configure CLAUDE.md / SCHEMA.md as the LLM's contract
5. Start ingesting raw sources
```

The LLM does the writing (via Claude Code, Cursor, etc.); Obsidian does the rendering. The two never need to know about each other.

## Anti-patterns when using Obsidian for LLM Wiki

- ❌ **Using proprietary plugin features** that produce non-portable markdown — the wiki should still work without Obsidian
- ❌ **Storing the vault inside Obsidian's iCloud sync** — use git for sync; iCloud + git in same folder is messy
- ❌ **Heavy use of Dataview queries inside pages** — they only render in Obsidian, breaking portability

## Vendor-neutrality

This is a `tool:` entity. The LLM Wiki pattern works without Obsidian — any markdown viewer (VS Code, GitHub web UI, Bear, even a CLI `cat`) renders the wiki. Obsidian is recommended *for the experience*, not required.

## Relationships

- enables → [[concept:wiki-layer]] (rendering) `{conf: 0.85}`
- alternative-to → [[tool:logseq]] `{conf: 0.7}`
- alternative-to → [[tool:vscode-markdown]] `{conf: 0.6}`

## Changelog

- 2026-05-09 — created

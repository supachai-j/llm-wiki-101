---
id: pattern:page-template
type: pattern
title: Standard wiki page template
status: active
confidence: 0.9
sources:
  - raw/2026-05-09-karpathy-llm-wiki-gist.md
created: 2026-05-09
updated: 2026-05-09
tiers: procedural
half_life_days: 180
tags: [deck]
---

# Page template

## Summary

Every wiki page follows the same shape — frontmatter, summary, claims (with citations), relationships, changelog. The shape is the contract that lets `lint` and `query` operate uniformly.

## The template

```markdown
---
id: <entity-type>:<kebab-slug>            # e.g., concept:rag
type: <entity-type>                        # one of SCHEMA's catalogue
title: <Human-readable title>
status: active                             # active | stale | faded | orphan
confidence: 0.5                            # page-level rollup
sources: []                                # raw/ files that contributed
created: YYYY-MM-DD
updated: YYYY-MM-DD
updated_log:
  - YYYY-MM-DD: created
tiers: semantic                            # episodic | semantic | procedural
half_life_days: 180
tags: []
---

# <Title>

## Summary

One paragraph. What this entity is, plain language.

## Claims

- <Claim.> `[src: raw/...] {conf: 0.5}`
- <Another.> `[src: raw/...] {conf: 0.5}`

## Relationships

- composes → [[entity-id]] `{conf: 0.x}`
- depends-on → [[entity-id]] `{conf: 0.x}`

## Open questions

- [ ] <question>

## Changelog

- YYYY-MM-DD — created
```

## Why each section matters

| Section | Purpose |
|---|---|
| Frontmatter | Machine-readable metadata for lint, query, decay |
| Summary | Human entry point — first paragraph a reader sees |
| Claims | Where citations live; the wiki's "facts" |
| Relationships | Mirrors `graph/edges.jsonl`; lets the graph view light up |
| Open questions | Honest record of what we still don't know |
| Changelog | Append-only audit (frontmatter `updated_log` is finer-grained) |

## Variation by entity type

Most entity types use the template as-is. Two exceptions:

- **`decision:`** pages add a "Context" + "Consequences" section (ADR-flavoured)
- **`source:`** pages don't exist as wiki pages — they're referenced from `raw/` only (per SCHEMA §2)

## Anti-patterns

- ❌ **Skipping frontmatter** — breaks lint, breaks query
- ❌ **Free-form sections per page** — defeats the uniform query
- ❌ **Empty Claims section** — if there are no claims, why does the page exist?
- ❌ **Bullet wrapping** — claims should be atomic single-sentence; if a claim needs multiple sentences, split it

## Relationships

- composes → [[concept:wiki-layer]] `{conf: 0.95}`
- depends-on → [[pattern:citation-discipline]] `{conf: 0.95}`

## Changelog

- 2026-05-09 — created

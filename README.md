# Aigentic website

Public marketing site for Aigentic, served by a small Flask app on Railway (Path A, public).

## Pages
- `index.html` — Home (three products: AI Visibility, Chief of Staff, Board Pack)
- `blueprint.html` — How it works
- `ai-visibility.html` — AI Visibility (free Snapshot)
- Samples: `sample-blueprint.html`, `reynolds-snapshot.html`, `reynolds-visibility-report.html`, `reynolds-cos-dashboard.html`, `reynolds-board-dashboard.html`

`reynolds-visibility-report.html` is the sample AI Search Audit deliverable: the Summary and the Scoreboard, then a gate before Layer 1. It mirrors the client report produced by `generate_exploris_aeo_method_report_pdf.py` in the Exploris Health client folder, but nothing generates it. Change the report format and this file will not follow, so update it by hand in the same pass.

## Articles

`/articles` lists every post; `/articles/<slug>` shows one. Each post is one file, `articles/<slug>.md`:

```
title: The headline
date: 2026-10-07
description: One or two sentences for the listing and search snippets.
status: draft
---
# The headline
The article in Markdown. Tables work. Paste the marketing agent's JSON-LD <script> block at the end, unfenced; PAGE-URL and PUBLISH-DATE fill themselves.
```

`status: draft` is hidden on the live site. Change it to `published`, commit, push. To preview drafts locally: `SHOW_DRAFTS=1 python server.py`, then open localhost:8080/articles. Page layout is in `templates/`; its nav is a copy of `index.html`'s, so change both together.

## Deploy
Railway → New Project → Deploy from GitHub repo → this repo. Then Networking → Custom Domain → Generate a Railway domain. No env vars needed (public).

## This repo is the source of truth

Edit the HTML here, commit, push. Railway auto-redeploys.

There is no second copy. A `outputs/website/` folder in the Aigentic workspace used to hold a duplicate, and this README used to call it the source and this repo "the deploy copy". That was wrong and it cost real time: the duplicate silently fell behind, so edits made there shipped nothing, while anyone following the old "copy the HTML in" instruction would have reverted this repo to the stale version. The duplicate was deleted on 2026-07-17. Don't recreate it.

The `sample-blueprint.html` in here is generated from the `audit` plugin's `strategy-blueprint` skill, which lives in a separate repo. If the Blueprint format changes, change it there and regenerate this file. Hand-editing it re-creates the same drift problem.

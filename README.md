# Aigentic website

Public marketing site for Aigentic, served by a small Flask app on Railway (Path A, public).

## Pages
- `index.html` — Home (three products: AI Visibility, Chief of Staff, Board Pack)
- `blueprint.html` — How it works
- `ai-visibility.html` — AI Visibility (free Snapshot)
- Samples: `sample-blueprint.html`, `reynolds-snapshot.html`, `reynolds-cos-dashboard.html`, `reynolds-board-dashboard.html`

## Deploy
Railway → New Project → Deploy from GitHub repo → this repo. Then Networking → Custom Domain → Generate a Railway domain. No env vars needed (public).

## This repo is the source of truth

Edit the HTML here, commit, push. Railway auto-redeploys.

There is no second copy. A `outputs/website/` folder in the Aigentic workspace used to hold a duplicate, and this README used to call it the source and this repo "the deploy copy". That was wrong and it cost real time: the duplicate silently fell behind, so edits made there shipped nothing, while anyone following the old "copy the HTML in" instruction would have reverted this repo to the stale version. The duplicate was deleted on 2026-07-17. Don't recreate it.

The `sample-blueprint.html` in here is generated from the `audit` plugin's `strategy-blueprint` skill, which lives in a separate repo. If the Blueprint format changes, change it there and regenerate this file. Hand-editing it re-creates the same drift problem.

# Aigentic website

Public marketing site for Aigentic, served by a small Flask app on Railway (Path A, public).

## Pages
- `index.html` — Home (three products: AI Visibility, Chief of Staff, Board Pack)
- `blueprint.html` — How it works
- `ai-visibility.html` — AI Visibility (free Snapshot)
- Samples: `sample-blueprint.html`, `reynolds-snapshot.html`, `bodnar-snapshot.html`, `reynolds-cos-dashboard.html`, `reynolds-board-dashboard.html`

## Deploy
Railway → New Project → Deploy from GitHub repo → this repo. Then Networking → Custom Domain → Generate a Railway domain. No env vars needed (public).

Source of truth for the HTML lives in the Aigentic workspace at `outputs/website/`; this repo is the deploy copy. Update = copy the HTML in, commit, push (Railway auto-redeploys).

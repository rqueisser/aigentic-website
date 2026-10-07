import os
import re
from datetime import date
from flask import Flask, send_from_directory, abort, render_template
import markdown

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
ARTICLES = os.path.join(BASE, "articles")
# Drafts are hidden on the live site. Set SHOW_DRAFTS=1 locally to preview them.
SHOW_DRAFTS = os.environ.get("SHOW_DRAFTS") == "1"


def load_article(slug):
    """Read articles/<slug>.md: a block of `key: value` lines, a `---` line, then Markdown."""
    path = os.path.join(ARTICLES, slug + ".md")
    if not re.fullmatch(r"[a-z0-9-]+", slug) or not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        head, _, body = f.read().partition("\n---\n")
    meta = dict(line.split(":", 1) for line in head.strip().splitlines() if ":" in line)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    d = date.fromisoformat(meta["date"])
    return {
        "slug": slug,
        "title": meta["title"],
        "description": meta.get("description", ""),
        "status": meta.get("status", "draft"),
        "date": d,
        "date_label": d.strftime("%-d %B %Y") if os.name != "nt" else d.strftime("%#d %B %Y"),
        "body": body,
    }


def visible(a):
    return a and (a["status"] == "published" or SHOW_DRAFTS)


@app.route("/articles")
@app.route("/articles/")
def articles():
    slugs = [f[:-3] for f in os.listdir(ARTICLES) if f.endswith(".md")] if os.path.isdir(ARTICLES) else []
    items = [a for a in map(load_article, slugs) if visible(a)]
    items.sort(key=lambda a: a["date"], reverse=True)
    return render_template("articles.html", articles=items)


@app.route("/articles/<slug>")
def article(slug):
    a = load_article(slug)
    if not visible(a):
        abort(404)
    # The page template prints the title, so drop a leading "# Title" line from the body.
    body = re.sub(r"\A\s*# .*\n", "", a["body"])
    # The marketing agent's JSON-LD block ships with these two placeholders.
    body = body.replace("PAGE-URL", f"https://aigentic.co.uk/articles/{slug}")
    body = body.replace("PUBLISH-DATE", a["date"].isoformat())
    a["html"] = markdown.markdown(body, extensions=["tables", "fenced_code"])
    return render_template("article.html", a=a)


@app.route("/")
def home():
    return send_from_directory(BASE, "index.html")


@app.route("/health")
def health():
    return "ok", 200


@app.route("/<path:page>")
def serve_page(page):
    # Serve any file that exists in the site folder (multi-page static site).
    if os.path.isfile(os.path.join(BASE, page)):
        return send_from_directory(BASE, page)
    # Allow extensionless links to resolve to .html
    if os.path.isfile(os.path.join(BASE, page + ".html")):
        return send_from_directory(BASE, page + ".html")
    abort(404)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)

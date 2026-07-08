import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))


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

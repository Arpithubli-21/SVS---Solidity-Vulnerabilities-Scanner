"""
app.py
Flask entry point for the Solidity Vulnerability Scanner.
Routes:
  GET  /        – render the upload form
  POST /scan    – accept a .sol file, scan it, render results
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from scanner import scan_solidity, get_severity_badge_class

# ── Configuration ─────────────────────────────────────────────────────────────
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
ALLOWED_EXTENSIONS = {"sol"}
MAX_FILE_SIZE_MB = 10  # megabytes

app = Flask(__name__)
app.secret_key = "solidity-scanner-secret-key-change-in-production"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE_MB * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ── Helpers ───────────────────────────────────────────────────────────────────
def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/", methods=["GET"])
def index():
    """Render the main upload page."""
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    """Handle file upload OR pasted text and return scan results."""

    input_mode = request.form.get("input_mode", "file")  # "file" or "text"

    # ── Mode 1: Pasted text ───────────────────────────────────────────────────
    if input_mode == "text":
        source_code = request.form.get("code_text", "").strip()
        if not source_code:
            flash("Please paste some Solidity code before scanning.", "error")
            return redirect(url_for("index"))
        filename = "pasted_code.sol"

    # ── Mode 2: File upload ───────────────────────────────────────────────────
    else:
        if "solidity_file" not in request.files:
            flash("No file part in the request.", "error")
            return redirect(url_for("index"))

        file = request.files["solidity_file"]

        if file.filename == "":
            flash("No file selected. Please choose a .sol file.", "error")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Invalid file type. Only .sol files are accepted.", "error")
            return redirect(url_for("index"))

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                source_code = f.read()
        except Exception as exc:
            flash(f"Could not read file: {exc}", "error")
            return redirect(url_for("index"))
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

    results = scan_solidity(source_code)

    return render_template(
        "index.html",
        results=results,
        filename=filename,
        badge_class=get_severity_badge_class,
        source_preview=source_code[:3000],
    )


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

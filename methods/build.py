#!/usr/bin/env python3
"""Build the Methods pages from their markdown sources.

Edit the .md files in this folder, then run:

    python3 methods/build.py

Each page is wrapped in the shared site chrome (topbar, section nav,
onward links, footer) and written next to its source as .html.
Requires the `markdown` package (pip install markdown).

A mu2sd project. (c) 2026 mu2sd LLC.
"""
import html
import pathlib
import re

import markdown

HERE = pathlib.Path(__file__).resolve().parent

# Order here is reading order: it sets the in-section nav and onward links.
PAGES = [
    {
        "src": "index.md",
        "nav": "Overview",
        "eyebrow": "Physician Innovator Track · Methods",
        "title": "Methods toolkit",
        "lede": "From an observed need to a question you can study and a project you can run.",
        "description": "Tutorials on conceptual models and logic models, a terms page, and a Sheffield practice exercise.",
    },
    {
        "src": "conceptual-model.md",
        "nav": "Conceptual model",
        "eyebrow": "Methods · Tutorial for students",
        "title": "Building a conceptual model",
        "lede": "Seven steps from a focused research question to a model you can test.",
        "description": "A step-by-step tutorial for students on building a conceptual model, with templates and a review checklist.",
    },
    {
        "src": "logic-model.md",
        "nav": "Logic model",
        "eyebrow": "Methods · Tutorial for project teams",
        "title": "Building a project logic model",
        "lede": "Seven steps from partners and evidence to a one-page plan everyone can act on.",
        "description": "A step-by-step tutorial on building a project logic model aligned with community priorities.",
    },
    {
        "src": "terms.md",
        "nav": "Terms",
        "eyebrow": "Methods · Reference",
        "title": "Terms and deeper dives",
        "lede": "Plain language for the words the tutorials lean on.",
        "description": "Definitions, a deeper look at research questions, and brief guides to five common health theories.",
    },
    {
        "src": "sheffield-exercise.md",
        "nav": "Sheffield exercise",
        "eyebrow": "Methods · 20-minute exercise · Synthetic data",
        "title": "Sheffield practice exercise",
        "lede": "Diabetes in a rural market: rehearse the conceptual model before arriving on site.",
        "description": "A 20-minute facilitated exercise using synthetic rural diabetes data set in Sheffield, Illinois.",
    },
]

FONTS = (
    "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;"
    "0,9..144,500;0,9..144,600;0,9..144,900;1,9..144,400;1,9..144,500"
    "&family=Archivo:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"
)

TRACK_NAV = [
    ("../index.html", "The way"),
    ("../notion.html", "Set up"),
    ("../trainee-guide.html", "Trainee guide"),
    ("../faculty-guide.html", "Faculty guide"),
    ("../fieldnotes.html", "Field notes"),
    ("../gantt.html", "Schedule"),
    ("index.html", "Methods"),
]

THEME_JS = """<script>
  (function(){
    var root=document.documentElement, btn=document.getElementById('tgl');
    function cur(){var t=root.getAttribute('data-theme'); if(t) return t; return matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';}
    try{var s=localStorage.getItem('mu2sd-theme'); if(s) root.setAttribute('data-theme',s);}catch(e){}
    if(btn) btn.addEventListener('click',function(){var next=cur()==='dark'?'light':'dark'; root.setAttribute('data-theme',next); try{localStorage.setItem('mu2sd-theme',next)}catch(e){}});
  })();
</script>"""


def out_name(page):
    return page["src"].replace(".md", ".html")


def render_body(md_text):
    body = markdown.markdown(
        md_text,
        extensions=["tables", "toc", "sane_lists", "md_in_html"],
        output_format="html5",
    )
    # Task-list items: "- [ ] text" -> a visual checkbox.
    body = re.sub(r"<li>\[ \] ", '<li class="task"><span class="box" aria-hidden="true"></span>', body)
    body = re.sub(r"<ul>(\s*<li class=\"task\">)", r'<ul class="tasks">\1', body)
    return body


def track_nav():
    items = []
    for href, label in TRACK_NAV:
        cur = ' aria-current="page"' if label == "Methods" else ""
        items.append(f'    <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)


def section_nav(active):
    items = []
    for p in PAGES:
        cur = ' aria-current="page"' if p is active else ""
        items.append(f'    <li><a href="{out_name(p)}"{cur}>{p["nav"]}</a></li>')
    return "\n".join(items)


def onward(i):
    parts = []
    if i > 0:
        prev = PAGES[i - 1]
        parts.append(f'  <a class="prev" href="{out_name(prev)}"><span>Back</span><b>{prev["nav"]}</b></a>')
    if i < len(PAGES) - 1:
        nxt = PAGES[i + 1]
        parts.append(f'  <a class="next" href="{out_name(nxt)}"><span>Next</span><b>{nxt["nav"]}</b></a>')
    return '<div class="onward">\n' + "\n".join(parts) + "\n</div>"


def build_page(i, page):
    md_text = (HERE / page["src"]).read_text(encoding="utf-8")
    body = render_body(md_text)
    title = html.escape(page["title"])
    return f"""<!doctype html>
<!--
  {page["title"]} — Physician Innovator Track · Methods
  GENERATED from methods/{page["src"]} by methods/build.py. Edit the markdown, not this file.
  A mu2sd project. © 2026 mu2sd LLC.
-->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(page["description"])}">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="../favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="../apple-touch-icon.png">
<title>{title} — Physician Innovator Track</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="../site.css">
</head>
<body>

<div class="topbar">
  <a class="brandmark" href="../index.html">mu<span class="two">2</span>sd</a>
  <button class="toggle" id="tgl" aria-label="Toggle light or dark theme">Theme</button>
</div>
<nav class="subnav" aria-label="Track sections">
  <ul>
{track_nav()}
  </ul>
</nav>

<div class="wrap narrow">

<header>
  <div class="eyebrow">{html.escape(page["eyebrow"])}</div>
  <h1>{title}</h1>
  <p class="lede">{html.escape(page["lede"])}</p>
</header>

<nav class="methods-nav" aria-label="Methods pages">
  <ul>
{section_nav(page)}
  </ul>
</nav>

<article>
{body}
</article>

{onward(i)}

<footer class="site">
  <span class="fq">“The competence should travel with the learner.”</span>
  <span class="src"><b>mu<span class="two">2</span>sd</b> · The Making of a Physician Innovator &nbsp;·&nbsp; Narratives &amp; rubrics: drvoz.com — a mu2sd studio</span>
</footer>

</div>

{THEME_JS}
</body>
</html>
"""


def main():
    for i, page in enumerate(PAGES):
        target = HERE / out_name(page)
        target.write_text(build_page(i, page), encoding="utf-8")
        print(f"wrote methods/{target.name}")


if __name__ == "__main__":
    main()

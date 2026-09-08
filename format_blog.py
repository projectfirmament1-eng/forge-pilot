#!/usr/bin/env python3
"""Simple blog post formatter.

Usage:
    python format_blog.py input.md > output.html

The script expects the input markdown to start with:
    # Title
    Date: YYYY-MM-DD
    Tags: tag1, tag2, tag3

Everything after the third line is treated as the body content.
"""

import sys
import re

def parse_header(lines):
    title = ""
    date = ""
    tags = []
    if lines and lines[0].startswith("#"):
        title = lines[0].lstrip("# ").strip()
    if len(lines) > 1 and lines[1].lower().startswith("date:"):
        date = lines[1].split(":", 1)[1].strip()
    if len(lines) > 2 and lines[2].lower().startswith("tags:"):
        tags = [t.strip() for t in lines[2].split(":", 1)[1].split(",") if t.strip()]
    return title, date, tags

def markdown_to_html(md):
    # Very minimal conversion: headings, paragraphs, bold, italics, links, lists
    html = []
    for line in md.splitlines():
        line = line.rstrip()
        if not line:
            continue
        # headings
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            content = line.lstrip("# ")
            html.append(f"<h{level}>{content}</h{level}>")
            continue
        # unordered list
        if line.startswith("- "):
            html.append(f"<li>{line[2:]}</li>")
            continue
        # bold **text**
        line = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", line)
        # italics *text*
        line = re.sub(r"\*(.+?)\*", r"<em>\1</em>", line)
        # links [text](url)
        line = re.sub(r"\[(.+?)\]\((.+?)\)", r"<a href='\2'>\1</a>", line)
        html.append(f"<p>{line}</p>")
    # wrap list items in <ul> if any
    if any(l.startswith("<li>") for l in html):
        new_html = []
        in_ul = False
        for l in html:
            if l.startswith("<li>"):
                if not in_ul:
                    new_html.append("<ul>")
                    in_ul = True
                new_html.append(l)
            else:
                if in_ul:
                    new_html.append("</ul>")
                    in_ul = False
                new_html.append(l)
        if in_ul:
            new_html.append("</ul>")
        html = new_html
    return "\n".join(html)

def main():
    if len(sys.argv) != 2:
        print("Usage: format_blog.py <input.md>", file=sys.stderr)
        sys.exit(1)
    input_path = sys.argv[1]
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {input_path}: {e}", file=sys.stderr)
        sys.exit(1)
    lines = content.splitlines()
    title, date, tags = parse_header(lines[:3])
    body_md = "\n".join(lines[3:])
    body_html = markdown_to_html(body_md)
    # Build final HTML with minimal CSS styling
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="date" content="{date}">
    <meta name="tags" content="{', '.join(tags)}">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 1rem; }}
        h1, h2, h3 {{ color: #333; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        ul {{ margin-left: 1.5rem; }}
    </style>
</head>
<body>
    <article>
        <h1>{title}</h1>
        <p><em>{date}</em></p>
        <p><strong>Tags:</strong> {', '.join(tags)}</p>
        {body_html}
    </article>
</body>
</html>"""
    print(html)

if __name__ == "__main__":
    main()

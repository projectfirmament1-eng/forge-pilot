import sys
import re
import pathlib

def parse_frontmatter(md_text):
    """Extract YAML frontmatter from markdown text.
    Returns a dict of metadata and the markdown body.
    """
    fm_pattern = r"^---\n(.*?)\n---\n(.*)$"  # simple non-greedy
    match = re.search(fm_pattern, md_text, re.DOTALL)
    if not match:
        return {}, md_text
    fm_text, body = match.groups()
    meta = {}
    for line in fm_text.splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            meta[key.strip()] = val.strip()
    return meta, body

def markdown_to_html(md_body):
    """Very naive markdown to HTML conversion for headings and paragraphs.
    For real use, replace with a proper markdown library.
    """
    html_lines = []
    for line in md_body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('# '):
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith('## '):
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith('### '):
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
        else:
            html_lines.append(f"<p>{line}</p>")
    return "\n".join(html_lines)

def build_html(meta, body_html):
    title = meta.get('title', 'Blog Post')
    tags = meta.get('tags', '')
    date = meta.get('date', '')
    # Simple CSS styling block
    style = """
    <style>
    body {font-family: Arial, sans-serif; line-height: 1.6; margin: 2rem;}
    h1, h2, h3 {color: #333;}
    </style>
    """
    meta_tags = f"<meta name='tags' content='{tags}'>" if tags else ''
    meta_date = f"<meta name='date' content='{date}'>" if date else ''
    html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>{title}</title>
{meta_tags}
{meta_date}
{style}
</head>
<body>
{body_html}
</body>
</html>"""
    return html

def main():
    if len(sys.argv) != 2:
        print('Usage: python format_blog_post.py <markdown_file>')
        sys.exit(1)
    md_path = pathlib.Path(sys.argv[1])
    if not md_path.is_file():
        print(f'File not found: {md_path}')
        sys.exit(1)
    md_text = md_path.read_text(encoding='utf-8')
    meta, body = parse_frontmatter(md_text)
    body_html = markdown_to_html(body)
    final_html = build_html(meta, body_html)
    out_path = md_path.with_suffix('.html')
    out_path.write_text(final_html, encoding='utf-8')
    print(f'Generated {out_path}')

if __name__ == '__main__':
    main()

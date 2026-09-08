import pathlib
import subprocess
import sys

def run_script(md_content: str) -> str:
    # Write temporary markdown file
    tmp_md = pathlib.Path('tmp_test.md')
    tmp_md.write_text(md_content, encoding='utf-8')
    # Run the script
    result = subprocess.run([sys.executable, 'format_blog_post.py', str(tmp_md)], capture_output=True, text=True)
    assert result.returncode == 0, f'Script failed: {result.stderr}'
    # Read generated HTML
    html_path = tmp_md.with_suffix('.html')
    html = html_path.read_text(encoding='utf-8')
    # Cleanup
    tmp_md.unlink()
    html_path.unlink()
    return html

def test_basic_conversion():
    md = """---
title: Test Post
date: 2024-01-01
tags: test,example
---
# Hello World
This is a paragraph.
"""
    html = run_script(md)
    assert '<title>Test Post</title>' in html
    assert "<meta name='date' content='2024-01-01'>" in html
    assert "<meta name='tags' content='test,example'>" in html
    assert '<h1>Hello World</h1>' in html
    assert '<p>This is a paragraph.</p>' in html

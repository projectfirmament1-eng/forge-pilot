'''test_research_summary.py

Simple pytest that validates the research summary meets the required word count (800‑1000 words).
''' 

from research_summary import SUMMARY

def test_word_count():
    # Split on whitespace to count words
    words = SUMMARY.split()
    count = len(words)
    assert 800 <= count <= 1000, f"Word count {count} is outside the required range (800‑1000)"

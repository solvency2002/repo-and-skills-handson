#!/usr/bin/env python3
"""humanizer_academic.py – Academic text humanizer.
Implements the guidelines defined in .agent/skills/humanizer-academic/SKILL.md:
- Keep sentence length around 40 characters.
- Replace "することができる" with "できる".
- Preserve the original claim strength.
- When multiple bullet points appear consecutively, merge them into a paragraph using "、" and add a trailing "。".
"""
import sys, re

def shorten_sentence(sentence, max_len=40):
    """If the sentence exceeds max_len, truncate at the nearest punctuation before the limit.
    If none found, cut at max_len and append an ellipsis.
    """
    s = sentence.strip()
    if len(s) <= max_len:
        return s
    # look for a punctuation before the limit
    for i in range(max_len, 0, -1):
        if s[i] in "、，,;：:"
            return s[:i].strip() + "…"
    return s[:max_len].strip() + "…"

def replace_can_do(text):
    return re.sub(r"することができる", "できる", text)

def merge_bullets(lines):
    merged = []
    buf = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('-'):
            # remove leading '-'
            buf.append(stripped[1:].strip())
        else:
            if buf:
                merged.append('、'.join(buf) + '。')
                buf = []
            merged.append(line)
    if buf:
        merged.append('、'.join(buf) + '。')
    return '\n'.join(merged)

def process(text):
    # split into paragraphs (double newline)
    paras = text.split('\n\n')
    out = []
    for para in paras:
        # handle bullet merging first
        lines = para.split('\n')
        para = merge_bullets(lines)
        # split into sentences (by '。')
        sentences = [s for s in para.split('。') if s]
        new_sentences = []
        for s in sentences:
            s = replace_can_do(s)
            s = shorten_sentence(s)
            new_sentences.append(s)
        out.append('。'.join(new_sentences) + '。')
    return '\n\n'.join(out)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    print(process(input_text))

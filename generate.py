import os

import markdown

md_path = os.path.join('pages', 'digital_sculptures', 'default.md')

with open(md_path, 'r') as infile:
    md = infile.read()

html = markdown.markdown(md)

print(html)

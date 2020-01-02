import os

import markdown

def main():
    print('install worked')

def get_pages(folder):
    """Return filepaths to page folders"""
    pages = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if not os.path.isdir(item_path):
            continue
        if not find_md_file(item_path):
            continue
        pages.append(item_path)
    return pages

def process_page(src, dst):
    """Create a webpage in the destination based on markdown in the source"""
    md_filepath = find_md_file(src)
    html = get_html(md_filepath)

    print(html)

def get_html(md_filepath):
    """Return html from the given markdown filepath"""

    with open(md_filepath, 'r') as infile:
        md = infile.read()

    html = markdown.markdown(md)

    return html

def find_md_file(folder):
    """Return path to the markdown file in a folder"""

    md_filepath = None

    for item in os.listdir(folder):
        if os.path.splitext(item)[1].lower() == '.md':
            md_filepath = os.path.join(folder, item)

    return md_filepath


if __name__ == '__main__':
    main()

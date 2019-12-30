import os

import markdown

def main():
    page = os.path.join('pages', 'digital_sculptures')

    process_page(page)

def process_page(folder):

    md_file = find_md_file(folder)

    with open(md_file, 'r') as infile:
        md = infile.read()

    html = markdown.markdown(md)

    print(html)


def find_md_file(folder):
    """Return path to the markdown file in a folder"""

    md_file = None

    for item in os.listdir(folder):
        if os.path.splitext(item)[1].lower() == '.md':
            md_file = os.path.join(folder, item)

    return md_file


if __name__ == '__main__':
    main()

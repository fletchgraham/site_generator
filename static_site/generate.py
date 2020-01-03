"""Generate a static html site from a bunch of markdown files."""

import os
import markdown

def main():

    print('install worked')


def process(src, dst):
    """If the src is a valid page,
    process it and spit out a webpage."""

    # if it's not a directory, get out early
    if not os.path.isdir(src):
        return

    # get a list of md files in the dir
    md_files = [
        x for x
        in os.listdir(src)
        if os.path.splitext(x)[1].lower() == '.md'
        ]

    # if no markdown files, get out early
    if not md_files:
        return

    # turn the md into html
    html = get_html(os.path.join(src, md_files[0]))

    page_name = os.path.basename(src)
    out_folder = os.path.join(dst, page_name)
    index_path = os.path.join(dst, page_name, 'index.html')

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    with open(index_path, 'w') as outfile:
        outfile.write(html)


def get_html(md_filepath):
    """Return html from the given markdown filepath"""

    with open(md_filepath, 'r') as infile:
        md = infile.read()

    html = markdown.markdown(md)

    return html


if __name__ == '__main__':
    main()

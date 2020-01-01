# Static Site

A python module for generating a static html website.

## Usage

1. Clone this repo.
1. cd into the repo.
1. run `pip install .`
1. cd to where your markdown content lives
1. run `python -m static_site.generate --destination <path/to/dst>` If no destination is provided, it will put the generated site in a subfolder.

## How to Structure MD content

content
  pages
    earth
      earth01.jpg
      earth02.jpg
      default.md
    venus
      venus01.jpg
      venus02.jpg
      default.md
    gallery
      image01.md
      image02.md
      gallery.md
  templates
    base.html
    default.html
    gallery.html

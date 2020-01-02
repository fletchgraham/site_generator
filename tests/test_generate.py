import os
from static_site import generate

def test_find_md_file():
    file = generate.find_md_file('tests/pages/the_sun')
    assert 'default.md' in file

def test_get_pages():
    root = os.path.join('tests', 'pages')
    pages = generate.get_pages(root)
    assert os.path.join(root, 'the_sun') in pages
    assert os.path.join(root, 'not_a_page') not in pages

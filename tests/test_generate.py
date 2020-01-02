from static_site import generate

def test_find_md_file():
    file = generate.find_md_file('tests/pages/the_sun')
    assert 'default.md' in file

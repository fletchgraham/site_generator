import os
import shutil
from static_site import generate


def test_proces_page():
    pages_folder = os.path.join('tests', 'pages')
    dst = os.path.join('tests', 'site')

    for i in os.listdir(pages_folder):
        i_path = os.path.join(pages_folder, i)
        generate.process(i_path, dst)

    assert os.path.exists(os.path.join(dst, 'the_sun'))

    shutil.rmtree(dst)

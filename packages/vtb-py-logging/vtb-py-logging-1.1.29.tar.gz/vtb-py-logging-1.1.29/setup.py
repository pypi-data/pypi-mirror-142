import io
from pathlib import Path

from setuptools import setup, find_packages

here = Path(__file__).parent

REQUIRED = ["orjson", "python-multipart"]
TEST_REQUIRED = ["pytest"]

with io.open(here / 'README.md', encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(here / 'vtb_py_logging' / '__about__.py') as fp:
    exec(fp.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__email__'],
    packages=find_packages(exclude=['tests']),
    install_requires=REQUIRED,
    tests_require=TEST_REQUIRED
)

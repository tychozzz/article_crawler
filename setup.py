from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.4'
DESCRIPTION = 'A package for crawling markdown formatted articles from certain webpage and storing them locally.'

# Setting up
setup(
    name="article_crawler",
    version=VERSION,
    author="ltyzzz (Tycho)",
    author_email="ltyzzz2000@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['bs4', 'html2text', 'parsel', 'requests'],
    keywords=['python', 'markdown', 'pdf', 'article', 'crawler'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
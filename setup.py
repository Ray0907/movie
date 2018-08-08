import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['requests', 'bs4', 'lxml', 'urwid', 'six']

setup(
    name = "rottentomatoes",
    version = "1.0.",
    author = "Ray Tien",
    author_email = "a0939552854@gmail.com",
    description = "Get movie information from rottentomates and display in your terminal",
    license = "MIT",
    keywords = "rottentomatoes terminal movie",
    #url = "https://github.com/chishui/douban-movie",
    packages=['src'],
    #long_description=read('README.md'),
    include_package_data=True,
    install_requires=requirements,
    entry_points={'console_scripts': ['rottentomatoes=src.__main__:main']},
)
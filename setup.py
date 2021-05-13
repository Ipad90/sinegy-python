from setuptools import setup, find_packages

with open('README.md', 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

setup(
    name = 'sinegy-python',
    version = '0.2',
    author = 'James Ong Rui Ming',
    author_email = 'jamesong054@gmail.com',
    description = 'Python library for connecting to the Sinegy API.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Ipad90/sinegy-python',
    project_urls = {
        'Bug Tracker': 'https://github.com/Ipad90/sinegy-python/issues',
    },
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages = [
        'sinegy_python'
    ],
    python_requires = '>=3.6'
)

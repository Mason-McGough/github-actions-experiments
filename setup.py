"""
No license!
"""

from setuptools import setup, find_packages

PACKAGE_NAME = 'GitHub-Actions-Experiments'
VERSION = '0.1.0'
AUTHOR = "Mason McGough"
AUTHOR_EMAIL = 'mcgough.mason@gmail.com'
SHORT_DESCRIPTION = 'A place to experiment with GitHub Actions.'
URL = 'https://github.com/Mason-McGough/github-actions-experiments'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    packages=find_packages(where='./src'),
    package_dir={
        '': 'src'
    },
    classifiers=[  # https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha'
    ],
    python_requires='>=3.6',
)

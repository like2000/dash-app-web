"""A setuptools based setup module."""
from io import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dash_web_app',
    version='0.0.1',
    description='First test of dash powered web application.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kli/dash-web-app',
    author='Kevin Li',
    author_email='kevin.li.cern@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Plotly Dash Flask',
    packages=find_packages(),
    install_requires=['flask',
                      'flask_assets',
                      'pandas',
                      'dash',
                      'dash_core_components',
                      'dash_html_components',
                      'dash_table',
                      'dash_renderer',
                      'pathlib'],
    entry_points={
        'console_scripts': [
            'run = wsgi:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/like2000/dash-web-app/issues',
        'Source': 'https://github.com/like2000/dash-web-app/',
    },
)

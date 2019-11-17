from os import path
from setuptools import find_packages, setup

VERSION = (0, 0, 5)

here = path.abspath(path.dirname(__file__))

# Get the long description trigramsom the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))

setup(
    name='addok-getbyid',
    version='.'.join(map(str, VERSION)),
    description=__doc__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/osmontrouge/addok-getbyid',
    author='François de Metz',
    author_email='francois@2metz.fr',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='addok',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    entry_points={'addok.ext': ['getbyid=addok_getbyid']},
)

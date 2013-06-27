try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Ben Ross',
        'url':
        'https://github.com/benjross/LearnPythonTheHardWay/tree/master/projects/ex47/',
        'download_url':
        'https://github.com/benjross/LearnPythonTheHardWay/tree/master/projects/ex47/',
        'author_email': 'benjross@cs.washington.edu',
        'version': '0.1',
        'intstall_requires': ['nose'],
        'packages': ['ex46'],
        'scripts': [],
        'name': 'project_ex46'
        }

setup(**config)

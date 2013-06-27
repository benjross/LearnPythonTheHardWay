try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Ben Ross',
        'url':
        'https://github.com/benjross/LearnPythonTheHardWay/tree/master/projects',
        'download_url':
        'https://github.com/benjross/LearnPythonTheHardWay/tree/master/projects',
        'author_email': 'benjross@cs.washington.edu',
        'version': '0.1',
        'intstall_requires': ['nose'],
        'packages': ['ex48'],
        'scripts': [],
        'name': 'project_ex48'
        }

setup(**config)

from distutils.core import setup
from pymqo import __version__, __author__, __email__

setup(
    name='pymqo',
    version=__version__,
    packages=[
        '',
        'pymqo',
    ],
    url='https://github.com/ducminhgd/pymqo',
    license='',
    author=__author__,
    author_email=__email__,
    description='Python Message Queue Object'
)

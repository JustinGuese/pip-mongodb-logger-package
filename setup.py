from setuptools import setup

from mongodblogger import __version__

setup(
    name='mongodblogger',
    version=__version__,

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Justin Guese',
    author_email='guese.justin@gmail.com',

    py_modules=['my_pip_package'],
)
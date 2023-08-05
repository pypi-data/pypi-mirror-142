from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

#with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    #long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'library for calculating different probabilities in poker'
LONG_DESCRIPTION = 'A package that takes the players cards and the table cards as input and spits out an output of the enemies card combination chances'

# Setting up
setup(
    name="pokerchancestest",
    version=VERSION,
    author="Tomi Bilcu",
    author_email="<bilcutomi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
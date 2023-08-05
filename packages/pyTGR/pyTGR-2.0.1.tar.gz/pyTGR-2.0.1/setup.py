from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '2.0.1'
DESCRIPTION = 'A minimal lib for rendering things on Terminal.'

# Setting up
setup(
    name="pyTGR",
    version=VERSION,
    author="Merwin",
    author_email="<merwinmathews1001@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/mastercodermerwin/TGR",
    project_urls={
        "Bug Tracker": "https://github.com/mastercodermerwin/TGR/issues",
    },
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'sty','pynput'],
    keywords=['python', 'terminal','color','graphics','shapes','terminal events'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

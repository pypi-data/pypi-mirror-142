from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Down Detector APIs utils'
LONG_DESCRIPTION = 'A package that allows to interact with Down Detector Service APIs'

# Setting up
setup(
    name="downdetecthon",
    version=VERSION,
    author="SteveEmmE (Stefano Monti)",
    author_email="<stefano.monti02@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'rest', 'requests', 'down detector', 'web service'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
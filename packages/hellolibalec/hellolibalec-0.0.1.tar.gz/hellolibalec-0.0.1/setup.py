from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A basic hello package'
LONG_DESCRIPTION = 'This package is used to help me learn what goes into creating python libraries and distributing them on PyPI'

# Setting up
setup(
    name="hellolibalec",
    version=VERSION,
    author="Alecgrater",
    author_email="<alecgrater@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'learning', 'useless'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
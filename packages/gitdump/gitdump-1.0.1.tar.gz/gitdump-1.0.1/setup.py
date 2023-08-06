from setuptools import setup, find_packages
import os


VERSION = '1.0.1'
DESCRIPTION = 'Dump all repos of a github account at once.'


# Setting up
setup(
    name="gitdump",
    version=VERSION,
    author="Divinemonk",
    author_email="<v1b7rc8eb@relay.firefox.com>",
    description=DESCRIPTION,
    # long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url = 'https://github.com/Divinemonk/gitdump/',
    packages=['gitdump'],
    keywords=['gitdump', 'divinemonk', 'gd', 'github', 'git'],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "gd=gitdump.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "License :: OSI Approved :: MIT License"
    ]
)
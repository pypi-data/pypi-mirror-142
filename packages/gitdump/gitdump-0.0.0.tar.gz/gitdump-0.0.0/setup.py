from setuptools import setup, find_packages
import os


VERSION = '0.0.0'
DESCRIPTION = 'Comming soon ...'


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
    # py_modules = ['jh_cmdcenter', 'jh_matrix','justhacking'],
    # install_requires=['rich'],
    # keywords=[],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "gd=gitdump.__main__:dump",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "License :: OSI Approved :: MIT License"
    ]
)
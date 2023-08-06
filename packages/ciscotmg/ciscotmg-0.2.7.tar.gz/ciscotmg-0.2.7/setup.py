""" pypi package """
from os import path
from setuptools import setup, find_packages
from ciscotmg.meta import Meta

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name="ciscotmg",
    author=Meta.__author__,
    author_email=Meta.__email__,
    description=Meta.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=Meta.__url__,
    version=Meta.__version__,
    packages=find_packages(),
    py_modules=["ciscotmg"],
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        ciscotmg=ciscotmg.cli:cli
    """,
    python_requires=">=3.9",
    license=Meta.__license__ + "; " + Meta.__copyright__,
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

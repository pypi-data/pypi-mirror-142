import pathlib
import re

from setuptools import find_packages, setup

NAME = "pathlib_extensions"
PACKAGES = find_packages(where="src")
META_PATH = pathlib.Path("src", NAME, "__init__.py")
KEYWORDS = ["backport", "pathlib", "path", "filesystem"]
PROJECT_URLS = {
    "Changelog": f"https://github.com/ThScheeve/{NAME}/blob/master/CHANGELOG.md",
    "Bug Tracker": f"https://github.com/ThScheeve/{NAME}/issues",
    "Source Code": f"https://github.com/ThScheeve/{NAME}",
}

LONG = f"""
Pathlib Extensions -- Backported and Experimental Filesystem Path Features for Python

The ``pathlib`` module was added to the standard library in Python 3.4, but
many new features have been added to the module since then.

This means users of older Python versions who are unable to upgrade will not be
able to take advantage of new features added to the ``pathlib`` module, such as
``pathlib.PurePath.with_stem()``.

The ``{NAME}`` module contains backports of these changes.
Experimental filesystem path features that are not found in the ``pathlib``
module are also included in ``{NAME}``.
"""

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

INSTALL_REQUIRES = ["mimetypes_extensions"]

###############################################################################

HERE = pathlib.Path(__file__).resolve().parent


def read(*parts):
    """
    Build an absolute path from *parts* and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with open(HERE.joinpath(*parts)) as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name=NAME,
    version=find_meta("version"),
    description=find_meta("description"),
    long_description=LONG.strip(),
    long_description_content_type="text/x-rst",
    url=find_meta("url"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    license=find_meta("license"),
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    project_urls=PROJECT_URLS,
    packages=PACKAGES,
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6",
)

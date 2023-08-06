==================
Pathlib Extensions
==================

.. raw:: html

  <p align="center">
    <a href="https://pypi.org/project/pathlib_extensions/">
      <img src="https://img.shields.io/pypi/pyversions/pathlib_extensions" alt="Supported versions"/>
    </a>
    <a href="https://pypi.org/project/pathlib_extensions/">
      <img src="https://img.shields.io/pypi/v/pathlib_extensions" alt="PyPI Package latest release"/>
    </a>
    <a href="https://github.com/ThScheeve/pathlib_extensions/blob/master/LICENSE">
      <img src="https://img.shields.io/pypi/l/pathlib_extensions" alt="License"/>
    </a>
  </p>
  <p align="center">
    <a href="https://github.com/ThScheeve/pathlib_extensions/issues/">
      <img src="https://img.shields.io/github/issues-raw/ThScheeve/pathlib_extensions" alt="Open issues"/>
    </a>
    <a href="https://github.com/ThScheeve/pathlib_extensions/issues">
      <img src="https://img.shields.io/github/issues-closed-raw/ThScheeve/pathlib_extensions" alt="Closed issues"/>
    </a>
  </p>

Overview
========

The ``pathlib_extensions`` module serves two related purposes:

- Enable use of new filesystem path features on older Python versions. For example,
  ``pathlib.PurePath.with_stem()`` is new in Python 3.9, but ``pathlib_extensions``
  allows users on Python 3.6 through 3.8 to use it too.
- Enable experimentation with new filesystem path features that are not found
  in the ``pathlib`` module.

Included Items
==============

This module currently contains the following:

- Experimental features

  - ``Path.is_image_file()``
  - ``Path.is_audio_file()``
  - ``Path.is_video_file()``

- In ``pathlib`` since Python 3.9

  - ``PurePath.with_stem()``
  - ``PurePath.is_relative_to()``
  - ``Path.readlink()``

- In ``pathlib`` since Python 3.8

  - ``Path.link_to()``

- In ``pathlib`` since Python 3.7

  - ``Path.is_mount()``

Running Tests
=============
To run tests, run ``tests/test_pathlib_extensions.py``. You will also need to install
the latest version of ``pathlib`` if you are using a version of Python that
does not include ``pathlib`` as a part of the standard library.
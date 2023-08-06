========
Overview
========

A cli tool to perform json and yaml object schema validation.

* Free software: MIT license

Installation
============

::

    pip install scheckcli

You can also install the in-development version with::

    pip install https://gitlab.com/ronmallory/python-scheckcli/-/archive/main/python-scheckcli-main.zip


Documentation
=============


https://python-scheckcli.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

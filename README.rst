#########
PyExample
#########

.. image:: https://travis-ci.org/tomfitzherbert/pyexample.svg?branch=master

**An example Python application to provide a template for Python apps**

This project provides a basic Python application that can be used as a
template for developing new applications or as a reference against which to
learn or confirm how an existing application could be restructured.

***********************
How to use this project
***********************

This project is intended to be used in two primary ways:

As a reference for a good practice Python application structure
===============================================================

When used as a reference it is recommended to download or clone the project
and then explore the files and commands. It is my intention to extend this
``README`` file over time to capture more of the reasons behind the suggested
structure and also explain some of the

As a base template that can be used to develop new Python applications
======================================================================

Feel free to ``fork`` the project or just download and copy into an empty
directory and start renaming the root directory to the name of your new
project.

Make sure to change all references to ``pyexample``, ``space`` and my contact
details prior to publishing any projects based on this template (to avoid
confusion later).

.. note::
  NB. my contact details and a reference to the MIT license are included at
  the top of every ``.py`` file plus the ``config.yaml.example`` file - so be
  sure to update these.

************************
Features in this example
************************

* Demonstrates the separation of ``scripts`` and ``core`` application code.
* Uses ``git`` for source control.
* Uses ``pytest`` to provide a test rig suitable to use with CI tools.
* Uses ``travis-ci`` for continuous integration tests.
* Uses ``setuptools`` to build a package that can be hosted in a PyPI repository
  and installed using ``pip``.

Separating the core application and associated scripts
======================================================

Many projects require some additional ``scripts`` to be packaged alongside the
main application code. These are often used to perform admin tasks related to
the application.

Running the core application
----------------------------

.. note::
  This example application currently only defines a ``Class`` and nothing else.
  Before the application can be run we will need to add something suitable.

Running the scripts
-------------------

.. note::
  Still need to make the script do something more than a ``print()`` command.

To run one of the scripts, simply use the following command from the project's
root directory::

  # from the project's root directory
  python scripts/db_setup.py

Using git for source control
============================

This project is hosted on
`GitHub <https://github.com/tomfitzherbert/pyexample>`_.

You can ``fork`` the project and practice various ``git`` operations on your
copy.

Using setuptools to build a distributable package
=================================================

When you want to distribute your Python application properly as an installable
package, you need to use ``setuptools`` to create the package. This makes it
possible for others to install your application using ``pip install pyexample``
(replacing ``pyexample`` with the name of you new package).

.. note::
  This project requires setuptools v30.3.0 or higher to be installed (since it
  uses the declarative package configuration approach introduced in that
  version).

You create your Python package by running the project's ``setup.py`` file,
which has been created to use ``setuptools`` and contains all the configuration
settings required to build the package.

If you want to change the information or files to be included in the built
package then you should edit the ``setup.cfg`` file before running the command.

Since ``setuptools`` also reads information from ``MANIFEST.in`` to determine
which other files to include in the package so you should make sure that this
is configured the way you need it to be.

Once you're ready to build the package, run the following command from the
project's root directory::

  # from the project's root directory
  python setup.py sdist


This will output a ``.tar`` file containing the shippable package, ready to be
uploaded to your chosen PyPI repository (such as
`PyPI <https://pypi.python.org/pypi>`_ or a private artefact repository).

`Read the official Setuptools docs <https://setuptools.readthedocs.io/en/latest/>`_

Using pytest to test the application
====================================

Instead of using the built in ``unittest`` framework directly, most projects
use one of the popular testing frameworks as they make testing significantly
easier.

This project uses ``pytest`` for testing.

`Read more about pytest on pytest.org <http://docs.pytest.org/en/latest/>`_

Using travis-ci to provide automated testing for CI
===============================================

This project uses `travis-ci` to perform automated testing on all branches.

`Read more about travis-ci on travis-ci.org <https://docs.travis-ci.com>`_


*************
Configuration
*************

This project uses a ``config.yaml`` file for configuring the settings.
Copy  the ``config.yaml.example`` file and then update the values to the local
settings.

.. code-block::

  # from the project's root directory
  cp config.yaml.example config.yaml
  vi config.yaml

.. separate code and note elements with a comment

.. note::
  In most instances where you will be deploying to a Production environment
  you should probably separate out any sensitive information into environment
  variables and only use the ``config.yaml`` file for configuration options

*******
Testing
*******

This project uses ``pytest`` for testing. It is recommended to run the
project's tests immediately after installing and configuring the application.
This is particularly important before starting to develop new features, in
order to identify any existing test failures prior to you beginning to make
changes.

The standard ``pip install -r requirements.txt`` will have installed ``pytest``
so once installed you are ready to run the tests.

.. note::
  Please make sure that you have configured the application settings before
  running the tests.

.. code-block::

  # from the project's root directory
  pytest

************
Contributing
************

This project was started as a personal project to capture some best practices
for structuring Python applications. It is now being hosted on GitHub so that
others can view and use the application template.

To work on the source code, clone the project from GitHub:

.. code-block::

  # from the (parent) directory into which you wish to install the application
  git clone ssh://git@github.com/tomfitzherbert/pyexample.git
  cd pyexample/
  python3 -m venv ~/.virtualenvs/pyexample
  source ~/.virtualenvs/pyexample/bin/activate
  pip install --upgrade pip
  pip install -r requirements-dev.txt
  pip install -e . # required to install the application into site packages

This will have downloaded a copy of the project source code and
created a virtual environment called ``pyexample`` with the required
dependencies installed.

Please feel free to raise issues and pull requests if you think you can help
improve the project.

*********
Licensing
*********

The code in this project is licensed under the MIT license.

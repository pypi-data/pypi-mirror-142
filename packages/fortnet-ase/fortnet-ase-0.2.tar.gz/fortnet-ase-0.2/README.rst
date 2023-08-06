***********************************************************************
fortnet-ase: Interfacing Fortnet with the Atomic Simulation Environment
***********************************************************************

|license|
|latest version|
|doi|
|issues|

fortnet-ase provides an interface between the neural network implementation
`Fortnet <https://github.com/vanderhe/fortnet>`_ and the Atomic Simulation
Environment (`ASE <https://wiki.fysik.dtu.dk/ase/>`_). The calculator employs
Fortnet as a prediction engine for the total energy of a system as well as the
calculation of atomic forces, e.g. for geometry optimizations and molecular
dynamics.

|logo|

Installation
============

Please note, that this package has been tested for Python 3.X support. Its usage
additionally requires

- `Atomic Simulation Environment
  <https://wiki.fysik.dtu.dk/ase/install.html>`_ (`ase`)
- `Fortnet Python tools <https://github.com/vanderhe/fortnet-python>`_
  (`fortnet-python`)

as well as the `pytest` framework in order to run the regression tests.

Via the Python Package Index
----------------------------

First, make sure you have an up-to-date version of pip installed::

  python -m pip install --upgrade pip

The package can be downloaded and installed via pip into the active Python
interpreter (preferably using a virtual python environment) by ::

  pip install fortnet-ase

or into the user space issueing::

  pip install --user fortnet-ase

Locally from Source
-------------------

Alternatively, you can install it locally from source, i.e. from the root folder
of the project::

  python -m pip install .

Documentation
=============

|docs status|

Consult following resources for documentation:

* `Step-by-step instructions with selected examples (Fortnet Recipes)
  <https://fortnet.readthedocs.io/en/latest/interfaces/ase/index.html>`_

Contributing
============

New features, bug fixes, documentation, tutorial examples and code testing is
welcome during the ongoing fortnet-ase development!

The project is `hosted on github <https://github.com/vanderhe/fortnet-ase/>`_.
Please check `CONTRIBUTING.rst <CONTRIBUTING.rst>`_ for guide lines.

I am looking forward to your pull request!

License
=======

fortnet-ase is released under the BSD 2-clause license. See the included
`LICENSE <LICENSE>`_ file for the detailed licensing conditions.

.. |logo| image:: ./utils/art/logo.svg
    :alt: Fortnet logo
    :width: 90
    :target: https://github.com/vanderhe/fortnet/

.. |license| image:: https://img.shields.io/github/license/vanderhe/fortnet-ase
    :alt: BSD-2-Clause
    :scale: 100%
    :target: https://opensource.org/licenses/BSD-2-Clause

.. |latest version| image:: https://img.shields.io/github/v/release/vanderhe/fortnet-ase
    :target: https://github.com/vanderhe/fortnet-ase/releases/latest

.. |doi| image:: https://zenodo.org/badge/356394988.svg
   :target: https://zenodo.org/badge/latestdoi/356394988

.. |docs status| image:: https://readthedocs.org/projects/fortnet/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://fortnet-python.readthedocs.io/en/latest/

.. |issues| image:: https://img.shields.io/github/issues/vanderhe/fortnet-ase.svg
    :target: https://github.com/vanderhe/fortnet-ase/issues/

.. |build status| image:: https://img.shields.io/github/workflow/status/vanderhe/fortnet-ase/CI
    :target: https://github.com/vanderhe/fortnet-ase/actions/

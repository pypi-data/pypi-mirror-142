Kamzik3 is a modular and lightweight experiment control framework written in Python3.

It is focused on minimalist yet unified way to control and orchestrate wide range of
devices used in experimental setup.

It uses ZeroMQ to exchange messages between server and clients. Qt5 is used for the
graphical interface. Kamzik3 provides tools for logging, visualizing and evaluation
of experimental data. Users can create and execute custom macros and scans using the
built-in macro-server.

The experimental setup is defined in one configuration file written in YAML,
human-readable data serialization standard.

The framework can be downloaded from PyPI (https://pypi.org/project/kamzik3/).

Documentation
=============

The documentation is available at: https://cfel-sc-public.pages.desy.de/kamzik3/

Requirements
============

  * Python: 3.7 and higher

  **Python Modules: Backend**

  * numpy
  * pyzmq
  * pint
  * bidict
  * pyqt5
  * pyqtgraph
  * pyserial
  * oyaml
  * psutil
  * natsort
  * reportlab
  * pandas
  * tables

  **Python Modules: Optional**

  * pytango
  * pyopengl
  * sysutil
  * pydaqmx
  * pypiwin32
  * rocketchat-API
  * pytest
  * pytest-cov
  * pytest-lazy-fixture
  * pytest-mock

Changelog
=========

.. include:: HISTORY.rst
  :end-before: EOF

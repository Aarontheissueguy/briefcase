.. image:: https://beeware.org/project/projects/tools/briefcase/briefcase.png
   :width: 72px
   :target: https://beeware.org/briefcase

Briefcase
=========

.. image:: https://img.shields.io/pypi/pyversions/briefcase.svg
   :target: https://pypi.python.org/pypi/briefcase
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/v/briefcase.svg
   :target: https://pypi.python.org/pypi/briefcase
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/status/briefcase.svg
   :target: https://pypi.python.org/pypi/briefcase
   :alt: Maturity

.. image:: https://img.shields.io/pypi/l/briefcase.svg
   :target: https://github.com/beeware/briefcase/blob/main/LICENSE
   :alt: BSD License

.. image:: https://github.com/beeware/briefcase/workflows/CI/badge.svg?branch=main
   :target: https://github.com/beeware/briefcase/actions
   :alt: Build Status

.. image:: https://img.shields.io/discord/836455665257021440?label=Discord%20Chat&logo=discord&style=plastic
   :target: https://beeware.org/bee/chat/
   :alt: Discord server

Briefcase is a tool for converting a Python project into a standalone native
application. You can package projects for:

* Mac
* Windows
* Linux
* iPhone/iPad
* Android
* Web

Support for AppleTV, watchOS, and wearOS deployments is planned.

If you want to see Briefcase in action, try the `BeeWare tutorial
<https://beeware.readthedocs.io>`__. That tutorial walks you through the
process of creating and packaging a new application with Briefcase.

Installation
----------

To install briefcase in your project's virtual environment, run the following::

   $ python -m pip install briefcase

It is important that you use ``python -m pip``, rather than a bare ``pip``. Briefcase needs to ensure that it has an up-to-date version of ``pip`` and ``setuptools``, and a bare invocation of ``pip`` can’t self-update. If you want to know more, `Brett Cannon has a detailed blog post about the issue <https://snarky.ca/why-you-should-use-python-m-pip/>`__.

Documentation
-------------

Documentation for Briefcase can be found on `Read The Docs`_.

Community
---------

Briefcase is part of the `BeeWare suite`_. You can talk to the community through:

* `@beeware@fosstodon.org on Mastodon <https://fosstodon.org/@beeware>`__

* `Discord <https://beeware.org/bee/chat/>`__

* The Briefcase `Github Discussions forum <https://github.com/beeware/briefcase/discussions>`__

We foster a welcoming and respectful community as described in our
`BeeWare Community Code of Conduct`_.

Contributing
------------

If you experience problems with Briefcase, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: https://beeware.org
.. _Read The Docs: https://briefcase.readthedocs.io
.. _BeeWare Community Code of Conduct: https://beeware.org/community/behavior/
.. _log them on Github: https://github.com/beeware/briefcase/issues
.. _fork the code: https://github.com/beeware/briefcase
.. _submit a pull request: https://github.com/beeware/briefcase/pulls

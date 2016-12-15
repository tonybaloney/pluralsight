===============================
pluralsight
===============================

.. image:: https://img.shields.io/pypi/v/pluralsight.svg
        :target: https://pypi.python.org/pypi/pluralsight

.. image:: https://img.shields.io/travis/tonybaloney/pluralsight.svg
        :target: https://travis-ci.org/tonybaloney/pluralsight

.. image:: https://readthedocs.org/projects/pluralsight/badge/?version=latest
        :target: https://readthedocs.org/projects/pluralsight/?badge=latest
        :alt: Documentation Status


Pluralsight client library for API management

* Free software: Apache-2 license
* Documentation: https://pluralsight.readthedocs.org.

Features
--------

* Invitation management using the license API
* User management using the license API
* Team information

Usage
-----

.. code-block:: python

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    invites = client.invites.get_all_invites()
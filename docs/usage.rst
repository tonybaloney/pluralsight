=====
Usage
=====

Licensing
~~~~~~~~~

To use pluralsight in a project::

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    invites = client.invites.get_all_invites()
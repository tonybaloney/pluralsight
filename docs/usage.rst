=====
Usage
=====

Licensing
~~~~~~~~~

To use pluralsight in a project

.. code-block:: python

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    # invites
    invites = client.invites.get_all_invites()
    
    # users
    users = client.users.get_all_users()
    
    # teams
    teams = client.teams.get_all_teams()
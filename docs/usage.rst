=====
Usage
=====

Licensing
~~~~~~~~~

To use pluralsight in a project

.. code-block:: python
    :linenos:

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    # invites
    invites = client.invites.get_all_invites()
    
    # users
    users = client.users.get_all_users()
    
    # teams
    teams = client.teams.get_all_teams()

Invites
~~~~~~~

.. literalinclude:: ../examples/get_link_for_email.py
   :language: python
   :linenos:


.. literalinclude:: ../examples/unregistered_users.py
   :language: python
   :linenos:
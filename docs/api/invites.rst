==============
Invitation API
==============

The invitation API is exposed as a field within the LicensingApiClient class.

.. code-block:: python

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    invites = client.invites.get_all_invites()

.. autoclass:: pluralsight.licensing.invites.InvitesClient
    :members:


Invite Model
~~~~~~~~~~~~

.. autoclass:: pluralsight.models.invite.Invite
    :members:
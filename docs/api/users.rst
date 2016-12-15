===================
User Management API
===================

The user management API is exposed as a field within the LicensingApiClient class.

.. code-block:: python

    from pluralsight.licensing import LicensingAPIClient

    client = LicensingAPIClient(plan, api_key)
    
    users = client.users.get_all_users()


.. autoclass:: pluralsight.licensing.users.UsersClient
    :members:


User Model
~~~~~~~~~~~~

.. autoclass:: pluralsight.models.user.User
    :members:
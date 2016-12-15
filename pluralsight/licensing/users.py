# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import arrow
from pluralsight.models.user import User


class UsersClient(object):
    """
    Users API
    """
    def __init__(self, client):
        self.client = client

    def get_all_users(self, first_name=None, last_name=None, email=None,
                      note=None, team_id=None):
        """
        Get all users

        :param first_name: Filter by first name
        :type  first_name: ``str``

        :param last_name: Filter by last name
        :type  last_name: ``str``

        :param email: Filter by email
        :type  email: ``str``

        :param note: Filter by note
        :type  note: ``str``

        :param team_id: Filter by team ID
        :type  team_id: ``str``

        :return: A list of :class:`User`
        :rtype: ``list`` of :class:`User`
        """
        params = {}

        if first_name is not None:
            params['firstName'] = first_name
        if last_name is not None:
            params['lastName'] = last_name
        if email is not None:
            params['email'] = email
        if note is not None:
            params['note'] = note
        if team_id is not None:
            params['teamId'] = team_id

        users = self.client.get('users', params=params)
        return [self._to_user(i) for i in users['data']]

    def get_user(self, id):
        """
        Fetch a user by ID

        :param id: The identifier
        :type  id: ``str``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
        user = self.client.get('users/{0}'.format(id))
        return self._to_user(user['data'])

    def update_user(self, id, team_id, note):
        """
        Update a user

        :param id: The identifier
        :type  id: ``str``

        :param team_id: Team the user belongs to
        :type  team_id: ``str``

        :param note: Additional notes on the user
        :type  note: ``str``

        :return: An instance :class:`User`
        :rtype: :class:`User`
        """
        data = {
            'data': {
                'teamId': team_id,
                'note': note
            }
        }
        user = self.client.put('users/{0}'.format(id), data=data)
        return self._to_user(user['data'])

    def delete_user(self, id):
        """
        Delete an existing user

        :param id: The identifier
        :type  id: ``str``

        :rtype: None
        """
        self.client.delete('users/{0}'.format(id))

    def _to_user(self, data):
        return User(
            data['id'],
            data['teamId'],
            data['firstName'],
            data['lastName'],
            data['email'],
            data['note'],
            arrow.get(data['startDate'])
        )

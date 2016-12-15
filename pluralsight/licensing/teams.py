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

from pluralsight.models.team import Team


class TeamsClient(object):
    """
    Teams API
    """
    def __init__(self, client):
        self.client = client

    def get_all_teams(self, name=None):
        """
        Get all teams

        :param name: Filter by name
        :type  name: ``str``

        :return: A list of :class:`Team`
        :rtype: ``list`` of :class:`Team`
        """
        params = {}

        if name is not None:
            params['name'] = name

        teams = self.client.get('teams', params=params)
        return [self._to_team(i) for i in teams['data']]

    def get_team(self, id):
        """
        Fetch a team by ID

        :param id: The identifier
        :type  id: ``str``

        :return: An instance :class:`Team`
        :rtype: :class:`Team`
        """
        team = self.client.get('teams/{0}'.format(id))
        return self._to_team(team['data'])

    def _to_team(self, data):
        return Team(
            data['id'],
            data['name'],
        )

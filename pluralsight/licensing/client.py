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

import requests

from pluralsight.exceptions import PluralsightApiException
from .invites import InvitesClient
from .users import UsersClient
from .teams import TeamsClient

BASE_URL = "https://app.pluralsight.com/plans/api/license/v1/{0}"


class LicensingAPIClient(object):
    """
    The licensing API client
    """
    def __init__(self, plan, api_key):
        """
        Instantiate a new reports API client
        
        :param plan: The plan name
        :type  plan: ``str``
        
        :param api_key: The API token (from the pluralsight team)
        :type  api_key: ``str``
        """
        self._plan = plan
        self._api_key = api_key

        self.base_url = BASE_URL.format(plan)

        self.session = requests.Session()
        self.session.headers.update(
            {'Accept': 'application/json',
             'Authorization': "Token {0}".format(api_key)})

        self.invites = InvitesClient(self)
        self.users = UsersClient(self)
        self.teams = TeamsClient(self)

    def get(self, uri, params=None):
        try:
            result = self.session.get("{0}/{1}".format(self.base_url, uri),
                                      params=params)
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise PluralsightApiException(e)

    def post(self, uri):
        try:
            result = self.session.post("{0}/{1}".format(self.base_url, uri))
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise PluralsightApiException(e)

    def put(self, uri):
        try:
            result = self.session.put("{0}/{1}".format(self.base_url, uri))
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise PluralsightApiException(e)

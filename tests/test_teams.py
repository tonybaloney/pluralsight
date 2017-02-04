# -*- coding: utf-8 -*-
# Licensed to Anthony Shaw (anthonyshaw@apache.org) under one or more
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

from requests_staticmock import (Adapter,
                                 BaseMockClass,
                                 mock_session_with_class)
import json
from pluralsight.licensing.client import LicensingAPIClient

TEST_PLAN = 'test_teams'
TEST_API_KEY = 'api_key'
TEST_URL = 'https://app.pluralsight.com'


def test_get_all_teams():
    """
    Test that get all invites returns properly formatted models
    """
    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    teams = client.teams.get_all_teams()
    assert len(teams) == 2
    assert teams[0].id == '2b947975-482a-4791-aa40-e199b3ca8738'
    assert teams[0].name == 'FED'
    assert str(teams[0]) == "Team 'FED' (2b947975-482a-4791-aa40-e199b3ca8738)"


def test_get_teams_filter():
    """
    Test that get invites with filter does apply the right params
    """

    class TestMockClient(BaseMockClass):
        def _plans_api_license_v1_test_teams_teams(self, params, headers):
            if params['name'] == 'test':
                return json.dumps({'data': [{
                    "id": '2b947975-482a-4791-aa40-e199b3ca8738',
                    "name": 'test'
                  }]})

    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)

    with mock_session_with_class(client.session, TestMockClient,
                                 'https://app.pluralsight.com'):
        teams = client.teams.get_all_teams(name='test')
        assert len(teams) == 1
        assert teams[0].name == 'test'


def test_get_team():
    """
    Test that you can fetch a single team
    """
    client = LicensingAPIClient('test_team', TEST_API_KEY)

    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    team = client.teams.get_team("2b947975-482a-4791-aa40-e199b3ca8738")
    assert team.id == "2b947975-482a-4791-aa40-e199b3ca8738"
    assert team.name == 'FED'

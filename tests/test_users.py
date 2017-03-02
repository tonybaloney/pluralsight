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

TEST_PLAN = 'test_users'
TEST_API_KEY = 'api_key'
TEST_URL = 'https://app.pluralsight.com'


def test_get_all_users():
    """
    Test that get all users returns properly formatted models
    """
    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    users = client.users.get_all_users()
    assert len(users) == 2
    assert users[0].id == "0bbdccac-dad1-4488-a69d-2ea78bf43280"
    assert users[0].team_id == "2b947975-482a-4791-aa40-e199b3ca8738"
    assert users[0].first_name == "first-25"
    assert users[0].last_name == "last-25"
    assert users[0].email == "email-25+9040@email.com"
    assert users[0].note == 'test note'
    assert users[0].start_date.timestamp == 1463020267
    assert str(users[0]) == "User 'first-25 last-25' email-25+9040@email.com " \
        "(0bbdccac-dad1-4488-a69d-2ea78bf43280)"


def test_get_users_filter():
    """
    Test that get users with filter does apply the right params
    """
    _first_name = 'fred'
    _last_name = 'flintstone'
    _email = 'fred@flintstone.com'
    _note = 'yabba dabba doo'
    _team_id = '2b947975-482a-4791-aa40-e199b3ca8738'

    class TestMockClient(BaseMockClass):
        def _plans_api_license_v1_test_users_users(self, params, headers):
            assert params['firstName'] == _first_name
            assert params['lastName'] == _last_name
            assert params['email'] == _email
            assert params['note'] == _note
            assert params['teamId'] == _team_id

            return json.dumps({'data': [{
                    "id": "0bbdccac-dad1-4488-a69d-2ea78bf43280",
                    "teamId": "2b947975-482a-4791-aa40-e199b3ca8738",
                    "firstName": "first-25",
                    "lastName": "last-25",
                    "email": "email-25+9040@email.com",
                    "note": "test note",
                    "startDate": "2016-05-12T02:31:07.233+00:00"
                  }]})

    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)

    with mock_session_with_class(client.session, TestMockClient,
                                 'https://app.pluralsight.com'):
        users = client.users.get_all_users(first_name=_first_name,
                                           last_name=_last_name,
                                           email=_email,
                                           note=_note,
                                           team_id=_team_id)
        assert len(users) == 1
        assert users[0].id == "0bbdccac-dad1-4488-a69d-2ea78bf43280"
        assert users[0].team_id == "2b947975-482a-4791-aa40-e199b3ca8738"
        assert users[0].first_name == "first-25"
        assert users[0].last_name == "last-25"
        assert users[0].email == "email-25+9040@email.com"
        assert users[0].note == 'test note'
        assert users[0].start_date.timestamp == 1463020267


def test_get_user():
    """
    Test that you can fetch a single user
    """
    client = LicensingAPIClient('test_user', TEST_API_KEY)

    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    user = client.users.get_user("3d4a29f7-aedc-46b8-bada-f84d04f98679")
    assert user.id == "3d4a29f7-aedc-46b8-bada-f84d04f98679"


def test_update_user():
    """
    Test that users can be updated
    """
    client = LicensingAPIClient('test_user', TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)

    client.users.update_user(id="3d4a29f7-aedc-46b8-bada-f84d04f98679",
                             team_id="1234512-aedc-46b8-bada-f84d04f98679",
                             note="test note")
    assert True


def test_delete_user():
    """
    Test that users can be deleted
    """
    client = LicensingAPIClient('test_user', TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    client.users.delete_user("3d4a29f7-aedc-46b8-bada-f84d04f98679")

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

TEST_PLAN = 'test_invites'
TEST_API_KEY = 'api_key'
TEST_URL = 'https://app.pluralsight.com'


def test_get_all_invites():
    """
    Test that get all invites returns properly formatted models
    """
    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    invites = client.invites.get_all_invites()
    assert len(invites) == 2
    assert invites[0].id == "bc30c000-eeee-11e6-8088-111111111111"
    assert invites[0].email == 'a.guy@test.com'
    assert invites[0].team_id is None
    assert invites[0].note == 'Services'
    assert invites[0].send_date.timestamp == 1483488000
    assert invites[0].expires_on.timestamp == 1487376000
    assert str(invites[0]) == "Invite to a.guy@test.com (Services) " \
        "with ID: bc30c000-eeee-11e6-8088-111111111111"
    assert 'https://app.pluralsight.com/' in invites[0].generate_url('test')


def test_get_invites_filter():
    """
    Test that get invites with filter does apply the right params
    """
    _test_email = 'test.email@domain.com'
    _test_note = 'test note'
    _test_team = 'team 1'

    class TestMockClient(BaseMockClass):
        def _plans_api_license_v1_test_invites_invites(self, params, headers):
            if params['email'] == _test_email and \
                params['note'] == _test_note and \
                    params['teamId'] == _test_team:
                return json.dumps({'data': [{
                    "id": "bc30c000-dddd-11e6-80c5-46f6aaaaaaaa",
                    "email": _test_email,
                    "teamId": None,
                    "note": "Professional Services",
                    "sendDate": "2017-01-04T00:00:00+00:00",
                    "expiresOn": "2017-02-18T00:00:00+00:00"
                  }]})

    client = LicensingAPIClient(TEST_PLAN, TEST_API_KEY)

    with mock_session_with_class(client.session, TestMockClient,
                                 'https://app.pluralsight.com'):
        invites = client.invites.get_invites(email=_test_email,
                                             note=_test_note,
                                             team_id=_test_team)
        assert len(invites) == 1


def test_get_invite():
    """
    Test that get all invites returns properly formatted models
    """
    client = LicensingAPIClient('test_invite', TEST_API_KEY)

    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    invite = client.invites.get_invite("bc30c000-eeee-11e6-8088-111111111111")
    assert invite.id == "bc30c000-eeee-11e6-8088-111111111111"
    assert invite.email == 'a.guy@test.com'
    assert invite.team_id is None
    assert invite.note == 'Services'
    assert invite.send_date.timestamp == 1483488000
    assert invite.expires_on.timestamp == 1487376000


def test_create_invite():
    """
    Test that invites can be issued
    """
    client = LicensingAPIClient('test_create_invite', TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)

    invite = client.invites.invite_user('test@test.com', None, "test note")
    assert invite.id == "bc30c000-eeee-11e6-8088-111111111111"
    assert invite.email == 'a.guy@test.com'
    assert invite.team_id is None
    assert invite.note == 'Services'
    assert invite.send_date.timestamp == 1483488000
    assert invite.expires_on.timestamp == 1487376000


def test_update_invite():
    """
    Test that invites can be updated
    """
    client = LicensingAPIClient('test_invite', TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)

    client.invites.update_invite("bc30c000-eeee-11e6-8088-111111111111",
                                 "test note")
    assert True

def test_cancel_invite():
    """
    Test that invites can be updated
    """
    client = LicensingAPIClient('test_invite', TEST_API_KEY)
    special_adapter = Adapter('tests/fixtures')
    client.session.mount('https://app.pluralsight.com', special_adapter)
    client.invites.cancel_invite("bc30c000-eeee-11e6-8088-111111111111")

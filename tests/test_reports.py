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
from requests_staticmock.responses import StaticResponseFactory
from six import b
import csv
import pytest
from pluralsight.exceptions import PluralsightApiException
from pluralsight.reports.client import ReportsAPIClient, BASE_URL

TEST_PLAN = 'test-plan'
TEST_API_KEY = 'api_key'
TEST_URL = 'https://app.pluralsight.com'


client = ReportsAPIClient(TEST_PLAN, TEST_API_KEY)
special_adapter = Adapter('tests/fixtures')
client.session.mount('https://app.pluralsight.com', special_adapter)


def test_base_url():
    assert BASE_URL in client.base_url


def test_download_user_report():
    report_name = client.download_user_report(TEST_PLAN, '')
    with open(report_name, 'r') as f:
        reader = csv.DictReader(f)
        data = [d for d in reader]
        assert data[0]['UserId'] == '12919ae2-c23f-480a-96a8-1534293b0bbe'
        assert data[0]['FirstName'] == 'Sandeep'
        assert data[1]['FirstName'] == 'Imranullah'


def test_download_course_completion_report():
    report_name = client.download_course_completion_report(TEST_PLAN, '',
                                                           start_date='2016-04-02',
                                                           end_date='2016-05-02')
    with open(report_name, 'r') as f:
        reader = csv.DictReader(f)
        data = [d for d in reader]
        assert data[0]['FirstName'] == 'Jason'
        assert data[1]['FirstName'] == 'Alex'


def test_download_course_usage_report():
    report_name = client.download_course_usage_report(TEST_PLAN, '',
                                                      start_date='2016-04-02',
                                                      end_date='2016-05-02')
    with open(report_name, 'r') as f:
        reader = csv.DictReader(f)
        data = [d for d in reader]
        assert data[0]['FirstName'] == 'Sam'
        assert data[1]['FirstName'] == 'Alexey'


def test_get_bad_request():
    class TestMockClient(BaseMockClass):
        def _plans_api_reports_v1_users_test_plan(self, request, method):
            return StaticResponseFactory.BadResponse(
                request=request,
                body=b('bad request'),
                status_code=500)
    with mock_session_with_class(client.session, TestMockClient, TEST_URL):
        with pytest.raises(PluralsightApiException):
            client.download_user_report(TEST_PLAN, '')

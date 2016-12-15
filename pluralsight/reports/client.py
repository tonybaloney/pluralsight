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

import os
import requests

from pluralsight.exceptions import PluralsightApiException

BASE_URL = "https://app.pluralsight.com/plans/api/reports/v1/"


class ReportsAPIClient(object):
    """
    Reports API client
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

        self.base_url = BASE_URL

        self.session = requests.Session()
        self.session.headers.update(
            {'Accept': 'application/json',
             'Authorization': "Token {0}".format(api_key)})

    def download_user_report(self, plan, path):
        """
        Download the user report and store in a file

        :param plan: The plan name
        :type  plan: ``str``

        :param path: Path to the downloaded CSV
        :type  path: ``str``
        """
        self._download_file("users/{0}".format(plan), path)

    def download_course_completion_report(self, plan, path,
                                          start_date=None, end_date=None):
        """
        Download the course completion report and store in a file

        :param plan: The plan name
        :type  plan: ``str``

        :param path: Path to the downloaded CSV
        :type  path: ``str``

        :param start_date: (optional) Start date in format YYYY-MM-DD
        :type  start_date: ``str``

        :param end_date: (optional) End date in format YYYY-MM-DD
        :type  end_date: ``str``
        """
        params = {}

        if start_date is not None:
            params['startDate'] = start_date
        if end_date is not None:
            params['endDate'] = end_date

        self._download_file("course-completion/{0}".format(plan), path, params)

    def download_course_usage_report(self, plan, path,
                                     start_date=None, end_date=None):
        """
        Download the course usage report and store in a file

        :param plan: The plan name
        :type  plan: ``str``

        :param path: Path to the downloaded CSV
        :type  path: ``str``

        :param start_date: (optional) Start date in format YYYY-MM-DD
        :type  start_date: ``str``

        :param end_date: (optional) End date in format YYYY-MM-DD
        :type  end_date: ``str``
        """
        params = {}

        if start_date is not None:
            params['startDate'] = start_date
        if end_date is not None:
            params['endDate'] = end_date

        self._download_file("course-usage/{0}".format(plan), path, params)

    def _download_file(self, url, path, params=None):
        local_filename = url.split('/')[-1]
        try:
            r = self.session.get("{0}{1}".format(self.base_url, url),
                                 stream=True, params=params)
            r.raise_for_status()

            with open(os.path.join(path, local_filename), 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            return local_filename
        except requests.HTTPError as e:
            raise PluralsightApiException(e)

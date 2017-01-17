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

from six.moves.urllib.parse import quote, quote_plus


class Invite(object):
    def __init__(self,
                 id,
                 email,
                 team_id,
                 note,
                 send_date,
                 expires_on):
        self.id = id
        self.email = email
        self.team_id = team_id
        self.note = note
        self.send_date = send_date
        self.expires_on = expires_on

    def generate_url(self, plan):
        _redirect_url = 'https://app.pluralsight.com/plans-data/invites/{0}/{1}'.format(
            plan,
            self.id
        )
        _base_url = 'https://app.pluralsight.com/id/createaccount/business' \
            '?firstName={0}&lastName={1}&companyEmail={2}&redirectTo={3}'.format(
            '',
            '',
            quote(self.email),
            quote_plus(_redirect_url)
        )
        return _base_url

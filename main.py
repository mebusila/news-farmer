#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
from models import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            limit = int(self.request.get('limit'))
        except :
            limit = 10

        try:
            page = int(self.request.get('page'))
        except:
            page = 0

        q = Item.all()
        q.order('-created')
        items = q.fetch(limit)

        self.response.headers['Content-Type'] = 'application/json'
        data = {
            'total' : q.count(),
            'limit' : limit,
            'page'  : page,
            'query' : '',
            'items' : [item.to_dict() for item in items]
        }
        self.response.out.write(
            json.dumps(
                data
            )
        )

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)

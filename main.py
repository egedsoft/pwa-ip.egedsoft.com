# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):
    def html_out(self,html,template_values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(template_values)) 
        
    def index(self):
        ip = self.request.remote_addr
        template_values = {'ip':ip}
        self.html_out('index.html',template_values)


    def head(self):
        
        self.html_out('head.html')

    def top(self):
        self.response.headers['Content-Type'] = "text/html; charset=utf-8"
        self.html_out('top.html')
        self.head()  
        self.index()      

    def get(self):
        self.top()






app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
import webapp2
import logging
import urllib2, urllib

from django.template import loader

from google.appengine.api import memcache
from google.appengine.api import urlfetch

from handlers.index import WebRequestHandler 
import templates.endpoint_template_values as values

auth_url = 'https://haggle-test1.appspot.com/oauth2/authorize?'
token_url = 'https://haggle-test1.appspot.com/oauth2/token?'

auth_params = {
        'client_id': '35a4d8829ee54b32943550a0fa507be1',
        'client_secret': '9b3c12828fd5424da936d482406ee1fc',
        'type': 'code'
        }

token_params = {
        'client_id': '35a4d8829ee54b32943550a0fa507be1',
        'client_secret': '9b3c12828fd5424da936d482406ee1fc',
        'grant_type': 'authorization_code'
        }

class EndpointsHandler(WebRequestHandler):
    def get(self):
        path = 'endpoints.html'
        self.response.out.write(self.get_rendered_html(path, None))
        
class EndpointRenderHandler(WebRequestHandler):
    def get(self):
        property = self.request.get('property')
        template_values = values.TEMPLATE_VALUES[property]
        template_values["token"]="asdsd"
        path = 'endpoint.html'
        self.response.out.write(self.get_rendered_html(path, template_values))
                
class FetchTokenHandler(WebRequestHandler):
    def get(self):
        url = auth_url + urllib.urlencode(auth_params)
        self.redirect(url)

class CallbackHandler(WebRequestHandler):
    def get(self):
        code = self.request.get('code')
        token_params.update({ 'code': code })
        url = token_url + urllib.urlencode(token_params)
        token = urlfetch.fetch(url).content
        self.response.out.write(token)

app = webapp2.WSGIApplication([('/endpoints', EndpointsHandler),
   ('/endpoints/render', EndpointRenderHandler), 
   ('/fetch_token', FetchTokenHandler),
   ('/callback', CallbackHandler)
   ])

import webapp2
import logging
from django.template import loader

from handlers.index import WebRequestHandler 
from templates.endpoint_template_values import TEMPLATE_VALUES

class EndpointsHandler(WebRequestHandler):
	def get(self):
		path = 'endpoints.html'
		self.response.out.write(self.get_rendered_html(path, dict()))
        
class EndpointRenderHandler(WebRequestHandler):
    def get(self):
        property = self.request.get('property')
        template_values = TEMPLATE_VALUES[property]
        path = 'endpoint.html'
        self.response.out.write(self.get_rendered_html(path, template_values))
                
app = webapp2.WSGIApplication([('/endpoints', EndpointsHandler),
   ('/endpoints/render', EndpointRenderHandler), 
   ])

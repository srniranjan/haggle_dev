import webapp2
import logging
from django.template import loader

class WebRequestHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))
        
    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class DiscountsMap(WebRequestHandler):
	def get(self):
		path = 'discounts_map.html'
		self.response.out.write(self.get_rendered_html(path,dict()))



app = webapp2.WSGIApplication([
	('/api/discount_map', DiscountsMap),
	])

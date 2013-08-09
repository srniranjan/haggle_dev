import webapp2
import logging
from django.template import loader

class WebRequestHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))
        
    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class APIUsers(WebRequestHandler):
	def get(self):
		path = 'users.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class APIVendors(WebRequestHandler):
	def get(self):
		path = 'vendors.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class APIAggregateCampaigns(WebRequestHandler):
	def get(self):
		path = 'aggregate_campaigns.html'
		self.response.out.write(self.get_rendered_html(path, dict()))
		
class APIIndividualCampaigns(WebRequestHandler):
	def get(self):
		path = 'individual_campaigns.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class APIAggregateDeals(WebRequestHandler):
	def get(self):
		path = 'aggregate_deals.html'
		self.response.out.write(self.get_rendered_html(path, dict()))
		
class APIIndividualDeals(WebRequestHandler):
	def get(self):
		path = 'individual_deals.html'
		self.response.out.write(self.get_rendered_html(path, dict()))



app = webapp2.WSGIApplication([
	('/api/users', APIUsers),
	('/api/vendors', APIVendors),
	('/api/aggregate_campaigns', APIAggregateCampaigns),
	('/api/individual_campaigns', APIIndividualCampaigns),
	('/api/aggregate_deals', APIAggregateDeals),
	('/api/individual_deals', APIIndividualDeals),
	])

import webapp2
import logging
from django.template import loader

from handlers.index import WebRequestHandler 

class Endpoints(WebRequestHandler):
	def get(self):
		path = 'endpoints.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class DiscountTrends(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_campaigns/discount_trends.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class ScorePreferenceTrends(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_campaigns/score_preference_trends.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class BidsTrends(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_deals/bids_trends.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class UserTrends(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_deals/user_trends.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class TimeTrends(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_deals/time_trends.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

class AverageSpending(WebRequestHandler):
	def get(self):
		path = 'endpoints/aggregate_deals/average_spending.html'
		self.response.out.write(self.get_rendered_html(path, dict()))

app = webapp2.WSGIApplication([('/endpoints', Endpoints),
   ('/endpoints/aggregate_campaigns/discount_trends', DiscountTrends), 
   ('/endpoints/aggregate_campaigns/score_preference_trends', ScorePreferenceTrends),
   ('/endpoints/aggregate_deals/bids_trends', BidsTrends),
   ('/endpoints/aggregate_deals/user_trends', UserTrends),
   ('/endpoints/aggregate_deals/time_trends', TimeTrends), 
   ('/endpoints/aggregate_deals/average_spending', AverageSpending)
   ])

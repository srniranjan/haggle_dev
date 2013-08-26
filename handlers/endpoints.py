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

app = webapp2.WSGIApplication([('/endpoints', Endpoints),
   ('/endpoints/aggregate_campaigns/discount_trends', DiscountTrends), 
   ('/endpoints/aggregate_campaigns/score_preference_trends', ScorePreferenceTrends)
   #('/aggregate_deals/bids_trends', BidsTrends),
   #('/aggregate_deals/user_trends', UserTrends), 
   #('/aggregate_deals/time_trends', TimeTrends), 
   #('/aggregate_deals/average_spending', AverageSpending)
   ])

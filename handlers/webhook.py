import json
import webapp2
import logging
import urllib
import base64
from customers import customers_dict
from handlers import RequestHandler
from google.appengine.ext import db
from google.appengine.api import urlfetch

elastic_url = 'https://38d28feb4cb392ef7ccce4ba36eabad7.us-east-1.aws.found.io:9243/'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic " + base64.encodestring("admin:00ein9q2exda7xhoiw").replace('\n', '')
}

def get_context(context_name, contexts):
    for context in contexts:
        if context['name'] == context_name:
            return context
    return None

class WebhookHandler(RequestHandler):
    def post(self):
        resp = {}
        logging.info(self.request)
        if self['botID'] == '11321' and self['moduleID'] == '147610':
            address = self['reply']
            logging.info(address)
            customer_name = 'a Sunoco Gas Station'
            if address in customers_dict:
                customer_name = customers_dict[address]
            logging.info(customer_name)
            resp = {
                "customer_address": address,
                "customer_name": customer_name
            }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(resp))

app = webapp2.WSGIApplication([
    ('/webhook', WebhookHandler)
])

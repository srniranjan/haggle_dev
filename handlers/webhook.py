import json
import webapp2
import logging
import urllib
import base64
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
        response = json.loads(self.request.body)['result']
        print(response)
        displayText = ''
        print(response)
        if response['action'] == 'determine.customer':
            context = get_context('welcome-context', response['contexts'])
            vertical = context['parameters']['vertical']
            if vertical == 'Gas Station':
                displayText = 'Thanks %s. I can help you diagnose the problem in your %s. I need some information to help you diagnose the issue. Can I have your customer ID?' % (context['parameters']['userName'], vertical)
            else:
                displayText = 'Thanks %s. I can help you diagnose the problem in your %s. Can you describe the issue to me?' % (context['parameters']['userName'], vertical)
        elif response['action'] == 'determine.customer':
            context = get_context('site-context', response['contexts'])
            customer = context['parameters']['CustomerID']
            location = context['parameters']['LocationID']
            customerID = customer + ' :: ' + location
            if customerID == '105892 :: 1':
                displayText = 'Thanks for the info, looks like you have Gilbarco dispensers on site. What seems to be the problem?'
            else:
                displayText = "Thanks for the info, I don't have your equipment at site on record. Can you please tell me what type of dispensers you have?"
        resp = {
            "speech": displayText,
            "displayText": displayText,
            "data": {},
            "contextOut": [],
            "source": "Pirates ML"
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(resp))

app = webapp2.WSGIApplication([
    ('/webhook', WebhookHandler)
])

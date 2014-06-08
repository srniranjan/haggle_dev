import webapp2
from handlers.web.web_request_handler import WebRequestHandler
from google.appengine.api import urlfetch

URL = 'https://haggle-test1.appspot.com/api/analytics/'

class HomepageHandler(WebRequestHandler):
    def get(self):
        path = 'index.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Tutorial(WebRequestHandler):
    def get(self):
        path = 'tutorial.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class RestAPI(WebRequestHandler):
    def get(self):
        path = 'rest_api.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class AppRedirect(WebRequestHandler):
    def get(self):
        path = 'iphone_app.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Contact(WebRequestHandler):
    def get(self):
        path = 'contact.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Documentation(WebRequestHandler):
    def get(self):
        path = 'integrate_docs.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class ServerFetchHandler(webapp2.RequestHandler):
    def post(self):
        data = self.request.get('data')
        endpoint = self.request.get('endpoint')
        token = self.request.get('token')
        url = URL + endpoint + '?token='+token+'&'+data

        response = urlfetch.fetch(url).content
        self.response.out.write(response)

class Landing(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

app = webapp2.WSGIApplication([('/', HomepageHandler),
                               ('/tutorial', Tutorial),
                               ('/documentation', Documentation),
                               ('/rest_api', RestAPI),
                               ('/iphone_app', AppRedirect),
                               ('/fetch_from_api_server', ServerFetchHandler),
                               ('/contact', Contact),
                               ('/landing', Landing)
])

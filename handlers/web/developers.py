import webapp2
from handlers.web.web_request_handler import WebRequestHandler

class DefaultHandler(WebRequestHandler):
    def get(self):
        self.redirect('/developers/api-docs')

class ApiDocumentation(WebRequestHandler):
    def get(self):
        path = 'developers/developers_api_docs.html'
        self.response.out.write(self.get_rendered_html(path))

class OauthIntegrate(WebRequestHandler):
    def get(self):
        path = 'developers/developers_oauth_integrate.html'
        self.response.out.write(self.get_rendered_html(path))

app = webapp2.WSGIApplication([('/developers/api-docs', ApiDocumentation),
                               ('/developers/oauth-integrate', OauthIntegrate),
                               ('/developers', DefaultHandler)
   ])
import webapp2
from handlers.web.web_request_handler import WebRequestHandler

class CaseStudies(WebRequestHandler):
    def get(self):
        path = 'integrate/integrate_case_studies.html'
        self.response.out.write(self.get_rendered_html(path))

class iOSHandler(WebRequestHandler):
    def get(self):
        path = 'integrate/integrate_ios_sdk.html'
        self.response.out.write(self.get_rendered_html(path))

class AndroidHandler(WebRequestHandler):
    def get(self):
        path = 'integrate/integrate_android_sdk.html'
        self.response.out.write(self.get_rendered_html(path))

class ApiSnippetHandler(WebRequestHandler):
    def get(self):
        path = 'integrate/integrate_api_snippet.html'
        self.response.out.write(self.get_rendered_html(path))

app = webapp2.WSGIApplication([('/integrate/case_studies', CaseStudies),
                               ('/integrate/ios', iOSHandler),
                               ('/integrate/android', AndroidHandler),
                               ('/integrate/api-snippet', ApiSnippetHandler),
                               ('/integrate', CaseStudies)
   ])
import third_party_libs
import webapp2

from util import http_util


APP_JSON = "application/json"

class RequestHandlerMixin(object):
    def write(self,text=None, status=None, content_type = None):
        http_util.write(self.response, text, status, content_type)

    def set_status(self,value):
        self.response.set_status(value)

    def __getitem__(self, name):
        return self.request.get(name)

    def get_all(self, name):
        return self.request.get_all(name)
        
class RequestHandler(webapp2.RequestHandler, RequestHandlerMixin): pass


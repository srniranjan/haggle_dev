import webapp2
import json
from django.template import loader
from handlers import RequestHandler
from google.appengine.api import urlfetch
from platforms_graphs.populate import get_graph_view
import logging
import datetime
from pytz import timezone

URL = 'https://haggle-test1.appspot.com/api/analytics/'

class WebRequestHandler(RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))

    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class HomepageHandler(WebRequestHandler):
    def get(self):
        path = 'index.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Overview(WebRequestHandler):
    def get(self):
        path = 'integrate_code.html'
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
        url = URL + endpoint + '?' + data
        response = urlfetch.fetch(url).content
        self.response.out.write(response)

class CaseStudies(WebRequestHandler):
    def get(self):
        path = 'integrate_case-studies.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Landing(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        self.response.out.write(self.get_rendered_html(path, dict()))

class Marketers(WebRequestHandler):
    def get(self):
        path = 'marketers.html'
        template_values = {'graphs':[
            {'id':'dollars-spent',
             'dimension_ids':'1, 3, 4',
             'model':'Deal',
             'title':'Dollars Spent',
             'graph_model':'LineGraphModelBuilder',
             'graph_view':'LineGraphView'}
        ]}
        self.response.out.write(self.get_rendered_html(path, template_values))


def get_filters_set(filters):
    filters_set = []
    filters_id_set = []

    for (k, v) in filters.iteritems():
        id = k[0]
        name = k[1]
        values = [value for value in v ]
        filter = {}
        filter['id'] = id
        filter['name'] = name
        filter['options'] = []
        option = {}
        option['name'] = '--SELECT--'
        option['value'] = ''
        filter['options'].append(option)
        for value in values:
            option = {}
            if id == 0:
                eastern = timezone('US/Eastern')
                option['name'] = datetime.datetime.fromtimestamp(float(value), eastern)
            else:
                option['name'] = value
            option['value'] = value
            filter['options'].append(option)
        filters_id_set.append(id)
        filters_set.append(filter)

    return filters_set, filters_id_set

class MarketersOptions(WebRequestHandler):
    def post(self):
        graph_id = self['graph_id']
        model = self['model']
        dimension_ids = self['dimensions']
        graph_model = self['graph_model']
        graph_view = self['graph_view']

        content = self.get_content(model, dimension_ids, graph_model, graph_view)
        self.response.headers['Content-Type'] = 'application/json'
        self.write(
            json.dumps(
                {'dimensions':self.get_rendered_html('marketers/graphs/dimensions_area.html',
                                {'dimensions' : content['dimensions'], 'graph_id' : graph_id}),
                 'filters':self.get_rendered_html('marketers/graphs/filters_area.html',
                                                 {'filters_set' : content['filters_set'], 'filters_id_set' : content['filters_id_set'], 'graph_id' : graph_id}),
                 'graph_id':graph_id
                }))

    def get_content(self, model, dimension_ids, graph_model, graph_view):
        graph_view = get_graph_view(dimension_ids, model, graph_model, graph_view)
        return graph_view.get_dimension()

app = webapp2.WSGIApplication([('/', HomepageHandler),
                               ('/overview', Overview),
                               ('/tutorial', Tutorial),
                               ('/documentation', Documentation),
                               ('/rest_api', RestAPI),
                               ('/iphone_app', AppRedirect),
                               ('/fetch_from_api_server', ServerFetchHandler),
                               ('/contact', Contact),
                               ('/case_studies', CaseStudies),
                               ('/landing', Landing),
                               ('/marketers', Marketers),
                               ('/marketers/options', MarketersOptions)
])

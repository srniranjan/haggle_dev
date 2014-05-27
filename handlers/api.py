import json
import webapp2
import logging
from handlers import RequestHandler
from django.template import loader
from platforms_graphs.populate import get_graph_view
from platforms_graphs.graph_mappings import graphs
from platforms_graphs.populate import get_graph_view

class WebRequestHandler(webapp2.RequestHandler):
    def render_template(self, template_name, template_values = None):
        self.response.out.write(self.get_rendered_html(template_name, template_values))

    def get_rendered_html(self, template_name, template_values = None):
        return loader.render_to_string(template_name, template_values)

class DiscountsMap(WebRequestHandler):
    def get(self):
        path = 'discounts_map.html'
        self.response.out.write(self.get_rendered_html(path,dict()))

class ChartDataHandler(RequestHandler):
    def get_filters(self, filters_str):
        params_sep = ',,,,'
        val_sep = '::::'
        filter_params = filters_str.strip().split(params_sep)
        return [(param.split(val_sep)[0], param.split(val_sep)[1]) for param in filter_params if len(param) > 0]

    def post(self):
        chart_name = self['id']
        filters = []
        if len(self['filters']) > 0:
            filters = self.get_filters(self['filters'])
        curr_graph = graphs[chart_name]
        graph_view = get_graph_view(curr_graph)
        chart_data_json = {'graph_id':chart_name,
                           'chart_data':graph_view.translate_to_json(filters),
                           'chart_type':curr_graph['graph_view']}
        self.write(json.dumps(chart_data_json))

app = webapp2.WSGIApplication([
    ('/api/discount_map', DiscountsMap),
    ('/api/marketers', ChartDataHandler)
])

import json
import webapp2
import logging
from handlers import RequestHandler
from django.template import loader
from platforms_graphs.populate import get_graph_view
from platforms_graphs.graph_mappings import graphs
from platforms_graphs.populate import get_graph_view
from platforms_graphs.graph_mappings import view_to_graphmodel_mapping, model_list

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
        graph_type = self['graph_type']
        model_type = self['model_type']
        filters = []
        filter_ids = ''
        if len(self['filters']) > 0:
            filters = self.get_filters(self['filters'])
            count = 0
            for t in filters:
                count += 1
                filter_ids=filter_ids+t[0]
                if count < len(filters):
                    filter_ids += ','
        dimensions = self['dimensions']
        model = model_list[model_type]
        graph_model = view_to_graphmodel_mapping[graph_type]
        curr_graph = {'model':model,'graph_model':graph_model,'dimension_ids':dimensions,'filter_ids':filter_ids,'graph_view':graph_type}
        graph_view = get_graph_view(curr_graph)
        chart_data_json = {'chart_data':graph_view.translate_to_json(filters),
                           'chart_type':curr_graph['graph_view']}
        self.write(json.dumps(chart_data_json))

app = webapp2.WSGIApplication([
    ('/api/discount_map', DiscountsMap),
    ('/api/marketers', ChartDataHandler)
])

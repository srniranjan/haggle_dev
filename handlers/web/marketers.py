import webapp2
import json
from handlers.web.web_request_handler import WebRequestHandler
from platforms_graphs.graph_mappings import view_to_graphmodel_mapping, model_list, time_strategy_list
from platforms_graphs.util import get_class
from platforms_graphs.model_factory import get_model_objs_for
from platforms_graphs.time_strategies import time_horizon

class Spending(WebRequestHandler):
    def get(self):
        path = 'marketers/marketers_spending.html'
        self.response.out.write(self.get_rendered_html(path))

class Social(WebRequestHandler):
    def get(self):
        path = 'marketers/marketers_social.html'
        self.response.out.write(self.get_rendered_html(path))

class Custom(WebRequestHandler):
    def get(self):
        path = 'marketers/marketers_custom.html'
        self.response.out.write(self.get_rendered_html(path))

class MarketersOptions(WebRequestHandler):
    def post(self):
        pass

class GraphOptions(WebRequestHandler):
    def get(self):
        req_type = self['req_type']
        options = self.get_options_for(req_type)
        self.write(json.dumps(options))

    def get_options_for(self, req_type):
        options = None
        if req_type == 'graph_types':
            options = [graph_type for graph_type in view_to_graphmodel_mapping]
            html = self.get_rendered_html('marketers/graphs/graph_types_area.html', {'types' : options})
        elif req_type == 'models':
            options = [model for model in model_list]
            html = self.get_rendered_html('marketers/graphs/models_area.html', {'types' : options})
        elif req_type == 'dimensions':
            model = model_list[self['model']]
            model_objs = get_model_objs_for(model)
            graph_type = self['graph_type']
            graph_model_name = view_to_graphmodel_mapping[graph_type]
            graph_model_obj = get_class(graph_model_name)()
            name, params = graph_model_obj.get_dimensions_html_for(get_class(model), model_objs)
            html = self.get_rendered_html(name, params)
        return {req_type : html}

class TimeDataHandler(WebRequestHandler):
    def get(self):
        values = self['vals'].split(',')
        strategy = time_strategy_list[self['strategy']] if self['strategy'] else time_horizon
        processed_vals = set()
        for val in values:
            if val:
                times = strategy(val)
                for time in times:
                    processed_vals.add(time)
        params = {'values' : processed_vals }
        html = self.get_rendered_html('marketers/graphs/dimension_area_templates/time_vals.html', params)
        self.write(json.dumps(html))

app = webapp2.WSGIApplication([('/marketers/spending', Spending),
                               ('/marketers/social', Social),
                               ('/marketers/custom', Custom),
                               ('/marketers', Spending),
                               ('/marketers/options', MarketersOptions),
                               ('/marketers/graph_options',GraphOptions),
                               ('/marketers/time', TimeDataHandler)
])
import json
import webapp2
import logging
from handlers import RequestHandler
from django.template import loader
from platforms_graphs.populate import get_graph_view
from platforms_graphs.util import get_class
from platforms_graphs.graph_mappings import view_to_graphmodel_mapping, model_list, aggregator_strategy_list, time_strategy_list
from geo import geomath
from google.appengine.ext import db

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
        aggregator_index = self['agg_idx'] if self['agg_idx'] else aggregator_strategy_list.keys()[0]
        time_strategy_index = self['time_strategy'] if self['time_strategy'] else time_strategy_list.keys()[0]
        aggregator_strategy = aggregator_strategy_list[aggregator_index] if aggregator_index else None
        time_strategy = time_strategy_list[time_strategy_index] if time_strategy_index else None
        curr_graph = {'model':model,'graph_model':graph_model,'dimension_ids':dimensions,'filter_ids':filter_ids,'graph_view':graph_type,'aggregator_strategy':aggregator_strategy,'time_strategy':time_strategy}
        graph_view = get_graph_view(curr_graph)
        dimension_id = graph_view.graph_model.xaxis_id
        metric_id = graph_view.graph_model.yaxis_id
        model_class = get_class(model)
        dimension = model_class.property_titles[dimension_id]
        metric = model_class.property_titles[metric_id]
        chart_data_json = {'chart_data':graph_view.translate_to_json(filters),
                           'chart_type':curr_graph['graph_view'],
                           'dimension':dimension,
                           'metric':metric}
        self.write(json.dumps(chart_data_json))

class Restaurant():
    def __init__(self, line):
        comps = line.strip().split('^')
        self.dlr_rating = comps[0]
        self.cuisine = comps[1]
        self.loc = comps[2]
        self.name = comps[3]
        self.user_rating = comps[4]
        self.neigh = comps[5]

    def str_match(self, str1, str2):
        str1 = str1.decode('utf-8')
        str2 = str2.decode('utf-8')
        return True if str2 in str1 else False

    def matches(self, reqHandler):
        keys = self.__dict__.keys()
        for key in keys:
            param_to_match = reqHandler[key].lower()
            if len(param_to_match) > 0:
                param = getattr(self, key).lower()
                if self.str_match(param, param_to_match):
                    return True
        return False

    def in_radius(self, reqHandler):
        distance = geomath.distance(db.GeoPt(self.loc), db.GeoPt("%s,%s"%(reqHandler['lat'], reqHandler['lon'])))
        radius = float(reqHandler['radius'])
        return True if distance < radius else False

def get_restaurants():
    rests = None
    rest_objs = []
    with open('assets/data/rests_with_neigh') as f:
        rests = f.readlines()
    for rest in rests:
        rest_obj = Restaurant(rest)
        rest_objs.append(rest_obj)
    return rest_objs

class RestaurantsDataHandler(RequestHandler):
    def get_matches_in(self, rests):
        matches = []
        for rest in rests:
            if self['lat'] and not rest.in_radius(self):
                continue
            if rest.matches(self):
                matches.append(rest)
        return matches

    def get(self):
        rests = get_restaurants()
        matches = self.get_matches_in(rests)
        ret_json = {'count' : len(matches), 'matches' : []}
        for match in matches:
            ret_json['matches'].append(match.__dict__)
        self.write(json.dumps(ret_json))

class RestaurantsOverviewHandler(RequestHandler):
    def get(self):
        rests = get_restaurants()
        ret_json = {'rest_count' : len(rests)}
        attrs = ['neigh', 'cuisine']
        attrs_dict = {}
        for rest in rests:
            for attr in attrs:
                val = getattr(rest, attr)
                if attr not in attrs_dict:
                    attrs_dict[attr] = set()
                attrs_dict[attr].add(val)

        for attr, vals in attrs_dict.iteritems():
            ret_json[attr] = {'count' : len(vals),
                              'values' : [v for v in vals]}
        self.write(json.dumps(ret_json))

class RestaurantsDistanceHandler(RequestHandler):
    def get_matches_in(self, rests):
        matches = []
        for rest in rests:
            if rest.in_radius(self):
                matches.append(rest)
        return matches

    def get(self):
        rests = get_restaurants()
        matches = self.get_matches_in(rests)
        ret_json = {'count' : len(matches), 'matches' : []}
        for match in matches:
            ret_json['matches'].append(match.__dict__)
        self.write(json.dumps(ret_json))

app = webapp2.WSGIApplication([
    ('/api/discount_map', DiscountsMap),
    ('/api/marketers', ChartDataHandler),
    ('/api/restaurants', RestaurantsDataHandler),
    ('/api/restaurants_distance', RestaurantsDistanceHandler),
    ('/api/restaurants_overview', RestaurantsOverviewHandler)
])

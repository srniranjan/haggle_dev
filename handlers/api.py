import json
import webapp2
import logging
from handlers import RequestHandler
from django.template import loader
from platforms_graphs.model import Deal
from platforms_graphs.graph_model import LineGraphModelBuilder
from platforms_graphs.graph_view import LineGraphView
from platforms_graphs.populate import get_graph_view


checkins = {}

checkins['chelsea'] = {}
checkins['chelsea']['day'] = {}
checkins['chelsea']['week'] = {}
checkins['chelsea']['month'] = {}
checkins['chelsea']['year'] = {}

checkins['soho'] = {}
checkins['soho']['day'] = {}
checkins['soho']['week'] = {}
checkins['soho']['month'] = {}
checkins['soho']['year'] = {}

checkins['westvillage'] = {}
checkins['westvillage']['day'] = {}
checkins['westvillage']['week'] = {}
checkins['westvillage']['month'] = {}
checkins['westvillage']['year'] = {}


checkins['chelsea']['day']['brunch'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['brunch'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['chelsea']['month']['brunch'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['year']['brunch'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['chelsea']['day']['happyhour'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['happyhour'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['month']['happyhour'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['year']['happyhour'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['chelsea']['day']['dinner'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['dinner'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['month']['dinner'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['year']['dinner'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['day']['brunch'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['week']['brunch'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['month']['brunch'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['year']['brunch'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['day']['happyhour'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['week']['happyhour'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['soho']['month']['happyhour'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['year']['happyhour'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['day']['dinner'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['week']['dinner'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['month']['dinner'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['soho']['year']['dinner'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['day']['brunch'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['brunch'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['brunch'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['brunch'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['westvillage']['day']['happyhour'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['happyhour'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['happyhour'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['happyhour'] = [{'dimension1':'Japanese','Men':200,'Women':50},
                                    {'dimension1':'Italian','Men':10,'Women':150},
                                    {'dimension1':'Sports Bar','Men':580,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':235}]

checkins['westvillage']['day']['dinner'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['dinner'] = [{'dimension1':'Japanese','Men':100,'Women':50},
                                    {'dimension1':'Italian','Men':90,'Women':150},
                                    {'dimension1':'Sports Bar','Men':280,'Women':70},
                                    {'dimension1':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['dinner'] = [{'dimension1':'Japanese','Men':130,'Women':50},
                                    {'dimension1':'Italian','Men':100,'Women':120},
                                    {'dimension1':'Sports Bar','Men':280,'Women':190},
                                    {'dimension1':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['dinner'] = [{'dimension1':'Japanese','Men':10,'Women':500},
                                    {'dimension1':'Italian','Men':390,'Women':150},
                                    {'dimension1':'Sports Bar','Men':480,'Women':710},
                                    {'dimension1':'Wine Bar','Men':15,'Women':1135}]





spending = {}

spending['chelsea'] = {}
spending['soho'] = {}
spending['westvillage'] = {}

spending['chelsea']['breakfast'] = [{'dimension1':'Mon','Japanese':10,'Indian':20,'French':40,'Mexican':30},
                                    {'dimension1':'Tue','Japanese':10,'Indian':20,'French':40,'Mexican':30},
                                    {'dimension1':'Wed','Japanese':30,'Indian':20,'French':50,'Mexican':30},
                                    {'dimension1':'Thu','Japanese':40,'Indian':30,'French':50,'Mexican':30},
                                    {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70,'Mexican':30},
                                    {'dimension1':'Sat','Japanese':85,'Indian':30,'French':70,'Mexican':30},
                                    {'dimension1':'Sun','Japanese':50,'Indian':20,'French':45,'Mexican':30}]

spending['chelsea']['lunch'] = [{'dimension1':'Mon','Japanese':10,'Indian':25,'French':40},
                                {'dimension1':'Tue','Japanese':30,'Indian':20,'French':80},
                                {'dimension1':'Wed','Japanese':60,'Indian':22,'French':50},
                                {'dimension1':'Thu','Japanese':80,'Indian':70,'French':53},
                                {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70},
                                {'dimension1':'Sat','Japanese':15,'Indian':32,'French':90},
                                {'dimension1':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['chelsea']['snack'] = [{'dimension1':'Mon','Japanese':80,'Indian':28,'French':85},
                                {'dimension1':'Tue','Japanese':60,'Indian':22,'French':35},
                                {'dimension1':'Wed','Japanese':20,'Indian':45,'French':86},
                                {'dimension1':'Thu','Japanese':80,'Indian':56,'French':34},
                                {'dimension1':'Fri','Japanese':55,'Indian':34,'French':75},
                                {'dimension1':'Sat','Japanese':95,'Indian':34,'French':53},
                                {'dimension1':'Sun','Japanese':150,'Indian':23,'French':98}]

spending['chelsea']['dinner'] = [{'dimension1':'Mon','Japanese':65,'Indian':85,'French':46},
                                {'dimension1':'Tue','Japanese':122,'Indian':60,'French':32},
                                {'dimension1':'Wed','Japanese':32,'Indian':45,'French':63},
                                {'dimension1':'Thu','Japanese':72,'Indian':35,'French':75},
                                {'dimension1':'Fri','Japanese':52,'Indian':15,'French':42},
                                {'dimension1':'Sat','Japanese':47,'Indian':74,'French':54},
                                {'dimension1':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['soho']['breakfast'] = [{'dimension1':'Mon','Japanese':65,'Indian':85,'French':46},
                                {'dimension1':'Tue','Japanese':122,'Indian':60,'French':32},
                                {'dimension1':'Wed','Japanese':32,'Indian':45,'French':63},
                                {'dimension1':'Thu','Japanese':72,'Indian':35,'French':75},
                                {'dimension1':'Fri','Japanese':52,'Indian':15,'French':42},
                                {'dimension1':'Sat','Japanese':47,'Indian':74,'French':54},
                                {'dimension1':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['soho']['lunch'] = [{'dimension1':'Mon','Japanese':80,'Indian':28,'French':85},
                            {'dimension1':'Tue','Japanese':60,'Indian':22,'French':35},
                            {'dimension1':'Wed','Japanese':20,'Indian':45,'French':86},
                            {'dimension1':'Thu','Japanese':80,'Indian':56,'French':34},
                            {'dimension1':'Fri','Japanese':55,'Indian':34,'French':75},
                            {'dimension1':'Sat','Japanese':95,'Indian':34,'French':53},
                            {'dimension1':'Sun','Japanese':150,'Indian':23,'French':98}]

spending['soho']['snack'] = [{'dimension1':'Mon','Japanese':10,'Indian':25,'French':40},
                            {'dimension1':'Tue','Japanese':30,'Indian':20,'French':80},
                            {'dimension1':'Wed','Japanese':60,'Indian':22,'French':50},
                            {'dimension1':'Thu','Japanese':80,'Indian':70,'French':53},
                            {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70},
                            {'dimension1':'Sat','Japanese':15,'Indian':32,'French':90},
                            {'dimension1':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['soho']['dinner'] = [{'dimension1':'Mon','Japanese':10,'Indian':20,'French':40},
                                    {'dimension1':'Tue','Japanese':10,'Indian':20,'French':40},
                                    {'dimension1':'Wed','Japanese':30,'Indian':20,'French':50},
                                    {'dimension1':'Thu','Japanese':40,'Indian':30,'French':50},
                                    {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'dimension1':'Sat','Japanese':85,'Indian':30,'French':70},
                                    {'dimension1':'Sun','Japanese':50,'Indian':20,'French':45}]

spending['westvillage']['breakfast'] = [{'dimension1':'Mon','Japanese':10,'Indian':20,'French':40},
                                    {'dimension1':'Tue','Japanese':10,'Indian':20,'French':40},
                                    {'dimension1':'Wed','Japanese':30,'Indian':20,'French':50},
                                    {'dimension1':'Thu','Japanese':40,'Indian':30,'French':50},
                                    {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'dimension1':'Sat','Japanese':85,'Indian':30,'French':70},
                                    {'dimension1':'Sun','Japanese':50,'Indian':20,'French':45}]

spending['westvillage']['lunch'] = [{'dimension1':'Mon','Japanese':65,'Indian':85,'French':46},
                                    {'dimension1':'Tue','Japanese':122,'Indian':60,'French':32},
                                    {'dimension1':'Wed','Japanese':32,'Indian':45,'French':63},
                                    {'dimension1':'Thu','Japanese':72,'Indian':35,'French':75},
                                    {'dimension1':'Fri','Japanese':52,'Indian':15,'French':42},
                                    {'dimension1':'Sat','Japanese':47,'Indian':74,'French':54},
                                    {'dimension1':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['westvillage']['snack'] = [{'dimension1':'Mon','Japanese':10,'Indian':25,'French':40},
                                    {'dimension1':'Tue','Japanese':30,'Indian':20,'French':80},
                                    {'dimension1':'Wed','Japanese':60,'Indian':22,'French':50},
                                    {'dimension1':'Thu','Japanese':80,'Indian':70,'French':53},
                                    {'dimension1':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'dimension1':'Sat','Japanese':15,'Indian':32,'French':90},
                                    {'dimension1':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['westvillage']['dinner'] = [{'dimension1':'Mon','Japanese':80,'Indian':28,'French':85},
                                    {'dimension1':'Tue','Japanese':60,'Indian':22,'French':35},
                                    {'dimension1':'Wed','Japanese':20,'Indian':45,'French':86},
                                    {'dimension1':'Thu','Japanese':80,'Indian':56,'French':34},
                                    {'dimension1':'Fri','Japanese':55,'Indian':34,'French':75},
                                    {'dimension1':'Sat','Japanese':95,'Indian':34,'French':53},
                                    {'dimension1':'Sun','Japanese':150,'Indian':23,'French':98}]



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
    def post(self):
        chart_name = self['name']
        dimension = self['dimension']
        filter_ids = self['filter_ids'].strip('[]').split(',')
        options_array = []
        for id in filter_ids:
            if self[id.strip()]:
                options_array.append((int(id.strip()), str(self[id.strip()])))

        #logging.info(chart_name)
        #logging.info(dimension)
        #logging.info(options_array)
        deal_amt_spent_graph = get_graph_view(chart_name, dimension, options_array)
        data = deal_amt_spent_graph.get_values_for(options_array)

        #logging.info(data)
        chart_data_json = deal_amt_spent_graph.translate_to_json(data)
        chart_data_json['dimension'] = dimension
        self.write(json.dumps(chart_data_json))

app = webapp2.WSGIApplication([
    ('/api/discount_map', DiscountsMap),
    ('/api/marketers', ChartDataHandler)
])

import json
import webapp2
import logging
from handlers import RequestHandler
from django.template import loader


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


checkins['chelsea']['day']['brunch'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['brunch'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['chelsea']['month']['brunch'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['year']['brunch'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['chelsea']['day']['happyhour'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['happyhour'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['month']['happyhour'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['year']['happyhour'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['chelsea']['day']['dinner'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['week']['dinner'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['chelsea']['month']['dinner'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['chelsea']['year']['dinner'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['day']['brunch'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['week']['brunch'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['month']['brunch'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['year']['brunch'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['day']['happyhour'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['week']['happyhour'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['soho']['month']['happyhour'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['year']['happyhour'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['soho']['day']['dinner'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['soho']['week']['dinner'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['soho']['month']['dinner'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['soho']['year']['dinner'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['day']['brunch'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['brunch'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['brunch'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['brunch'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['westvillage']['day']['happyhour'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['happyhour'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['happyhour'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['happyhour'] = [{'Cuisine':'Japanese','Men':200,'Women':50},
                                    {'Cuisine':'Italian','Men':10,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':580,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':235}]

checkins['westvillage']['day']['dinner'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]

checkins['westvillage']['week']['dinner'] = [{'Cuisine':'Japanese','Men':100,'Women':50},
                                    {'Cuisine':'Italian','Men':90,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':70},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':135}]

checkins['westvillage']['month']['dinner'] = [{'Cuisine':'Japanese','Men':130,'Women':50},
                                    {'Cuisine':'Italian','Men':100,'Women':120},
                                    {'Cuisine':'Sports Bar','Men':280,'Women':190},
                                    {'Cuisine':'Wine Bar','Men':150,'Women':35}]

checkins['westvillage']['year']['dinner'] = [{'Cuisine':'Japanese','Men':10,'Women':500},
                                    {'Cuisine':'Italian','Men':390,'Women':150},
                                    {'Cuisine':'Sports Bar','Men':480,'Women':710},
                                    {'Cuisine':'Wine Bar','Men':15,'Women':1135}]





spending = {}

spending['chelsea'] = {}
spending['soho'] = {}
spending['westvillage'] = {}

spending['chelsea']['breakfast'] = [{'weekday':'Mon','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Tue','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Wed','Japanese':30,'Indian':20,'French':50},
                                    {'weekday':'Thu','Japanese':40,'Indian':30,'French':50},
                                    {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'weekday':'Sat','Japanese':85,'Indian':30,'French':70},
                                    {'weekday':'Sun','Japanese':50,'Indian':20,'French':45}]

spending['chelsea']['lunch'] = [{'weekday':'Mon','Japanese':10,'Indian':25,'French':40},
                                {'weekday':'Tue','Japanese':30,'Indian':20,'French':80},
                                {'weekday':'Wed','Japanese':60,'Indian':22,'French':50},
                                {'weekday':'Thu','Japanese':80,'Indian':70,'French':53},
                                {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                                {'weekday':'Sat','Japanese':15,'Indian':32,'French':90},
                                {'weekday':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['chelsea']['snack'] = [{'weekday':'Mon','Japanese':80,'Indian':28,'French':85},
                                {'weekday':'Tue','Japanese':60,'Indian':22,'French':35},
                                {'weekday':'Wed','Japanese':20,'Indian':45,'French':86},
                                {'weekday':'Thu','Japanese':80,'Indian':56,'French':34},
                                {'weekday':'Fri','Japanese':55,'Indian':34,'French':75},
                                {'weekday':'Sat','Japanese':95,'Indian':34,'French':53},
                                {'weekday':'Sun','Japanese':150,'Indian':23,'French':98}]

spending['chelsea']['dinner'] = [{'weekday':'Mon','Japanese':65,'Indian':85,'French':46},
                                {'weekday':'Tue','Japanese':122,'Indian':60,'French':32},
                                {'weekday':'Wed','Japanese':32,'Indian':45,'French':63},
                                {'weekday':'Thu','Japanese':72,'Indian':35,'French':75},
                                {'weekday':'Fri','Japanese':52,'Indian':15,'French':42},
                                {'weekday':'Sat','Japanese':47,'Indian':74,'French':54},
                                {'weekday':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['soho']['breakfast'] = [{'weekday':'Mon','Japanese':65,'Indian':85,'French':46},
                                {'weekday':'Tue','Japanese':122,'Indian':60,'French':32},
                                {'weekday':'Wed','Japanese':32,'Indian':45,'French':63},
                                {'weekday':'Thu','Japanese':72,'Indian':35,'French':75},
                                {'weekday':'Fri','Japanese':52,'Indian':15,'French':42},
                                {'weekday':'Sat','Japanese':47,'Indian':74,'French':54},
                                {'weekday':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['soho']['lunch'] = [{'weekday':'Mon','Japanese':80,'Indian':28,'French':85},
                            {'weekday':'Tue','Japanese':60,'Indian':22,'French':35},
                            {'weekday':'Wed','Japanese':20,'Indian':45,'French':86},
                            {'weekday':'Thu','Japanese':80,'Indian':56,'French':34},
                            {'weekday':'Fri','Japanese':55,'Indian':34,'French':75},
                            {'weekday':'Sat','Japanese':95,'Indian':34,'French':53},
                            {'weekday':'Sun','Japanese':150,'Indian':23,'French':98}]

spending['soho']['snack'] = [{'weekday':'Mon','Japanese':10,'Indian':25,'French':40},
                            {'weekday':'Tue','Japanese':30,'Indian':20,'French':80},
                            {'weekday':'Wed','Japanese':60,'Indian':22,'French':50},
                            {'weekday':'Thu','Japanese':80,'Indian':70,'French':53},
                            {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                            {'weekday':'Sat','Japanese':15,'Indian':32,'French':90},
                            {'weekday':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['soho']['dinner'] = [{'weekday':'Mon','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Tue','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Wed','Japanese':30,'Indian':20,'French':50},
                                    {'weekday':'Thu','Japanese':40,'Indian':30,'French':50},
                                    {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'weekday':'Sat','Japanese':85,'Indian':30,'French':70},
                                    {'weekday':'Sun','Japanese':50,'Indian':20,'French':45}]

spending['westvillage']['breakfast'] = [{'weekday':'Mon','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Tue','Japanese':10,'Indian':20,'French':40},
                                    {'weekday':'Wed','Japanese':30,'Indian':20,'French':50},
                                    {'weekday':'Thu','Japanese':40,'Indian':30,'French':50},
                                    {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'weekday':'Sat','Japanese':85,'Indian':30,'French':70},
                                    {'weekday':'Sun','Japanese':50,'Indian':20,'French':45}]

spending['westvillage']['lunch'] = [{'weekday':'Mon','Japanese':65,'Indian':85,'French':46},
                                    {'weekday':'Tue','Japanese':122,'Indian':60,'French':32},
                                    {'weekday':'Wed','Japanese':32,'Indian':45,'French':63},
                                    {'weekday':'Thu','Japanese':72,'Indian':35,'French':75},
                                    {'weekday':'Fri','Japanese':52,'Indian':15,'French':42},
                                    {'weekday':'Sat','Japanese':47,'Indian':74,'French':54},
                                    {'weekday':'Sun','Japanese':23,'Indian':43,'French':64}]

spending['westvillage']['snack'] = [{'weekday':'Mon','Japanese':10,'Indian':25,'French':40},
                                    {'weekday':'Tue','Japanese':30,'Indian':20,'French':80},
                                    {'weekday':'Wed','Japanese':60,'Indian':22,'French':50},
                                    {'weekday':'Thu','Japanese':80,'Indian':70,'French':53},
                                    {'weekday':'Fri','Japanese':75,'Indian':15,'French':70},
                                    {'weekday':'Sat','Japanese':15,'Indian':32,'French':90},
                                    {'weekday':'Sun','Japanese':80,'Indian':20,'French':25}]

spending['westvillage']['dinner'] = [{'weekday':'Mon','Japanese':80,'Indian':28,'French':85},
                                    {'weekday':'Tue','Japanese':60,'Indian':22,'French':35},
                                    {'weekday':'Wed','Japanese':20,'Indian':45,'French':86},
                                    {'weekday':'Thu','Japanese':80,'Indian':56,'French':34},
                                    {'weekday':'Fri','Japanese':55,'Indian':34,'French':75},
                                    {'weekday':'Sat','Japanese':95,'Indian':34,'French':53},
                                    {'weekday':'Sun','Japanese':150,'Indian':23,'French':98}]




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
        chart = self['name']
        options = json.loads(self['options'])

        chart_data_json = {}
        if chart == 'checkins':
            neighbourhood = options['neighbourhood'] if options['neighbourhood'] else 'chelsea'
            horizon = options['horizon'] if options['horizon'] else 'day'
            time = options['time'] if options['time'] else 'brunch'
            chart_data_json['chart_data'] = checkins[neighbourhood][horizon][time]
        else:
            neighbourhood = options['neighbourhood'] if options['neighbourhood'] else 'chelsea'
            time = options['time'] if options['time'] else 'breakfast'
            chart_data_json['chart_data'] = spending[neighbourhood][time]
        self.write(json.dumps(chart_data_json))

app = webapp2.WSGIApplication([
    ('/api/discount_map', DiscountsMap),
    ('/api/marketers', ChartDataHandler)
])

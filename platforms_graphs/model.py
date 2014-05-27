from pytz import timezone
import datetime
from datetime import timedelta

def time_value_strategy(timestamp):
    time_array = []
    eastern = timezone('US/Eastern')
    dt = datetime.datetime.fromtimestamp(float(timestamp), eastern)
    today = datetime.datetime.now().date()
    timedelta = today - dt.date()
    days = timedelta.days
    if days <= 1:
        time_array.append('Last Day')
    if days <= 7:
        time_array.append('Last Week')
    if days <= 30:
        time_array.append('Last Month')
    if days <= 365:
        time_array.append('Last Year')
    return time_array

def day_value_strategy(day_of_week):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days[int(day_of_week)]

def user_score_value_strategy(score):
    return round(float(score), 2)

def user_score_type_strategy(type_id):
    types = {'H':'History','L':'Loyalty','I':'Influence'}
    return types[type_id]

class Property():
    def __init__(self):
        self.raw_value = ''
        self.unique_id = 0
        self.title = ''
        self.graph_type = None
        self.value_strategy = None

    @property
    def value(self):
        if self.value_strategy:
            return self.value_strategy(self.raw_value)
        return self.raw_value

class Model():
    property_titles = []
    def __init__(self):
        self.properties = []

    def getTitleFor(self, index):
        return self.property_titles[index]

    def pretty_print(self):
        for prop in self.properties:
            print prop.title, prop.value

class Deal(Model):
    property_titles = ["Time", "Day of week", "Neighborhood", "Cuisine", "$ Spent", "Status", "User ID"]

    def populate(self, line):
        comps = line.strip().split('::::')
        self.property_size = len(comps)
        idx = 0
        for comp in comps:
            prop = Property()
            prop.raw_value = comp
            prop.unique_id = idx
            prop.title = self.getTitleFor(idx)
            if idx == 0:
                prop.value_strategy = time_value_strategy
            elif idx == 1:
                prop.value_strategy = day_value_strategy
            self.properties.append(prop)
            idx += 1

class UserScore(Model):
    property_titles = ["Restaurant", "User Email", "User Name", "Misc1", "Score Type", "Misc2", "Score", "Cuisine", "Neighborhood"]

    def populate(self, line):
        comps = line.strip().split('####')
        self.property_size = len(comps)
        idx = 0
        for comp in comps:
            prop = Property()
            prop.raw_value = comp.strip()
            prop.unique_id = idx
            prop.title = self.getTitleFor(idx)
            if idx == 4:
                prop.value_strategy = user_score_type_strategy
            elif idx == 6:
                prop.value_strategy = user_score_value_strategy
            self.properties.append(prop)
            idx += 1
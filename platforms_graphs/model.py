from pytz import timezone
import datetime

def time_value_strategy(timestamp):
    eastern = timezone('US/Eastern')
    return datetime.datetime.fromtimestamp(float(timestamp), eastern)

def day_value_strategy(day_of_week):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days[int(day_of_week)]

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

class Deal(Model):
    property_titles = ["Time", "Day of week", "Neighborhood", "Cuisine", "$ Spent", "Status", "User ID"]

    def getTitleFor(self, index):
        return Deal.property_titles[index]

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

    def pretty_print(self):
        for prop in self.properties:
            print prop.title, prop.value
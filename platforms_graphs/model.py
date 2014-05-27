from graph_model import LineGraphModelBuilder, BarGraphModelBuilder

class Property():
    def __init__(self):
        self.value = ''
        self.unique_id = 0
        self.title = ''
        self.graph_type = None

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
            prop.value = comp
            prop.unique_id = idx
            prop.title = self.getTitleFor(idx)
            self.properties.append(prop)
            idx += 1

    def pretty_print(self):
        for prop in self.properties:
            print prop.title, prop.value
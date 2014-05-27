import logging

def get_graph_model_for(model_name):
    if model_name == 'LineGraphModelBuilder':
        return LineGraphModelBuilder()
    return None

class PlotValue():
    def __init__(self):
        self.co_ord = None
        self.model = None

class GraphModelBuilder():
    def __init__(self):
        self.property_titles = None
        self.filters = None
        self.filter_unique_vals = {}

    def populate(self, model_objs, ids, property_titles):
        self.property_titles = property_titles
        self.filters = []
        for i in range(0, len(property_titles)):
            if i not in ids:
                self.filters.append((i, property_titles[i]))

    def add_to_filter_vals(self, model_obj):
        for filter in self.filters:
                if filter not in self.filter_unique_vals:
                    self.filter_unique_vals[filter] = set()
                self.filter_unique_vals[filter].add(model_obj.properties[filter[0]].value)

class LineGraphModelBuilder(GraphModelBuilder):
    def __init__(self):
        GraphModelBuilder.__init__(self)
        self.xaxis_id = 0
        self.additional_xaxis_id = 0
        self.yaxis_id = 0
        self.lines_map = None

    def populate(self, model_objs, ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, ids, property_titles)
        self.xaxis_id = ids[0]
        self.additional_xaxis_id = ids[1]
        self.yaxis_id = ids[2]

        self.lines_map = dict()
        for model_obj in model_objs:
            curr_additional_dimension = model_obj.properties[self.additional_xaxis_id].value
            curr_dimension = model_obj.properties[self.xaxis_id].value
            if curr_dimension not in self.lines_map:
                self.lines_map[curr_dimension] = []
            curr_x = curr_additional_dimension
            curr_y = model_obj.properties[self.yaxis_id].value
            plot_val = PlotValue()
            plot_val.co_ord = (curr_x, curr_y)
            plot_val.model = model_obj
            self.add_to_filter_vals(model_obj)
            self.lines_map[curr_dimension].append(plot_val)

class BarGraphModelBuilder(GraphModelBuilder):
    def __init__(self):
        GraphModelBuilder.__init__(self)
        self.xaxis_id = 0
        self.yaxis_id = 0
        self.plots = []

    def populate(self, model_objs, ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, ids, property_titles)
        self.xaxis_id = ids[0]
        self.yaxis_id = ids[1]

        for model_obj in model_objs:
            curr_x = model_obj.properties[self.xaxis_id].value
            curr_y = model_obj.properties[self.yaxis_id].value
            plot_val = PlotValue()
            plot_val.co_ord = (curr_x, curr_y)
            plot_val.model = model_obj
            self.add_to_filter_vals(model_obj)
            self.plots.append(plot_val)

class SalesPerHeadByCuisineGraphModelBuilder(GraphModelBuilder):
    def __init__(self, filters=None):
        GraphModelBuilder.__init__(self)
        self.xaxis_id = 0
        self.yaxis_id = 0
        self.aggregator_id = 0
        self.plots = []
        self.selected_filters = filters

    def populate(self, model_objs, ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, ids, property_titles)
        self.xaxis_id = ids[0]
        self.yaxis_id = ids[1]
        self.aggregator_id = ids[2]

        model_objs = self.find_matches_in(model_objs, self.selected_filters)

        aggregated_data = {}
        for model_obj in model_objs:
            dimension = model_obj.properties[self.xaxis_id].value
            aggregator = model_obj.properties[self.aggregator_id].value
            if not dimension in aggregated_data:
                aggregated_data[dimension] = {'aggregators':{},'total':0.0}
            if not aggregator in aggregated_data[dimension]['aggregators']:
                aggregated_data[dimension]['aggregators'][aggregator] = True
            aggregated_data[dimension]['total'] += float(model_obj.properties[self.yaxis_id].value)
            self.add_to_filter_vals(model_obj)

        for (k,v) in aggregated_data.iteritems():
            curr_x = k
            curr_y = v['total']/len(v['aggregators'])
            plot_val = PlotValue()
            plot_val.co_ord = (curr_x, curr_y)
            self.plots.append(plot_val)

    def find_matches_in(self, model_objs, filter_vals):
        matches = []
        for model_obj in model_objs:
            add_model_obj = True
            if filter_vals:
                for filter_val in filter_vals:
                    idx = filter_val[0]
                    val = filter_val[1]
                    if model_obj.properties[idx].value.lower() != val.lower():
                        add_model_obj = False
                        break
            if add_model_obj:
                matches.append(model_obj)
        return matches

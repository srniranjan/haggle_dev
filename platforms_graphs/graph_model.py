from platforms_graphs.graph_mappings import aggregator_strategy_list

def get_graph_model_for(model_name):
    if model_name == 'LineGraphModelBuilder':
        return LineGraphModelBuilder()
    elif model_name == 'BarGraphModelBuilder':
        return BarGraphModelBuilder()
    elif model_name == 'AggregateBarGraphModelBuilder':
        return AggregateBarGraphModelBuilder()
    return None

class PlotValue():
    def __init__(self):
        self.co_ord = None
        self.model = None

class GraphModelBuilder():
    def __init__(self):
        self.property_titles = None
        self.filter_ids = None
        self.filters = None
        self.filter_unique_vals = {}

    def get_dimensions_html_for(self, model_cls, model_objs):
        pass

    def get_unique_dimension_vals(self, model_cls, model_objs):
        retVal = {}
        for model_obj in model_objs:
            for dimension in model_cls.get_x_candidates():
                title = model_cls.property_titles[dimension]
                key = (dimension, title)
                if key not in retVal:
                    retVal[key] = set()
                retVal[key].add(model_obj.properties[dimension].value)
        return retVal


    def populate(self, model_objs, dimension_ids, filter_ids, property_titles):
        self.property_titles = property_titles
        self.filters = []
        for i in filter_ids:
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

    def get_dimensions_html_for(self, model_cls, model_objs):
        template_vals = {'x_candidates' : [(x, model_cls.property_titles[x]) for x in model_cls.get_x_candidates()],
                         'y_candidates' : [(y, model_cls.property_titles[y]) for y in model_cls.get_y_candidates()]}
        template_vals['dimension_vals'] = self.get_unique_dimension_vals(model_cls, model_objs)
        return 'marketers/graphs/dimension_area_templates/line_graph_dimension_area.html', template_vals

    def populate(self, model_objs, dimension_ids, filter_ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, dimension_ids, filter_ids, property_titles)
        self.xaxis_id = dimension_ids[0]
        self.additional_xaxis_id = dimension_ids[1]
        self.yaxis_id = dimension_ids[2]

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

    def get_dimensions_html_for(self, model_cls, model_objs):
        template_vals = {'x_candidates' : [(x, model_cls.property_titles[x]) for x in model_cls.get_x_candidates()],
                         'y_candidates' : [(y, model_cls.property_titles[y]) for y in model_cls.get_y_candidates()]}
        template_vals['dimension_vals'] = self.get_unique_dimension_vals(model_cls, model_objs)
        return 'marketers/graphs/dimension_area_templates/bar_graph_dimension_area.html', template_vals

    def populate(self, model_objs, dimension_ids, filter_ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, dimension_ids, filter_ids, property_titles)
        self.xaxis_id = dimension_ids[0]
        self.yaxis_id = dimension_ids[1]

        for model_obj in model_objs:
            curr_x = model_obj.properties[self.xaxis_id].value
            curr_y = model_obj.properties[self.yaxis_id].value
            plot_val = PlotValue()
            plot_val.co_ord = (curr_x, curr_y)
            plot_val.model = model_obj
            self.add_to_filter_vals(model_obj)
            self.plots.append(plot_val)

class AggregateBarGraphModelBuilder(GraphModelBuilder):
    def __init__(self):
        GraphModelBuilder.__init__(self)
        self.xaxis_id = 0
        self.yaxis_id = 0
        self.aggregator_id = 0
        self.aggregated_data = None
        self.plots = []

    def get_dimensions_html_for(self, model_cls, model_objs):
        template_vals = {'x_candidates' : [(x, model_cls.property_titles[x]) for x in model_cls.get_x_candidates()],
                         'y_candidates' : [(y, model_cls.property_titles[y]) for y in model_cls.get_y_candidates()]}
        template_vals['dimension_vals'] = self.get_unique_dimension_vals(model_cls, model_objs)
        template_vals['aggregator_strategy_vals'] = aggregator_strategy_list.keys()
        return 'marketers/graphs/dimension_area_templates/agg_bar_graph_dimension_area.html', template_vals

    def populate(self, model_objs, dimension_ids, filter_ids, property_titles):
        GraphModelBuilder.populate(self, model_objs, dimension_ids, filter_ids, property_titles)
        self.xaxis_id = dimension_ids[0]
        self.yaxis_id = dimension_ids[1]
        self.aggregator_id = dimension_ids[2]

        aggregated_data = {}
        for model_obj in model_objs:
            dimension = model_obj.properties[self.xaxis_id].value
            aggregator = model_obj.properties[self.aggregator_id].value
            if dimension not in aggregated_data:
                aggregated_data[dimension] = {}
            aggregator_dict = aggregated_data[dimension]
            if aggregator not in aggregator_dict:
                aggregator_dict[aggregator] = []

            curr_x = model_obj.properties[self.xaxis_id].value
            curr_y = model_obj.properties[self.yaxis_id].value
            plot_val = PlotValue()
            plot_val.co_ord = (curr_x, curr_y)
            plot_val.model = model_obj
            self.add_to_filter_vals(model_obj)
            aggregator_dict[aggregator].append(plot_val)
        self.aggregated_data = aggregated_data
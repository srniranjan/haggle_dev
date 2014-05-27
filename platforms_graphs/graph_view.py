import logging

def get_graph_view_for(graph_name):
    if graph_name == 'LineGraphView':
        return LineGraphView()
    return None

class GraphView():
    def __init__(self):
        self.graph_model = None

    def get_dimension(self):
        pass

    def get_values_for(self, filter_vals):
        pass

    def find_matches_in(self, values, filter_vals):
        matches = []
        for plot_val in values:
            add_co_ord = True
            co_ord = plot_val.co_ord
            model = plot_val.model
            for filter_val in filter_vals:
                idx = filter_val[0]
                val = filter_val[1]
                if model.properties[idx].value.lower() != val.lower():
                    add_co_ord = False
                    break
            if add_co_ord:
                matches.append(co_ord)
        return matches

    def translate_to_json(self, filters):
        pass


class LineGraphView(GraphView):
    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id] + ' - ' + \
                          self.graph_model.property_titles[self.graph_model.additional_xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        ret_val = {}
        for additional_xaxis, values in self.graph_model.lines_map.iteritems():
            matches = self.find_matches_in(values, filter_vals)
            if matches and len(matches) > 0:
                ret_val[additional_xaxis] = matches
        return ret_val

    def translate_to_json(self, filters):
        chart_data = []
        for curr_dimension, plot_vals in self.graph_model.lines_map.iteritems():
            data_row = {'dimension1':curr_dimension}
            for plot_val in plot_vals:
                data_row[plot_val.co_ord[0]] = plot_val.co_ord[1]
            chart_data.append(data_row)
        return chart_data

class BarGraphView(GraphView):
    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        return self.find_matches_in(self.graph_model.plots, filter_vals)

    def translate_to_json(self, data):
        data_dict = {}
        dimension2 = 'All'
        for t in data:
            if not t[0] in data_dict:
                data_dict[t[0]] = []
            data_dict[t[0]].append((dimension2,t[1]))

        chart_data = []

        for (k, v) in data_dict.iteritems():
            dimension1 = k
            data_row = {'dimension1':dimension1}
            for t in v:
                dimension2 = t[0]
                value = t[1]
                data_row[dimension2] = int(float(value)) + (data_row[dimension2] if dimension2 in data_row else 0)
            chart_data.append(data_row)

        return chart_data

class AggregatedBarView(GraphView):
    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        return [plot_val.co_ord for plot_val in self.graph_model.plots]

    def translate_to_json(self, data):
        data_dict = {}
        dimension2 = 'All'
        for t in data:
            if not t[0] in data_dict:
                data_dict[t[0]] = []
            data_dict[t[0]].append((dimension2,t[1]))

        chart_data = []

        for (k, v) in data_dict.iteritems():
            dimension1 = k
            data_row = {'dimension1':dimension1}
            for t in v:
                dimension2 = t[0]
                value = t[1]
                data_row[dimension2] = int(float(value)) + (data_row[dimension2] if dimension2 in data_row else 0)
            chart_data.append(data_row)

        return chart_data
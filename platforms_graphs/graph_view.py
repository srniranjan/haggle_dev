import logging
from math import ceil

def get_graph_view_for(graph_name):
    if graph_name == 'LineGraphView':
        return LineGraphView()
    elif graph_name == 'BarGraphView':
        return BarGraphView()
    elif graph_name == 'AggregateBarGraphView':
        return AggregateBarGraphView()
    return None

def average_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            curr_agg_dim_sum = 0.0
            agg_count = 0
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                agg_count += len(plot_vals)
                for (x, y) in plot_vals:
                    curr_agg_dim_sum += float(y)
            logging.info(str(dimension1) + ' :::::::::: '+str(curr_agg_dim_sum) + ' :::::::::: ' +str(agg_count))
            agg_dim_sum[dimension1] = round((curr_agg_dim_sum / agg_count), 2) if agg_count > 0 else 0.0
        return agg_dim_sum

def median_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            median = 0.0
            plot_vals_array = []
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                for (x, y) in plot_vals:
                    plot_vals_array.append((x,y))
            plot_vals_array.sort(key=lambda tup: float(tup[1]))
            if len(plot_vals_array)%2 == 0:
                median_idx_low = len(plot_vals_array)/2
                median_idx_high = median_idx_low + 1
                median = (float(plot_vals_array[median_idx_low][1]) + float(plot_vals_array[median_idx_high][1]))/2
            else:
                median_idx = ceil(len(plot_vals_array)/2)
                median = float(plot_vals_array[median_idx][1])
            agg_dim_sum[dimension1] = round(median, 2)
        return agg_dim_sum

def blind_addition_aggregator(aggregator_dimension_map):
        agg_dim_sum = {}
        for dimension1, agg_dim_dict in aggregator_dimension_map.iteritems():
            curr_agg_dim_sum = 0.0
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                for (x, y) in plot_vals:
                    curr_agg_dim_sum += float(y)
            agg_dim_sum[dimension1] = curr_agg_dim_sum
        return agg_dim_sum

class GraphView():
    def __init__(self):
        self.graph_model = None
        self.aggregator_strategy = None

    def get_dimension(self):
        dimension_title = self.graph_model.property_titles[self.graph_model.xaxis_id]
        ret_val = {}
        ret_val[dimension_title] = self.graph_model.filter_unique_vals
        return ret_val

    def get_values_for(self, filter_vals):
        pass

    def find_matches_in(self, plot_vals, filter_vals):
        matches = []
        for plot_val in plot_vals:
            add_co_ord = True
            co_ord = plot_val.co_ord
            model = plot_val.model
            if len(filter_vals) > 0:
                for filter_val in filter_vals:
                    idx = filter_val[0]
                    val = filter_val[1]
                    if model.properties[int(idx)].value not in val:
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
            matches = self.find_matches_in(plot_vals, filters)
            data_row = {'dimension1':curr_dimension}
            for co_ord in matches:
                data_row[co_ord[0]] = co_ord[1]
            chart_data.append(data_row)
        return chart_data

class BarGraphView(GraphView):
    def get_values_for(self, filter_vals):
        return self.find_matches_in(self.graph_model.plots, filter_vals)

    def translate_to_json(self, filters):
        chart_data = []
        matches = self.find_matches_in(self.graph_model.plots, filters)
        plot_dict = {}
        for (x, y) in matches:
            if x not in plot_dict:
                plot_dict[x] = 0.0
            plot_dict[x] += float(y)
        for k, v in plot_dict.iteritems():
            curr_dict = {'dimension1' : k, 'All' : v}
            chart_data.append(curr_dict)
        return chart_data


class AggregateBarGraphView(GraphView):
    def translate_to_json(self, filters):
        chart_data = []
        agg_data = self.graph_model.aggregated_data
        agg_dim_map = {}
        for dimension1, agg_dim_dict in agg_data.iteritems():
            agg_map = {}
            for agg_dim, plot_vals in agg_dim_dict.iteritems():
                curr_agg = []
                matches = self.find_matches_in(plot_vals, filters)
                for (x, y) in matches:
                    curr_agg.append((x, y))
                agg_map[agg_dim] = curr_agg
            agg_dim_map[dimension1] = agg_map
        processed_data = self.aggregator_strategy(agg_dim_map)
        for dimension1, avg_value in processed_data.iteritems():
            curr_dict = {'dimension1' : dimension1,
                         'All' : avg_value}
            chart_data.append(curr_dict)
        return chart_data
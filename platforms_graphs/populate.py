from model import Deal
from graph_model import GraphModelBuilder, LineGraphModelBuilder, BarGraphModelBuilder, SalesPerHeadByCuisineGraphModelBuilder
from graph_view import GraphView, LineGraphView, BarGraphView, AggregatedBarView
import logging

#deals = []
#with open('./data/availed_deals_with_price') as f:
#    deals = f.readlines()
#
#deal_objs = []
#for deal_line in deals:
#    deal = Deal()
#    deal.populate(deal_line)
#    deal_objs.append(deal)
#
#graph_model = LineGraphModelBuilder()
#graph_model.populate(deal_objs, [1, 3, 4], Deal.property_titles)
#
#deal_amt_spent_graph = LineGraphView()
#deal_amt_spent_graph.graph_model = graph_model
##print deal_amt_spent_graph.get_dimension()
##print deal_amt_spent_graph.graph_model.filters
#print deal_amt_spent_graph.get_values_for([(2, 'Midtown'), (6, 'aiyappa@b-eagles.com')])


def get_graph_view(chart_name, dimension='Day of week', filters=None):
    deals = []
    with open('platforms_graphs/data/availed_deals_with_price') as f:
        deals = f.readlines()

    deal_objs = []
    for deal_line in deals:
        deal = Deal()
        deal.populate(deal_line)
        deal_objs.append(deal)

    graph_model = GraphModelBuilder()
    if chart_name == 'dollars-spent':
        if dimension == 'Day of week':
            graph_model = LineGraphModelBuilder()
            graph_model.populate(deal_objs, [1, 3, 4], Deal.property_titles)
        elif dimension == 'Cuisine':
            graph_model = BarGraphModelBuilder()
            graph_model.populate(deal_objs, [3, 4], Deal.property_titles)
    elif chart_name == 'sales-per-head':
        if dimension == 'Cuisine':
            graph_model = SalesPerHeadByCuisineGraphModelBuilder(filters)
            graph_model.populate(deal_objs, [3, 4, 6], Deal.property_titles)

    deal_amt_spent_graph = None
    if chart_name == 'dollars-spent':
        if dimension == 'Day of week':
            deal_amt_spent_graph = LineGraphView()
        elif dimension == 'Cuisine':
            deal_amt_spent_graph = BarGraphView()
    elif chart_name == 'sales-per-head':
        if dimension == 'Cuisine':
            deal_amt_spent_graph = AggregatedBarView()

    if deal_amt_spent_graph != None:
        deal_amt_spent_graph.graph_model = graph_model

    return deal_amt_spent_graph
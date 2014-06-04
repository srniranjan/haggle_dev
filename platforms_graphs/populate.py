from model_factory import get_model_objs_for, get_model_obj_for
from graph_view import get_graph_view_for
from platforms_graphs.graph_mappings import aggregator_strategy_list

def get_graph_view(graph_obj):
    model_objs = get_model_objs_for(graph_obj['model'])
    graph_model = get_model_obj_for(graph_obj['graph_model'])
    dimensions = graph_obj['dimension_ids']
    filters = graph_obj['filter_ids']
    filter_ids = [int(f.strip()) for f in filters.split(',')] if filters != '' else []
    graph_model.populate(model_objs,
                         [int(d.strip()) for d in dimensions.split(',')],
                         filter_ids,
                         model_objs[0].property_titles)
    graph_view = get_graph_view_for(graph_obj['graph_view'])
    graph_view.graph_model = graph_model
    graph_view.aggregator_strategy = graph_obj['aggregator_strategy']
    return graph_view

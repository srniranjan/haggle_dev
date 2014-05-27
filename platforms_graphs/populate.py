from model_factory import get_model_objs_for
from graph_model import get_graph_model_for
from graph_view import get_graph_view_for

def get_graph_view(graph_obj):
    model_objs = get_model_objs_for(graph_obj['model'])
    graph_model = get_graph_model_for(graph_obj['graph_model'])
    dimensions = graph_obj['dimension_ids']
    filters = graph_obj['filter_ids']
    graph_model.populate(model_objs,
                         [int(d.strip()) for d in dimensions.split(',')],
                         [int(f.strip()) for f in filters.split(',')],
                         model_objs[0].property_titles,)
    graph_view = get_graph_view_for(graph_obj['graph_view'])
    graph_view.graph_model = graph_model
    return graph_view

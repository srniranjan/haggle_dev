from model_factory import get_model_objs_for
from graph_model import get_graph_model_for
from graph_view import get_graph_view_for

def get_graph_view(dimensions, model, graph_model_name, graph_view_name):
    model_objs = get_model_objs_for(model)
    graph_model = get_graph_model_for(graph_model_name)
    graph_model.populate(model_objs, [int(d.strip()) for d in dimensions.split(',')], model_objs[0].property_titles)
    graph_view = get_graph_view_for(graph_view_name)
    graph_view.graph_model = graph_model
    return graph_view

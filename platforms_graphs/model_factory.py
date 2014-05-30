from platforms_graphs.util import get_class

def get_model_records_for(model_name):
    model_records = []
    model_cls = get_class(model_name)
    with open(model_cls.file_name) as f:
        model_records = f.readlines()
    return model_records

def get_model_obj_for(model_name):
    return get_class(model_name)()

def get_model_objs_for(model_name):
    model_records = get_model_records_for(model_name)
    model_objs = []
    for record in model_records:
        model_obj = get_model_obj_for(model_name)
        model_obj.populate(record)
        model_objs.append(model_obj)
    return model_objs

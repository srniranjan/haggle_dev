from model import Deal, UserScore

def get_model_records_for(model_name):
    model_records = []
    with open(get_data_file_for(model_name)) as f:
        model_records = f.readlines()
    return model_records

def get_model_obj_for(model_name):
    if model_name == 'Deal':
        return Deal()
    elif model_name == 'UserScore':
        return UserScore()
    return None

def get_model_objs_for(model_name):
    model_records = get_model_records_for(model_name)
    model_objs = []
    for record in model_records:
        model_obj = get_model_obj_for(model_name)
        model_obj.populate(record)
        model_objs.append(model_obj)
    return model_objs

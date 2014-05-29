function loadGraphTypes(){
    $.get('/marketers/graph_options', {'req_type' : 'graph_types'})
    .done(function(data){
        data_json = JSON.parse(data)
        $('#graph_area #choosing_area #graph_type_chooser').append(data_json['graph_types']);
    });
}

function loadModels(){
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(graph_type.length > 0){
        $.get('/marketers/graph_options', {'req_type' : 'models',
                                           'graph_type' : graph_type})
        .done(function(data){
            data_json = JSON.parse(data)
            $('#graph_area #choosing_area #model_type_chooser').append(data_json['models']);
        });
    }
}

function loadDimensions(){
    var model_type = $('#graph_area #choosing_area #model_type_chooser select :selected').val();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(model_type.length > 0){
        $.get('/marketers/graph_options', {'req_type' : 'dimensions',
                                           'model' : model_type,
                                           'graph_type' : graph_type})
        .done(function(data){
            data_json = JSON.parse(data)
            $('#graph_area #choosing_area #dimension_chooser').append(data_json['dimensions']);
        });
    }
}
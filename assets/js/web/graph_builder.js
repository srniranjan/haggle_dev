function loadGraphTypes(){
    $.get('/marketers/graph_options', {'req_type' : 'graph_types'})
    .done(function(data){
        data_json = JSON.parse(data)
        $('#graph_area').append(data_json['graph_types']);
    });
}
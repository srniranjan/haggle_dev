function loadGraphTypes(){
    $.get('/marketers/graph_options', {'req_type' : 'graph_types'})
    .done(function(data){
        data_json = JSON.parse(data);
        $('#graph_area #choosing_area #graph_type_chooser').append(data_json['graph_types']);
    });
}

function loadModels(){
    $('#graph_area #choosing_area #model_type_chooser').empty();
    $('#graph_area #choosing_area #dimension_chooser').empty();
    $('#graph-submit').hide();
    d3.select("#plot_area").select("svg").remove();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(graph_type.length > 0){
        $.get('/marketers/graph_options', {'req_type' : 'models',
                                           'graph_type' : graph_type})
        .done(function(data){
            data_json = JSON.parse(data);
            $('#graph_area #choosing_area #model_type_chooser').append(data_json['models']);
        });
    }
}

function loadDimensions(){
    $('#graph_area #choosing_area #dimension_chooser').empty();
    $('#graph-submit').hide();
    d3.select("#plot_area").select("svg").remove();
    var model_type = $('#graph_area #choosing_area #model_type_chooser select :selected').val();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(model_type.length > 0){
        $.get('/marketers/graph_options', {'req_type' : 'dimensions',
                                           'model' : model_type,
                                           'graph_type' : graph_type})
        .done(function(data){
            data_json = JSON.parse(data);
            $('#graph_area #choosing_area #dimension_chooser').append(data_json['dimensions']);
        });
    }
}

function getAllFilterValues(){
    var retVal = "";
    $('#filter_values_container .options-list').each(function(){
        if($(this).val() != '')
            retVal += $(this).attr('name') + "::::" + $(this).val() + ",,,,";
    });
    return retVal;
}

function updateChart() {
    d3.select("#plot_area").select("svg").remove();
    var dimensions = getDimensionsList();
    var filters = getAllFilterValues();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    var model_type = $('#graph_area #choosing_area #model_type_chooser select :selected').val();
    var params = {
                    'dimensions':dimensions,
                    'graph_type':graph_type,
                    'model_type':model_type,
                    'filters':filters
                 }
    $.post("/api/marketers", params)
        .done(function(data){
            var chart_data = JSON.parse(data);
            render_graph('plot_area', chart_data.chart_type, chart_data.chart_data);
    });
}

function render_graph(graph_id, chart_type, chart_data){
    if(chart_type == 'LineGraphView'){
        drawLineChart(graph_id, chart_data, graph_id);
    }
    else if(chart_type == 'BarGraphView' ||
            chart_type == 'AggregateBarGraphView'){
        drawStackedBarChart(graph_id, chart_data, graph_id);
    }
}
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
    $('#plot_area').css('border', 'none');
    $('#graph-submit').hide();
    d3.select("#plot_area").select("svg").remove();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(graph_type && graph_type.length > 0){
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
    $('#plot_area').css('border', 'none');
    $('#graph-submit').hide();
    d3.select("#plot_area").select("svg").remove();
    var model_type = $('#graph_area #choosing_area #model_type_chooser select :selected').val();
    var graph_type = $('#graph_area #choosing_area #graph_type_chooser select :selected').val();
    if(model_type && model_type.length > 0){
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
        if($(this).val() && $(this).val() != '' && $(this).attr('name'))
            retVal += $(this).attr('name') + "::::" + $(this).val() + ",,,,";
    });
    $('#secondary_dimension_values_container .options-list').each(function(){
        if($(this).val() && $(this).val() != '')
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
    var aggregator_strategy = $('#aggregator_strategy_values_container select :selected').val();
    var time_strategy = $('#time-strategy :selected').val();
    var time_as_dimension_strategy = $('#time-as-dimension-strategy :selected').val();
    var params = {
                    'dimensions':dimensions,
                    'graph_type':graph_type,
                    'model_type':model_type,
                    'filters':filters,
                    'agg_idx':aggregator_strategy,
                    'time_strategy':time_strategy,
                    'time_as_dimension_strategy':time_as_dimension_strategy
                 }
    $.post("/api/marketers", params)
        .done(function(data){
            var chart_data = JSON.parse(data);
            render_graph('plot_area', chart_data.chart_type, chart_data.chart_data, chart_data.metric, chart_data.dimension);
            $('#plot_area').css('border', '1px solid lightgray');
    });
}

function render_graph(graph_id, chart_type, chart_data, metric, dimension){
    if(chart_type == 'LineGraphView'){
        drawLineChart(graph_id, chart_data, metric, dimension);
    }
    else if(chart_type == 'BarGraphView' ||
            chart_type == 'AggregateBarGraphView'){
        drawStackedBarChart(graph_id, chart_data, metric, dimension);
    }
}
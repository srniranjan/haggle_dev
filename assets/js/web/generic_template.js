function loadChart(graph_id) {
    console.log('here..' + graph_id);
    var option_params = {
        'graph_id':graph_id
    }
    $.post('/marketers/options', option_params)
    .done(function(data){
        var dimensions = data.dimensions;
        var filters = data.filters;
        var curr_graph_id = data.graph_id;
        $('#'+curr_graph_id+' .dimensions-area').empty();
        $('#'+curr_graph_id+' .filters-area').empty();
        $('#'+curr_graph_id+' .dimensions-area').append( dimensions );
        $('#'+curr_graph_id+' .filters-area').append( filters );
        updateChart(curr_graph_id);
    });
}

function getAllFilterValues(graph_id){
    var retVal = "";
    $('#'+graph_id+' .filter-set .options-list').each(function(){
        if($(this).val() != '')
            retVal += $(this).attr('name') + "::::" + $(this).val() + ",,,,";
    });
    return retVal;
}

function updateChart(graph_id) {
    d3.select("#"+graph_id+" .graph-area").select("svg").remove();
    var filters = getAllFilterValues(graph_id);
    var params = {
                    'id':graph_id,
                    'filters':filters
                 }
    $.post("/api/marketers", params)
        .done(function(data){
            var chart_data = JSON.parse(data);
            render_graph(chart_data.graph_id, chart_data.chart_type, chart_data.chart_data);
    });
}

function render_graph(graph_id, chart_type, chart_data){
    if(chart_type == 'LineGraphView'){
        drawLineChart(graph_id + ' .graph-area', chart_data, graph_id);
    }
    else if(chart_type == 'BarGraphView' ||
            chart_type == 'AggregateBarGraph'){
        drawStackedBarChart(graph_id + ' .graph-area', chart_data, graph_id);
    }
}
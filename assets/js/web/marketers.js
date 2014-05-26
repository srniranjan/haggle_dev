$(document).ready(function(){
    //updateCheckinsChart();
    var graph_id_list = ['dollars-spent'];
    console.log(graph_id_list);
    loadCharts(graph_id_list);
});

function updateCheckinsChart() {
    d3.select("#checkins").select("svg")
       .remove();
    var neighbourhood = $('#checkins-neighbourhood').val();
    var horizon = $('#checkins-horizon').val();
    var time = $('#checkins-time').val();
    var params = {
                    'name':'checkins',
                    'options':JSON.stringify({'neighbourhood':neighbourhood,'horizon':horizon,'time':time})
                 }
    var dat;
    $.post("/api/marketers", params)
    .done(function(data){
        var chart_data = JSON.parse(data)
        dat = chart_data.chart_data;
        drawStackedBarChart('checkins',dat,'No. of Checkins');
    });
}

function loadCharts(graph_id_list) {
    console.log(graph_id_list);
    for(var i=0; i < graph_id_list.length; i++) {
        graph_id = graph_id_list[i];
        console.log(graph_id);
        var option_params = {
            'graph_id':graph_id
        }
        $.post('/marketers/options', option_params)
        .done(function(data){
            var dimensions = data.dimensions;
            var filters = data.filters;
            $('#'+graph_id+' .dimensions-area').append( dimensions );
            $('#'+graph_id+' .filters-area').append( filters );
            updateChart(graph_id);
        });
    }
}

function updateChart(graph_id) {
    d3.select("#"+graph_id+" .graph-area").select("svg").remove();

    var params = {
                    'name':graph_id,
                    'dimension':$("input:radio[name=dimension]:checked").val()
                 }

    $('#'+graph_id+' .active-filter-set .options-list').each(function(){
        if($(this).val() != ''){
            params[$(this).attr('name')] = $(this).val();
        }
    });

    var filter_ids = $('#'+graph_id+' .active-filter-id-set').val();

    params['filter_ids'] = filter_ids;

    $.post("/api/marketers", params)
    .done(function(data){
        var chart_data = JSON.parse(data);
        var dat = chart_data.chart_data;
        if(chart_data.dimension == 'Day of week') {
            drawLineChart(graph_id+' .graph-area',dat,'Spent ($)');
        } else if(chart_data.dimension == 'Cuisine') {
            drawStackedBarChart(graph_id+' .graph-area',dat,'Spent ($)');
        }
    });
}

function updateSalesPerHeadChart() {
    d3.select("#sales-per-head .graph-area").select("svg").remove();

    var params = {
                    'name':'sales per head',
                    'dimension':$("input:radio[name=dimension]:checked").val()
                 }

    $('.active-filter-set .options-list').each(function(){
        if($(this).val() != ''){
            params[$(this).attr('name')] = $(this).val();
        }
    });

    var filter_ids = $($('.active-filter-id-set')[0]).val();

    params['filter_ids'] = filter_ids;

    $.post("/api/marketers", params)
    .done(function(data){
        var chart_data = JSON.parse(data);
        var dat = chart_data.chart_data;
        console.log(dat);
        if(chart_data.dimension == 'Day of week') {
            drawLineChart('sales-per-head .graph-area',dat,'Spent ($)');
        } else if(chart_data.dimension == 'Cuisine') {
            drawStackedBarChart('sales-per-head .graph-area',dat,'Spent ($)');
        }
    });
}

function enableFilters(graph_id, index) {
    $('#'+graph_id+' .filter-set').each(function(){
        $(this).removeClass('active-filter-set');
        $(this).addClass('inactive-filter-set');
    });
    $('#'+graph_id+' #filter-set-'+index).removeClass('inactive-filter-set');
    $('#'+graph_id+' #filter-set-'+index).addClass('active-filter-set');
    $('#'+graph_id+' .filter-id-set').each(function(){
        $(this).removeClass('active-filter-id-set');
    });
    $('#'+graph_id+' #filter-id-set-'+index).addClass('active-filter-id-set');
    updateChart(graph_id);
}











$(document).ready(function(){
    var width = $('.small-chart').width(),
    height = $('.small-chart').height(),
    radius = Math.min(width, height) / 2;

    var color = d3.scale.ordinal()
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(radius - 70);

    var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.population; });

    var svg = d3.select(".small-chart").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    data = [{age:'<5',population:2704659},{age:'5-13',population:4499890},{age:'14-17',population:2159981},{age:'18-24',population:3853788},{age:'25-44',population:14106543},{age:'45-64',population:8819342},{age:'≥65',population:612463}];
    data.forEach(function(d) {
    d.population = +d.population;
    });

    var g = svg.selectAll(".arc")
    .data(pie(data))
    .enter().append("g")
    .attr("class", "arc");

    g.append("path")
    .attr("d", arc)
    .style("fill", function(d) { return color(d.data.age); });

    g.append("text")
    .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
    .attr("dy", ".35em")
    .style("text-anchor", "middle")
    .text(function(d) { return d.data.age; });
});
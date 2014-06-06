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
    var ageData = [{age:'18-25',population:30},
            {age:'25-30',population:40},
            {age:'30-35',population:20},
            {age:'35-40',population:10}];
    addDonut(ageData, '.small-chart');
    var genderData = [{gender:'Male',population:65},
                      {gender:'Female',population:35}];
    addDonut(genderData, '.med-chart');
});

function addLineChart(){

}

function addDonut(data, sel){
    var width = $(sel).width(),
    height = $(sel).height(),
    radius = Math.min(width, height) / 2;

    var color = d3.scale.ordinal()
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(radius - 70);

    var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.population; });

    var svg = d3.select(sel).append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    data.forEach(function(d) {
        d.population = +d.population;
    });

    var g = svg.selectAll(".arc")
    .data(pie(data))
    .enter().append("g")
    .attr("class", "arc");

    g.append("path")
    .attr("d", arc)
    .style("fill", function(d) {
        if(sel == '.small-chart')
            return color(d.data.age);
        return color(d.data.gender);
    });

    g.append("text")
    .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
    .attr("dy", ".35em")
    .style("text-anchor", "middle")
    .text(function(d) {
        if(sel == '.small-chart')
            return d.data.age;
        return d.data.gender;
    });
}

function showChartTab(page) {
    $('.tab-select').each(function(){
        $(this).css('color','#9c9c9c');
    });
    $('.chart-page').each(function(){
        $(this).fadeOut(500);
    });
    $('#' + page + '-select').css('color','#c62530');
    $('#' + page + '-page').fadeIn(1500);
}
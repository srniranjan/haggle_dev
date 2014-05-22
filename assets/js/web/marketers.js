$(document).ready(function(){
    updateCheckinsChart();
    updateSpendingChart();
});

function drawCheckinsChart(dt, yTitle) {

    var dat = dt.slice(0);

    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

    var y = d3.scale.linear()
    .rangeRound([height, 0]);

    var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

    var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(d3.format(".2s"));

    var svg = d3.select("#checkins").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var color = d3.scale.ordinal()
    .range(["#ff3912", "#35ab45", "#35ab45", "#25de33", "#12dc54", "#ab21ef", "#ff3912"]);

    color.domain(d3.keys(dat[0]).filter(function(key) { return key !== "Cuisine"; }));

    dat.forEach(function(d) {
    var y0 = 0;
    d.genders = color.domain().map(function(name) { return {name: name, y0: y0, y1: y0 += +d[name]}; });
    d.total = d.genders[d.genders.length - 1].y1;
    });

    dat.sort(function(a, b) { return b.total - a.total; });

    x.domain(dat.map(function(d) { return d.Cuisine; }));
    y.domain([0, d3.max(dat, function(d) { return d.total; })]);

    svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

    svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text(yTitle);

    var cuisine = svg.selectAll(".cuisine")
    .data(dat)
    .enter().append("g")
    .attr("class", "g")
    .attr("transform", function(d) { return "translate(" + x(d.Cuisine) + ",0)"; });

    cuisine.selectAll("rect")
    .data(function(d) { return d.genders; })
    .enter().append("rect")
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d.y1); })
    .attr("height", 0)
    .transition()
    .duration(2000)
    .ease("linear")
    .attr("height", function(d) { return y(d.y0) - y(d.y1); })
    .style("fill", function(d) { return color(d.name); });

    var legend = svg.selectAll(".legend")
    .data(color.domain().slice().reverse())
    .enter().append("g")
    .attr("class", "legend")
    .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

    legend.append("rect")
    .attr("x", width - 18)
    .attr("width", 18)
    .attr("height", 18)
    .style("fill", color);

    legend.append("text")
    .attr("x", width - 24)
    .attr("y", 9)
    .attr("dy", ".35em")
    .style("text-anchor", "end")
    .text(function(d) { return d; });
}

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

function updateSpendingChart() {
    d3.select("#spending").select("svg").remove();
    var neighbourhood = $('#spending-neighbourhood').val();
    var time = $('#spending-time').val();
    var params = {
                    'name':'spending',
                    'options':JSON.stringify({'neighbourhood':neighbourhood,'time':time})
                 }
    var dat;
    $.post("/api/marketers", params)
    .done(function(data){
        var chart_data = JSON.parse(data);
        dat = chart_data.chart_data;
        drawLineChart('spending',dat,'Spent ($)');
    });
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
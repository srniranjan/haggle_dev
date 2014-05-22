function drawLineChart(id, data, metricTitle) {

    var margin = {top: 20, right: 80, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], 0.1);

    var y = d3.scale.linear()
    .range([height, 0]);

    var color = d3.scale.category10();

    var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

    var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

    var line = d3.svg.line()
    .interpolate("basis")
    .x(function(d) { return x(d.dimension1); })
    .y(function(d) { return y(d.metric); });

    var svg = d3.select("#"+id).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    color.domain(d3.keys(data[0]).filter(function(key) { return key !== "dimension1"; }));

    var dimension2s = color.domain().map(function(name) {
    return {
    name: name,
    values: data.map(function(d) {
    return {dimension1: d.dimension1, metric: +d[name]};
    })
    };
    });

    x.domain(data.map(function(d) { return d.dimension1; }));

    y.domain([
    d3.min(dimension2s, function(c) { return d3.min(c.values, function(v) { return v.metric; }); }),
    d3.max(dimension2s, function(c) { return d3.max(c.values, function(v) { return v.metric; }); })
    ]);

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
    .text(metricTitle);

    var dimension2 = svg.selectAll(".dimension2")
    .data(dimension2s)
    .enter().append("g")
    .attr("class", "dimension2");

    path = dimension2.append("path")
    .attr("class", "line")
    .attr("d", function(d) { return line(d.values); })
    .style("stroke", function(d) { return color(d.name); })
    .attr("stroke-width", "2")
    .attr("fill", "none");

    var totalLength = path.node().getTotalLength();

    path
    .attr("stroke-dasharray", totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition()
    .duration(2000)
    .ease("linear")
    .attr("stroke-dashoffset", 0);

    dimension2.append("text")
    .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
    .attr("transform", function(d) { return "translate(" + x(d.value.dimension1) + "," + y(d.value.metric) + ")"; })
    .attr("x", 3)
    .attr("dy", ".35em")
    .text(function(d) { return d.name; });
}
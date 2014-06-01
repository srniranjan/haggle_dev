function drawStackedBarChart(id, data, metricTitle, dimensionTitle) {

    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 710 - margin.left - margin.right,
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
    .orient("left");

    function make_x_axis() {
        return d3.svg.axis()
        .scale(x)
        .orient("bottom");
    }

    function make_y_axis() {
        return d3.svg.axis()
        .scale(y)
        .orient("left");
    }

    var svg = d3.select("#"+id).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var color = d3.scale.ordinal()
    .range(["#ff3912", "#35ab45", "#35ab45", "#25de33", "#12dc54", "#ab21ef", "#ff3912"]);

    color.domain(d3.keys(data[0]).filter(function(key) { return key !== "dimension1"; }));

    data.forEach(function(d) {
    var y0 = 0;
    d.dimension2 = color.domain().map(function(name) { return {name: name, y0: y0, y1: y0 += +d[name]}; });
    d.total = d.dimension2[d.dimension2.length - 1].y1;
    });

    data.sort(function(a, b) { return b.total - a.total; });

    data = data.slice(0,5);

    x.domain(data.map(function(d) { return d.dimension1; }));
    y.domain([0, d3.max(data, function(d) { return d.total; })]);

    /*svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis)
    .attr("font-family", "sans-serif")
    .attr("font-size", "12px");*/

    svg.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + height + ")")
    .call(make_x_axis()
        .tickSize(-height, 0, 0)
    )
    .attr("font-family", "sans-serif")
    .attr("font-size", "12px")
    .selectAll("text")
    .attr("y", 15);

    /*svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text(metricTitle);*/

    svg.append("g")
    .attr("class", "grid")
    .call(make_y_axis()
        .tickSize(-width, 0, 0)
    )
    .attr("font-family", "sans-serif")
    .attr("font-size", "12px")
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", -(margin.left))
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text(metricTitle);

    var dimension1 = svg.selectAll(".dimension1")
    .data(data)
    .enter().append("g")
    .attr("class", "g")
    .attr("transform", function(d) { return "translate(" + x(d.dimension1) + ",0)"; });

    dimension1.selectAll("rect")
    .data(function(d) { return d.dimension2; })
    .enter().append("rect")
    .attr("class", "stacked-bar")
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d.y1); })
    .attr("height", 0)
    .transition()
    .duration(1000)
    .ease("linear")
    .attr("height", function(d) { return y(d.y0) - y(d.y1); })
    .style("stroke", function(d) { return color(d.name); })
    .style("fill", function(d) { return color(d.name); });

    /*var legend = svg.selectAll(".legend")
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
    .text(function(d) { return d; });*/
}
function drawStackedBarChart(id, data, metricTitle, dimensionTitle) {

    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 940 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], 0.7);

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
    .range(["#2bcac4", "#ffc000", "#35ab45", "#25de33", "#12dc54", "#ab21ef", "#ff3912"]);

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

    svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(make_x_axis()
        .tickSize(-height, 0, 0)
    )
    .attr("font-family", "sans-serif")
    .attr("font-size", "12px")
    .selectAll("text")
    .attr("y", 15);

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
    .duration(500)
    .ease("linear")
    .attr("height", function(d) { return y(d.y0) - y(d.y1); })
    .style("stroke", function(d) { return color(d.name); })
    .style("fill", function(d) { return color(d.name); });

    $('svg rect').tipsy({
        gravity: 's',
        html: true,
        fade: true,
        title: function() {
            var d  = this.__data__;
            return d.y1;
        }
    });
}
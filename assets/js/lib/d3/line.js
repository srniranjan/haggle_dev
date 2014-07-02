function drawLineChart(id, data, metricTitle, dimensionTitle) {

    var dataCirclesGroup = null;
    var pointRadius = 10;
    var interpolation_mode = "linear";
    var margin = {top: 85, right: 40, bottom: 40, left: 40},
    width = 940 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], 1, 0.25);

    var y = d3.scale.linear()
    .range([height, 0]);

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

    var color = d3.scale.category10();

    var line = d3.svg.line()
    .interpolate(interpolation_mode)
    .x(function(d) { return x(d.dimension1); })
    .y(function(d) { return y(d.metric); });

    var area = d3.svg.area()
    .interpolate(interpolation_mode)
    .x(function(d) { return x(d.dimension1); })
    .y0(y(0))
    .y1(function(d) { return y(d.metric); });

    var svg = d3.select("#"+id).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var domain_dict = {};
    for(var k in data) {
        var curr = d3.keys(data[k]).filter(function(key) { return key !== "dimension1"; });
        for(var i=0; i<curr.length; i++) {
            if(!(curr[i] in domain_dict)){
                domain_dict[curr[i]] = 'True';
            }
        }
    }

    domain_array = []
    for(key in domain_dict) {
        domain_array.push(key);
    }

    color.domain(domain_array);

    var dimension2s = color.domain().map(function(name) {
        return {
            name: name,
            values: data.map(function(d) {
                if (d[name] && d[name].toLowerCase() != 'none' && d[name].toLowerCase() != '') {
                    return {dimension1: d.dimension1, metric: +d[name]};
                } else {
                    return {dimension1: d.dimension1, metric: 0};
                }
            })
        };
    });

    x.domain(data.map(function(d) { return d.dimension1; }));

    y.domain([
    d3.min(dimension2s, function(c) { return d3.min(c.values, function(v) { return v.metric; }); }),
    d3.max(dimension2s, function(c) { return d3.max(c.values, function(v) { return v.metric; }); })
    ]);

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
    ).attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("font-weight", "600")
    .attr("fill","#868686")
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", -(margin.left))
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text(metricTitle);

    var dimension2 = svg.selectAll(".dimension2")
    .data(dimension2s)
    .enter().append("g")
    .attr("class", "dimension2");

    var path = dimension2.append("path")
    .attr("class", "line")
    .attr("d", function(d) { return line(d.values); })
    .style("stroke", function(d) { return color(d.name); })
    .attr("stroke-width", "2")
    .attr("fill", "none");

    var path1 = dimension2.append("path")
    .attr("class", "area")
    .attr("d", function(d) { return area(d.values); })
    .style("fill", function(d) { return color(d.name); });

    var legend = svg.selectAll(".legend")
    .data(color.domain().slice().reverse())
    .enter().append("g")
    .attr("class", "legend");

    legend.append("rect")
    .attr("y", -50)
    .attr("x", function(d,i){return width-(100*(i+1));})
    .attr("width", 18)
    .attr("height", 18)
    .style("fill", color);

    legend.append("text")
    .attr("y", -50)
    .attr("x", function(d,i){return width-(100*(i+1));})
    .attr("dy", "1em")
    .style("text-anchor", "end")
    .text(function(d) { return d; })
    .attr("fill", color)
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("font-weight", "600");

    for (var i=0; i<dimension2s.length; i++) {
        dimension2 = dimension2s[i];
        dataCirclesGroup = svg.append('svg:g').attr("class", "point-set");

        var circles = dataCirclesGroup.selectAll('.data-point')
            .data(dimension2.values);

        var circle = circles
            .enter()
                .append('svg:circle')
                    .attr('class', 'data-point');

        circle.attr('class', 'data-point')
                    .style('opacity', 1e-6)
                    .attr('cx', function(d) { return x(d.dimension1) })
                    .attr('cy', function() { return y(0); })
                    .attr('r', 0)
                .transition()
                .duration(2000)
                    .style('opacity', 1)
                    .attr('cx', function(d) { return x(d.dimension1) })
                    .attr('cy', function(d) { if(d.metric){return y(+(d.metric))} else {return y(0)} })
                    .attr('r', pointRadius)
                    .style("fill", function(d){ return color(dimension2.name) });

        circle.append("svg:title").text(function(d)
            {
                var y_val = 0;
                if(d.metric){
                    y_val = +(d.metric);
                }
                var ttl = d.dimension1+' : '+dimension2.name+' : '+y_val;
                $($(this).parent()).attr('original-title',ttl);
                $(this).remove();
                return;
            }
        );

        $('svg circle').tipsy({
            gravity: 's',
            html: true,
            fade: true,
            title: function() {
                return $(this).attr('original-title');
            }
        });
    }

    $('.area').mouseover(function(){
        $(this).css('opacity','0.8');
        $($(this).parent().children('.line')[0]).css('stroke-width',8);
    });

    $('.area').mouseout(function(){
        $(this).css('opacity','0.15');
        $($(this).parent().children('.line')[0]).css('stroke-width',6);
    });
}
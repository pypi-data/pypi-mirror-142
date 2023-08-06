$('.bad-actor-visualization').each(function (index, element) {
    var series = $(element).find('.bad-actor-header').map(function () {
        return $(this).text();
    }).get();
    var labels = $(element).find('.bad-actor-labels').map(function () {
        return $(this).text();
    }).get();
    var values = $(element).find('.bad-actor-value').map(function () {
        return parseFloat($(this).text());
    }).get();
    var url_values = $(this).find('td[bad-actor-url]').map(function () {
        return this.getAttribute('bad-actor-url');
    }).get();
    var correlations = [];
    var urls = [];
    for (var i=0; i<values.length; i+=labels.length) {
        correlations.push(values.slice(i, i + labels.length));
        urls.push(url_values.slice(i, i + labels.length));
    }

    var colorscaleValue = [
        [0, '#009D89'],
        [0.18, '#FDDB7F'],
        [0.9, '#FCB800'],
        [1, '#FF0153']
    ];

    var data = [{
                x: labels,
                y: series,
                z: correlations,
                type: 'heatmap',
                customdata: urls,
                colorscale: colorscaleValue,
                showscale: false,
                zmin: 0,
                zmax: 1,
                hoverinfo: "x+y",
                xgap: 1,
                ygap: 1,
    }];
    var layout = {
        xaxis: {
            type: 'category',
            tickangle: -45,
            automargin: true,
            tickmode: 'auto',
            nticks: 24,
            fixedrange: true,
        },
        yaxis: {
            type: 'category',
            automargin: true,
            tickmode: 'array',
            fixedrange: true,
        },
        margin: {
            r: 20,
            t: 20,
        },
        height: 700,
    };
    config = {
        displayModeBar: false,
        responsive: true,
    };

    Plotly.newPlot(element, data, layout, config);
    element.on('plotly_click', function (data) {
        if (data.points.length > 0 && data.points[0].customdata) {
            window.location.href = data.points[0].customdata;
        }
    });
});

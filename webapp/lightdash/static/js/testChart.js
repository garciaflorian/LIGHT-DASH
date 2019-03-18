var config = {
    type: 'line',
    data: {
        labels: DATE,
        datasets: [{
            label: 'Puissance apparente',
            backgroundColor: window.chartColors.red,
            borderColor: window.chartColors.red,
            data: PAPP,
            fill: false,
            label: 'VA',
            yAxisID: 'VA',
				}]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Linky'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Heures'
                }
					}],
            yAxes: [{
                display: true,
                id: 'VA',
                position: 'left',
                scaleLabel: {
                    display: true,
                },
                ticks: {
                    beginAtZero: true
                }
					}]
        }
    }

};

window.onload = function () {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
};
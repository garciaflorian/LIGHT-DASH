function addZero(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

$.getJSON('./jsonData', function(data) {    
    var DATE = data.map(function(item) {
        var tmp = new Date(item.date);
        return addZero(tmp.getHours())+":"+addZero(tmp.getMinutes());
    });
    
    var PAPP = data.map(function(item) {
        return item.papp;
    });
    
    configChart(DATE,PAPP)
});


var config;

function configChart(DATE,PAPP){

    console.log(DATE);
    console.log(PAPP);

config = {
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
    initChart(config)
}

function initChart(config) {
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
};
    
        

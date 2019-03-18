console.log(randomScalingFactor());

		var config = {
			type: 'line',
			data: {
				labels: [
                        '19h15',
                        '19h16',
                        '19h17',
                        '19h18',
                        '19h19',
                        '19h20',
                        '19h21',
                        '19h22',
                        '19h23',
                        '19h24',
                        '19h25',
                        '19h26',
                        '19h27',
                        '19h28',
                        '19h29',
                        '19h30',
                        '19h31',
                        '19h32',
                        '19h33',
                        '19h34',
                        '19h35',
                        '19h36',
                        '19h37',
                        '19h38',
                        '19h39',
                        '19h40',
                        '19h41',
                        '19h42',
                        '19h43',
                        '19h44',
                        '19h45',
                        '19h46',
                        '19h47',
                        '19h48',
                        '19h49',
                        '19h50',
                        '19h51',
                        '19h52',
                        '19h53',
                        '19h54',
                        '19h55',
                        '19h56',
                        '19h57',
                        '19h58',
                        '19h59',
                        '20h00',
                        '20h01',
                        '20h02',
                        '20h03',
                        '20h04',
                        '20h05',
                        '20h06',
                        '20h07',
                        '20h08',
                        '20h09',
                        '20h10',
                        '20h11',
                        '20h12',
                        '20h13',
                        '20h14'],
				datasets: [{
					label: 'Puissance apparente',
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					data: [
						00770,
                        00860,
                        00800,
                        00780,
                        00780,
                        00860,
                        00870,
                        00870,
                        00880,
                        00870,
                        00860,
                        00870,
                        00940,
                        00940,
                        00860,
                        00930,
                        01000,
                        00880,
                        00910,
                        00910,
                        00900,
                        00910,
                        00930,
                        02040,
                        02000,
                        02000,
                        02070,
                        02060,
                        02000,
                        02150,
                        01050,
                        01040,
                        02470,
                        02510,
                        00980,
                        00950,
                        00970,
                        00940,
                        01020,
                        01020,
                        01010,
                        01000,
                        00980,
                        00910,
                        00900,
                        00910,
                        00910,
                        00910,
                        00920,
                        00900,
                        01020,
                        00920,
                        01000,
                        00960,
                        00870,
                        00880,
                        00890,
                        00880,
                        00960,
                        00980,
					],
					fill: false,
                    label: 'VA',
                    yAxisID: 'VA',
				},{
                    label: 'Consommation',
					backgroundColor: window.chartColors.blue,
					borderColor: window.chartColors.blue,
					data: [
                        003396313,
                        003396325,
                        003396337,
                        003396349,
                        003396360,
                        003396373,
                        003396409,
                        003396412,
                        003396425,
                        003396438,
                        003396451,
                        003396464,
                        003396477,
                        003396492,
                        003396506,
                        003396520,
                        003396535,
                        003396551,
                        003396564,
                        003396578,
                        003396591,
                        003396605,
                        003396619,
                        003396640,
                        003396673,
                        003396707,
                        003396741,
                        003396775,
                        003396807,
                        003396842,
                        003396863,
                        003396879,
                        003396902,
                        003396943,
                        003396969,
                        003396984,
                        003396998,
                        003397013,
                        003397029,
                        003397047,
                        003397063,
                        003397079,
                        003397095,
                        003397110,
                        003397124,
                        003397138,
                        003397152,
                        003397166,
                        003397180,
                        003397194,
                        003397208,
                        003397224,
                        003397238,
                        003397253,
                        003397267,
                        003397280,
                        003397294,
                        003397307,
                        003397320,
                        003397336,
					],
					fill: false,
                    label: 'Wh',
                    yAxisID: 'Wh',
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
						}
					}, {
                        display: true,
                        id: 'Wh',
                        position: 'right',
						scaleLabel: {
							display: true,
						}
                      }]
                      }
				}
			
		};

		window.onload = function() {
			var ctx = document.getElementById('canvas').getContext('2d');
			window.myLine = new Chart(ctx, config);
		};

		document.getElementById('randomizeData').addEventListener('click', function() {
			config.data.datasets.forEach(function(dataset) {
				dataset.data = dataset.data.map(function() {
					return randomScalingFactor();
				});

			});

			window.myLine.update();
		});

		var colorNames = Object.keys(window.chartColors);
		document.getElementById('addDataset').addEventListener('click', function() {
			var colorName = colorNames[config.data.datasets.length % colorNames.length];
			var newColor = window.chartColors[colorName];
			var newDataset = {
				label: 'Dataset ' + config.data.datasets.length,
				backgroundColor: newColor,
				borderColor: newColor,
				data: [],
				fill: false
			};

			for (var index = 0; index < config.data.labels.length; ++index) {
				newDataset.data.push(randomScalingFactor());
			}

			config.data.datasets.push(newDataset);
			window.myLine.update();
		});

		document.getElementById('addData').addEventListener('click', function() {
			if (config.data.datasets.length > 0) {
				var month = MONTHS[config.data.labels.length % MONTHS.length];
				config.data.labels.push(month);

				config.data.datasets.forEach(function(dataset) {
					dataset.data.push(randomScalingFactor());
				});

				window.myLine.update();
			}
		});

		document.getElementById('removeDataset').addEventListener('click', function() {
			config.data.datasets.splice(0, 1);
			window.myLine.update();
		});

		document.getElementById('removeData').addEventListener('click', function() {
			config.data.labels.splice(-1, 1); // remove the label first

			config.data.datasets.forEach(function(dataset) {
				dataset.data.pop();
			});

			window.myLine.update();
		});
/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs11
  var ctx = document.getElementById('myChart11')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'
      ],
      datasets: [{
        data: [
          15339,11345,18483,34003,23489,24092,12034
        ],
        lineTension: 0, backgroundColor: 'transparent', borderColor: '#007bff',
        borderWidth: 4, pointBackgroundColor: '#007bff'
      }]
    },
    options: {
//    Title 추가 그런데 안먹히네
      title: {
        display: true,
        text: 'Static Chart sample'
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: true
      }
    }
  })
})()



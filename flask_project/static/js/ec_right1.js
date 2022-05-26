var ec_right1 = echarts.init(document.getElementById('r1'),'dark')

var ec_right1_option = option = {
  title: {
    text: '销售额同比环比',
    subtext:'单位：万元'
  },
  color:['#7EBFB9','#98B3B1','#F2E674'],
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  legend: {},
  grid: {
    // left: '3%',
    // right: '4%',
    // bottom: '3%',
    // containLabel: true
    top:'20%'
  },
  yAxis: [
      {
    type: 'value',
    name: '销售额',
        min: 0,
        max: 80000,
        splitLine:{
      show:false
        }
    // boundaryGap: [0, 0.01]
      },
    {
      type: 'value',
      name: '同比',
      min: -1,
      max: 1,
      splitLine: {
        show:false
      }
    }
  ],
  xAxis: {
    type: 'category',
    data: []
  },
  series: [
    {
      name: '2021',
      type: 'bar',
      data: []
    },
    {
      name: '2022',
      type: 'bar',
      data: []
    },
    {
      name: '同比',
      type: 'line',
      yAxisIndex:1,
      data: []
    }
  ]
};
ec_right1.setOption(ec_right1_option)
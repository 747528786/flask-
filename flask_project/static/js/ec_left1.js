var ec_left1 = echarts.init(document.getElementById('l1'),'dark')

var ec_left1_option = {
    color: ['#56727D', '#6B8584'],
    // legend:{
    //     top:'8%'
    // },
    title:{
        text:"热销单品TOP10",
        textStyle:{
            color:'white',
        },
        left: 'left'
    },
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '10%',
    containLabel: true
  },
  xAxis:
      {
          splitLine:{show:false},
        type: 'category',
          show:true,
        "axisLabel":{
          interval:0
        },
        data: [],
        axisTick: {
          alignWithLabel: true
        }
      },
  yAxis: [
    {
        splitLine: {
            show:false
        },
      type: 'value',
        show: true
    }
  ],
  series: [
    {
      name: 'KA渠道',
      type: 'bar',
      barWidth: '60%',
        // stack:'total',
      data: []
    },
  ]
};
ec_left1.setOption(ec_left1_option)
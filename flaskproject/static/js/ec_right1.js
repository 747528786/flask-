var ec_right1 = echarts.init(document.getElementById('r1'),'dark')

var ec_right1_option = {
    title: {
        text: '年份销售额趋势',
        color:'white',
    },
    color:'#73A070',
    xAxis: {
        show:true,
        title:{
            text:'年份销售额变化趋势',
            color:'white',
        },
        type: 'category',
        data: []
  },
    yAxis: {
        type: 'value',
        show:false
  },
    grid: {
        left: '5%',
        right: '4%',
        bottom: '10%',
        containLabel: true
  },
    series: [
    {
        data: [],
        type: 'line',
        smooth: true
    }
  ]
};
ec_right1.setOption(ec_right1_option)
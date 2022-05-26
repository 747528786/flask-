var ec_left2 = echarts.init(document.getElementById('l2'),'dark');

var ec_left2_option = {
    title:{
        text:'门店类型',
        color: 'white'
    },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    top: '8%',
    left: 'center',
      color:'white'
  },
    color:['#F0F78B','#1DAE7F','#334087','#8AC6D0','#4B84A1'],
  series: [
    {
      name: '门店类型',
      type: 'pie',
      radius: ['50%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#333',
        borderWidth: 0
      },
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '40',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: []
    }
  ]
};
ec_left2.setOption(ec_left2_option)
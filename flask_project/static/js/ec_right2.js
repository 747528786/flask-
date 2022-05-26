var ec_right2 = echarts.init(document.getElementById('r2'),'dark')

var ec_right2_option = {
    title:{
        text:'KA客户集团进货占比',
        color:'white'
    },
    tooltip:{},
    series: [
        {
        type: 'treemap',
        data: []
      },
  ]
}
ec_right2.setOption(ec_right2_option)
var ec_china_map = echarts.init(document.getElementById('m2'), "dark");

var data = [{'name':'上海', 'value': 10000}, {'name':'云南','value': 20000}]

var ec_china_map_option = {
    title: {
        text: '省份销售额',
        subtext: '',
        x: 'left'
    },

    tooltip: {
        // show:true,
        // backgroundColor:"#ff7f50",//提示标签背景颜色
        // textStyle:{color:"#fff"},//提示标签字体颜色
        trigger: 'item'
    },

    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{ start: 0,end: 99 },
            {start: 100, end: 499 },
			{ start: 499, end: 999 },
            {  start: 1000, end: 9999 },
            { start: 10000 }],
        color: ['#FF7A4E', '#BCD78A', '#E4E391', '#449E8B', '#CDC4B3']
    },

    //配置属性
    series: [{
        name: '省份销售金额（万）',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#62d3ff', //区域边框颜色
                areaColor: "#b7ffe6", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#fff',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data:[] //mydata //数据
    }]
};
ec_china_map.setOption(ec_china_map_option)



function get_time(){
    var date = new Date()
    var year = date.getFullYear()
    var month = date.getMonth()+1
    var day = date.getDate()
    var hour = date.getHours()
    var minute = date.getMinutes()
    var second = date.getSeconds()
    if(hour < 10){ hour = "0"+hour}
    if(minute < 10){ minute = "0"+minute}
    if(second < 10){ second = "0"+second}
    var time = year + "年"+ month + "月"+day + "日"+hour + ":"+minute + ":"+second
    $("#time").html(time)
}
function get_m1_data(){
    $.ajax({
        url:"/m1",
        timeout: 10000,
        success:function(data){
            $(".num h1").eq(0).text(data.sum_total);
            $(".num h1").eq(1).text(data.fre);
            $(".num h1").eq(2).text(data.per_retailer);
            $(".num h1").eq(3).text(data.new_store);
        },
        error:function(xhr){}
    });
}
function get_m2_data(){
    $.ajax({
        url:"/m2",
        timeout: 10000,
        success:function(data){
            ec_china_map_option.series[0].data = data.data
            ec_china_map_option.visualMap.max = data.max_num
            // ec_china_map_option.visualMap.min = data.min_num
            ec_china_map_option.series[0].data.push({
                name:"海南诸岛",value:0,
                itemStyle:{
                    normal:{opacity:0},
                },
                label:{show:true}
            })
            ec_china_map.setOption(ec_china_map_option)
        },
        error:function (xhr){

    }
    })
}
function get_l1_data(){
    $.ajax({
        url:"/l1",
        timeout:10000,
        success:function(data){
            ec_left1_option.xAxis.data = data.sku;
            ec_left1_option.series[0].data = data.num;
            ec_left1.setOption(ec_left1_option);
        }
    })
}
function get_r1_data(){
    $.ajax({
        url:'/rl',
        timeout:10000,
        success:function(data){
            ec_right1_option.xAxis.data = data.month;
            ec_right1_option.series[0].data = data.order_pay1;
            ec_right1_option.series[1].data = data.order_pay;
            ec_right1_option.series[2].data = data.year_rate;
            ec_right1.setOption(ec_right1_option);
        }
    })
}
function get_l2_data(){
    $.ajax({
        url:'/l2',
        timeout:10000,
        success:function (data){
            ec_left2_option.series[0].data = data.data;
            ec_left2.setOption(ec_left2_option);
        }
    })
}
function get_r2_data(){
    $.ajax({
        url:'/r2',
        timeout:10000,
        success:function(data){
            ec_right2_option.series[0].data = data.data
            ec_right2.setOption(ec_right2_option)
        }
    })
}
setInterval(get_time,1000)
setInterval(get_m1_data,60000)
setInterval(get_l1_data,60000)
setInterval(get_r2_data,60000)
setInterval(get_m2_data,60000)
setInterval(get_l2_data,60000)
setInterval(get_r1_data,300000)
get_m1_data()
get_m2_data()
get_l1_data()
get_r1_data()
get_l2_data()
get_r2_data()
import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    conn = pymysql.connect(
        host='name',
        user='user_name',
        password='password',
        db='database_name',
        charset='utf8'
    )
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_new_store_num():
    sql = '''
    SELECT count(reg_time) FROM `user_retailer`
    where year(reg_time) = '2021'
    and `status` = 1
    '''
    res = query(sql)
    return res[0]


def get_order_data():
    sql = '''
    SELECT
    FLOOR( SUM( pay_amount )/ 10000 ) AS sum_total,
    ROUND( sum( pay_amount )/ count( DISTINCT retailer_id )/ 12, 0 ) AS per_sum,
    round( sum( pay_amount )/ count( order_code ), 0 ) AS per 
    FROM
    `order_oms_info` 
    WHERE
    `status` IN ( 2, 3, 4 ) 
    AND YEAR ( order_time ) = '2021'
    '''
    res = query(sql)
    return res[0][0], res[0][1], res[0][2]


def get_map_data():
    sql = '''
    SELECT t2.name,round(sum(pay_amount)/10000,0) as sum FROM `order_oms_info` t1
    left join region t2
    on t1.province = t2.id
    where `status` in (2,3,4)
    and province <> ""
    and date_format(t1.order_time,'%%Y') = '2021'
    GROUP BY name
    order by sum desc
    '''
    res = query(sql)
    return res


def get_l1_data():
    sql = '''
    SELECT t2.abbreviation 'sku',sum(t1.goods_num) as num,t4.channel FROM `order_oms_goods` t1
    left join goods_agent t3
    on t1.goods_id = t3.id
    left join goods_base t2
    on t3.goods_id = t2.id
    left join order_oms_info t4
    on t1.order_code = t4.order_code
    where t4.`status` in (2,3,4)
    and date_format(t4.order_time,'%%Y') = '2021'
    and t2.abbreviation in ('AP3','AC3','AP2','AP1','NC3','NC Tin S3','AC4','AC2','AP4','AP1MINI')
    GROUP BY t2.abbreviation,t4.channel
    order by num desc
    '''
    res = query(sql)
    return res


def get_rl_data():
    sql = '''
    SELECT year(order_time) 'year',sum(total_amount) 'amount' FROM `order_oms_info`
    where channel = 1
    and `status` in (2,3,4)
    GROUP BY year(order_time)
    limit 4
    '''
    res = query(sql)
    return res


def get_l2_data():
    sql = '''
    select type,SUM(num) from (select CASE
    new_type 
    WHEN 1 THEN
    "联盟店" 
    WHEN 2 THEN
    "联盟店" 
    WHEN 3 THEN
    "分销商" 
    WHEN 4 THEN
    "分销商" 
    WHEN 5 THEN
    "分销商" 
    WHEN 6 THEN
    "分销商" 
    WHEN 7 THEN
    "总店" 
    WHEN 8 THEN
    "配货门店" 
    WHEN 9 THEN
    "总店" 
    WHEN 10 THEN
    "单体门店" 
    WHEN 11 THEN
    "分销商" 
    END AS type,count(*) as num from user_retailer
    where `status` = 1
    GROUP BY new_type) t1
    GROUP BY type
    '''
    res = query(sql)
    return res


def get_r2_data():
    sql = '''
    SELECT t6.`name` as company,round(sum(t2.goods_num*t4.jy_price),0) as price FROM `order_oms_info` t1
    left join order_oms_goods t2
    on t1.order_code = t2.order_code
    left join goods_agent t3
    on t2.goods_id = t3.id
    left join goods_base t4
    on t3.goods_id = t4.id
    left join user_retailer t5
    on t1.retailer_id = t5.id
    left join user_retailer_company_group t6
    on t5.company_id = t6.id
    where year(t1.order_time) = '2021'
    and t1.channel = 2
    group by t6.name
    order by price desc
    '''
    res = query(sql)
    return res


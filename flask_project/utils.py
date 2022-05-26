import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_conn():
    conn = pymysql.connect(
        host='host',
        user='user',
        password='password',
        db='db',
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
    """
    新店数量
    :return:
    """
    sql = '''
    SELECT count(reg_time) FROM `user_retailer`
    where year(reg_time) = '2022'
    and `status` = 1
    '''
    res = query(sql)
    return res[0]


def get_order_data():
    """
    订单总金额、订单件数、门店平均进货额
    :return:
    """
    sql = '''
    SELECT 
    round(sum(t2.goods_num*t4.jy_price)/10000,0) as price, 
    count(distinct t1.order_code) as fre,
    round(sum(t2.goods_num*t4.jy_price)/count(distinct t1.retailer_id)/10000,0) as per_retailer 
    FROM `order_oms_info` t1
    left join order_oms_goods t2
    on t1.order_code = t2.order_code
    left join goods_agent t3
    on t2.goods_id = t3.id
    left join goods_base t4
    on t3.goods_id = t4.id
    where year(t1.order_time) = '2022'
    and t1.channel = 2
    and t1.`status` in (2,3,4)
    order by price desc
    '''
    res = query(sql)
    return res[0][0], res[0][1], res[0][2]


def get_map_data():
    """
    省份销售额
    :return:
    """
    sql = '''
    SELECT t6.`name` as company,sum(t2.goods_num*t4.jy_price) as price FROM `order_oms_info` t1
    left join order_oms_goods t2
    on t1.order_code = t2.order_code
    left join goods_agent t3
    on t2.goods_id = t3.id
    left join goods_base t4
    on t3.goods_id = t4.id
    left join user_retailer t5
    on t1.retailer_id = t5.id
    left join region t6
    on t5.province = t6.id
    where year(t1.order_time) = '2022'
    and t1.channel = 2
    and t1.`status` in (2,3,4)
    group by t6.name
    order by price desc
    '''
    res = query(sql)
    return res


def get_map_range_data():
    """
    省份销售额最大值
    :return:
    """
    sql = '''
    select max(price) as max_num,min(price) as min_num from (SELECT t6.`name` as company,sum(t2.goods_num*t4.jy_price) as price FROM `order_oms_info` t1
    left join order_oms_goods t2
    on t1.order_code = t2.order_code
    left join goods_agent t3
    on t2.goods_id = t3.id
    left join goods_base t4
    on t3.goods_id = t4.id
    left join user_retailer t5
    on t1.retailer_id = t5.id
    left join region t6
    on t5.province = t6.id
    where year(t1.order_time) = '2022'
    and t1.channel = 2
    and t1.`status` in (2,3,4)
    group by t6.name
    order by price desc) a
    '''
    res = query(sql)
    return res


def get_l1_data():
    """
    热销单品
    :return:
    """
    sql = '''
    SELECT t2.abbreviation 'sku',sum(t1.goods_num) as num FROM `order_oms_goods` t1
    left join goods_agent t3
    on t1.goods_id = t3.id
    left join goods_base t2
    on t3.goods_id = t2.id
    left join order_oms_info t4
    on t1.order_code = t4.order_code
    where t4.`status` in (2,3,4)
    and date_format(t4.order_time,'%%Y') = '2022'
    and t4.channel = 2
    GROUP BY t2.abbreviation
    order by num desc
    limit 10
    '''
    res = query(sql)
    return res


def get_rl_data():
    """
    取年同比数据
    :return: tuple
    """
    sql = '''
        select temp.datetime,temp.orderpay,temp.datetimeb,temp.orderpay1,year_rate from (SELECT
        a.datetime,
        a.d,
        a.orderpay,
        b.dd,
        b.datetime as datetimeb,
        b.orderpay1,(
            a.orderpay - b.orderpay1 
        )/ b.orderpay1 AS year_rate 
    FROM
        (
        SELECT
            DATE_FORMAT( t1.order_time, '%%Y-%%m' ) AS datetime,
            date_format( concat( DATE_FORMAT( t1.order_time, '%%Y-%%m' ), '-1' ), '%%Y-%%m-%%d' ) AS d,
            round( sum( t2.goods_num * t4.jy_price ), 0 ) AS orderpay 
        FROM
            `order_oms_info` t1
            LEFT JOIN order_oms_goods t2 ON t1.order_code = t2.order_code
            LEFT JOIN goods_agent t3 ON t2.goods_id = t3.id
            LEFT JOIN goods_base t4 ON t3.goods_id = t4.id 
        WHERE
            t1.`status` IN ( 2, 3, 4 ) 
            AND t1.channel = 2 
        GROUP BY
        DATE_FORMAT( t1.order_time, '%%Y-%%m' )) a
        LEFT JOIN (
        SELECT
            DATE_FORMAT( t1.order_time, '%%Y-%%m' ) AS datetime,
            DATE_ADD( concat( DATE_FORMAT( t1.order_time, '%%Y-%%m' ), '-1' ), INTERVAL 1 year ) AS dd,
            round( sum( t2.goods_num * t4.jy_price ), 0 ) AS orderpay1 
        FROM
            `order_oms_info` t1
            LEFT JOIN order_oms_goods t2 ON t1.order_code = t2.order_code
            LEFT JOIN goods_agent t3 ON t2.goods_id = t3.id
            LEFT JOIN goods_base t4 ON t3.goods_id = t4.id 
        WHERE
            t1.`status` IN ( 2, 3, 4 ) 
            AND t1.channel = 2 
    GROUP BY
        DATE_FORMAT( t1.order_time, '%%Y-%%m' )) b ON a.d = b.dd
        where b.datetime <> ''
        and SUBSTR(a.datetime,1,4) = '2022') temp
    '''
    res = query(sql)
    return res


def get_l2_data():
    """
    门店类型
    :return:
    """
    sql = '''
    select type,SUM(num) from (select CASE
    new_type 
    WHEN 1 THEN "联盟总店" 
    WHEN 2 THEN "联盟分店" 
    WHEN 3 THEN "分销商" 
    WHEN 4 THEN "分销商" 
    WHEN 5 THEN "分销商" 
    WHEN 6 THEN "经销商" 
    WHEN 7 THEN "总仓和门店" 
    WHEN 8 THEN "总仓配货门店" 
    WHEN 9 THEN "总仓" 
    WHEN 10 THEN "直接订货门店" 
    WHEN 11 THEN "分销商"
    END AS type,count(*) as num from user_retailer
    where `status` = 1
    and channel = 2
    GROUP BY new_type) t1
    GROUP BY type
    '''
    res = query(sql)
    return res


def get_r2_data():
    """
    KA渠道各客户集团销售额
    """
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
    where year(t1.order_time) = '2022'
    and t1.channel = 2
    group by t6.name
    order by price desc
    '''
    res = query(sql)
    return res



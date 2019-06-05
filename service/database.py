import pymysql
import datetime

#只提供查询和插入功能，在获取数据时应判断数据库内是否有当日及之前数据
#如果没有，应当从最近有数据的一天将两张表的数据补齐(调用插入功能的接口）
#应当具有往年数据
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='stock'
)

def get_codes_num():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from codes"
    cursor.execute(sql)
    num = cursor.rowcount
    cursor.close()
    return num

def get_k_list(date):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    start = datetime.datetime.strptime(date, "%Y-%m-%d")
    end = start + datetime.timedelta(days=1)
    sql = "select * from k_day where date >= %s and date < %s "
    params = (str(start), str(end))
    cursor.execute(sql, params)
    list = cursor.fetchall()
    return list

def get_k(code,date):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    start = datetime.datetime.strptime(date, "%Y-%m-%d")
    end = start + datetime.timedelta(days=1)
    sql = "select * from k_point where date >= %s and date < %s "
    params = (str(start), str(end))
    cursor.execute(sql, params)
    list = cursor.fetchall()

def add_k_list(list):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "INSERT INTO k_day (code,open,close,preclose,high,low,date,volume) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
    for i in list:
        date = str(i['date'])
        data = (i['code'], i['open'], i['close'], i['preclose'], i['high'], i['low'], date, i['volume'])
        cursor.execute(sql, data)
        conn.commit()

def add_k(list):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "INSERT INTO k_point (code,open,close,preclose,high,low,date,volume) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
    for i in list:
        date = str(i['date'])
        data = (i['code'], i['open'], i['close'], i['preclose'], i['high'], i['low'], date, i['volume'])
        cursor.execute(sql, data)
        conn.commit()

def get_latest():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select max(date) from k_day"
    cursor.execute(sql)
    ret = cursor.fetchall()[0]['max(date)']
    conn.commit()
    return str(ret)[0:10]
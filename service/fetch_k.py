import baostock as bs
import pandas as pd
import tushare as ts
from datetime import date, timedelta


def time_converge(param):
    return param[0:len(param) - 3]

def code_converge(param):
    return param[-2:].lower() + '.' + param[:6]

def get_code():
    columns = 'ts_code'
    ts_pro = ts.pro_api('08134d01f5097a4e8833b9b0bfa878920760d3c9b06ac500b899c0a0')
    data = ts_pro.query('stock_basic', exchange='', list_status='L', fields=columns)
    data['ts_code'] = data['ts_code'].apply(code_converge)
    return data

def stock_k(time_start: str = '2016-01-01', time_end:str ='2099-01-01',gap: str = 'd', code: str = 'sz.000001') -> pd.DataFrame:
    """ gap 值可为 5/15/30/60/d/w/m """

    #### 登陆系统 ####
    lg = bs.login()

    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    print(gap)
    if gap == 'd':
        columns = 'date,code,open,high,low,close,preclose,volume'
    elif gap == 'w' or gap == 'm':
        print('not min')
        columns = 'date,code,open,high,low,close,volume'
    else:
        print("?????")
        columns = 'time,code,open,high,low,close,volume'

    #### 获取沪深A股历史K线数据 ####
    rs = bs.query_history_k_data_plus(code,
                                      columns,
                                      start_date=time_start, end_date=time_end,
                                      frequency=gap, adjustflag="3")
    print('query_history_k_data_plus respond error_code:' + rs.error_code)
    print('query_history_k_data_plus respond error_msg:' + rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        piece = rs.get_row_data()
        data_list.append(piece)

    result = pd.DataFrame(data_list, columns=rs.fields)

    #### converge dtype ####
    result[['open', 'high', 'low', 'close', 'volume']] = result[['open', 'high', 'low', 'close', 'volume']].astype(
        'float')

    if gap == 'd':
        result['preclose'] = result['preclose'].astype('float')
        result['date'] = result['date'].astype('datetime64[ns]')
    elif gap == 'w' or gap == 'm':
        result['date'] = result['date'].astype('datetime64[ns]')
    else:
        result['date'] = result['time'].apply(time_converge).astype('datetime64[ns]')
        del result['time']

    #### 登出系统 ####
    bs.logout()


    #### 返回结果 ####
    return result


def  fetch_EMA(time_start: str = '2016-01-01', time_end:str ='2099-01-01',gap: str = 'd', code: str = 'sz.000001'):
    result=fetch_EMA(time_start, time_end,gap, code)
    ###EMA计算###
    shortEMA = calc_EMA(result['close'],12)
    longEMA = calc_EMA(result['close'],26)
    return shortEMA, longEMA


def stock_list(date:str, once:int, pages:int):
    code_list = list(get_code()['ts_code'])[once*(pages-1):once*pages]
    stock_list = [v.to_dict('records')[0] for v in [stock_k(date, date, code=code) for code in code_list]]
    return stock_list

def get_codes_count():
    return 3610

def calc_EMA(closeList,num):
    list = []
    k = 2.0/(num+1.0)
    for i in range(0, len(closeList)-1):
        if i == 0:
            list.append(float(closeList[0]))
        else:
            list.append(round(float(closeList[i])*k+list[i-1]*(1-k), 2))
    return list

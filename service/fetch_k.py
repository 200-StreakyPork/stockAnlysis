import baostock as bs
import pandas as pd
import tushare as ts
from .database import *

def time_converge(param):
    return param[0:len(param) - 3]

def code_converge(param):
    return param[-2:].lower() + '.' + param[:6]

def get_code():
    columns = 'ts_code'
    ts_pro = ts.pro_api('f1f25760dc44dc9e65f78f58739fe7b1e8596ffd2d47401fa7f0ce21')
    data = ts_pro.query('stock_basic', exchange='', list_status='L', fields=columns)
    data['ts_code'] = data['ts_code'].apply(code_converge)
    return data

def stock_k(time_start,gap,code,time_end= '2099-01-01'):
    """ gap 值可为 5/15/30/60/d/w/m """
    print('参数', time_start, code, gap)
    #### 登陆系统 ####
    lg = bs.login()

    # 显示登陆返回信息
    #print('login respond error_code:' + lg.error_code)
    #print('login respond  error_msg:' + lg.error_msg)

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
    #print('query_history_k_data_plus respond error_code:' + rs.error_code)
    #print('query_history_k_data_plus respond error_msg:' + rs.error_msg)

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

def stock_list(date:str, once:int, pages:int):
    code_list = list(get_code()['ts_code'])[once*(pages-1):once*pages]
    stock_list = [v.to_dict('records')[0] for v in [stock_k(time_start=date, gap='d', code=code, time_end=date) for code in code_list]]
    get_latest()
    return stock_list

def get_codes_count():
    # return get_codes_num()
    return 3610

def  fetch_EMA(time_start,gap,code,time_end= '2099-01-01'):
    result=stock_k(time_start, gap, code,time_end)
    ###EMA计算###
    shortEMA = calc_EMA(result['close'],12)
    longEMA = calc_EMA(result['close'],26)
    return shortEMA, longEMA

def calc_EMA(closeList,num):
    list = []
    k = 2.0/(num+1.0)
    for i in range(0, len(closeList)-1):
        if i == 0:
            list.append(float(closeList[0]))
        else:
            list.append(round(float(closeList[i])*k+list[i-1]*(1-k), 3))
    return list

def fetch_BIAS(time_start,gap,code,time_end= '2099-01-01'):
    result=stock_k(time_start,gap, code,time_end)
    ###BIAS计算###
    closeList = result['close']
    list = []
    pre = 0.0
    avg = 0.0
    for i in range(0, len(closeList)-1):
        if i < 5:
            avg = (avg * i + float(closeList[i]))/(i+1)
        else:
            avg = (avg * 5 - pre + float(closeList[i]))/5
        list.append(round(avg, 3))
        pre = float(closeList[i])
    return list

def fetch_WARN(time_start,gap,code,time_end= '2099-01-01'):
    result=stock_k(time_start, gap, code,time_end)
    ###WARN计算###
    highList = result['high']
    lowList = result['low']
    closeList = result['close']
    list = []
    warn = 0.0
    for i in range(0,len(result)-1):
        highList[i] = float(highList[i])
        lowList[i] = float(lowList[i])
        closeList[i] = float(closeList[i])
    for i in range(0, len(result)-1):
        if i==0:
            list.append(round((lowList[i]-closeList[i])/(highList[0]-lowList[0])*100), 3)
        elif i < 5:
            list.append(round((min(lowList[0:i])-closeList[i])/(max(highList[0:i])-min(lowList[0:i]))*100), 3)
        else:
            list.append(round((min(lowList[i-5:i])-closeList[i])/(max(highList[i-5:i])-min(lowList[i-5:i]))*100), 3)
    return list


def fetch_RSI(time_start, gap, code, time_end='2099-01-01'):
    result = stock_k(time_start, gap, code, time_end)
    return calc_RSI(result['close'], 5)

def calc_RSI(t,periods):
    length = len(t)
    rsies = []
    #数据长度不超过周期，无法计算；
    if length <= periods:
        return rsies
    #用于快速计算；
    up_avg = 0
    down_avg = 0
    
    for i in range(0,len(t)-1):
        t[i] = float(t[i])
        if i == 0:
            up_avg = 0
            down_avg = 0
            rsies.append(0)
        else:
            if t[i] >= t[i-1]:
                up = t[i] - t[i-1]
                down = 0
            else:
                up = 0
                down = t[i-1] - t[i]
            up_avg = (up_avg*(periods - 1) + up)/periods
            down_avg = (down_avg*(periods - 1) + down)/periods
            rs = up_avg/down_avg
            rsies.append(round(100 - 100/(1+rs),3))
    return rsies

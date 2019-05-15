import baostock as bs
import pandas as pd


def stock_k(time_start: str = '2016-01-01', gap: str = 'd', code: str = 'sz.000001') -> pd.DataFrame:
    """ gap 值可为 5/15/30/60/d/w/m """

    #### 登陆系统 ####
    lg = bs.login()

    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    if gap == 'd' or gap == 'w' or gap == 'm':
        print('not min')
        columns = 'date,code,open,high,low,close,volume'
    else:
        columns = 'time,code,open,high,low,close,volume'

    #### 获取沪深A股历史K线数据 ####
    rs = bs.query_history_k_data_plus(code,
                                      columns,
                                      start_date=time_start, end_date='2099-01-05',
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

    if gap == 'd' or gap == 'w' or gap == 'm':
        result['date'] = result['date'].astype('datetime64[ns]')
    else:
        result['date'] = result['time'].apply(time_converge).astype('datetime64[ns]')
        del result['time']

    #### 登出系统 ####
    bs.logout()

    #### 返回结果 ####
    return result

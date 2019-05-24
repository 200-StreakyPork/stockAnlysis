from flask import jsonify, json
from service.fetch_k import stock_k, stock_list, get_codes_count
from service.spider import eventSpider, commentSpider

def get_k(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_k:', body)
    code = body['code']
    time_start = body['time_start']
    gap = body['gap']
    print('t',code,time_start,gap)
    result = stock_k(time_start, gap, code)
    return jsonify(result.to_dict('records'))


def get_events(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_events:', body)
    layout = body['layout']
    return jsonify(eventSpider(layout))

def get_comments(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_comments:', body)
    page = body['page']
    print(page)
    return jsonify(commentSpider(page))

def get_stock_list(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_stock_list:', body)
    date = body['date']
    once = body['once']
    pages = body['page']
    return jsonify(stock_list(date, once, pages))

def get_count(request):
    return jsonify(get_codes_count())

from flask import jsonify, json, Flask, current_app
from service.fetch_k import stock_k, stock_list, get_codes_count
from service.spider import pageSpider
from django.http import JsonResponse

app = Flask(__name__)
with app.app_context():
    print('ppp', current_app.name)

def get_k(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_k:', body)
    code = body['code']
    time_start = body['time_start']
    gap = body['gap']
    print('t',code,time_start,gap)
    result = stock_k(time_start, gap, code)
    return JsonResponse(result.to_dict('records'),safe=False)

def get_events(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_events:', body)
    page = body['page']
    return JsonResponse(pageSpider(page), safe=False)

def get_stock_list(request):
    str = request.body.decode(encoding='utf-8')
    body = json.loads(str)
    print('get_stock_list:', body)
    date = body['date']
    once = body['once']
    pages = body['page']
    return JsonResponse(stock_list(date, once, pages), safe=False)

def get_count(request):
    return JsonResponse(get_codes_count(), safe=False)

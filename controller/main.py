from flask import Flask, request, jsonify
from service.fetch_k import stock_k, stock_list, get_codes_count
from service.spider import eventSpider, commentSpider

app = Flask(__name__)


@app.route('/fetch_k')
def get_k():
    body = request.json
    code = body['code']
    time_start = body['time_start']
    gap = body['gap']

    result = stock_k(time_start=time_start, gap=gap, code=code)
    return jsonify(result.to_dict('records'))


@app.route('/get_events')
def get_events():
    body = request.json
    layout = body['layout']
    return jsonify(eventSpider(layout))


@app.route('/get_comments')
def get_comments():
    body = request.json
    page = body['page']
    return jsonify(commentSpider(page))


@app.route('/get_stock_list')
def get_stock_list():
    body = request.json
    date = body['date']
    once = body['once']
    pages = body['page']
    return jsonify(stock_list(date, once, pages))


@app.route('/get_codes_count')
def get_count():
    return jsonify(get_codes_count())


if __name__ == '__main__':
    app.run(port='5000', debug=True)

from flask import Flask, request, jsonify
from service.fetch_k import stock_k
from service.spider import eventSpider, commentSpider

app = Flask(__name__)


@app.route('/fetch_k')
def get_k():
    body = request.json
    code = body['code']
    time_start = body['time_start']
    gap = body['gap']

    result = stock_k(time_start, gap, code)
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

if __name__ == '__main__':
    app.run(port='5001')

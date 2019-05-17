import requests
from bs4 import BeautifulSoup
import json


# 事件点爬虫

def eventSpider(layout):
    res = requests.get('https://wallstreetcn.com/live/' + layout)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(class_='live-item')
    list = []
    for item in items:
        time = item.find(class_='live-item_created')
        title = item.find(class_='live-item_title')
        brief = item.p
        if title is None:
            print(time['datetime'], '\n', brief.text, '\n\n')
            list.append(json.dumps([{"date": time['datetime'], "title": "", "brief": brief.text}], ensure_ascii=False))
        else:
            print(time['datetime'], '\n', title.text, '\n', brief.text, '\n\n')
            list.append(
                json.dumps([{"date": time['datetime'], "title": title.text, "brief": brief.text}], ensure_ascii=False))
    return list


# 评论爬虫

def commentSpider(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    if page != 1:
        page = str(page)
        page = '_' + page
    else:
        page = ''
    res = requests.get('http://finance.eastmoney.com/news/cgspl' + page + '.html')  # 抓取信息
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')  # 解析信息
    commentList = soup.find(class_='repeatList')
    items = commentList.find_all('li')
    list = []
    for item in items:
        time = item.find(class_='time')
        title = item.find(class_='title')
        link = title.a['href']
        print(time.text, '\n', title.text, '\n', link, '\n\n')
        list.append(json.dumps([{"date": time.text, "title": title.text, "link": link}], ensure_ascii=False))
    return list


# print(eventSpider('sz.000001'))
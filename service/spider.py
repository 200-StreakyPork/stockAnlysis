import requests
from bs4 import BeautifulSoup
import json

def spider():
    count = 0
    list = []
    '''
    layoutList = {'global', 'theme', 'a-stock', 'us-stock', 'forex', 'commodity', 'blockchain'}
    for layout in layoutList:
        res=requests.get('https://wallstreetcn.com/live/'+layout)
        html=res.text
        soup=BeautifulSoup(html, 'html.parser')
        items=soup.find_all(class_='live-item')
        for item in items:
            count = count+1
            time_ = item.find(class_='live-item_created')
            title = item.find(class_='live-item_title')
            link = item.a
            if(link != None):
                link = link['href']
                link = link.replace("juicy.", "")
                link = link.replace("/edit", "")
            brief = item.p
            time_ = time_['datetime']
            index = time_.find('-')
            time_ = time_[index+1:len(time_)]
            index = time_.rfind(":")
            time_ = time_[0:index]
            index = time_.rfind(":")
            time_ = time_[0:index]
            time_ = time_.replace("-", "月")
            time_ = time_.replace("T", "日 ")
            if title is None and brief is not None:
                #print(time_, '\n', brief.text, '\n', link, '\n\n')
                list.append(json.dumps({"date": time_, "title": "", "brief": strTrans(brief.text), "link": link, "source": switch_layout(layout)}, ensure_ascii=False))
            elif brief is not None:
                #print(time_, '\n', title.text, '\n', brief.text, '\n', link, '\n\n')
                list.append(json.dumps({"date": time_, "title": strTrans(title.text), "brief": strTrans(brief.text), "link": link, "source": switch_layout(layout)}, ensure_ascii=False))
    '''
    for page in [1, 25]:
        if page != 1:
            page = str(page)
            page = '_'+page
        else:
            page = ''
        res=requests.get('http://finance.eastmoney.com/news/cgspl'+page+'.html')#抓取信息
        res.encoding = 'utf-8'
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')#解析信息
        commentList = soup.find(class_='repeatList')
        items = commentList.find_all('li')
        for item in items:
            count = count+1
            time = item.find(class_='time')
            title = item.find(class_='title')
            brief = item.find(class_='info')
            link = title.a['href']
            # print(time.text, '\n', title.text, '\n', brief.text, link, '\n', '\n\n')
            list.append(json.dumps(
                {"date": strTrans(time.text),
                 "title": strTrans(title.text),
                 "brief": strTrans(brief.text),
                 "link": strTrans(link),
                 "source": "东方财富网"}
                , ensure_ascii=False))
    list.sort(key=getTime,reverse=True)
    print(len(list))
    return list

def pageSpider(page):
    list = spider()
    size = len(list)
    perpage = 10
    totalPage = 5
    if page == totalPage:
        return list[(page-1)*perpage:len(list)-1]
    else:
        return list[(page-1)*perpage:page*perpage-1]

def strTrans(str:str):
    str=str.replace('\n','')
    str=str.replace('\r','')
    str=str.replace(' ','')
    return str

def getTime(jsonData):
    return json.loads(jsonData)["date"]

def switch_layout(str : str):
    switcher = {"global":"华尔街见闻-要闻", "theme":"华尔街见闻-科创版", "a-stock":"华尔街见闻-A股", "us-stock":"华尔街见闻-美股", "forex":"华尔街见闻-外汇", "commodity" :"华尔街见闻-商品", "blockchain":"华尔街见闻-区块链", }
    return switcher.get(str, 'wrong value')

print(spider())




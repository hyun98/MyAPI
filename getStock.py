import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import xmltodict
from sqlalchemy import create_engine
import datetime
import MySQLdb

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from stockapp.models import Company, StockInfo
from django.db.models import Q

def getStockcode():
    stock_code = pd.read_excel('/home/ubuntu/MyAPI/kospicompany.xlsx',
                               sheet_name='Sheet1', converters={'종목코드':str})
    stock_code = stock_code[['종목코드', '종목명']]
    print(stock_code)
    return stock_code

def getDailyStockPrice(stockcode, name, count):
    print(f"now : {stockcode}, {name}")
    url = f'https://fchart.stock.naver.com/sise.nhn?symbol={ stockcode }&timeframe=day&count={ count }&requestType=0'
    req = requests.get(url)
    dic = xmltodict.parse(req.text)
    js = json.dumps(dic)
    js = json.loads(js)
    
    data = pd.json_normalize(js['protocol']['chartdata']['item'])
    df = data['@data'].str.split('|', expand=True)
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
    
    # print(df)

    company = Company.objects.filter(name__exact=name)
    if(company.count() == 0):
        print("create new company")
        company = Company(name=name)
        company.save()
    else:
        print("use resi company")
        company = Company.objects.get(name=name)
    
    for i in range(count):
        try:
            row = df.loc[i]
        except:
            break
        
        date_string = row['date']
        date_format = '%Y%m%d'
        date_obj = datetime.datetime.strptime(date_string, date_format)
        
        is_data = StockInfo.objects.filter(Q(date__exact=date_obj) &
                                            Q(company__id__exact=company.id))
        
        if(is_data.count() > 0):
            # print("already exist!")
            continue
        
        stock = StockInfo(company=company, date=date_obj, 
                        low=row['low'], high=row['high'], 
                        open=row['open'], close=row['close'], volume=row['volume'])
        stock.save()
    
    # engine = create_engine("mariadb://root:"+"1234"+"@mariadb/django", encoding='utf-8')
    # print("find engine")
    # conn = engine.connect()
    # print("success connect!")
    # df.to_sql(name=name, con=engine, if_exists='replace')
    # print("to sql clear")


if __name__ == '__main__':
    stocks = getStockcode()
    
    for i in range(len(stocks)):
        code = stocks.loc[i][0]
        name = stocks.loc[i][1]
        getDailyStockPrice(code, name, 700)
    
        
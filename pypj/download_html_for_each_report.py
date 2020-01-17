# -*- coding:utf-8 -*-
import csv
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

csvfile = file('D://pypj//wjw//url//resulttest.csv', 'rb')
reader = csv.reader(csvfile)
i = 1

for line in reader:
    print line[0]+','+line[1]
    print i
    i = i + 1
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, sdch",
               "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
               "Referer": line[0],
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                     (KHTML, like Gecko) Chrome/51,.0.2704.106 Safari/537.36"
               }
    fileaddress='D://pypj//wjw//shtml//'+line[1]
    url = line[0]
    r = requests.get(url, headers=headers)
    ft = open(fileaddress + "//html.txt", 'wb')
    ft.write(r.text)
    ft.close()
csvfile.close()

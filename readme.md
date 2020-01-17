
# Readme

This practicing project is going to crawl published infectious disease data from official website of health department of Shanghai (上海市卫生与计划生育委员会).

This project is finished in 2016. I don't know whether their website has been updated or not. The name of the department has already changed from "卫计委" to "卫健委".

However, the code should be valuable.

## Basic Processes

+ On the official sites, there is a special page where saved all history reports.

![1](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/1.png)

*<center>This screen shot was taken in 2016.</center>*

From this picture, we can see there are for pages of the url. So the following processes are clear:

+ Save the html file of the four pages.

+ Extract urls from the four pages by finding the special pattern of saving the urls.

Finally, all urls are recongized and downloaded:

![2](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/2.png)

![3](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/3.png)

+ The next step is download all html pages of the urls, where data is saving.

![4](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/4.png)

*<center>This is a snapshot of one of the reporting pages.</center>*

![5](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/5.png)

![6](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/6.png)

*<center>These are the html codes of one reporting page.</center>*

+ The last step is recongnizing patterns of the data and save them.

Maybe due to the changes of the staff, there are three patterns of the data. (I found this after trying for a huge times (^o^;).)

But, finally, I made it.

![7](https://raw.githubusercontent.com/Ry2an/my_picture_garage/master/crawler_prac/7.png)

## Core Codes

+ to get access to the server and require html codes, we should firstly let our program pretent to be a browser. And thus we need to have a "head claim":

```
for i in range(0,2):
    url = 'http://www.hnwst.gov.cn/cms/showsubpage.jsp?ocid=363&ncid=363&pno='+str(i)+'.html'

    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                "Referer":'http://www.wsjsw.gov.cn/wsj/n429/n426/index.html'
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
                 (KHTML, like Gecko) Chrome/51,.0.2704.106 Safari/537.36"
                }
    tempp=i+1
    r = requests.get(url,headers=headers)
    f=open ("D:\\pypj\\wjwhn\\page"+str(tempp)+".txt",'wb')
    f.write(r.text)
    f.close()
```

+ After we get the html file, we need to find the pattern and copy the "matched strings"

*Plase notice that this method is called 'Regular Expression', 'regexp', or '正则表达式'. There is a more advanced plug-in in python called 'Beautiful Soup'.*

*To understand what's the meaning of '\\d' or '\\w', please find the tutorials of regexp by yourself.*

```
f = open("D://pypj//wjw//page1.txt")
line1 = f.readlines()
patternu = re.compile(r'/wsj/n\d\d\d/n\d\d\d/u1ai\d+\.html')
result1u = re.findall(patternu,str(line1))
```

---------------------

Please use the getpip.py to install pip

Since I am clearing up my code 4 years ago. The code for the 3rd pattern was lost. But the luckly I have enough codes to do the crawling processes.












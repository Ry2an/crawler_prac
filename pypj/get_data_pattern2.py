# -*- coding:utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

yy = ['2011','2012','2013','2014','2015','2016']
mm  = ['01','02','03','04','05','06','07','08','09','10','11','12']
kk = 0
datelist = []
finalrr = []
ff = open("D:\\pypj\\wjw\\finalr\\" + 'ffrr' + ".csv", 'wb')
for ii in yy:
    for jj in mm:
        date = str(ii) + str(jj)
        if date == '201610':
            break
        f = open("D://pypj//wjw//shtml//" + date + "//html.txt")
        line1 = f.readlines()
        f.close()

        patternu = re.compile(r'<div  ><span >\d+</span></div>')
        result = re.findall(patternu, str(line1))
        result1 = []
        if len(result) != 0:
            datelist.append(date)
            kk = kk+1
            print len(result)
            print date
            for each in result:
                patternn = re.compile(r'\d+')
                result1.append(re.findall(patternn, each)[0])
            print len(result1)
            ff.write(str(date)+','+str(jj)+',')
            print str(date)+','+str(jj)+','
            for i in [6,9,14,17,18,20,21,22,24,25,27]:
                ff.write(str(result1[(i) * 3]) + ',' + str(result1[(i) * 3 + 1]) +',')
                print str(result1[(i) * 3]) + ',' + str(result1[(i) * 3 + 1]) +','
            ff.write('\n')
            print 'cichuhuanh'
ff.close()
print '-------------------------------'
print 'sum num = ' + str(kk)
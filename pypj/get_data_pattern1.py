# -*- coding:utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
ff = open("D:\\pypj\\wjw\\finalr\\" + 'ffrr2' + ".csv", 'wb')
yy = ['2011','2012','2013','2014','2015','2016']
mm  = ['01','02','03','04','05','06','07','08','09','10','11','12']
kk = 0
for ii in yy:
    for jj in mm:
        date = str(ii) + str (jj)
        if date == '201610':
            break
        f = open("D://pypj//wjw//shtml//" + date + "//html.txt")
        line1 = f.readlines()
        f.close()

        patternu = re.compile(r'<td style="width:\d+px;">\\n\', \'\\t\\t\\t\\t\d+</td>\\n')
        result = re.findall(patternu, str(line1))
        result1 = []
        if len(result) != 0:
            kk = kk+1
            print date
            print len(result)
            print kk
            for each in result:
                patternn = re.compile(r'\d+')
                result1.append(re.findall(patternn, each)[1])
            ff.write(str(date) + ',' + str(jj) + ',')
            print str(date) + ',' + str(jj) + ','
            for i in [7, 11, 15, 18, 19, 21, 22, 23, 25, 26, 28]:
                ff.write(str(result1[(i) * 3]) + ',' + str(result1[(i) * 3 + 1]) + ',')
                print str(result1[(i) * 3]) + ',' + str(result1[(i) * 3 + 1]) + ','
            ff.write('\n')
            print 'cichuhuanh'
ff.close()
print '------------------'
print 'sum num = ' + str(kk)
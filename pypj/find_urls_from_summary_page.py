# -*- coding:utf-8 -*-
import re
f = open("D://pypj//wjw//page1.txt")
line1 = f.readlines()
f.close()
f = open("D://pypj//wjw//page2.txt")
line2 = f.readlines()
f.close()
f = open("D://pypj//wjw//page3.txt")
line3 = f.readlines()
f.close()
f = open("D://pypj//wjw//page4.txt")
line4 = f.readlines()
f.close()

patternu = re.compile(r'/wsj/n\d\d\d/n\d\d\d/u1ai\d+\.html')
patternt = re.compile(r'\d\d\d\d-\d\d-\d\d')

result1u = re.findall(patternu,str(line1))
result1t = re.findall(patternt,str(line1))

result2u = re.findall(patternu,str(line2))
result2t = re.findall(patternt,str(line2))

result3u = re.findall(patternu,str(line3))
result3t = re.findall(patternt,str(line3))

result4u = re.findall(patternu,str(line4))
result4t = re.findall(patternt,str(line4))

resultsumu = []
resultsumt = []
for i in range(len(result1u)):
    resultsumu.append('http://www.wsjsw.gov.cn' + result1u[i-1])
    resultsumt.append(result1t[i-1])

for i in range(len(result2u)):
    resultsumu.append('http://www.wsjsw.gov.cn' + result2u[i - 1])
    resultsumt.append(result2t[i - 1])

for i in range(len(result3u)):
    resultsumu.append('http://www.wsjsw.gov.cn' + result3u[i - 1])
    resultsumt.append(result3t[i - 1])

for i in range(len(result4u)):
    resultsumu.append('http://www.wsjsw.gov.cn' + result4u[i - 1])
    resultsumt.append(result4t[i - 1])
print len(resultsumu)
print resultsumu
print len(resultsumt)
print resultsumt

f = open("D://pypj//wjw//url//resulttest.txt",'w')
for i in range(len(resultsumu)):
    f.write(str(resultsumu[i-1])+','+str(resultsumt[i-1]))
    f.write('\n')
f.close()
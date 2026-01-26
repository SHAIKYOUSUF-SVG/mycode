'''using findall
the output of findall is in list mode'''

import re
exp="\d+"
data="hi this is yousuf my roll no is12my scores also 12 and mt=y age also2"
out=re.findall(exp,data)
print(out)

exp="\d\.\d"
data="i got score 8.0 gps in ssc in telugu 6.6 and in hindi 6.0 and in maths 9.0 and in evs 9.8"
out=re.findall(exp,data)
print(out)


exp=("^\d+$")
data="9989549088"
out=re.findall(exp,data)
print(out)


#using sub-search,replace,substitute
#syntax:out=re.sub(regex,replacemnt,input data)
import re
data="bvewi34bfsj21424bncwkj34jbf54"
out=re.sub("\d+","",data)
print(out)
print(type(out))

#using paths
data='/home/asus/python/re1.py'
out=re.sub(".py$",".xlx",data)
print(out)
out=re.sub("^/home","yousuf",data)
print(out)

data="/home/users/a.xls/report.xls"
out=re.sub("(\.xls$|\.xlsx$)",".txt",data)
out=re.sub("(\.xls|\.xlsx)$",".txt",data)
out=re.sub("\.xls(|x)$",".txt",data)
print(out)


data="8498742g348g"
exp="^\d+g|\d+g$"
out=re.search(exp,data)
print(out) #to get the search position
print(out.start())
print(out.end())
if out:
    print("fopund")
else:
    print("not found")

#split,and
data="sfjkkfe45fdiiww45fdi23hcawi7"
exp="\d+"
out=re.split(exp,data)
print(out)

data="1212dj32n434nk343nknk342"
exp="\d+"
out=re.split(exp,data)
print(out)

exp1="g\d+k"
exp2="\d+$"
data="g63kinidia p2d usa9384"
out1=re.search(exp1,data)
out2=re.search(exp2,data)
if out1 and out2:
    print("found")
else:
    print("not found")
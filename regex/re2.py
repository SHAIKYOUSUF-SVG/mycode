'''
regular exressions are for data searching,data extraction,data manipulation
charecter class-[]
quantifires-{}repetation,+[1,],*[0,],?{0,1}

'''
import re
import sys
data="i am indian"
exp="indian"
out=re.search(exp,data)
if out:
    print("foiund")
else:
    print('not found')
'''gives first occurance inly to fina all u]we use findall'''


mno="9989549088"

exp='[6-9]\d{9}'
out=re.search(exp,mno)
if out:
    print(out.group())
else:
    print("not found")


ip="107.111.168.123"
exp="(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
out=re.match(exp,ip)
if out:
    for i in out.groups():
        if int(i)>255:
            sys.exit()
    else:
        print("valid ip")
else:
    print("not found")



str1='my ip1 is 192.168.0.111 and ip2 is 107.111.2.0 and mac if 90-E8-68-13-83-2C'
#regex:findall ips and all mac
'''
def get_ip(ip1):
    <>
    return ellipsis

def get_mac(ip1):
    <>
    return mac'''
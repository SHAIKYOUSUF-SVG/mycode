import re

data="winteck2024@gmail.com"
exp="[a-z,A-Z]+[0-9]{4}\@[a-z]{5}\.[a-z]{3}"
'''
data="/dev/sda"
exp="\/\w+\/\w+"'''
out=re.match(exp,data)
if out:
    print("found")
else:
    print("not founf")

a="yousuf/esuf"
b='\w+\/[a-z]+'
out=re.search(b,a)
if out:
    print(out.group())
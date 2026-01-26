import re
data="usa|uk|germany|italy"
out=re.search("uk",data)
if out:
    print("found",out.group())
else:
    print("not found")

#\d[]
exp="g[0-9]k"
#data="g22k"
data="g9k"
out=re.search(exp,data)
if out:
    print("found that is",out.group())
else:
    print("not found")

exp="a\db"
data="a7b"
out=re.search(exp,data)
if out:
    print(out.group())
else:
    print("not found")

exp="a\wb"
data="awb|a22b|aeb|a2b"
out=re.search(exp,data)
if out:
    print(out.group())
else:
    print("not found")
#it will show first getting obj

#using .
exp="4\.5"
data="abcdreqwdui4.5bwfuewbuifweuifqewiuehueg"
out=re.search(exp,data)
if out:
    print("found",out.group())
else:
    print("not found")
#using quantifires {},+,*,?
exp="u\d+b"
#exp="s\w+w$"
exp="s\w+y$"
data="iusccueu737bdjbcwy"

out=re.search(exp,data)
if out:
    print(out.group())
else:
    print("not found")

exp="e\d?j"
data="uccuiwe5jcd"
out=re.search(exp,data)
if out:
    print(out.group())
else:
    print("notfound")

#groups[serarch and extract]:memmory panthsis,memorygrouping
exp="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
data="123.197.0.15"
out=re.search(exp,data)
if out:
    print("found",out.group())
else:
    print("not found")
#making groups
exp="(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
data="123.251.12.166"
out=re.search(exp,data)
if out:
    g1=out.group(1)
    g2=out.group(2)
    print(type(g1),g2)
else:
    print("not found")

exp="(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
data="111.2.3.45" #ip must be <=255
out=re.search(exp,data)
if out:
    g1=int(out.group(1))
    g2=int(out.group(2))
    g3=int(out.group(3))
    g4=int(out.group(4))
    if g1<255 and g2<255 and g3<255 and g4<255:
        print("ip is valid")
        print(out.group())
    else:
        print("ip is not valid")
else:
    print('not found')
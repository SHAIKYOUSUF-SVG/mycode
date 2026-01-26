import json
dict1={"ip":"192.168.0.143","username":"winteck"}
#dump-used to dump our dictinary to json
with open("file3.json","w") as fr:
    out=json.dump(dict1,fr)
print(out)


dict2={'a':200,'b':100}
with open('file1.json','w') as fw:
    out=json.dump(dict2,fw)
print(out)

#load-used to load json file
with open('file1.json','r') as fr:
    out=json.load(fr)
print(out)
print(out.keys())
print(out.values())

dict3={"india":123,"usa":345,"uk":1234,"germany":5674,"italy":9492}

with open('file4.json','w') as fw:
    out=json.dump(dict3,fw)
print(type(out))


with open('file4.json','r') as fr:
    out=json.load(fr)
print(out)

d={"a":100,"b":200,"c":300}
with open("file5.json",'w') as fw:
    out=json.dump(d,fw)
print(out)


d1={'a':1,'b':2,'c':3}
with open('file6.json','w') as fw:
    out=json.dump(d1,fw)
print(out)

with open('file5.json','r') as fr:
    out=json.load(fr)
print(out)

with open('file4.json','r') as fr:
    out=json.load(fr)
print(out)

with open('file6.json','r') as fr:
    out=json.load(fr)
print(out)

with open('file3.json','r') as fr:
    out=json.load(fr)
print(out)

with open ('file4.json','r') as fr:
    out1=json.load(fr)
print(out1)

d2={'name':'yousuf','age':28,"dob":1996,'job':"qa"}
with open('file7.json','w') as fw:
    out=json.dump(d2,fw)
print(out)

with open('file7.json','r') as fr:
    out=json.load(fr)
print(out['name'])
out['age']=44
out['name']='esuf'

out.update({'livingstate':'ap','martialstatus':'married'})
out.pop('livingstate')
out.popitem()
print(out)


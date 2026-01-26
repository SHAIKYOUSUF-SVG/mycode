d1={'a':10,'b':20,'c':30,'d':40}
d2={'e':50,'f':60}
for i,j in d2.items():
    d1[i]=j
print(d1)
#in func method
def addtodict(d1,d2):
    for i,j in d2.items():
        d1[i]=j
    return d1


dict1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
dict2 = {'e': 50, 'f': 60}
out=addtodict(dict1,dict2)
print(out)



def primenum(*args):
    list=[]
    for i in args:
        if i%1==0 and i%i==0:
            list.append(i)
    return list
out=primenum(1,2,3,4,5,6,7,8,9,10)
print(out)

list1=[2,1120,3,248,1009,879,980,1001]
list2=sorted(list1)
print(list2[-2])


dict1={'a':10,'b':20,'c':30}
dict2={'a':20,'c':40,'d':50}

for i,j in dict2.items():
    if i in dict1.keys():
        dict1[i] +=j
    else:
        dict1[i]=j
print(dict1)

def neq_d(dict1,dict2):
    for i,j in dict2.items():
        if i in dict1.keys():
            dict1[i] +=j
        else:
            dict1[i]=j
    return dict1


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 20, 'c': 40, 'd': 50}
out=neq_d(dict1,dict2)
print(out)




def new_list(numbers):
    dict={}
    for i in range(numbers+1):
        dict[i]=i+10
    return dict


numbers=50
out=new_list(numbers)
print(out)



def common(d1,d2):
    d3={}
    for i,j in d1.items():
        if i in d2.keys():
            d3[i]=j
    return d3


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 10, 'c': 30, 'd': 50}
out=common(dict1,dict2)
print(out)


dict1 = {'a': 10, 'b': 20, 'c': 10}
dict2 = {'c': 5, 'd': 50}
for i,j in dict2.items():
    dict1[i]=j
print(dict1)


dict1 = {'a': 10, 'b': 20, 'c': 10,'d':12}

for i in dict1.keys():
    if i=='d':
        print("found")
    else:
        print("not found")



students={'alice':85,'bob':85,'charlie':90,'daina':82}
toppers={}
for i,j in students.items():
    if j>80:
        toppers[i]=j
print(toppers)


inventory={'fruits':{'apples':50,'bananas':100,'oranges':75},'vegitables':{'carrots':40,'broccoli':30,'spinach':20}}

l1=[1,2,3]
l2=[4,5,6,7]
d={}
for i,j in zip(l1,l2):
    #if len(l1)==len(l2):
        d[i]=j
print(d)

print(d.get(2))
print(d.get(4))

aa=d.setdefault(4,5)
aa1=d.setdefault(6)
print(aa)
print(d)


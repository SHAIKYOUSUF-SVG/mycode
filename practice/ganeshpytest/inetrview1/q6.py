'''
diffrenece b/w shallow copy,deepcopy,refrence copy
pass by refrence and pass by value in functions
by default python uses pass by reference or pass by value:pass by reference
'''

'''data=[10,20,30]
print(id(data[0]))
print(id(data[1]))
print(id(data[2]))
print(id(data))
xy=10
abc=[1,2,3,10]
print(id(abc[3]))
print(id(xy))'''
'''
refernce copy:it will not create anew id
shallow copy can be used for a singel time
here original data is data and data is copy to temp
here the id of 2 lists will become same 
if we change data from 1 list then from second type data also that will change'''

data=[10,20,30]
temp=data

print(data,id(data)) # 2170990531968
print(temp,id(temp)) # 2170990531968

temp[0]=100

print(data[0],id(data[0]))
print(temp[0],id(temp[0]))

'''
another type of copy is list method copy that is shallow copy
in this '.copy()' method 
the id of data will not remain same
id will change for copy one
in this if we change any 1 obj from  a|b list and the
another  list will not as in shallow copy
another one will remain satble
which one that one only chnage 

ex:'''
a=[1,2,3,4]
b=a.copy()
print(a,id(a)) #2170992080256
print(b,id(b)) # 2170991983872

b[0]=12
print(b,id(b))
print(a,id(a))

'''
shallow copy will copy for one layer
fro inside another layer[multi layes] it will not work 
work refrence copy'''

list=[[10,20],[30,40],[540,60]]  #this multi layer/multi ndimentional
list1=list.copy()   #this method shallow copy


print(list,id(list)) #1397560836480
print(list1,id(list1)) #1397560836480
#for 1 layer shallow copy will done
#here inside list ther is another layer for that list shallow copy will not work

print(list[0],id(list[0])) # 2185896670528

print(list1[0],id(list1[0]))  # 2185896670528

'''
for this inside another layer reference copy only work
1.same id
2.if we update in list[0]
   then list1[0] will also change
   
to avoid that we use deep copy'''





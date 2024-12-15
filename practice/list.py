'''
list is data type
used to store any data type
list is mujtable
memory id of list will change
take more time compared to tuple
when the data not fixed we use list data type

dmethod:append,insert,remover pop,index,copy,clear,split,join
'''

#append is used to add the data in end
list=[1,2,3,4,5]
list.append(5)
print(list)

#insewrt:is usewd to insert the charcetr using index

list[0]=11
print(list)

#pop used to remove lat one
out=list.pop()
print(out)

#remove is used to remove using object
out=list.remove(11)
print(out)
print(list)

print(list.index(4))


#count is used to get no.of chracters
list.append(3)
list.append(3)
out=list.count(3)
print(out)


#join:used to join the data

out=":".join(list)
print(out)
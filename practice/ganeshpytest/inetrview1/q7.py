'''
pass by refrence and pass by value in functions
by default python uses pass by reference or pass by value:pass by reference


deep copy: will best for multiple layers
it will create new id for every layer and
if we update from 1 list then it will only update oin that list
the remain list will remain as it was
for deep copy we need to import module
import copy
'''
import copy
list=[[10,20],[30,40],[50,60]]
temp=copy.deepcopy(list)

print(id(list)) #2440638104064  diffrent ids
print(id(temp)) #2440638116992

print(id(list[0])) #2688489816768
print(id(temp[0])) #2688489632896
# for this layer also a new id will cfreated but not in shallow copy
#if we update in 1 list ,that list only update and another list will remian same
#in shjallow copy it will for 1st layer,but for second layer it will work as referenccopy

list[0][0]="x"
print(list)
print(temp)






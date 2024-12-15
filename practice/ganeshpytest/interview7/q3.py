#function overloading?
'''
where we will be able to define multiple funcions with same name but different typ of
arguments or different number of arguments

function or any definitions wiil over write
python will not support function overlooading
'''
 def add(x,y):
     return x+y
 def add(x,y,z):
     return x+y+z
out=add(2,0)
print(out)
'''
if we wrote the 2 funtions with same name then
new will overwrite the old function'''
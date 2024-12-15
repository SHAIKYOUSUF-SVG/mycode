#a single line function also called as anonymos function
l1=["a",'b','c','d','e']
l2=["india","uk","us","germany","france"]



def func(x):
    return x+1
out=func(10)
print(out)

#both are same lambda used to write function 1 line
func=lambda x:x+1
out=func(10)
print(out)


func1=lambda x,y:x*y
out=func1(10,1)
print(out)


func2=lambda inp:1 if (type(inp)==list and len(inp)%2==0) else 0
data=[1,2,3,4]
out=func2(data)
print(out)





func=lambda inp:1 if (type(inp)==dict and len(inp)==3) else 0
data={'a':'india','b':'uk','c':'italy'}
out=func(data)
print(out)


fun1=lambda x,y:x+y
fun2=lambda x:x**2  #we import aspecific function from this file also ex: from filename import fun2
fun3=lambda x,y:x*y

print(fun1(100,120),
      fun2(20),
      fun3(10,10))
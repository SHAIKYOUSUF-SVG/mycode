fun1=lambda x,y:x+y
fun2=lambda x:x**2  #we import aspecific function from this file also ex: from filename import fun2
fun3=lambda x,y:x*y
if __name__=="__main__":
    print(fun1(100, 120))
    print(fun2(20))
    print(fun3(10, 10))

'''
__name__,__main__are spcial built in varibles in python
when  a module is dircetly executed it will be set to __amin__  else it will be set to module name'''
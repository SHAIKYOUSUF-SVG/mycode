'''
what is the use of __name__
how to use a pyhton file like module and as well as script

when we import or load the module,entire fill  will egt excecutedinetrnally

'''
'''
import arith #arith will load for only mext time and then next it will not load



import arith #for theses aroth will not load

import airth #this one also not load

'''
print("q11 is",__name__)
def add (x,y):
    return x+y
def sub(x,y):
    return x-y
if __name__=="__main__":
    out=add(10,10)
    print(out)
'''
this is not module to import
if we import this file as a module
codes outputt also comes 
how to avoid that
'''
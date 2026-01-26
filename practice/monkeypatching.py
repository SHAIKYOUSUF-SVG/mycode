'''used to
if there is an mistake in module and we cant change that module
than we can rechange that in out presewnt file '''


#file module1.py
# def add(x,y):
#     return x*y
# insted of adding it will do multipling but module1 we cant  change then

import sys
sys.path.insert(0,f"C:\python\pycharm\interview\inetrview1")
import modul1
def add(x,y):
    return x+y
modul1.add=add
out=add(10,10)
print(out)
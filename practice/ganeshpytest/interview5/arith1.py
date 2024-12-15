'''
whenever there are many functions in a module if we wants import only
some no.if functions from a function
then we goes to __all__
__all__=[add,sub]
if we worte this then if we call mul then it will not work
'''

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y

__all__=['add','sub']
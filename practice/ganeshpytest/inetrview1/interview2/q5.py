'''
doen python support function overloading-no
if function names are same,they overwrite
function opverloading means:same function with different no.of arguments
or differnet type of argumnets
'''
def add(x,y):
    return x+y

def add(x,y,z):
    return x+y+z

out=add(10,10)
'''
if there are 2 values with the same name 
then value comes from the ;atest one
like that when we call the function woth same names
it will take only latest one ont old one i
means it will over wirte'''
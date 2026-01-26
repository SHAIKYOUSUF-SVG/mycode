
def dec_function(a1):
    def wrapper(*args):
        result=a1(*args)
        if len(a1(*args))<2:
            return None
        return result
    return wrapper



@dec_function
def main_code(a):
    l=[]
    for i in a:
        if isinstance(i,str):
            l.append(i)
    return l
a=[1,2,3,4,'india','usa','uk','k']
out=main_code(a)
print(out)
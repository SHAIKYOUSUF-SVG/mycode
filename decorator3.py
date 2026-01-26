
def dec_function(a1):
    def wrapper(*args,**kwargs):
        print('this is extra functionality before normal function')
        a1(*args,**kwargs)
        print('this is extra functionality after normal function')
    return wrapper
@dec_function
def main_code(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    print(l3)

a1=[1,2,3]
a2=[2,3]
main_code(a1,a2)



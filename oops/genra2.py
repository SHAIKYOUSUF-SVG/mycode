'''if write yield ,it will act like generator,it will didnt start executing the generator '''

'''
how to start excecuting the code inside the generator'''
def test1():
    print("a")
    yield 10
    print("b")
    yield 20

x=test1()

'''
when we use generator,function will start to excecute the code amd pause at yield statement '''
i=next (x)
print(i)
'''
a 
10
'''
#it will start iteration from where it stops
i=next(x)
print(i)
'''
b
20
'''

"""
we dont get all at a time
we write each time for getting putput"""
'''
to avoid this problem we use loops'''
def test():
    global x  #after make x another x will gone which is global
    x=10
    y=20
    print("locals are",locals()) #locals are {'x': 10, 'y': 20}
    print("globals are",globals())
    print("globals are",globals()['x']) #to get x value
    print("globals are",globals()['z']) #to get z value

x=100
z=200
test()

'''
after makes local as global 
it will not shown in locals,shown in only globals'''
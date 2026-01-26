#how to know ehich are global valuee and which are global

def test():

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
int q:how to get global values from functon:
print("globals are",globals()['x'])
print("globals are",globals()['z'])'''
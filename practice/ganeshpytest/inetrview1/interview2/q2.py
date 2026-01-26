#loacl function
#how to make global
def test():
    #global z
    #any objct defined inside the funtion is local to function
    #you can access it only inside the function
    z=10

    y=20
    print("z is",z)
    print("x is",x)
x=100 #this global,it anywhere till end of this programe
z=900 #these x,z are global we can call them from inside the function and outside the function
test()
print("outside z is",z) # name 'z' is not defined
print("out side x is",x)

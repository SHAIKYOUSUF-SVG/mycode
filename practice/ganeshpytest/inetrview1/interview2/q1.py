'''what is global and what is loacl?
'''
#global
'''
here x is  inside loop
in python any data from inside it acts as a global except in function
in funtions what we wrote inside the funtion that will local to that function only'''
data=["india","uk","germany"]
for i in data:
    print(i.upper())
    x=100

print(x)












#what is zip function??
#to print data accorfding to index from all  inputs at a time


data1=["india","uk","germany"]
data2=["sachun","abcd","test"]
data3=[100,200,300]

'''
for i in range(len(data1)):
    print(data1[i],data2[i],data3[i])
'''
for i,j,k in zip(data1,data2,data3):
    print(i,j,k)



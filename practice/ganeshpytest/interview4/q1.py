#what is 'enumaret fucntion':it will output index and coresponding value also

#to get both index and value we use range(len())
data=["india","uk","usa"]
for i in range(len(data)):
    print(i,data[i])

print("###############")
#intead of this we use enumarate function
for i ,j in enumerate(data):
    print("using enumarate",i,j)

#range function is squence of numbers


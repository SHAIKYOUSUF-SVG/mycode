d1={"a":100,"b":200,"c":300}
d2={"a":200,"b":200,"d":500}
for i,j in d1.items():
    if i in d2:
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=j
print(d1)


d1={"a":100,"b":200,"c":300}
d2={"a":200,"b":200,"d":500}
d3={}
for i,j in d2.items():
    if i in d1:
        d3[i]=d2[i]+d1[i]
    else:
        d3[i]=j
print(d3)


d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 200, "b": 200, "d": 500}

# Create a new dictionary to store the result
d3= d1.copy()   #d3={"a": 100, "b": 200, "c": 300}

# Add values from d2 to result, summing up the values for common keys
for i,j in d2.items():  #"a": 200, "b": 200, "d": 500
    if i in d3:
        d3[i] += j   #"a":300,"b":400,"c":300
    else:
        d3[i] = j    #"d":500

print(d3)

dict1={"india":1,"uk":2,"usa":3}
dict2={"india":10,"uk":3,"germany":5}
# dict3=dict1.copy()
# for i,j in dict2.items():
#     if i in dict3:
#         dict3[i] += j
#     else:
#         dict3[i] = j
# print(dict3)

for i,j in dict2.items():
    if i in dict1.keys():
        dict1[i]+=j
    else:
        dict1[i]=j
print(dict1)




for i in range(1,11):
    print(f"27 x {i} = {27*i}")



















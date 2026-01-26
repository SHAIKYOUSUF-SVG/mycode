#map:mapping one to one

data=[10,20,30]
'''for i in range(len(data)):
    print(f"enp{i}")'''

out=map(lambda i: i+2,data)
'''
take one object from data
    pass to function
        excecute function
            result will pass to out   here result and in filter pass i to out
'''
print(list(out))



data=[1,2,3,4]
out=map(lambda i: i+10,data)
out=map(lambda i: "enp"+str(i),data)

print(list(out))



data=["inida","uk","germany"]
out=map(lambda i: i.upper(),data)
print(list(out))
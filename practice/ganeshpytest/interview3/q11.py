#how tyo write single line for loop
#also called as list comprohension cause output comes in lsit mode
#emp10,emp20,emp30
data=[10,20,30]
for i in data:
    print(f"emp{i}")



out=[i+1 for i in data]
out1=[f"ok{i}" for i in data]

print(out)
print(out1)
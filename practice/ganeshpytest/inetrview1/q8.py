'''
# pass by reperence and pass by value?
'''

#pass by reference
def test(data):
    data.append(10)

inp=["india","uk","germany"]
'''here data is nothing but inp 
this is pass by reference
if we change in data , it will impoact on inp also'''
test(inp)
print(inp) #['india', 'uk', 'germany', 10]


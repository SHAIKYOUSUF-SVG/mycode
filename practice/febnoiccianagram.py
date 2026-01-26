def feb(n):
    feb_list=[0,1]
    while len(feb_list)<n:
        feb_list.append(feb_list[-1]+feb_list[-2])
    return feb_list
out=feb(10)
print(out)

#anagram
a='listen'
b='silent'
c=True
if len(a)!=len(b):
    c=False
if c:
    if sorted(a)==sorted(b):
        print('anagram')
    else:
        print('nhtg')

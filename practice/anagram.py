a='listen'
b='silent'
print(sorted(a))
print(sorted(b))
c=True

if len (a)!=len(b):
    c=False
if c:
    if sorted(a)==sorted(b):
        print('anagram')
    else:
        print('not anagram')


records=[list(input())]
a = []
b=[]
for i in records:
    for j in i:
        if type(j)==float:
            if j not in a:
                a.append(j)
for k in a:
    if k==max(a):
        for l in records:
            if k==l[1]:
                b.append(l[0])
for i in reversed(b):
    print(i)








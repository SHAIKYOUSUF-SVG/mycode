a='listen'
b='silent'
c=True

if len(a)!=len(b):
    c=False
if c:
    if sorted(a)==sorted(b):
        print('anagram')
    else:
        print('not anagram')


        
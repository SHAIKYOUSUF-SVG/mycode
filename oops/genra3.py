def test1():
     print("a")
     yield 10
     print("b")
     yield 20
     print("c")
     yield 30

a=test1()
for i in a:
    print("i is",i)
    input()

'''
here we wrote input() to get the command in our hand we can operate the function
with output we get all at a time'''
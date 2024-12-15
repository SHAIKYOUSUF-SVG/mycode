#what is monkey patching and use of it?
'''
monkey aotching what is when there is error in module and we cant change
that error which is in anither file and operating that from another folder
what we can do" we can copy that code to prsent running file and chnage
or reset the code how we want"
and write like this
modul1.add=add
'''
import modul1
def add (x,y):
    return ("add is", x+y)
modul1.add=add

out1=modul1.add(100,10)
print(out1)

out=modul1.sub(1,2)
print(out)




print(modul1.add(10,10))
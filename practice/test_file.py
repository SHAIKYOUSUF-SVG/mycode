
import logging as log

log.basicConfig(filename="tests_output.log",level="DEBUG")

def add(x,y):
    log.info("testcase about adding two numbers")
    return x+y
def test_add():
    out=add(10,20)
    if out==30:
        assert True
        log.info("testcase passed")
    else:
        assert False
        log.error("testcase failed")


def squares(*obj):
    mylist=[]
    for i in obj:

        mylist.append(i*i)
    return mylist
def test_squares():
    out1=squares(1,2,3,4,5)
    if out1==[1,4,9,16,25]:
        assert True
    else:
        assert False

def mylist(*obj):
    list1=[]
    for i in obj:
        if i not in list1:
            list1.append((i))
    return list1
# out=list(1,2,3,4,5,1,2,3,4)
# print(out)
def test_list():
    out1=mylist(1,2,3,4,5)
    #out1=list1(mylist)

    if out1==[1,2,3,4,5]:
        assert True
    else:
        assert False

def base(*obj):
    oddlist=[]
    for i in obj:
        if i%2!=0:
            oddlist.append(i)
    return oddlist
def test_base():
    #for i in range(obj):
    out2=base(1,2,3,4,5,6,7,8,9,10)
    if out2==[1,3,5,7,9]:
        assert True
    else:
       assert False
def name1():
    global name,name2
    name='yousuf'
    name2="hi"
    print(name)

name="esuf"
name1()
print(name,"is global")
print(name2,"is global")

def name1():
    #global name
    name='yousuf'
    name2="hi"
    print(name)
name="esuf"
name1()
print(name,"is global")


def name2():
    #global city1,city2
    city1='hyd'
    city2='mumbai'
    print('locals are ',locals())
    print('globals are ',globals())
city3='bangalore'
city4='pune'
name2()



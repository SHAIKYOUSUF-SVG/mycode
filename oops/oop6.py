#constructor:__init__ getting called automatically
#when we initialize a class ,__init__ method will egt called auntomatically
#this is called as constructor/initializer
#this is used for initialization
class bank:
    def __init__(self):  #method
        #it will call automatically
        print("hey,i am in init")
    def test1(self):
        print("a")

b1=bank()
b2=bank()
b3=bank()

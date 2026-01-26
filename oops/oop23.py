#class attributes
#code inside bank code will be executed
class bank:
    print("a")
    counter=0
    def __init__(self,an):
        print("init")
        self.an=an
    def test1(self):
        print("test1")
b1=bank(123)
b1=bank(124)

fw=open("oop24.py","w")
fw.close()
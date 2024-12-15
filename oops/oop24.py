class bank:
    counter=0  #class attribute belongs to entire class
    def __init__(self,an,name):
        self.an=an  #this one is object attributes
        self.name=name
        bank.counter += 1
    def test1(self):
        return "this is yousuf"
b1=bank(123)
b2=bank(122)
print(b1.an)

fw=open("oop25.py","w")
fw.close()
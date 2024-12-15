#we can use class attributes any where
class bank:
    counter=0
    def __init__(self,an,name):
        print("init")
        self.an=an
        self.name=name
        bank.counter += 1
        print("counter is",bank.counter)

    def test1(self):
        return "this is yosuf"
b1=bank(123,'kiran')
b2=bank(123,'rahul')

fw=open("oop28.py", "w")
fw.close()
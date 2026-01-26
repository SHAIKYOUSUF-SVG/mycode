#another way to get called attributes without init? with different name not init

class student:
    def start(self,name,rno):
        self.name=name
        self.rno=rno

s1=student()
s1.start("kiran",1234)

print(s1.__dict__)

print(s1.get_name())
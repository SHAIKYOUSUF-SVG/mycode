#private attributes can not be accessed putside
#how to access private attributes using any trick?
#hoiw to a ccess private attributes from out side of the class
#private attributes are not stricrly privare we can acces them
class student:
    def __init__(self,name,rno):
        print("init")
        self.__name=name
        self.__rno=rno
    def get_name(self):
        return self.__name

s1=student("rakesh",1234)

#print(s1.__name)

print(s1._student__name) #to call private attributes form outside
print(s1.get_name())
s1._student__name="suresh"
print(s1.get_name())
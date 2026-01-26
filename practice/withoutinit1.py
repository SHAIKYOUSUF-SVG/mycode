class details:
    def a(self,name,gender,age,address):
        self.name=name
        self.gender=gender
        self.age=age
        self.address=address

class marks(details):
    def b(self,name,gender,age,address,maths,english,science,telugu,social):
        self.a(name,gender,age,address)
        self.maths=maths
        self.english=english
        self.science=science
        self.telugu=telugu
        self.social=social

#out=details()
#out.a('esuf','male',10,'ap')

student=marks()
student.b('esuf','male',15,'ap',91,78,67,89,56)

print(student.name)
print(student.gender)

print(student.age)

print(student.address)
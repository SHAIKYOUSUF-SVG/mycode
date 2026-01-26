class student:
    def get_name(self):
        return self.name
    def get_rno(self):
        return self.rno




s1=student()
s2=student()


s1.name="kiran"
s1.rno=1234



s2.name="ramesh"
s2.rno=124
print(s1.__dict__)


print(s2.__dict__)


print(s1.get_name())
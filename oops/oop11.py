'''
by using set method we can set any as we want like 1,0,"hi","guntur"
to aoide that we can wrote condition using regex
that is
'''
import re
class bank:
    def __init__(self,an,name,branch,balance):  #method
        self.an = an
        self.name = name
        self.branch = branch
        self.balance = balance
    def get_branch(self):
        return self.branch
    def set_branch(self,new_branch):
        if re.search("^[A-Z|a-z]{1,3}$",str(new_branch)):

            self.branch=new_branch

b1=bank(123,"ramesh","hsr",5000)


b1.set_branch(0)

print(b1.branch)


print(b1.get_branch())
print(b1.__dict__)


for i,j in b1.__dict__.items():
    print(i,j)
'''
inheritance:accessing properties of parent class from child class
or difining child class from parent class
'''
'''
salarybank(bank)-by this we can methods override/so that we can access properties of parent class
'''
'''
method overriding-methods written in parent class was over ridden by method written in child class
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
class salarybank(bank):
    def get_an(self):
        return self.an

b1=bank(123,"ramesh","hsr",5000)
s1=salarybank(122,"suresh","mth",6000)
out=s1.get_branch()
print(out) #mth [we get]
#in child class we didnt write get_branchmethod it takes from mail class this is method overridden


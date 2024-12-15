'''
child class can access properties of parent class but parent class cant access properties of child class
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
s1=salarybank(122,"suresh","mth","6000")

out=b1.get_an()
print(out) #'bank' object has no attribute 'get_an'
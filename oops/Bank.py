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
    def get_balance(self):
        return self.balance


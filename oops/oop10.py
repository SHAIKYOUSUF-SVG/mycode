#how to write get,set methods
class bank:
    def __init__(self,an,name,branch,balance):  #method
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    def get_branch(self):
        return self.branch
    def set_branch(self,new_branch):
        self.branch=new_branch

b1=bank(123,"ramesh","hsr",5000)
print(b1.get_branch())  #b1.get_branch()
b1.set_branch("guntur")
b1.set_branch(0)
print(b1.__dict__)



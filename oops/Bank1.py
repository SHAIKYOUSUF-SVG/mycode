class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
    def get_an(self):
        return self.an
    def get_balance(self):
        return self.balance
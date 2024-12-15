class bank:
    def __init__(self, an, name, branch, balance):
        self.an = an
        self.name = name
        self.branch = branch
        self.balance = balance

    def get_name(self):
        return self.name

    def get_branch(self):
        return self.branch


class salaryacc:
    def __init__(self, an, name, branch, balance, salary):
        self.an = an
        self.name = name
        self.branch = branch
        self.balance = balance
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_amt):
        if type(new_amt) == int:
            self.salary = new_amt


class me(bank, salaryacc):
    def __init__(self, an, name, branch, balance, salary):
        bank.__init__(self, an, name, branch, balance)
        salaryacc.__init__(self, an, name, branch, balance, salary)

    def get_an(self):
        return self.an


p = me(123, "yousuf", "pdrl", 0, 70000)
print(p.get_an())
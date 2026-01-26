#how to call objectmethods using class?
#can we call object method using class?
from Bank import bank
from salarybank2 import salarybank

b1=bank(123,"ramesh","hsr1",700)
b2=bank(123,"ramesh","hsr2",700)
s1=salarybank(123,"ramesh","hsr3",700,"tcs","23000")
#b1.get_branch() until now we call method using object
#we can call method using class also
print(bank.get_branch(b1))

print(salarybank.get_salary(s1))
'''when we call ovject methdo using class we must pass first agumnet as object:ob
ex:print(bank.get_branch(b1))'''

'''
until now we do object method
there are 2 more methods class method and static method'''
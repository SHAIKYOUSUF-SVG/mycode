'''
for calling private attributes we use methods
only through methods we can access private attributes
'''
'''
defining a class with private attributes will achive data hiding[we cant access the data directly from out side the class]
'''
import re
class bank:
    def __init__(self,an,name,branch,balance):  #method
        self.__an = an
        self.__name = name
        self.__branch = branch
        self.__balance = balance  #making attributes private
    def get_an(self):
        return self.__an
    def get_branch(self):
        return self.__branch
    def set_branch(self,new_branch):
        if re.search("^[A-Z|a-z]{1,3}$",str(new_branch)):

            self.__branch=new_branch

b1=bank(123,"ramesh","hsr",5000)

'''encapsulation:
defining attributes as private and access them through the methods
is called encapsulation'''
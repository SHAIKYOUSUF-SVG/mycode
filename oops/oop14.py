'''
what is 'closed class?'
if we make attributes private and do not define any method the that class act as closed class
'''

class bank:
    def __init__(self,an,name,branchm,balance):
        self.__an=an
        self.__name=name
        self.__branch=branch
        self.__balance=balance

b1=bank(123,"yousuf","pdrl",9000)

#after making private attributes if we dont write any method it is called as closed class
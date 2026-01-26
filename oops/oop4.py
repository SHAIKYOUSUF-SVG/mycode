class Bank:
    def test1(self):  #takes arguments
        print("a")
    def test2(self):
        print("b")

b1=Bank()
b2=Bank()
'''when we calling method using object(b1),internally object will be passed as first argument  test1(b1) that why we must 
write in methods also 1 agument that may be anything. mostly  we write self'''
b1.test1()  #test1(b1) passing 1 argument
b2.test1()
'''
how call methods
ex:x=[]
x.append()
x.insert()  
here we assaing list with x and similarly we assaign bank with b1/b2 anything we want
b1.test1()
'''
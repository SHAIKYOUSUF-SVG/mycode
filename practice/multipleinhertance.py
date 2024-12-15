#multiinheritance:acccessing properties of 2 parent clss from 1 child class
#it is the process of cerating child class from more than 1 parent class

class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_an(self):
        return (slef.an)
class creditlimit:
    def get_creditlimt(self):
        return 50000
    def get_name(self):
        print("from creditkimt")
        return self.name

class salarybank(bank,creditlimit):
    def get_name(self):
        super().get_name()
        print("from salary bank")
        return self.name

s1=salarybank(123,"rajesh")
out=s1.get_name()
print(out)

#################################################

class A:
    def __init__(self,arg1):
        self.arg1=arg1
class B:
    def __init__(self,arg2):
        self.arg2=arg2

class C(A,B):
    def __init__(self,arg3):
        self.arg3=arg3
        A.__init__(arg1)
        #super().__init__(arg1)
        b.__init__(arg2)
        #super().__init__(arg2):


##################################################################

#multiple inheritance
class server:
    def __init__(self,bmc,bios,cpld):
        self.bmc=bmc
        self.bios=bios
        self.cpld=cpld
    def get_bios(self):
        return self.bios
    def get_bmc(self):
        return self.bmc
    def get_cpld(self):
        return self.cpld
class desktop:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def get_cpu(self):
        return self.cpu
class storage(server,desktop):
    def __init__(self,bmc,bios,cpld,cpu,ram,ioms):
        #server.__init__(self,bmc,bios,cpld)
        super().__init__(bmc,bios,cpld)
        desktop.__init__(self,cpu,ram)
        #super().__init__(cpu,ram)
        self.ioms=ioms
    def get_ioms(self):
        return self.ioms
    def get_bmc(self):
        print("from storage class")
        super().get_bmc()
        return self.bmc


s=storage('bmc1','bios1','cpld1','cpu1','ram1','ioms1')

out=s.get_bios()
print(out)


print(s.get_cpu())

print(s.get_bmc())


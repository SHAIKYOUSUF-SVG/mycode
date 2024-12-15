#__del__
# destructor-used for deleting/destroying th object
# ,after running constuctor destructor will auto matically runs
#it will not show to look use __del__.it will alos auto called
class animals:
    def __init__(self,wild,domestic,sea):
        print("constructor")
        self.wild=wild
        self.domestic=domestic
        self.sea=sea
    def __del__(self):
        print("deleting...")

out=animals('lion','cow','fish')
out1=animals('lion','cow','fish')


class animals:
    def __init__(self,wild,domestic,sea):
        print("constructorrrr")
        self.wild=wild
        self.domestic=domestic
        self.sea=sea
    def __del__(self):
        print("deleting...")

out=animals('lion','cow','fish')
out1=animals('lion','cow','fish')
del(out1)
print("############")


'''
__init__ constuctor
__del__ destructor
__new__ used to create instances of class
__iter__in iterator this run for 1st time
__next__ in iteration after __iter__,__next__ will iterfor loop, this is infinite loop
__all__ used inside modules files for which 1 to import from a bulk
__add__ used addition operator
__str__ used to return a string
__len__  will returns the length of
__getitem__(self,index) enables indexing to access
__setitem__(self,index,new_value) enables setting values
__delitem__(self,index) enables delete using index
'''
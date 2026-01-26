#top level class
class bank:
    def __init__(self,an):
        self.an=an

b1=bank(123)
print(bank.mro())
#[<class '__main__.bank'>, <class 'object'>]

#how to get  all class attributes?
#how to get all object attributes?
#object.__dict__

class school:
    school_name="sdm"
    school_type="private"
    school_principal="ajay"
    def __init__(self,an,name):
        self.aan=an
        self.name=name
#print(vars(school))###########
out=[i for i in vars(school).items() if (not i[0].startswith("__") and not i[0].endswith("__"))]
print(out)
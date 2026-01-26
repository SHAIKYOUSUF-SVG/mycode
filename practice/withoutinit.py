#how to initialize attributes with out using constructer


class animals:
    def start(self,wild,domestic,sea):
        self.wild=wild
        self.domestic=domestic
        self.sea=sea

out=animals()
out.start('lion','cow','fish')
#animals.start(out,'lion','cow','fish') it will not work
print(out.wild)


class school:
    def start(self,teacher1,teacher2):
        self.teacher1=teacher1
        self.teacher2=teacher2
        self.hm="abcd"
out=school()
out.start("ravi","kiran")
print(out.teacher1)
print(out.hm)

#how to initialize/create attributes without using __init__
class deatils:
    def get_name(self):
        return self.name
    def get_roll(self):
        return self.roll

out=deatils()
out.name="kiran"
out.roll=123
print(out.__dict__)
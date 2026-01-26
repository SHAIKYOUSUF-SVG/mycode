class school:
    name="xyz"
    __sclid="123454"
    def start(self,teacher1,teacher2):
        self.__teacher1=teacher1
        self.__teacher2=teacher2
        self.hm="abcd"
    def get_mth1(self):
        return self.__teacher1
    def __get_mth2(self):
        return self.__teacher2
out=school()
out.start("ravi","kiran")

print(out._school__teacher1)


print(out._school__teacher2)

print(out._school__get_mth2())


print(school.name)
print(out._school__sclid)
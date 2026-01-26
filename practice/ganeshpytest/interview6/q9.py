
class test:
    def __init__(self,*args):
        self.data=[]
        for i in args:
            if type(i) ==int:
                self.data.append(i)
    def __add__(a1, a2):

        print("hi in add method")
        print(a1.data, a2.data)
        all_data=a1.data+a2.data
        print("@@@@@@@@@@@@@@")
        print(all_data)
        print("############")
        out=sum(all_data)

        print(sum(all_data))
        print("$$$$$$$$$$$")
        print(out)
        return out


t1=test(10,20,30,"india",40)
t2=test(11,2,3,4,5)

out=t1 + t2  #here t1,t2 are test type
print(out)
#write a programe that genrate sqaures:
class squares:
    def __init__(self,x,y):
        self.list=[]
        for i in range(x,y+1):
            self.list.append(i*i)

    def __str__(self):
       return str(self.list)



x=squares(2,10)
#print(x.list)
print(x)
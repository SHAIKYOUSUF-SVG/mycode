class server:
    def display(self):
        print('this is server dispaly')
class pc(server):
    def display(self):
        print('this is pc dispaly')
class mobile(pc):

    def display(self):
        super().display()
        #print('this is mobile display')
out=mobile()
print(out.display())
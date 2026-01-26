#2.how to intialize/cerate attributes with out using __init__?
#__init__ is constuctor whih will automatically get called  when obj initialized
#science automatically getting cal;lled,we can using for initializing attributes
#advamtage is we donot need to call it ourself



class student:
    def __init__(self,name,rno):
        print("init")
        self.name=name
        self.rno=rno

s1=student("rakesh",1234)

#__dict__ will called all attributes
print(s1.__dict__)



#filter:FILTER SOME DATA THE FROM DATA
#FILTER CSan work for list comprohension also

#list comprohesion:
data=[10,20,"ab"]
out=[i for i in data if type(i)==int]
print(out)
#using same in filetr:used to remove unwanted objects from iterators
#out=filter(func,iterator)
'''
take obj from data-ex:10
    pass it to lambda function
        execute function
        if funtion returns True
            store i in out   here i will come in output
'''
import sys
out=filter(lambda i:True if type(i)== int else False,data)
print(out)
print(list(out),sys.getsizeof(list(out)))
'''
os.getsixeof()-to get size of file
sys.getsizeof()-to get the size of object
'''
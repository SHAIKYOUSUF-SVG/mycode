import q11   #for this module we get out result also


'''
whatr is the use of __name__?
how toi use a python file like module as well as a script'''

'''
python q11.py here q11.py is called as 'main script'
'''
import q11
#value of __name__ will be __main__ if it is main script
print("q12",__name__)  #output __main__

print(q11.add(10,10))


fw=open("q13.py","w")
fw.close()
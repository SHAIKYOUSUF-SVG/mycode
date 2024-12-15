#from file handling

'''
what is with keyword?
we can open using open function
we can open files "with" word also
'''

fr=open("data.txt")  #here fr is called as file handler
out=fr.read()
fr.close()


print(out)
o=fr.closed
print(o)
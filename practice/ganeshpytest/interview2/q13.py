'''
in a file there are modules and code also
if we import that file as module then code also run
how to import module  with our run the code
if __name__="__main__":
with this condion we can import only module and code will not import
here conding what syas is:
 if  __name__ is main script means thte module is running
 then run the cod elaso
 if it is not a main script then only impoer module code will not run
'''

'''
if __name__=="__main__":
if this not wrote in mdule file
and running in another file as module thet the code inside this module filke
also run 
to avoid that we wropte this condtion
'''

import q11


print(q11.add(1,2))

fw=open("q14.py","w")
fw.close()
'''
q2.how to load the module which is from other drive perminantly?
when we need to import the same module in several files,if someone change
the name of that module or change address then it not work
then how to fix:that is
1.go to environ setup
2.wrote PYTHONPATH
and in next box copy that particular path
"after doing this we must close and reopen the pycharm or notepad or something
otherwise it will not work"

'''

import sys
sys.path.insert(0,r"C:\python\pycharm\pytest\case2\codes")

import arith1

print(arith1.add(1,10))
print(arith1.sub(1,10))

'''
regularly asked questions from modules :
what is sys.path
different way to load module
    import ggg
    import ggg as g
    from file import *
    how to create a package
'''


'''
how to load a file/module that dont have .py extention?
'''

import imp

a=imp.load_source("modul1.txt",r"C:\python\pycharm\interview\inetrview1")
print(modul1.add(10,100))

'''
import imp
imp.load_source("filemname","that file path")
'''
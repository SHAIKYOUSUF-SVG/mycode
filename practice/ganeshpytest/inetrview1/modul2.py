'''
module can reload again and again?
no,it will load only once
"if you change the module or add somemore after load the module,then it will not take new data"
we needs to reload that :for that
in cmd prompt

"import importlib
importlib.reload(module_name)" we have write 2lines and then it will reload the module

'''
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x / y


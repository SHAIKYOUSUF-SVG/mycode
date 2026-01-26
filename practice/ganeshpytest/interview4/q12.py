#functool reduce

import functools
data=[10,20,30,40]
out=functools.reduce(lambda i,j: i+j ,data)
print(out)  #100





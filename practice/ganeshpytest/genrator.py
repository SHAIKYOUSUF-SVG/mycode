import sys
import time
start=time.time()

def squares(x,y):
    for i in range(x,y+1):
        yield i*i


out=squares(1,10000000000000)
end=time.time()
ttime=end-start
print(ttime,'seconds')
size=sys.getsizeof(out)
print(size,'bytes')
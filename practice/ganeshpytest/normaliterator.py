#normal iterator
import sys
import time
st=time.time()
def sq(x,y):
    l=[]
    for i in range(x,y+1):
        l.append(i*i)
    return l
out=sq(1,1000000000000)
#print(out)
end=time.time()
ttime=end-st
print(ttime,'seconds')
size=sys.getsizeof(out)
print(size,'bytes')
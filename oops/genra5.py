import time
import sys
'''start=time.time()

def test1(x,y):
    for i in range(x,y+1):
        yield(i*i)


a=test1(2,1000)
end=time.time()
out=start-end
print(out)
size=get sizeof(out)
print('size is',size)
'''
start=time.time()
def squares(x,y):
    for i in range(x,y+1):
        yield(i*i)

a=squares(2,1000)
end=time.time()   #5 secinds
out=start-end
print(out)

size=sys.getsizeof(out)  #232 bytes
print(out,"bytes")

#it will take less and less size compare to normal iterator
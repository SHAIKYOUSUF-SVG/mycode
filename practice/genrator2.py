# def squares1(x,y):
#     for i in range(x,y+1):
#         yield i*i
# out2=squares1(2,10)
# print(next(out2))
# for i in out2:
#     print(i)

import time
import sys
start=time.time()
def cubes(x,y):
    for i in range(x,y+1):
        yield i*i*i
out=cubes(2,1000000000000000000000000000)
end=time.time()
time=end-start
print(time,"seconds")
print(sys.getsizeof(out))


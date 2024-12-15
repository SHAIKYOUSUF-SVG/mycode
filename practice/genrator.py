#genratoir is an type of iterator used to get the sequence of values
#in genrator we use yield insted of return
#yeild will pass the iteratoation at yield line
#data will be witten on the flow
#with gen how to create
#low run time
#it will restart the loop from where we stop the iteration

#example for genrator
def tests():
    print("a")
    yield 10  #equals to return
    print("b")
    yield 20
out=tests()
print(next(out))
#iteratoion will strat from where it was stopped
print(next(out))



def tests1():
    print("q")
    yield 32
    print("q")
    yield 23
x=tests1()

print(next(x))



#gerntaing squres

def squares(x,y):
    for i in range(x,y+1):
        yield i*i
out=squares(2,10)
for i in out:  #best way to iterate in genration
    print(i)
    #input()#to control oputput
import sys
import time
start=time.time()
def squares(x,y):
    for i in range(x,y+1):
        yield i*i

a=squares(2,100000000000)
end=time.time()
out=start-end
print(f"{out} seconds")
out1=sys.getsizeof(a)
print(f"{out1} bytes")


#genrator is type of iterator when compared to normal iterator in consumes less memory and less time.we use yield
# satetment insted of return we use yield in genrator




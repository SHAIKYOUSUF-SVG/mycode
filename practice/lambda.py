'''
lambda is function it defined in a single line
map:mao is built in funcgtion used to chage the values of iterable
filter:built in function used to get/remove wanted data
redunce:defined in functools it will take 2 arguments a funtion an itarable and it return into a singel value
'''

#lambda
out=lambda x,y: x+y
print(out(1,2))

li=(lambda a,b: a**b)
print(li(2,33))

#map
data=[10,20,30]
out=map(lambda x:x+2,data)
print(list(out))

#filter
out=filter(lambda x:x%2==0,data)
print(list(out))


#reduce
import functools
out=functools.reduce(lambda i,j:i+j,data)
print(out)


#listcomprohension:it will create lsits effectively with in singel loine code
out=[i*2 for i in range(1,10)]
print(out)

#dictionary comprohension:it will create dictionries effectively with the silngle line code
out={i:i+2 for i in range(1,10)}
print(out)

'''
what is oops?
object orientd programing language is way of constructing the code in classes,
objects,method,contructor
easy to understand
reusabilty
we can inherit methods 
principle of data hinding helps the programer to build secure programes'''
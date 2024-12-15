
import time
def func(x):
    def wrapper(*args):
        start=time.time()
        for a in args:
            if not isinstance(a,int):
                return 'invalid statement'
        out = x(*args)
        end=time.time()
        ttime=end-start

        return out,ttime
    return wrapper

@func
def gen(x,y):
    time.sleep(10)
    yield x*y

out,ttime=gen(89,98)
for i in out:
    print(i)
print(ttime,'seconds')


#chapgpt


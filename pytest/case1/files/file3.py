def test_prime(*args):
    k=True
    for num in args:
        if num<2:
            continue
    for i in range(2,num):
        if num%i==0:
            k=False
            break
    if k:
        return 'prime'


out=test_prime(2,3,4,5,6,7,8,90)
print(out)
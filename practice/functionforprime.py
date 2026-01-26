def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime_numbers_up_to(limit):
    prime_list=[]
    for num in range(2,limit):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

limit=100
prime_list=prime_numbers_up_to(limit)
print(prime_list)



# l = []
# for i in range(101):
#
#     l.append(i)
#     out=l[::2]
#     out1=l[1::2]
# print(out1)
# print(out)

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime_list(limit):
    l=[]
    for num in range(2,limit):
        if is_prime(num):
            l.append(num)
    return l
limit=200
out=prime_list(limit)
print(out)

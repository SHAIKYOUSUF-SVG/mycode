def is_leap(year):
    leap=True
    if year%4!=0:
        leap=False,'not a leap year'
    return leap


out=int(input())
print(is_leap(out))


def is_leap(year):
    leap = False
    if year%4==0 and year%100==0:
        if year%400==0:
            leap=True
    elif year%4==0 and year%100!=0:
        leap=True

    return leap

year = int(input())
print(is_leap(year))

records = [['chi', 20.0], ['beta', 50.0], ['alpha', 50.0]]
a = []
for i in records:
    for j in i:
        if type(i) == float:
            i = int(i)
            a.append(i)
            print(a)
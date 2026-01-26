def decorate_func(func1):
    def wrapper(*args):
        print(f'total args are {len(args)}')
        return func1(*args)
    return wrapper


@decorate_func
def main_func(*args):
    return sum(args)

out=main_func(1,2,3,4,5)
print(out)



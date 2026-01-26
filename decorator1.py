
'''
decorators:
decorator is a function which is used to add extra functionality to the existing function without modifying

decorators are function inside a function
decorators will take function name as argument
we need to decorate mian function with decorator
syntax:@decorator
'''

def decorator_func(f1):
    def wrapper():
        print('this is extra functionality before normal function')
        f1()
        print('this is extra functionality after normal function')
    return wrapper

@decorator_func
def main_function():
    print('main function')



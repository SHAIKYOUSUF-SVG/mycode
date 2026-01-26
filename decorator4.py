def dec_function(a1):
    def wrapper(a,b):
        a +=100
        b +=100
        result=a1(a,b)
        return result
    return wrapper

@dec_function
def main_code(a,b):
    return a+b
out=main_code(10,20)
print(out)



def dec_function(a1):
    def wrapper(a, b):
        # Modifying the input values
        a += 100
        b += 100
        # Calling the original function with modified arguments
        result = a1(a, b)
        return result
    return wrapper

@dec_function
def main_code(a, b):
    return a + b

# Calling the decorated function
out = main_code(10, 20)
print(out)

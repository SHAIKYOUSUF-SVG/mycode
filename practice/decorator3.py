import time

def func(x):
    def wrapper(*args):
        start = time.time()  # Start timer

        # Argument validation
        for a in args:
            if not isinstance(a, int):
                return 'invalid statement'

        # Create the generator and measure time
        out = x(*args)
        end = time.time()  # End timer
        ttime = end - start  # Time difference

        return out, ttime  # Return generator and time

    return wrapper

@func
def gen(x, y):
    time.sleep(10)  # Simulate a delay
    yield x * y

# Unpack the result (out is the generator, ttime is the time taken)
out, ttime = gen(89, 98)

# Iterate through the generator
for i in out:
    print(i)  # Output the product

# Print the time taken
print(f"Time taken: {ttime} seconds")

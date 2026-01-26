#what is named arguments and how use it?
#passing parameter in function with argyment name
#calling the function by passing arguments by their names

def test(name,number):
    print(f"number is {number}")
    print(f"name is {name}")
    print('###################')

cap="virat kohli"
score=500


test(number=score,name=cap)
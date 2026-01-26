#how to make arguments optional in named arguments?



def test(name="sachin",number=0):  #we need to write default
    print(f"number is {number}")
    print(f"name is {name}")
    print('###################')

cap="virat kohli"
score=500


test(number=score)
test()
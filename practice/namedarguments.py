#whta is named arguments
'''
calling the funtion by passing arguments by their names
'''
def test(number,name):
    print(f"name is {name}")
    print(f"number is {number}")

a="virat"
score=900

test(a,score)

print("#####################")

def test(name,number):
    print(f"name is {name}")
    print(f"number is {number}")

a="virat"
score=900

test(name=a,number=score)
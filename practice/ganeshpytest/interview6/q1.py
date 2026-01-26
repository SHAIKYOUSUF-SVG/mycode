#1.what is named arguments? and uses of it



#in fucntion give args amnd takes args ,ust be  in order,it will takes blind according to order
#there is no freedom of oraer
#ex:
def test(name,number):
    print(f"number is {number}")
    print(f"name is {name}")
    print('###################')

cap="virat kohli"
score=500

test(cap,score)
test(score,cap)
'''
ouput:
number is 500
name is virat kohli
###################
number is virat kohli
name is 500
###################
'''

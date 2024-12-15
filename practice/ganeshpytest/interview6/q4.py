#how to pass dictinary{} to kwywprd arguments

def test(**kwargs):
    print(f"kwargs are {kwargs}")
    print("###################")

test(a=10,b=20,c=30)  #like thsi if give
#if wehave take {} then how to wroite

data={'a':10,'b':20,'c':30}  #for this
test(**data)  #give ** to data
'''
kwargs are {'a': 10, 'b': 20, 'c': 30}
###################
kwargs are {'a': 10, 'b': 20, 'c': 30}
###################

'''
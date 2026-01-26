def check_anagram(func):
    def wrapper(a,b):
        if len(a)!=len(b):
            return 'not anagram'
        if sorted(a)==sorted(b):
            return 'anagram'
    return wrapper


@check_anagram
def anagram(a,b):
    return a,b
print(anagram('silent','listen'))
print(anagram('hello', 'world'))


# l=[1,2,3,45,5]
# print(l)
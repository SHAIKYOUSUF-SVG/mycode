# from para2 import sshclient
# from para21 import mainlib
#import pytest
# def test_biosinfo():
#     out = mainlib()
#     out1 = out.get_bios()
#
#     # You could assert that out1 is not None or not empty, depending on the expected result.
#     assert out1 is not None, "Expected BIOS info but got None."
#     assert isinstance(out1, dict), "Expected BIOS info to be a dictionary."
#     # You can add more specific assertions depending on what get_bios() is supposed to return.


def add(x,y):
    return x+y

def test_add():
    z=add(10,12)
    if z==22:
        assert True
    else:
        assert False
def common(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c
def test_common():
    a=[1,2,3]
    b=[2,3]
    out=common(a,b)
    if out==[2,3]:
        assert True
    else:
        assert False
def even(x):
    y=[]
    for i in x:
        if i%2==0:
            y.append(i)
    return y
def test_even():
    a=[1,2,3,4]
    out=even(a)
    if out==[2,4]:
        assert True
    else:
        assert False


def test_prime():
    k=True
    num=2
    for i in range(2,num):
        if num%i==0:
            assert False
    if k:
        assert True

def prime1(x,y):
    l = []
    for num in range(x,y):
        if num>1:
            k=True
            for i in range(2,num):
                if num%i==0:
                    k=False
                    break
            if k:
                l.append(num)
    return l

def test_prime1():
    out = prime1(2, 5)  # Testing for numbers between 2 and 10
    if out == [2, 3]:
        assert True
    else:
        assert False
        # f"Test failed: Expected [2, 3, 5, 7], but got {out}"







# def prime1(x, y):
#     l = []
#     for num in range(x, y):
#         if num > 1:  # Skip 0 and 1 as they are not prime
#             k = True
#             for i in range(2, int(num**0.5) + 1):
#                 if num % i == 0:
#                     k = False
#                     break
#             if k:
#                 l.append(num)
#     return l
#
# def test_prime1():
#     out = prime1(2, 10)  # Testing for numbers between 2 and 10
#     assert out == [2, 3, 5, 7], f"Test failed: Expected [2, 3, 5, 7], but got {out}"
#
# # Running the test
# test_prime1()

def uniq(x,y):
    z=[]
    for i in x:
        if i not in y:
            z.append(i)
    return z

def test_unq():
    a=[1,2,3]
    b=[1,4,5]
    out=uniq(a,b)
    assert out==[2,3],f"test failed:expected [1] but got {out}"

def dicttostr(dict):
    str=''
    for i,j in dict.items():
        str+=f'{i}={j}?'
    return str.rstrip('?')

def test_dicttostr():
    out=dicttostr({'p2': 10, 'p4': 50, 'p1': 80})
    if out=="p2=10?p4=50?p1=80":
        assert True
    else:
        assert False

def remove_duplictae(list):
    l=[]
    for i in list:
        if i not in l:
            l.append(i)
    return l

def test_remove_duplictae():
    out=remove_duplictae(["ajay", "ramesh", "kiran", "ramesh", "ramesh"])
    if out==['ajay','ramesh','kiran']:
        assert True
    else:
        assert False

def replace(list,item,item1):
    l=[]
    for i in list:
        if i == item:
            l.append(item1)
        else:
            l.append(i)
    return l
    # return [item1 if i == item else i for i in list]


def test_replace():
    l=replace(["india", "uk", "austria", "germany", "uk"],'uk','usa')
    if l==["india", "usa", "austria", "germany", "usa"]:
        assert True
    else:
        assert False

def remove_duplicates(list,arg):
    return [i for i in list if i!=arg]
def test_remove_duplicates():
    out=remove_duplicates(["ajay", "ramesh", "kiran", "ramesh", "ramesh"],"ramesh")
    if out==['ajay','kiran']:
        assert True
    else:
        assert False


def remove_second_occurance(data,arg):
    count=0
    for i in range(len(data)):
        if data[i]==arg:
            count+=1
            if count==2:
                data.pop(i)
                break
    return data
def test_remove_second_occurance():
    out=remove_second_occurance(["ajay", "ramesh", "kiran", "ramesh", "ajay", "ramesh"],'ramesh')
    if out==['ajay','ramesh','kiran','ajay','ramesh']:
        assert True
    else:
        assert False
def remove_white_space(inp):
    temp=[]
    for i in inp:
        i=i.strip()
        temp.append(i)
    return temp
def test_remove_white_space():
    out=remove_white_space(['   test   ', 'abc  ', '   testend'])
    if out==['test', 'abc', 'testend']:
        assert True
    else:
        assert False

def reverse_dict_items(data):
    return {j:i for i,j in data.items()}
def test_reverse_dict_items():
    out=reverse_dict_items({12:3, 5:6, 100:200})
    if out=={3:12, 6:5, 200:100}:
        assert True
    else:
        assert False

def reverse_list(ls):
    return ls[::-1]
def test_reverse_list():
    out=reverse_list([1,2,3])
    if out==[3,2,1]:
        assert True
    else:
        assert False

def remove_spaces_dictkeys(data):
    return {i.strip():j for i,j in data.items()}
def test_remove_spaces_dictkeys():
    out=remove_spaces_dictkeys({'key1  ': 1, '   key2': 3, '  key3  ': 2})
    if out=={'key1': 1, 'key2': 3, 'key3': 2}:
        assert True
    else:
        assert False

def match_dicts(data1,data2):
    data3={}
    for i,j in data1.items():
        if i in data2.keys():
            data3[i]=j
    return data3
def test_match_dicts():
    out=match_dicts({'key1': 1, 'key2': 3, 'key3': 2},{'key1': 1, 'key2': 2})
    if out=={'key1': 1, 'key2': 3}:
        assert True
    else:
        assert False

def uniq_values_from_dict(data):
    ll=[]
    for i in data:
        for j in i.values():
            if j not in ll:
                ll.append(j)
    return set(ll)
def test_uniq_values_from_dict():
    out=uniq_values_from_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])
    if out=={'S005', 'S002', 'S007', 'S001', 'S009'}:
        assert True
    else:
        assert False

def add_two_dict(d1,d2):
    #d3={}
    for i, j in d2.items():
        if i in d1.keys():
            d1[i] += j
        else:
            d1[i] = j
    return d1
def test_add_two_dict():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    out=add_two_dict(d1,d2)
    if out=={'a': 400, 'b': 400, 'c': 300, 'd': 400}:
        assert True
    else:
        assert False

def get_largest(list1):
    largest=list1[0]
    for i in list1:
        if i>largest:
            largest=i
    return largest
def test_get_largest():
    out=get_largest([3,4,1,3])
    if out==4:
        assert True
    else:
        assert False

def count_no_of_char(list2):
    count=0
    for i in list2:
        if i[0]==i[-1] and len(i)>=2:
            count+=1
    return count
def test_count_no_of_char():
    out=count_no_of_char(['abc', 'xyz', 'aba', '1221'])
    if out==2:
        assert True
    else:
        assert False

def remove_duplicates1(list3):
    l=[]
    for i in list3:
        if i not in l:
            l.append(i)
    return l
def test_remove_duplicate1():
    out=remove_duplicates1([11,2,11,3,4,4,1,1,1])
    if out==[11,2,3,4,1]:
        assert True
    else:
        assert False


def get_rep(ls):
    d={}
    for i in ls:
        d[i]=ls.count(i)
    return d
def test_get_rep():
    out=get_rep([11,2,3,4,4,1,1,1])
    if out=={ 11:1, 2:1, 3:1, 4:2, 1:3 }:
        assert True
    else:
        assert False




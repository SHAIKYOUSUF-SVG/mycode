'''
1. Write a Python program to sum all the items in a list.
# use only for loop (not by using 'sum' function)
x = [3,4,1,3]
# output => 1
'''
x=[3,4,1,3]
z=0
for i in x:
    z=z+i
print(z)


'''
2. Write a Python program to multiplies all the items in a list
x = [3,4,1,3]
# output => 36
'''
y=1
for i in x:
    y=y*i
print(y)
print("@@@@@@@@")
'''
3. Write a Python program to get the largest number from a list.
x = [3,4,1,3]
# output => 4'''
maxvalue=x[0]
for i in x:  #3
    if i>maxvalue: #3>0
        print(i)
        #num = num + i


'''
4. Write a Python program to count the number of strings 'where the string length is 2 or more and the first and last character are same from a given list of strings.' 
Sample List : data = ['abc', 'xyz', 'aba', '1221']'''
data = ['abc', 'xyz', 'aba', '1221']
count=0
for i in data:
    if len(i)>=2 and i[0]==i[-1]:
       count=count+1
print(count)

'''
5. Write a Python program to remove duplicates from a list.
alist = [11,2,11,3,4,4,1,1,1]'''
alist = [11,2,11,3,4,4,1,1,1]
d=[]
for i in alist:
    if i not in d:
        d.append(i)
print(d)
######################
d = {}
for i in range(len(alist)):  #0,1,2,3,4,5,6,7,8
    d[alist[i]] = 1  #dict will not allow duplicates keys so that why this method

print(d)

l1=[1,2,3,4,54,5,2,1,2,34,5,6,2,1,232,3,4,5,1,232,4]
dict={}
for i in l1:
    dict[i]=1
print(dict)

'''

6. Write a Python program to print the numbers of from specified list after removing even numbers from it.
alist = [11,2,3,4,4,1,1,1]
# Expected out = [11,3,1,1,1]'''
list1=[]
for i in alist:
    if i%2!=0 and i not in list1:
        list1.append(i)
print(list1)

'''
8. Write a Python program to find common elements from two lists
x = [11,22,33]
y = [12,22,33]
# Expected out = [22,33]'''
x = [11,22,33]
y = [12,22,33]
z=[]
for i in x:
    if i  in y:
        z.append(i)
print(z)

'''
9. Write a Python program to convert a list of elements into a string (should work for any 1 dimensional list)
a = ['a', 'c', 'c', 23, 1,'d']
# sample string = "acc231d"'''
a = ['a', 'c', 'c',23,1,'d']
out = ""
for i in a:
    out = out + str(i)
print(out)


b=[1,2,"a","w","e","r","eqw"]
c=""
for i in b:
    c=c+str(i)
print(c)


str1="yousuf"
out=str1+str(123)
print(out)

str2="hi this is yousuf"
str3=9989549088
out=str2+' '+str(str3)
print(out)


a="abcd"
b=1234
a=a+str(b)
print(a)


#10. Write a Python program to get the frequency of the elements in a list.
alist = [11,2,3,4,4,1,1,1]
# sample =>  { 11:1, 2:1, 3:1, 4:2, 1:3 }
dict={}
for i in alist:
    dict[i]=alist.count(i)
print(dict)

a=[1,2,3,4,5,6,1,2,3,4,3,4,1,2,3,5,1,3,2,1,2,4,1,2,3]

dict={}
for i in a:
    dict[i]=a.count(i)
print(dict)




#11. Write a Python program to insert an element before each element of a list.
# alist = [4, 5, 6]
# a = 10
# # alist.insert(0,a)
# # print(alist)
#
# for i in range(len(alist)):
#     alist.append(a)
#
# print(alist)



#12. Write a Python program to replace the last element in a list with another list.
#Sample data :
x = [1, 3, 5, 7, 9, 10]
y = [2, 4, 6, 8]
#Expected Output: x = [1, 3, 5, 7, 9, 2, 4, 6, 8]
for i in x:
    x[-1]=y
print(x)


'''
13. Write a Python program to insert a given string at the beginning of all items in a list. -> done
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
inp = [1,2,3,4]
out = []
for i in inp:
    out.append('emp'+str(i))
print(out)

14. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

15. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
inp = 'restrart'
# in above string string first character is 'r' (replace all 'r' with '$' except first 'r')
Expected Result : 'rest$a$t'
********************************************
inp = 'restrart'
out = inp[0] + inp[1:].replace(inp[0],"$")
print(out)
********************************************

16. Write a Python program to count and display the vowels of a given text.
a = "atest string for finding i vowels"

17. Write a Python program to iterate over dictionaries using for loops.
data = {1:2,34:56, 67:9}
# Expected below output
1 2
34 56
67 9

18. Write a Python script to create a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. - done
Sample Dictionary 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

19. Write a Python program to map two lists into a dictionary.
a = ['a', 'b', 'c']
b = [1,2,3]
# sample : {'a':1, 'b':2, 'c':3}

20. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}


21. Write a Python program to print all unique values in a dictionary. Try after 3rd chapter
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

22. Write a Python program to remove spaces from dictionary keys.
data = {'key1  ': 1, '   key2': 3, '  key3  ': 2}
# sample = {'key1': 1, 'key2': 3, 'key3': 2}

23. Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: out = {key1: 1} is present in both x and y
(extract common key value pairs from 2 dict)
dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}
dict3 = {}
for i in dict1:
    if i in dict2:
        if dict1[i] == dict2[i]:
            dict3[i] = dict1[i]
print(dict3)

24. Write a program to reverse a list without using builtins
a = [1,2,3]
# sample : [3,2,1]
data = [11,22,33,44,55,66]
#data.reverse()

out = []

for i in range(len(data)-1,-1,-1): # 5,4,3,2,1,0
    #print(i,data[i])
    out.append(data[i])
print(out)

25. Write a program to reverse a dict( value should be keys & keys should be values) - Assuming values are unique
data = {12:3, 5:6, 100:200}
# Expected output
data = {3:12, 6:5, 200:100}

26. Find the key of largest value in below dict
data = {3:12, 6:5, 4:100}
# Expected output => 4

28. Create a output dictionary from below 2 dicts
# values of data1 should be key & corresponding values from data2 should be values
# Example:: (Assuming elements are unique)
data1 = {1:2, 4:5, 3:9}
data2 = {4:8, 3:10, 1:15}

output dict => out = {2:15, 5:8, 9:10}

29. Write a program to strip a list *
inp = ['   test   ', 'abc  ', '   testend']
# Expected output => inp = ['test', 'abc', 'testend']

30. Write a program to create a dict from keyboard input (create dict of 5 elements) and print the dict using while loop

31) Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


32) Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

33) Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

        *
       ***
      *****
     *******
      *****
       ***
        *
pattern = 10

for i in range(1, pattern+1): # 1,2,3,4,5,6,7,8,9,10
    print("*" * i)

for i in range(pattern-1,0,-1): # 9,8,7,6,5,4,3,2,1
    print("*" * i)

35) Write a Python program that prints all the numbers from 0 to 6 except 3 and 8.
Expected Output : 0 1 2 4 5 7 8
35) Given a sequence of number like below
inp = [4,5,7,8,9,2]
write a program to find missing objects between min and max number from above sequence
expected output => 3,6

start = min(inp)
end = max(inp)

step1: take each object from start to end
step2: ------

36)  Write a Python program to create the multiplication table (from 1 to 10) of a number.
Expected Output:
Input a number: 6                                                       
6 x 1 = 6                                                              
6 x 2 = 12                                                              
6 x 3 = 18                                                              
6 x 4 = 24                                                              
6 x 5 = 30                                                              
6 x 6 = 36                                                              
6 x 7 = 42                                                              
6 x 8 = 48                                                              
6 x 9 = 54                                                              
6 x 10 = 60

37) Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999

38)(try after learning about command line arguments) Accept 3 inputs from the command line <no1> <operator> <no2>
Perform the operation depending on variable
# Assume program name you have written is = arith.py
executing as below
python arith 10 + 2
# output should be 12
python arith 10 - 2
# output should be 8
python arith 11 * 2
# output should be 22
python arith 10 & 2
# Error since operator is not valid (Allow only +,-,%,*,/)
# Please  handle negative cases as well
# Ex: if user runs
python arith.py 10 +
# Means 2nd arg not passed (it should  throw proper message)


38)(b) Accept 3 inputs from keyboard input <no1> <operator> <no2>
Perform the operation depending on operator
no1 = input("Please enter no1:") # 5
opr = input("Please enter opr:") # [+,-,*,/,//,**],abc.. -
no2 = input("Please enter no2:") # 3
# 2

if opr == "+":
    s = no1 + no2
elif opr == "-":
    s = no1 - no2



39)
inp = "#test input#"
#	   0123456789
write a program to find position of all occurances of 't' in above string(Use find method & loop)


41) 
inp = "a10290358891835677bc0d12454xyz"
remove all the numbers from above string using while loop

# using for loop
for i in range(10):
    inp = inp.replace(str(i),"")
print(inp)

i = 0
while i < 10:
    i = i + 1

42) Below program is to find the common objects between 2 iterators, but this shows us duplicates as well. Fix the code to avoid storing duplicates 
a = [1, 1, 1, 2, 2, 2, 20, 20, 40, 40]
b = [4,2,20,5]
for i in a: # [1, 1, 1, 2, 2, 2, 20, 20, 40, 40]
	# i = 2
	for j in b: # [4,2,20,5]
		if i == j:
			print(i)
			
43) 
reverse a dictionary using while loop
data = {1:2, 3:4, 5:6}
exapected: data = {2:1, 4:3, 6:5}


44)
adict = {'RN1':'Ajay', 'RN2':'Kiran', 'RN3':'Vijay'}
create list out of above dict where both key & value should be stored in list
expected:
out = ['RN1', 'Ajay', 'RN2', 'Kiran', 'RN3', 'Vijay']

45)
inp = ['RN1', 'Ajay', 'RN2', 'Kiran', 'RN3', 'Vijay']
create dict out of list where even index should be key and it's next index(odd) should be value
expected:
adict = {'RN1':'Ajay', 'RN2':'Kiran', 'RN3':'Vijay'}

46)
a = "p1=0,p2=1,p3=0,p6=0"
convert above string into dict as below
# expected data'''


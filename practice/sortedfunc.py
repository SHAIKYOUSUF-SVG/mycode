list1=[1,0,2,3,4,72,21,21,321,342,312]
out=sorted(list1,reverse=True)
print(out)

list2=['india','uk','usa']
list3=sorted(list2,key=len)
print(list3)

list2=['india','uk','usa']
list3=sorted(list2,key=lambda word:word[-1])
print(list3)



'''
In Python, the `key` argument is used in sorting functions like `sorted()` and `list.sort()`. It allows you to specify a function to be called on each list element before making comparisons. This enables customized sorting based on various criteria.

Here are different ways you can use the `key` argument, along with examples:

### 1. **Sorting by String Length**
   - **Use Case:** Sort based on the length of strings.
   ```python
   list2 = ['india', 'uk', 'usa']
   sorted_list = sorted(list2, key=len)
   print(sorted_list)  # Output: ['uk', 'usa', 'india']
   ```

### 2. **Sorting by Absolute Value**
   - **Use Case:** Sort a list of numbers based on their absolute values.
   ```python
   nums = [-10, 5, -2, 8]
   sorted_nums = sorted(nums, key=abs)
   print(sorted_nums)  # Output: [-2, 5, 8, -10]
   ```

### 3. **Sorting by Lowercase (Case-Insensitive Sorting)**
   - **Use Case:** Sort strings regardless of their case.
   ```python
   words = ['Apple', 'banana', 'cherry']
   sorted_words = sorted(words, key=str.lower)
   print(sorted_words)  # Output: ['Apple', 'banana', 'cherry']
   ```

### 4. **Sorting by a Specific Index in a Tuple**
   - **Use Case:** Sort a list of tuples based on a specific element.
   ```python
   tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
   sorted_tuples = sorted(tuples, key=lambda x: x[1])
   print(sorted_tuples)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
   ```

### 5. **Sorting by Multiple Criteria (e.g., Primary and Secondary Sorting)**
   - **Use Case:** Sort first by one criterion, then by another.
   ```python
   people = [('Alice', 30), ('Bob', 25), ('Charlie', 30)]
   sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
   print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 30')]
   ```

### 6. **Sorting by Reverse Order of a Custom Function**
   - **Use Case:** Sort based on a custom function in reverse order.
   ```python
   nums = [10, 5, 8, 3]
   sorted_nums = sorted(nums, key=lambda x: x % 3, reverse=True)
   print(sorted_nums)  # Output: [10, 8, 5, 3]
   ```

### 7. **Sorting with Complex Numbers**
   - **Use Case:** Sort complex numbers based on their real or imaginary parts.
   ```python
   complex_nums = [3+4j, 1+2j, 2-1j]
   sorted_complex = sorted(complex_nums, key=lambda x: x.real)
   print(sorted_complex)  # Output: [(1+2j), (2-1j), (3+4j)]
   ```

### 8. **Sorting by a Custom Object’s Attribute**
   - **Use Case:** Sort objects based on their attributes.
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name
           self.age = age

   people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
   sorted_people = sorted(people, key=lambda p: p.age)
   print([p.name for p in sorted_people])  # Output: ['Bob', 'Alice', 'Charlie']
   ```

### 9. **Sorting by Date**
   - **Use Case:** Sort a list of dates.
   ```python
   from datetime import datetime
   dates = [datetime(2021, 6, 5), datetime(2020, 8, 1), datetime(2021, 4, 15)]
   sorted_dates = sorted(dates, key=lambda x: x)
   print(sorted_dates)
   ```

### 10. **Sorting a Dictionary by Value**
   - **Use Case:** Sort dictionary items by their values.
   ```python
   my_dict = {'a': 3, 'b': 1, 'c': 2}
   sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
   print(sorted_dict)  # Output: [('b', 1), ('c', 2), ('a', 3)]
   ```

### 11. **Sorting by Custom Sorting Function**
   - **Use Case:** Sort by any custom function.
   ```python
   words = ['apple', 'banana', 'cherry']
   sorted_words = sorted(words, key=lambda x: sum(ord(c) for c in x))
   print(sorted_words)  # Output based on sum of ASCII values
   ```

### 12. **Sorting Using `operator` Module**
   - **Use Case:** Sort using functions from the `operator` module.
   ```python
   from operator import itemgetter
   tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
   sorted_tuples = sorted(tuples, key=itemgetter(1))
   print(sorted_tuples)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
   ```

These examples show various ways to leverage the `key` argument to customize sorting behavior in Python.

Sure! Here are some additional examples to further demonstrate the versatility of the `key` argument in Python:

### 13. **Sorting by Digit Sum**
   - **Use Case:** Sort numbers based on the sum of their digits.
   ```python
   nums = [102, 12, 31, 45]
   sorted_nums = sorted(nums, key=lambda x: sum(int(digit) for digit in str(x)))
   print(sorted_nums)  # Output: [12, 31, 102, 45]
   ```

### 14. **Sorting Strings by Vowel Count**
   - **Use Case:** Sort strings based on the number of vowels they contain.
   ```python
   def vowel_count(word):
       return sum(1 for char in word if char.lower() in 'aeiou')

   words = ['apple', 'banana', 'cherry']
   sorted_words = sorted(words, key=vowel_count)
   print(sorted_words)  # Output: ['cherry', 'banana', 'apple']
   ```

### 15. **Sorting by the Last Character of a String**
   - **Use Case:** Sort strings based on their last character.
   ```python
   words = ['apple', 'banana', 'cherry']
   sorted_words = sorted(words, key=lambda x: x[-1])
   print(sorted_words)  # Output: ['banana', 'apple', 'cherry']
   ```

### 16. **Sorting Nested Lists by Specific Elements**
   - **Use Case:** Sort nested lists based on specific sub-list elements.
   ```python
   nested_list = [[3, 'apple'], [2, 'banana'], [1, 'cherry']]
   sorted_list = sorted(nested_list, key=lambda x: x[0])
   print(sorted_list)  # Output: [[1, 'cherry'], [2, 'banana'], [3, 'apple']]
   ```

### 17. **Sorting Tuples by the Length of the Second Element**
   - **Use Case:** Sort tuples where the second element is a string, based on the length of that string.
   ```python
   tuples = [(1, 'apple'), (2, 'banana'), (3, 'kiwi')]
   sorted_tuples = sorted(tuples, key=lambda x: len(x[1]))
   print(sorted_tuples)  # Output: [(3, 'kiwi'), (1, 'apple'), (2, 'banana')]
   ```

### 18. **Sorting by the Number of Divisors**
   - **Use Case:** Sort numbers based on the number of divisors they have.
   ```python
   def count_divisors(n):
       return len([i for i in range(1, n+1) if n % i == 0])

   nums = [10, 6, 8]
   sorted_nums = sorted(nums, key=count_divisors)
   print(sorted_nums)  # Output: [10, 8, 6]
   ```

### 19. **Sorting a List of Lists by the Sum of Elements**
   - **Use Case:** Sort nested lists by the sum of their elements.
   ```python
   list_of_lists = [[1, 2, 3], [4, 5, 6], [1, 1, 1]]
   sorted_list = sorted(list_of_lists, key=sum)
   print(sorted_list)  # Output: [[1, 1, 1], [1, 2, 3], [4, 5, 6]]
   ```

### 20. **Sorting a List of Dictionaries by a Specific Key**
   - **Use Case:** Sort a list of dictionaries based on the value of a specific key in the dictionary.
   ```python
   dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
   sorted_dicts = sorted(dicts, key=lambda d: d['age'])
   print(sorted_dicts)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
   ```

### 21. **Sorting by a Custom Function That Involves Conditional Logic**
   - **Use Case:** Sort based on a custom function that includes conditional logic.
   ```python
   nums = [3, -2, 4, 0, -5]
   sorted_nums = sorted(nums, key=lambda x: x if x > 0 else x + 10)
   print(sorted_nums)  # Output: [0, 3, 4, -2, -5]
   ```

### 22. **Sorting Strings by the Number of Unique Characters**
   - **Use Case:** Sort strings based on the number of unique characters they contain.
   ```python
   words = ['apple', 'banana', 'kiwi']
   sorted_words = sorted(words, key=lambda x: len(set(x)))
   print(sorted_words)  # Output: ['banana', 'apple', 'kiwi']
   ```

### 23. **Sorting by a Function that Uses External Data**
   - **Use Case:** Sort based on a function that uses external data (e.g., a lookup table).
   ```python
   priority = {'apple': 2, 'banana': 1, 'cherry': 3}
   words = ['cherry', 'banana', 'apple']
   sorted_words = sorted(words, key=lambda x: priority[x])
   print(sorted_words)  # Output: ['banana', 'apple', 'cherry']
   ```

### 24. **Sorting by Boolean Values**
   - **Use Case:** Sort based on a boolean function (e.g., whether a string starts with a vowel).
   ```python
   words = ['apple', 'banana', 'orange', 'grape']
   sorted_words = sorted(words, key=lambda x: x[0].lower() in 'aeiou')
   print(sorted_words)  # Output: ['banana', 'grape', 'apple', 'orange']
   ```

### 25. **Sorting with a More Complex Lambda Function**
   - **Use Case:** Sort based on a more complex lambda function involving multiple criteria.
   ```python
   nums = [3, -2, 4, 0, -5]
   sorted_nums = sorted(nums, key=lambda x: (x % 2 == 0, x))
   print(sorted_nums)  # Output: [-2, 0, 4, -5, 3]
   ```

These examples showcase even more ways you can customize sorting using the `key` argument in Python, from working with 
numbers and strings to more complex data structures like tuples, dictionaries, and nested lists.'''
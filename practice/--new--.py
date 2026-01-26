'''__new__ is a special method that is responsible for ''creating'' a new instance of class.
__init__ and is typically used to ''control the creation of instance''

__new__ is a static method that takes the class itself as a first argument.it creates and returns a new
instance of the class
this can useful for implementing design pattern like singeltons or for classes that require
initilization before __init__ is called'''


class myclass:
    def __new__(cls,*args):
        print("creating intance")
        instance=super(myclass,cls).__new__(cls)
        return instance
    # def __init__(self):
    #     print('initilization')
    #     #self.value=value
myclass()


class subclass(myclass):
    def __new__(cls):
        print("crerating instance from sub class")
    #     instance=super(subclass,cls).__new__(cls)
    #     return instance
subclass()

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, value):
        self.value = value

# Test the Singleton class
singleton1 = Singleton(1)
singleton2 = Singleton(2)

print(singleton1.value)  # Output: 1
print(singleton2.value)  # Output: 1
print(singleton1 is singleton2)  # Output: True

'''
The `__new__` method in Python is a special method that is ''called to create a new instance of a CLASS. It is responsible
 for returning a new instance of the CLASS. This method is less commonly used compared to `__init__`'', which initializes 
 the instance, but `__new__` is essential when creating immutable types like tuples or strings. Here is an example to 
 illustrate the use of `__new__`:

```python
class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self, value):
        self.value = value

# Test the Singleton class
singleton1 = Singleton(1)
singleton2 = Singleton(2)

print(singleton1.value)  # Output: 1
print(singleton2.value)  # Output: 1
print(singleton1 is singleton2)  # Output: True
```
### Explanation:
1. **Class Definition**:
   - The `Singleton` class is designed to ensure only one instance is created.
2. **`__new__` Method**:
   - `__new__` is overridden to control the creation of a new instance.
   - It checks if an instance of the class already exists in the `_instances` dictionary.
   - If it does not exist, it creates a new instance using `super().__new__(cls)` and stores it in the `_instances` dictionary.
   - It returns the existing instance if one already exists.

3. **`__init__` Method**:
   - This initializes the instance with a value but does not create a new instance.
   
4. **Testing Singleton**:
   - When `singleton1` and `singleton2` are created, both refer to the same instance.
   - Thus, changes to one instance reflect in the other.

This example demonstrates how `__new__` can be used to implement design patterns like Singleton, where control over 
instance creation is necessary.'''


"""__NEW__used to create a new instances of class while __init__ constructor used to initialize the instance with the a 
value but doen not create a new instance
__new__ will check is their any existed instenace and it will create new instances"""
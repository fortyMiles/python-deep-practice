"""
1. Nested Functions
2. Rich Comparison
3. Weak Reference
"""

# Weak Reference Example

import weakref


class Student:
    def __init__(self, name):
        self.name = name


# Case 1
tom = Student('tom')

another = tom

del tom

print(another.name)

tom = Student('tom')
anther_two = weakref.proxy(tom)

del tom

try:
    print(anther_two.name)
except ReferenceError as e:
    print('error: ', e)

# Case 2
new_tom = Student('new_tom')
another = new_tom

del new_tom

print(another.name)

new_tom = Student('new_tom')
anther_two = weakref.ref(new_tom)

print('get value by ref: ', anther_two().name)

del new_tom

try:
    print(anther_two().name)
except ReferenceError as e:
    print('error: ', e)
except AttributeError as e:
    print('error: ', e)


# Function attributes

def some_func(x):
    some_func.name = 'hello'
    some_func.age = 10
    some_func.cache = {}

    if x in some_func.cache:
        return some_func.cache[x]
    else:
        value = x ** 2
        some_func.cache[x] = value

        return value


if __name__ == '__main__':
    print(some_func(2))
    print(some_func(2))

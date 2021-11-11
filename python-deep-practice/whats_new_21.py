"""
1. Nested Functions
2. Rich Comparison
3. Weak Reference
"""

# Weak Reference Example

import time
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


if __name__ == '__main__':
    pass

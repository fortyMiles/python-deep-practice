class Player:
    count = 1

    def __init__(self, name):
        self.name = name
        self.count += 1


p1 = Player('Newman')
print(p1.count)
print(Player.count)

"""

the attribute lookup order: 

    1. if name in obj.__dict___;
    2. if name in obj.__class__.dict;
    3. for cls in obj.__class__.mro__:
        if name in cls.__dict__: 
            pass
"""

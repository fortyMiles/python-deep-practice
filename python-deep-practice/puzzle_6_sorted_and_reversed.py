a_list = [1, 4, 2, 3]

rev = reversed(a_list)

print(sorted(rev) == sorted(rev))

"""
reversed return is an iterator

when rev be sorted first time, the iterator is used up. 

when sorted second time, the iterator became an empty.

therefore, the result is False  

"""
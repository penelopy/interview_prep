""" Reverse a list in place"""

my_list = ["dog", "cat", "mouse", "bird", "tree"]  # tree, bird, mouse, cat, dog

for x in range(len(my_list)/2):  # only need to iterate through half the list
    y = my_list.pop()
    my_list.insert(i, y)
print my_list
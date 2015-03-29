""" Reverse a list in place"""

my_list = ["dog", "cat", "mouse", "bird", "tree"]  # tree, bird, mouse, cat, dog

for i in range(len(my_list)):
    x = my_list.pop()
    my_list.insert(i, x)

print my_list
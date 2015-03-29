""" Reverse a list in place"""


list_1 = ["dog", "cat", "mouse", "bird", "tree"]  # tree, bird, mouse, cat, dog
list_2 = [1, 2, 3, 4, 5, 6, 7]

def reverse_list(my_list):
    for i in range(len(my_list)/2):  # only need to iterate through half the list
        my_list[i], my_list[-1 - i] = my_list[-1 - i], my_list[i]
    return my_list

print reverse_list(list_1)
print reverse_list(list_2)
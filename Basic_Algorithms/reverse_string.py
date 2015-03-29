""" Reverse a string"""

def reverse_string(stringy): 
    reversed_list = []  #strings are immutable, must convert to list and reverse
    reversed_list.extend(stringy)
    for i in range(len(reversed_list)/2):
        reversed_list[i], reversed_list[-1 - i] = reversed_list[-1 -i], reversed_list[i]

    print "".join(reversed_list)

string1 = "cat in the hat"

reverse_string(string1)


# str_1 = "do have salami snot"
# str_2 = "Thomas Alva Edison"
# str_1 = "listen"
# str_2 = "silent"
str_1 = "dormitory"
str_2 = "dirty room"

def is_anagram(string1, string2):
    rev_string1 = string1.lower().replace(" ", "")
    rev_string2 = string2.lower().replace(" ", "")
    d1 = {}
    d2 = {}

    for char in rev_string1: 
        d1[char] = d1.get(char, 0) + 1

    for char in rev_string2: 
        d2[char] = d2.get(char, 0) + 1

    return d1 == d2

print is_anagram(str_1, str_2)



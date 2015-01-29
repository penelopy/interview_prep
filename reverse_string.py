"""Input a string, return the reverse of that string"""


def reverse_string(stringy):
    reversed_stringy = ""
    for i in range(len(stringy)):
        temp = stringy[-1 - i]
        reversed_stringy += temp
    return reversed_stringy

stringy = "Sunshine on a rainy day"

print reverse_string(stringy)

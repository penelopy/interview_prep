"""Input a string, return the reverse of that string"""


def reverse_string(stringy):
    reversed_stringy = ""
    for i in range(len(stringy)):
        temp = stringy[-1 - i]
        reversed_stringy += temp
    return reversed_stringy

stringy = "Sunshine on a rainy day"

# print reverse_string(stringy)


 
def reverse_words(stringy): 
    reversed_stringy = ""
    new_string = stringy.split()
    word_list = list(new_string)

    for i in range(len(word_list)): 
        temp = word_list[-1 - i]
        reversed_stringy += temp + " "
    return reversed_stringy

print reverse_words("hello world dog charlie")
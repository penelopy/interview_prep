""" 
Given a string of letters, compress to number of letters in a row that are the same. 
Example: turn "aabcccccaaa" into "a2b1c5a3"
    BUT if compressed string is not shorter than the original string, just return the original string
"""


def compressed_string(string1):
    current_letter = string1[0]
    current_count = 1
    output = ""
    for i in range(1, len(string1)): 
        next_letter = string1[i]
        if next_letter != current_letter: 
            output += current_letter
            output += str(current_count)
            current_letter = next_letter
            current_count = 1
        current_count += 1
    output += current_letter
    output += str(current_count)
    if len(string1) < len(output): 
        return string1
    else: 
        return output

string_1 = "aabcccccaaa"
string_2 = "aaaaabbcdddded"
string_3 = "abcde"
string_4 = "a"

print compressed_string(string_1)



# """Christian's solution"""
# def compress(s):
#     current_letter = s[0]
#     current_count = 1
#     out = ""
#     for i in range(1, len(s)):
#         next_letter = s[i]
#         if next_letter != current_letter:
#             out += current_letter
#             out += str(current_count)
#             current_letter = next_letter
#             current_count = 1
#         current_count += 1
#     out += current_letter
#     out += str(current_count)
#     if len(s) < len(out):
#         return s
#     else:
#         return out

# string_1 = "aabcccccaaa"
# string_2 = "aaaaabbcdddded"
# string_3 = "abcde"
# string_4 = "a"

# print compress(string_1)
# print compress(string_2)
# print compress(string_3)
# print compress(string_4)
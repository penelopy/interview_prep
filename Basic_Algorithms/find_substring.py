
def find_substring(astring):
    output = []

    for start_letter in range(len(astring)):
        for end_letter in range(start_letter,  len(astring)):
            substring = (astring[start_letter:end_letter + 1])
            output.append(substring)    
            print substring
    return output

find_substring("01234")
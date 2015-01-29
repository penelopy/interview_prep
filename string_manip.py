#output a new string comprised of every 3rd letter

def every_third_letter(astring):
    new_string = ""
    for i in range(len(astring)): 
        if i % 3 == 0: 
            new_string += astring[i -1]
    return new_string        

print every_third_letter("marsbarsrock")

#output all the unique characters in a given string
def unique(astring): 
    unique_letters = []
    d = {}
    for letter in astring: 
        d[letter] = d.get(letter, 0) + 1
    for k, v in d.iteritems(): 
        if v == 1: 
            unique_letters.append(k)
    return unique_letters

print unique("marshmellow")

def slice_this(astring):
    #print first three letters 
    print astring[:3]
    #print last three letters 
    print astring[-3:]
    #print middle letter 
    mid = len(astring)/2
    print astring[mid]
slice_this("cracking")

def reverse_every_2_letters(astring):
    new_string = ''
    for i in range(len(astring)):
        if i % 2 == 1: 
            new_string += astring[i]
            new_string += astring[i - 1]

    return new_string
print reverse_every_2_letters("mother")



""" https://www.interviewcake.com/question/find-rotation-point"""
# O(lg n) time and O(1) space

def find_rotation_pt(alist): 
    first_word = alist[0]
    floor_index = 0
    ceiling_index = len(alist) - 1

    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index)/2)
        if alist[guess_index] > first_word: 
            floor_index = guess_index
        else: 
            ceiling_index = guess_index
        if floor_index + 1 == ceiling_index: 
            return ceiling_index


print find_rotation_pt(['j', 'l', 'n', 'w', 'a', 'd', 'e'])


# Iterative approach
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)/2
        if alist[midpoint] == item: 
            found = True
        else: 
            if item < alist[midpoint]:
                last = midpoint - 1
            else: 
                first = midpoint + 1

    return found

my_array = [2, 4, 6, 8, 10]

print binary_search(my_array, 10)

# Recursive approach -Using Binary search it would be O(logn) time

def binary_search_r(alist, item): 
    if len(alist) == 0: 
        return False

    else: 
        midpoint = len(alist)/2
        if alist[midpoint] == item:
            return True
        if item < alist[midpoint]: 
            return binary_search_r(alist[0:midpoint], item)
        elif item > alist[midpoint]: 
            return binary_search_r(alist[midpoint:], item)



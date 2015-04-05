"""Given an array_of_ints, find the highest_product you can get from three of the integers."""

def highest_product_of_three(alist):
    if len(alist) < 3: 
        raise Exception("List needs at least three items")

    highest_product_of_three = alist[0] * alist[1] * alist[2]
    highest_product_of_two = alist[0] * alist[1]
    highest_product = max(alist[0], alist[1])
    lowest_product_of_two = alist[0] * alist[1]
    lowest_product = min(alist[0], alist[1])

    for num in range(alist[2:]):
        highest_product_of_three = max(highest_product_of_three, highest_product_of_two * num, lowest_product_of_two * num)
        highest_product_of_two = max(highest_product_of_two, highest_product * num, lowest_product * num)
        highest_product = max(highest_product, num)
        lowest_product = min(lowest_product, num)

    return highest_product_of_three

# O(n) time and O(1) additional space
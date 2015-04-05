# An iterative bottom up approach to fibonacci which eliminates 2-to-the-n runtime which occurs in the recursive approach

# O(n) time, O(1)space

def fib_iterative(n):
    # edge case
    if n < 0: 
        raise Exception("Index can't be negative")

    if n in [0, 1]:
        return n

    prev = 0
    prev_prev = 1

    for index in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

print fib_iterative(6)
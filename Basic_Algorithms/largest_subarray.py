"""Write a function that takes in an array of arrays, where each sub-array is a list of integers. Find the sub-array with the highest average. Return the entire sub-array, the index position, or the average (your choice, but explain which one you chose and why. Or, try all three!)

Return sub-array, index position, or average. 

"""

array_1 = [ [11, 2, 5, 57], [54, 2, 8, 15], [89, 1, 4, 5], [35, 13, 7, 22]]
d = {}
values = []


for i in range(len(array_1)): 
    product = 1
    for num in array_1[i]:
        product *= num
        divisor = len(array_1[i])
        average = product/divisor
        d[i] = average


for v in d.itervalues():
    values.append(v)
highest_average = max(values)

print highest_average

for k, v in d.iteritems():
    if v == highest_average: 
        index = k
print index

highest_subarray = array_1[index]

print highest_subarray



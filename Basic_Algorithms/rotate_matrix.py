""" Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?"""


""" Solution 1 - not in place"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotated_matrix = []

for x in range(len(matrix)): 
    rotated_matrix.append([])
    
for x in range(len(matrix)):  
    for y in range(len(rotated_matrix)): 
        rotated_matrix[y].append(matrix[len(matrix) - x - 1][y])
# print rotated_matrix

##########################################################################
""" Solution 2 - in place"""

# adds numbers to the end of matrix - making it double in size   
for x in range(len(matrix)):  
    for y in range(len(matrix)): 
        matrix[y].append(matrix[len(matrix) - x - 1][y])

# removes the unwanted values from matrix
j = -1
for h in range(len(matrix)):
    j += 1
    matrix[j] = matrix[h][4:]

print matrix

""" Solution 3 - in place"""


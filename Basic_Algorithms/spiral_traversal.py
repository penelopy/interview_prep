"""Write a function that takes a matrix and examines each item in a spiral order, printing each item as it comes to it.
For example, given a matrix like this as input:
[[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45]]
Your program must print:
11 12 13 14 15 25 35 45 44 43 42 41 31 21 22 23 24 34 33 32"""

matrix = [ [11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45]]

def traverse_matrix(input_matrix):
    right_limit = len(input_matrix[0]) 
    lower_limit = len(input_matrix) 
    output_string = ""
    left_limit = 0
    upper_limit = 0
    matrix_size = right_limit * lower_limit

    while matrix_size > 0: 
        # MOVE RIGHT
        for x in range(left_limit, right_limit):
            output_string += str(input_matrix[upper_limit][x]) + " "
            matrix_size -= 1      
        right_limit -= 1 
        left_limit += 1 

        # MOVE DOWN
        for x in range(upper_limit + 1, lower_limit):
            output_string += str(input_matrix[x][right_limit]) + " "
            matrix_size -= 1
        lower_limit -= 1 

        # MOVE LEFT
        for num in range(right_limit - 1, left_limit -2, -1):
            output_string += str(input_matrix[lower_limit][num]) + " "
            matrix_size -= 1

        # MOVE UP
        for x in range(lower_limit - 1, upper_limit, -1):
            output_string += str(input_matrix[x][left_limit - 1]) + " "
            matrix_size -= 1
        upper_limit += 1

    return output_string   

print traverse_matrix(matrix)


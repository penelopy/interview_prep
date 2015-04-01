""" Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0 """

matrix = [[1, 2, 3, 0], [5, 6, 7, 8], [9, 0, 11, 12], [13, 14, 15, 16]]
zero_list = []

def locate_zeros():
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] == 0:
                x_position = x
                y_position = y
                zero_list.append((x_position, y_position))
    return zero_list


def nullify_column():
    for position in zero_list: 
        for y in range(len(matrix)): 
            matrix[y][position[1]] = 0
    return matrix

def nullify_row():
    for position in zero_list: 
        for x in range(len(matrix)):
            matrix[position[0]][x] = 0
    return matrix


def main(): 
    locate_zeros()
    nullify_row()
    nullify_column()

    for i in range(len(matrix)):
        print matrix[i]
main()

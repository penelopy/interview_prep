

def build_matrix(width, height):
    count = 0
    matrix = []

    for i in range(height): #7 (0, 1, 2, ...6)
        row = []
        for x in range(width): #5 (0, 1, 2, 3, 4)
            count += 1
            row.append(count)
        matrix.append(row)

    return matrix

matrix = build_matrix(5, 7)


def print_matrix(matrix):
    for row in matrix: 
        print row

print_matrix(matrix)

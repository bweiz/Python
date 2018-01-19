# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# Benton Weizenegger
# --------------------------------------

def print_matrix(mat, rows, columns, sent):
    print(sent)
    
    for i in range(rows):
        print_header(columns)
        div = "|"
        for x in range(columns):
            if (i,x) in mat:
                 value = mat[(i, x)]
            else:
                value = 0
            div = div + str("{:3d}".format(value)) + "|"
        print(div)
    print_header(columns)
    print("\n")
        
def add_matrices(matrix1, matrix2, rows, columns):
    new_matrix = {}
    
    for i in range(rows):
        for x in range(columns):
            if (i, x) in matrix1:
                v1 = matrix1[(i, x)]    
            else:
                v1 = 0
            if (i, x) in matrix2:
                v2 = matrix2[(i, x)]
            else:
                v2 = 0
            if v1 + v2 != 0:
                new_matrix[(i, x)] = v1 + v2
    return new_matrix
    

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
        
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")

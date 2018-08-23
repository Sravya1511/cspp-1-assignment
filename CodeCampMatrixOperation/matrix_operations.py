def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix1) == len(matrix2):
        b = []
        for i in range(len(matrix1)):
            a = []
            for j in range(len(matrix1[i])):
                a.append(matrix1[i][j]+matrix2[i][j])
            b.append(a)
        return b
    else:
        print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    li = []
    rows = input()
    # cols = input()
    r = rows.split(',')
    e = []
    # for i in range(int(r[0])):
    #     lj = []
    #     ele = input()
    #     e = ele.split(',')
    #     print(e)
    #     li.append(e)
    # print(li)
    # for j in range(int(r[1])):
    #     k = li[j].split(',')
    try:
        for i in range(int(r[0])):
        ele = list(map(int, input().split()))
        e.append(ele)
        return e
    except: 
        print("IndexError: list index out of range")






  


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix1 = read_matrix()
    matrix2 = read_matrix()
    add = add_matrix(matrix1, matrix2)
    print(add)

if __name__ == '__main__':
    main()

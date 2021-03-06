"""matrix"""
def mult_matrix(matrix1, matrix2):
    """mul"""
    if len(matrix1[0]) == len(matrix2):
        l_row = []
        l_1 = len(matrix1)
        l_2 = len(matrix2)
        for i in range(l_1):
            l_col = []
            
            for j in range(len(matrix2[0])):
                s_1 = 0
                for k in range(l_2):
                    s_1 = s_1 + (matrix1[i][k] * matrix2[k][j])
                l_col.append(s_1)
            l_row.append(l_col)
        return l_row
    print("Error: Matrix shapes invalid for mult")



def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix1) == len(matrix2):
        l_row = []
        len_1 = len(matrix1)
        for i in range(len_1):
            l_col = []
            len_2 = len(matrix1[i])
            for j in range(len_2):
                # if len(matrix1[i]) != len(matrix2[i]):
                #     break
                # else:
                l_col.append(matrix1[i][j]+matrix2[i][j])
            l_row.append(l_col)
        return l_row
    print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = input()
    # cols = input()
    r_c = rows.split(',')
    li_1 = []
    # for i in range(int(r[0])):
    #     lj = []
    #     ele = input()
    #     e = ele.split(',')
    #     print(e)
    #     li.append(e)
    # print(li)
    # for j in range(int(r[1])):
    #     k = li[j].split(',')

    for i in range(int(r_c[0])):
        ele = list(map(int, input().split()))
        i += 1
        li_1.append(ele)
        if len(ele) != int(r_c[1]):
            print("Error: Invalid input for the matrix")
            return None
    return li_1

def main():
    """main"""
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    matrix1 = read_matrix()
    matrix2 = read_matrix()
    if (matrix1 != None and matrix2 != None):
        add = add_matrix(matrix1, matrix2)
        print(add)
        mul = mult_matrix(matrix1, matrix2)
        print(mul)

if __name__ == '__main__':
    main()

'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    n_m = 9
    for i in range(n_m):
        list_hori = []
        list_veri = []
        # count = 0
        # list_grid = []
        for k in range(n_m):
            if sudoku[i][k] in list_hori:
                return False
            list_hori.append(sudoku[i][k])
        for j in range(n_m):
            if sudoku[j][i] in list_veri:
                return False
            list_veri.append(sudoku[j][i])


    # for i in range(0, 3, len(sudoku)):
    # #     list_grid = []
    # #     for j in range(0, 3, len(sudoku)):
    # #         for k in range(3):
    # #             list_grid.append(sudoku[j][k])
    # #             if sudoku[j][k] in list_grid:
    # #                 count = count+1
    # #     if count == 1:
    # #         return False
    return True




def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()

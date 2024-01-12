def sudoku_print(board):
    for i in range(9):
        for j in range(9):
            #test if the cell value is a tuple (meaning it's digit isn't known yet)
            if type(board[i][j]) == type(('','')):
                print('?', end= ' ')
            else:    
                print(board[i][j], end= ' ')
        print('')

def fill_board():
    """Input the board; if you make a mistake, input -1 to go back.\n
    Each input must be an integer between 1 and 9 inclusive.\n
    Start by listing the digits to the left of the top row, then from left to right.
    Repeat for the rest of the rows, in descending order.\n
    For empty cells, input 0"""
    print("Input the board; if you make a mistake, input -1 to go back.\n Each input must be an integer between 1 and 9 inclusive.\n Start by listing the digits to the left of the top row, then from left to right. Repeat for the rest of the rows, in descending order.\n For empty cells, input 0")
    board = [[[] for i in range(9)] for i in range(9)]
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            # lists the current row and column of the digit to be inputted (+1 so 9 is the max):
            cell = input("Row: {} Column: {}\n".format(i+1, j+1))
            #checks if integer:
            try:
                int(cell)
            except ValueError:
                print("the number must be an integer, try again")
            else: 
                cell = int(cell)
                if cell == -1:
                    j -= 1 # j becomes previous j so the user can re-try their input
                else:
                    if ((cell >= 0) and (cell <=9)): # if digit is 1-9 inclusive
                        if cell == 0: # if cell is unknown, assigns it its pencil values:
                            board[i][j] = (1,2,3,4,5,6,7,8,9) 
                        else:
                            board[i][j] = cell
                        j += 1
                    else:
                        print("the number must be between 1 and 9 inclusive, try again")
        i += 1
    sudoku_print(board)
    return board


def solve_sudoku(board):
    sudoku_solved = False
    while sudoku_solved == False:
        for i in range(9):
            for j in range(9):
                current_cell = board[i][j]
                if type(current_cell) != type(('','')): # if cell's value is known
                    continue
                else:
                    current_cell = check_cell(current_cell)




def check_cell(cell): 
    """
    Todo:
    - Finish functions (if possible don't make them functions)
    - Add a notes generator
    """
    def only_one_of_each_number(cell):
        pass
    
    def last_free_cell(cell):
        pass
        # rows:
        if 
        # columns:

        # 3x3 cell block:

    def last_remaining_cell(cell):
        pass

    #last_possible_number:
    if len(cell) == 1:
        return int(cell)

    def obvious_single(cell):
        pass

    def obvious_pair(cell):
        pass

    def obvious_triple(cell):
        pass

    def hidden_single(cell):
        pass

    def hidden_pair(cell):
        pass

    def hidden_triple(cell):
        pass

    def pointing_pair(cell):
        pass

    def pointing_triple(cell):
        pass

    def x_wing(cell):
        pass

    def y_wing(cell):
        pass

    def swordfish(cell):
        pass






#fill_board()
#sudoku_print([[0]*9]*9)

#sudoku_print(fill_board())


test_board = [[1,3,4,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)],
              [8,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),3,(1,2,3,4,5,6,7,8,9),6,5,(1,2,3,4,5,6,7,8,9)],
              [(1,2,3,4,5,6,7,8,9),9,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),2,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)],
              [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),5,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),4],
              [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),1,7,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),2,(1,2,3,4,5,6,7,8,9)],
              [6,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),1],
              [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)],
              [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),5,2,(1,2,3,4,5,6,7,8,9),8,3,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9)],
              [(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),2,(1,2,3,4,5,6,7,8,9),9,(1,2,3,4,5,6,7,8,9),(1,2,3,4,5,6,7,8,9),7,(1,2,3,4,5,6,7,8,9)],]

sudoku_print(test_board)


"""
Steps:
 - Assign each cell a list of possible values.
 - Iterate through each cell, checking its row, column, and box
     - Check last free cell in column/row/box
     - Check for naked/hidden singles, naked/hidden doubles, triples, etc.
     - Pointing pairs/triples/etc. (i.e. all 3 notes in a box are alligned on 1 row, so other 3s can be eliminated from the row)
     - execute the techniques
     - Check for x-wing (sudoku.com/sudoku-rules/h-wing/)
     - Check for y-wing (sudoku.com/sudoku-rules/y-wing/)
     - Check for swordfish (sudoku.com/sudoku-rules/swordfish/)

Variable Names:
 - notes <tuple>
 - cell_solved <bool>
 - 
 
 Extras:
 - Add killer sudoku support
"""

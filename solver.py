









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

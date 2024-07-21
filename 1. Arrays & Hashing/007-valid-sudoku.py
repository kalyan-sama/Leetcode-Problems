'''
Difficulty: Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

'''

from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grids = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if ( board[i][j] in rows[i] or
                    board[i][j] in cols[j] or 
                    board[i][j] in grids[(i//3, j//3)] ):
                    
                    return False
                    
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    grids[(i//3, j//3)].add(board[i][j])

        return True
    
#Time: O(9^2)
#Sapce: O(9^2)

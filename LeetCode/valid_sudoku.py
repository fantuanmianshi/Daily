"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the
filled cells need to be validated.
"""


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board:
            return False

        for row in board:
            records = {}
            for element in row:
                if element in records:
                    records[element] += 1
                else:
                    records[element] = 1
                if records[element] > 1 and element != '.':
                    return False

        i = 0
        while i < len(board):
            records = {}
            j = 0
            while j < len(board):
                if board[j][i] in records:
                    records[board[j][i]] += 1
                else:
                    records[board[j][i]] = 1
                if records[board[j][i]] > 1 and board[j][i] != '.':
                    return False
                j += 1
            i += 1

        i = 0
        while i < len(board):
            j = 0
            while j < len(board):

                records = {}
                m = i
                while m < i + 3:
                    n = j
                    while n < j + 3:
                        if board[m][n] in records:
                            records[board[m][n]] += 1
                        else:
                            records[board[m][n]] = 1
                        if records[board[m][n]] > 1 and board[m][n] != '.':
                            return False
                        n += 1
                    m += 1

                j += 3
            i += 3

        return True

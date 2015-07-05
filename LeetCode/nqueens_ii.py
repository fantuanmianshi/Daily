"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of
distinct solutions.
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        return self.solver(n, 0, [None] * n)

    def solver(self, n, row, colForRows):
        count = 0
        if row == n:
            return 1
        else:
            col = 0
            while col < n:
                colForRows[row] = col
                if not self.can_attack(row, colForRows):
                     count += self.solver(n, row + 1, colForRows)
                col += 1
            return count

    def can_attack(self, row, colForRows):
        i = 0
        while i < row:
            if colForRows[i] == colForRows[row] or \
               abs(colForRows[i] - colForRows[row]) == row - i:
                return True
            i += 1
        return False

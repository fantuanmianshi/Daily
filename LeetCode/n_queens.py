"""
The n-queens puzzle is the problem of placing n queens on an nxn chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

```
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
```
"""


class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []
        self.nQueens(n, [None] * n, 0, result)
        return result

    def nQueens(self, n, columnForRows, row, result):
        if row == n:
            temp = []
            for row, col in enumerate(columnForRows):
                temp.append('.' * col + 'Q' + '.' * (n - col - 1))
            result.append(temp)
        else:
            col = 0
            while col < n:
                columnForRows[row] = col
                if not self.canAttack(row, columnForRows):
                    self.nQueens(n, columnForRows, row + 1, result)
                col += 1

    def canAttack(self, row, columnForRows):
        i = 0
        while i < row:
            if columnForRows[i] == columnForRows[row] or \
               abs(columnForRows[row] - columnForRows[i]) == abs(row - i):
                return True
            i += 1
        return False

if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(4)

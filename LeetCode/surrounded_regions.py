"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""


class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return
        self.fill_borders(board, 'O', 'Y')
        self.replace(board, 'O', 'X')
        self.fill_borders(board, 'Y', 'O')

    def fill(self, board, i, j, target, c):
        m, n = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != target:
            return
        visit_queue = [(i, j)]
        while visit_queue:
            x, y = visit_queue.pop(0)
            board[x][y] = c
            if x > 0 and board[x - 1][y] == target:
                visit_queue.insert(0, (x - 1, y))
            if x < m - 1 and board[x + 1][y] == target:
                visit_queue.insert(0, (x + 1, y))
            if y > 0 and board[x][y - 1] == target:
                visit_queue.insert(0, (x, y - 1))
            if y < n - 1 and board[x][y + 1] == target:
                visit_queue.insert(0, (x, y + 1))

    def fill_borders(self, board, target, c):
        m, n = len(board), len(board[0])
        for x in range(m):
            if board[x][0] == target:
                self.fill(board, x, 0, target, c)
            if board[x][n - 1] == target:
                self.fill(board, x, n - 1, target, c)

        for x in range(1, n - 1):
            if board[0][x] == target:
                self.fill(board, 0, x, target, c)
            if board[m - 1][x] == target:
                self.fill(board, m - 1, x, target, c)

    def replace(self, board, target, c):
        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == target:
                    board[x][y] = c


if __name__ == '__main__':
    s = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    s.solve(board)
    print board

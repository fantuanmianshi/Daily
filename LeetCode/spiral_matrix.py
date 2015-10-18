"""
Given a matrix of m x n elements (m rows, n columns), return all elements of
the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        row = len(matrix)
        if row == 0:
            return result
        col = len(matrix[0])
        if col == 0:
            return result

        x = [1, 0, -1, 0]
        y = [0, 1, 0, -1]

        visited_rows = 0
        visited_cols = 0

        direction = 0
        startx, starty = 0, 0
        candidateNum, moveStep = 0, 0
        while True:
            if x[direction] == 0:
                candidateNum = row - visited_rows
            else:
                candidateNum = col - visited_cols

            if candidateNum <= 0:
                break

            result.append(matrix[starty][startx])
            moveStep += 1
            if candidateNum == moveStep:
                x_incre = 0 if x[direction] == 0 else 1
                y_incre = 0 if y[direction] == 0 else 1
                visited_rows += x_incre
                visited_cols += y_incre
                direction = (direction + 1) % 4
                moveStep = 0
            startx += x[direction]
            starty += y[direction]

        return result

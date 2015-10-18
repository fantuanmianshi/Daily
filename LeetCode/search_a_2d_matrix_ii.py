"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        i = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                return False

            start, end = 0, len(matrix[i]) - 1
            while start <= end:
                mid = start + (end - start) / 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            i += 1

        return False

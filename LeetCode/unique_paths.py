"""
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0

        matrix = [[0 for _ in range(m)] for _ in range(n)] 

        i = 0
        while i < m:
            matrix[0][i] = 1
            i += 1
        i = 0
        while i < n:
            matrix[i][0] = 1
            i += 1

        i = 1
        while i < n:
            j = 1
            while j < m:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
                j += 1
            i += 1

        return matrix[n - 1][m - 1]

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        start, end = 0, len(matrix) - 1
        while start < end:
            i = start
            while i < end:
                offset = i - start
                temp = matrix[start][i]
                matrix[start][i] = matrix[end - offset][start]
                matrix[end - offset][start] = matrix[end][end - offset]
                matrix[end][end - offset] = matrix[start + offset][end]
                matrix[start + offset][end] = temp
                i += 1
            start += 1
            end -= 1

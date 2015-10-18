"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = [0 for x in range(rowIndex + 2)]
        result[1] = 1

        i = 0
        while i < rowIndex:
            j = rowIndex + 1
            while j > 0:
                result[j] = result[j - 1] + result[j]
                j -= 1
            i += 1

        return result[1:]

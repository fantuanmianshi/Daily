"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            if not result:
                result.append([1])
                continue
            temp = []
            j = 1
            while j < i:
                temp.append(result[i - 1][j - 1] + result[i - 1][j])
                j += 1
            temp = [1] + temp + [1]
            result.append(temp)

        return result

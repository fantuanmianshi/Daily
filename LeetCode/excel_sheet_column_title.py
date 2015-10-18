"""
Given a positive integer, return its corresponding column title as appear in
an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""


class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result = ''

        while n > 0:
            n -= 1
            t = chr(ord('A') + (n % 26))
            n /= 26
            result = t + result

        return result


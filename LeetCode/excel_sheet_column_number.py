"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        if not s:
            return 0

        start, end = ord('A'), ord('Z')
        result, length = 0, len(s)
        if length == 1:
            return ord(s) - start + 1
        else:
            i = 0
            while i < length:
                result += (26 ** (length - i - 1)) * (ord(s[i]) - start + 1)
                i += 1
            return result


if __name__ == '__main__':
    s = Solution()
    print s.titleToNumber('AB')

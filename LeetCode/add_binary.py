"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        carry = 0
        result = ''

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                ai = int(a[i])
            else:
                ai = 0
            if j >= 0:
                bj = int(b[j])
            else:
                bj = 0
            val = (ai + bj + carry) % 2
            carry = (ai + bj + carry) / 2
            result = str(val) + result
            i -= 1
            j -= 1
        if carry == 1:
            result = '1' + result
        return result


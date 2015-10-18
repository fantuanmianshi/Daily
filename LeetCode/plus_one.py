"""
Given a non-negative number represented as an array of digits, plus one to the
number.

The digits are stored such that the most significant digit is at the head of
the list.
"""


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        i = len(digits) - 1

        add = 1
        while i >= 0:
            s = digits[i] + add
            if s >= 10:
                digits[i] = s - 10
                add = 1
            else:
                digits[i] = s
                add = 0
            i -= 1
        if add == 1:
            return [1] + digits
        return digits


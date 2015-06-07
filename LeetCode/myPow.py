"""
Implement pow(x, n).
"""


class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return self.myPow(1.0 / x, -n)
        result = 1
        while n != 0:
            if n % 2 != 0:
                result *= x
                n -= 1
            x *= x
            n /= 2
        return result

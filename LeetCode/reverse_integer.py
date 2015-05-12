
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 10 and x >= 0:
            return x

        s = str(x)[::-1].lstrip('0')
        result = 0
        if s[-1] == '-':
            result = int(s[-1] + s[:-1])
        else:
            result = int(s)

        return result

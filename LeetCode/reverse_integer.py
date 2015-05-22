"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you
have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as
10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a
32-bit integer, then the reverse of 1000000003 overflows. How should you
handle such cases?

For the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.
"""


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

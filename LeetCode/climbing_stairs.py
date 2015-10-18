"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n <= 1:
            return 1
        prev, count = 1, 2
        stairs = n - 2
        while stairs > 0:
            temp = count
            count += prev
            prev = temp
            stairs -= 1
        return count

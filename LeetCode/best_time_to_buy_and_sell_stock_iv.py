"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
"""


class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        size = len(prices)
        if k > size / 2:
            return self.quickSolve(size, prices)
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(min(2 * k, i + 1) , 0 , -1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return max(dp)

    def quickSolve(self, size, prices):
        s = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                s += prices[x + 1] - prices[x]
        return s

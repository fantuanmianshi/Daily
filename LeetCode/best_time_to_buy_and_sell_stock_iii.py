"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell
the stock before you buy again).
"""


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0

        maxEndWith = []
        lowest_price = prices[0]
        max_profit = 0
        maxEndWith.append(0)
        for price in prices[1:]:
            profit = price - lowest_price
            max_profit = max(max_profit, profit)
            lowest_price = min(price, lowest_price)
            maxEndWith.append(max_profit)

        result = maxEndWith[-1]
        highest = prices[-1]
        max_profit = 0
        i = len(prices) - 2
        while i >= 0:
            profit = highest - prices[i]
            max_profit = max(max_profit, profit)
            result = max(max_profit + maxEndWith[i], result)
            highest = max(highest, prices[i])
            i -= 1

        return result

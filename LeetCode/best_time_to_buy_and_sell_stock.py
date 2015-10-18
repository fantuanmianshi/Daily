"""
Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one
and sell one share of the stock), design an algorithm to find the maximum
profit.
"""


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices:
            return 0

        max_profit = 0
        lowest_price = prices[0]

        for price in prices[1:]:
            profit = price - lowest_price
            max_profit = max(max_profit, profit)
            lowest_price = min(lowest_price, price)

        return max_profit

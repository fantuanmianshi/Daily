"""
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
"""


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit = 0
        i = 1
        while i < len(prices):
            delta = prices[i] - prices[i - 1]
            if delta > 0:
                profit += delta
            i += 1
        return profit

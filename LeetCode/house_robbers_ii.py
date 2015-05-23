"""
After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these
houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        current, previous = 0, 0
        for x in nums[1:]:
            temp = current
            current = max(current, x + previous)
            previous = temp
        missing_first = current

        current, previous = 0, 0
        for x in nums[:len(nums) - 1]:
            temp = current
            current = max(current, x + previous)
            previous = temp
        missing_last = current
        
        return max(missing_first, missing_last)

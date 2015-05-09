"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Tags: Array, Two Pointers
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        result, diff = 0, 1 << 31
        i = 0
        while i < len(nums):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sumv = nums[i] + nums[start] + nums[end]
                new_diff = target - sumv
                if abs(new_diff) < diff:
                    diff = abs(new_diff)
                    result = sumv

                if new_diff > 0:
                    start += 1
                elif new_diff < 0:
                    end -= 1
                else:
                    return result
            i += 1
        return result

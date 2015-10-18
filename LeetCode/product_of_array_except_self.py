"""
Given an array of n integers where n > 1, nums, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        size = len(nums)
        result = [1] * size

        left = 1
        for x in range(size - 1):
            left *= nums[x]
            result[x + 1] *= left

        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            result[x - 1] *= right

        return result

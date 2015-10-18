"""
Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        maxCover = 0
        i = 0
        while i <= maxCover and i < len(nums):
            if nums[i] + i > maxCover:
                maxCover = nums[i] + i
            if maxCover >= len(nums) - 1:
                return True
            i += 1
        return False

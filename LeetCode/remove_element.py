"""
Given an array and a value, remove all instances of that value in place and
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            nums[j] = nums[i]
            j += 1
            i += 1
        return j

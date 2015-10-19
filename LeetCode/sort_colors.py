"""
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s, t, e = 0, 0, len(nums) - 1
        while s <= e:
            if nums[s] == 0:
                if s != t:
                    nums[s], nums[t] = nums[t], nums[s]
                s, t = s + 1, t + 1
            elif nums[s] == 1:
                s += 1
            elif nums[s] == 2:
                if s != e:
                    nums[s], nums[e] = nums[e], nums[s]
                e -= 1

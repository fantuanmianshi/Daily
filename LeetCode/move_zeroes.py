"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        head, tail = 0, len(nums) - 1
        while head != tail:
            if nums[head] == 0:
                temp = head
                while temp < tail:
                    nums[temp] = nums[temp + 1]
                    temp += 1
                nums[tail] = 0
                tail -= 1
            else:
                head += 1

    def moveZeroes_linear(self, nums):
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1

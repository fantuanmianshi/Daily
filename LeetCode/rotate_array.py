"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
to [5,6,7,1,2,3,4].
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if k >= len(nums):
            k = k % len(nums)
        nums += nums[:len(nums) - k]
        i = 0
        while i < len(nums) - k:
            nums.pop(0)
            i += 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2]
    s.rotate(nums, 1)
    print nums
    nums = [1, 2]
    s.rotate(nums, 3)
    print nums

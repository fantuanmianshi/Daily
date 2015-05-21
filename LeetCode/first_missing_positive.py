"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositiveSpaceN(self, nums):
        d = {}
        for x in nums:
            d[x] = True

        i = 1
        while True:
            if i not in d:
                return i
            i += 1

    def firstMissingPositiveBit(self, nums):
        d = 0
        for x in nums:
            if x > 0:
                d |= (1 << (x - 1))
        i = 1
        while d != 0:
            if d & 1 == 0:
                return i
            d >>= 1
            i += 1
        return i

    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        i, length = 0, len(nums)
        while i < len(nums):
            if nums[i] <= length and \
               nums[i] > 0 and \
               nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                i -= 1
            i += 1

        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return length + 1

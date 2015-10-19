"""
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that
appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is
also correct.
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant space complexity?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        appearence = {}
        for n in nums:
            if n not in appearence:
                appearence[n] = 1
            else:
                appearence[n] += 1
        return [k for k, v in appearence if v == 1]

    def singleNumber_xor(self, nums):
        xor = reduce(lambda x, y: x ^ y, nums)
        low = xor & -xor
        a, b = 0, 0
        for n in nums:
            if n & low:
                a ^= num
            else:
                b ^= num
        return [a, b]

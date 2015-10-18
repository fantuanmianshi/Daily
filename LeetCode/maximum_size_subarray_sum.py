"""
Given an array of n positive integers and a positive integer s, find the
minimal length of a subarray of which the sum >= s. If there isn't one, return
0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

[1, 2, 3, 4, 5]
"""


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        min_count, count, total = len(nums) + 1, 0, 0
        start, end = 0, 0
        while start < len(nums):
            if total >= s:
                min_count = min(count, min_count)
                total -= nums[start]
                count -= 1
                start += 1
            elif end < len(nums):
                total += nums[end]
                count += 1
                end += 1
            else:
                break
        if min_count == len(nums) + 1:
            return 0
        return min_count


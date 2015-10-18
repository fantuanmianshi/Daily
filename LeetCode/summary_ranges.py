"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if not nums:
            return []
        result = []
        start, i = 0, 1
        while i < len(nums):
            if nums[i] - nums[i - 1] > 1:
                if start == i - 1:
                    result.append('{0}'.format(nums[start]))
                else:
                    result.append('{0}->{1}'.format(nums[start], nums[i - 1]))
                start = i
            i += 1
        if start == i - 1:
            result.append('{0}'.format(nums[start]))
        else:
            result.append('{0}->{1}'.format(nums[start], nums[i - 1]))
        return result

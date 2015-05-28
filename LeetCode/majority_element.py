"""
Given an array of size n, find the majority element. The majority element is
the element that appears more thanhi n/2 times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""


class Solution:
    def majorityElementSort(self, nums):
        return sorted(nums)[len(nums) / 2]

    def majorityElementHash(self, nums):
        count_dict, half = {}, len(nums) / 2
        for x in nums:
            count_dict[x] = count_dict.get(x, 0) + 1
            if count_dict[x] > half:
                return x

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

    def majorityElementMooreVoting(self, nums):
        index, count = 0, 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[index]:
                count += 1
            else:
                count -= 1
            if count == 0:
                index, count = i, 1
            i += 1

        count = 0
        for x in nums:
            if x == nums[index]:
                count += 1
        if count > len(nums) / 2:
            return nums[index]
        return -1


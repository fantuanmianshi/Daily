"""
Given an array of integers, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


Notice: diff value as key of Hash table
"""


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        diff_dict = {}
        for i, n in enumerate(num):
            if n in diff_dict:
                return (diff_dict[n] + 1, i + 1)
            else:
                diff_dict[target - n] = i
        return (None, None)

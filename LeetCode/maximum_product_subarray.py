"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if not nums:
            return 0
        result, minSum, maxSum = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            temp_max = maxSum
            temp_min = minSum
            maxSum = max(max(temp_max * n, temp_min * n), n)
            minSum = min(min(temp_max * n, temp_min * n), n)
            result = max(result, maxSum)
        return result

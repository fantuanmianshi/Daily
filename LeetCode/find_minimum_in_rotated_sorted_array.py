"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        start, end = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if (mid == 0 or nums[mid] < nums[mid - 1]) and \
               (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[lo] and lo > end:
                lo = mid + 1
            elif nums[mid] < nums[lo] and lo > end:
                hi = mid - 1
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1


if __name__ == '__main__':
    s = Solution()
    print s.findMin([2, 1])

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return
its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that num[-1] = num[n] = infinity small 

For example, in array [1, 2, 3, 1], 3 is a peak element and your function
should return the index number 2.
"""


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        length = len(nums) - 1
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            elif mid == length and nums[mid] > nums[mid - 1]:
                return mid
            elif mid > 0 and mid < length and \
                 nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


if __name__ == '__main__':
    s = Solution()
    print s.findPeakElement([1, 2, 3])

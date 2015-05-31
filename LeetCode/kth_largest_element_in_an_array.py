"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 <= k <= array's length.

Tags: Divide and Conquer, Heap
"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            p = self.partition(nums, lo, hi)
            if p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1
            else:
                break
        return nums[k]

    def partition(self, nums, lo, hi):
        i, j = lo, hi + 1
        while True:
            i += 1
            while i < hi and nums[i] < nums[lo]:
                i += 1
            j -= 1
            while j > lo and nums[lo] < nums[j]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        return j

    def findKthLargestHeap(self, nums, k):
        import heapq
        h = []
        for x in nums:
            new_element = x
            if len(h) == k:
                v = heapq.heappop(h)
                if x < v:
                    new_element = v
            heapq.heappush(h, new_element)
        return h[0]


if __name__ == '__main__':
    s = Solution()
    print s.findKthLargestHeap([1], 1)
    print s.findKthLargestHeap([2, 1], 1)
    print s.findKthLargestHeap([99, 99], 1)
    print s.findKthLargestHeap([7, 6, 5, 4, 3, 2, 1], 5)

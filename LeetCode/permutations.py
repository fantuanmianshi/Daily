"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        results = []
        self.permuteSolver(nums, 0, results)
        return results

    def permuteSolver(self, nums, start, results):
        if start >= len(nums):
            results.append(nums[:])
        else:
            i = start
            while i < len(nums):
                nums[i], nums[start] = nums[start], nums[i]
                self.permuteSolver(nums, start + 1, results)
                nums[i], nums[start] = nums[start], nums[i]
                i += 1


if __name__ == '__main__':
    s = Solution()
    print s.permute([1, 2, 3])

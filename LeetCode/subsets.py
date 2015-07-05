"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        result = []
        self.solver(sorted(nums), 0, [], result)
        return result

    def solver(self, nums, idx, solution, result):
        result.append(solution[:])
        i = idx
        while i < len(nums):
            solution.append(nums[i])
            self.solver(nums, i + 1, solution, result)
            solution.pop()
            i += 1

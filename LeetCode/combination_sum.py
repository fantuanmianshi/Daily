"""
Given a set of candidate numbers (C) and a target number (T), find all unique
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order.

The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 

A solution set is: 

[7] 
[2, 2, 3] 
"""


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        sorted_candidates = sorted(candidates)
        result = []
        self.solver(sorted_candidates, target, [], result, 0)
        return result

    def solver(self, candidates, target, solution, result, start):
        cur_sum = sum(solution)
        if cur_sum == target:
            result.append(solution[:])
        elif cur_sum > target:
            return
        else:
            i = start
            while i < len(candidates):
                solution.append(candidates[i])
                self.solver(candidates, target, solution, result, i)
                solution.pop()
                i += 1
                

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2, 3, 6, 7], 7)

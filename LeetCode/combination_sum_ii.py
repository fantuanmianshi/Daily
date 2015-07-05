"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order.

The solution set must not contain duplicate combinations.

For example, given candidate set 10,1,2,7,6,1,5 and target 8, 

A solution set is: 

[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
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
                self.solver(candidates, target, solution, result, i + 1)
                solution.pop()
                while i < len(candidates) - 1 and \
                      candidates[i] == candidates[i + 1]:
                    i += 1
                i += 1
                

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([2, 3, 6, 7], 7)

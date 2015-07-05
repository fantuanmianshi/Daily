"""
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        if n > sum(range(10)):
            return result
        self.solver(k, n, [], result, 1)
        return result

    def solver(self, k, n, solution, result, start):
        if sum(solution) == n:
            if len(solution) == k:
                result.append(solution[:])
        else:
            i = start
            while i < 10:
                solution.append(i)
                self.solver(k, n, solution, result, i + 1)
                solution.pop()
                i += 1


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(3, 9)

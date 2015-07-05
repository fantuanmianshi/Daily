"""
Given two integers n and k, return all possible combinations of k numbers out
of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        result = []
        self.solver(n, k, 1, [], result)
        return result

    def solver(self, n, k, start, solution, result):
        if len(solution) == k:
            result.append(solution[:])
        else:
            for x in range(start, n + 1):
                solution.append(x)
                self.solver(n, k, x + 1, solution, result)
                solution.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combine(4, 2)

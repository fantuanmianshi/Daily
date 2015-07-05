"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        result = []
        self.perms(n, 0, range(n + 1), result)
        print result
        return result[k]

    def perms(self, n, start, solution, result):
        result.append(solution[:])
        i = start
        while i < n:
            solution[i], solution[start] = solution[start], solution[i]
            self.perms(n, i + 1, solution, result)
            solution[i], solution[start] = solution[start], solution[i]
            i += 1


if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(4, 16)

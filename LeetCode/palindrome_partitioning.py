"""
Given a string s, partition s such that every substring of the partition is a
palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""


class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        result = []
        self.solver(s, 0, [], result)
        return result

    def is_palindrome(self, s):
        return s[::-1] == s

    def solver(self, s, start, solution, result):
        if start == len(s):
            result.append(solution[:])
        else:
            i = start
            while i < len(s):
                if self.is_palindrome(s[start:i + 1]):
                    solution.append(s[start: i + 1])
                    self.solver(s, i + 1, solution, result)
                    solution.pop()
                i += 1


if __name__ == '__main__':
    s = Solution()
    print s.partition('aab')
    print s.partition('a')

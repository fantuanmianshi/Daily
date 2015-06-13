"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        possible = [False] * (len(s) + 1)
        possible[0] = True

        for i in range(1, len(s) + 1):
            for k in range(i):
                possible[i] = possible[k] and s[k:i] in wordDict
                if possible[i]:
                    break
        return possible[-1]


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak('a', ['a'])
    print s.wordBreak('ab', ['a', 'b'])

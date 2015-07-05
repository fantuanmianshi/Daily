"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""


class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = {}
        for s in strs:
            ss = str(sorted(s))
            if ss not in result:
                result[ss] = [s]
            else:
                result[ss].append(s)
        str_results = []
        for x in result.values():
            if len(x) > 1:
                str_results += x
        return str_results


if __name__ == '__main__':
    s = Solution()
    print s.anagrams([""])

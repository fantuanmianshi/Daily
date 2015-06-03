"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        h, n = 0, 0
        while h < len(haystack) and n < len(needle):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
            else:
                h = h - n + 1
                n = 0
        if n == len(needle):
            return h - n
        return -1

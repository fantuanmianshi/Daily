"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        i = 0
        s_to_t = {}
        t_to_s = {}
        while i < len(s):
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False
            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]:
                    return False
            else:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            i += 1
        return True

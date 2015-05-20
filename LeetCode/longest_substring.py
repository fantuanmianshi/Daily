"""
Given a string, find the length of the longest substring without repeating
characters. For example, the longest substring without repeating letters for
"abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring
is "b", with the length of 1.
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        start, end, result = 0, 0, 0
        character_dict = {}
        while end < len(s):
            if s[end] not in character_dict:
                character_dict[s[end]] = end
            else:
                result = max(result, end - start)
                start = max(start, character_dict[s[end]] + 1)
                character_dict[s[end]] = end
            end += 1
        result = max(result, end - start)

        return result

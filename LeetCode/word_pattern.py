"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, words):
        """
        :type pattern: str
        :type words: str
        :rtype: bool
        """
        words_list = words.split()
        if len(words_list) != len(pattern):
            return False
        word_dict, pattern_dict = {}, {}
        for p, w in zip(pattern, words_list):
            if p not in pattern_dict:
                pattern_dict[p] = w
            if w not in word_dict:
                word_dict[w] = p
            if word_dict[w] != p or pattern_dict[p] != w:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.wordPattern('abba', 'dog cat cat dog')
    print s.wordPattern('abba', 'dog cat cat fish')

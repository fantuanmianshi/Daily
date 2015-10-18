"""
Given two words (beginWord and endWord), and a dictionary, find the length of
shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""


class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        if not beginWord or not endWord or not wordDict:
            return 0

        queue = [beginWord]
        level, last_num, curr_num = 1, 1, 0

        while queue:
            curr = queue.pop(0)
            last_num -= 1

            i = 0
            curr_array = [x for x in curr]
            while i < len(curr_array):
                c = ord('a')
                while c <= ord('z'):
                    orig = curr_array[i]
                    curr_array[i] = chr(c)
                    temp = ''.join(curr_array)
                    if temp == endWord:
                        return level + 1
                    if temp in wordDict:
                        curr_num += 1
                        queue.append(temp)
                        wordDict.remove(temp)
                    curr_array[i] = orig
                    c += 1
                i += 1

            if last_num == 0:
                last_num == curr_num
                curr_num = 0
                level += 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength('hot', 'dog', ['hot', 'dog', 'dot'])

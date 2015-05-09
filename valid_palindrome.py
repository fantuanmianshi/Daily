"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Tags: String, Two Pointers
"""


class Solution:
    def isAlphanumeric(self, s):
        return s.isalpha() or s.isdigit()

    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        length = len(s)
        left, right = 0, length - 1
        while left < right:
            # Move left to ignore non alphanumeric string
            while left < length and not self.isAlphanumeric(s[left]):
                left += 1
            # Move right to ignore non alphanumeric string
            while right >= 0 and not self.isAlphanumeric(s[right]):
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

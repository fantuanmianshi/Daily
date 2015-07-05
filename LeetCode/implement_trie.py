"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_key = False
        self.leaves = [None for _ in range(26)]


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        temp = self.root
        for w in word:
            index = ord(w) - ord('a')
            if temp.leaves[index] is None:
                temp.leaves[index] = TrieNode()
            temp = temp.leaves[index]
        temp.is_key = True
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        temp = self.root
        for w in word:
            index = ord(w) - ord('a')
            if temp.leaves[index] is None:
                return False
            temp = temp.leaves[index]
        return temp.is_key
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        temp = self.root
        for w in prefix:
            index = ord(w) - ord('a')
            if temp.leaves[index] is None:
                return False
            temp = temp.leaves[index]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

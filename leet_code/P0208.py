# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 09:49:27
# LastEditTime: 2020-03-08 10:26:06
# LastEditors: ssdcxy
# Description: 实现 Trie (前缀树)
# FilePath: /arithmetic_oj/LeetCode/P0208.py

class Trie:
    class Node:
        def __init__(self):
            self.childs = [None] * 26
            self.isLeaf = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.insert1(word, self.head)

    def insert1(self, word:str, node) -> None:
        if not node: return
        if not word:
            node.isLeaf = True
            return
        index = self.indexForChar(word[0])
        if not node.childs[index]:
            node.childs[index] = self.Node()
        self.insert1(word[1:], node.childs[index])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.search1(word, self.head)
    
    def search1(self, word:str, node) -> bool:
        if not node: return False
        if not word: return node.isLeaf
        index = self.indexForChar(word[0])
        return self.search1(word[1:], node.childs[index])


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.startsWith1(prefix, self.head)
    
    def startsWith1(self, prefix:str, node) -> bool:
        if not node: return False
        if not prefix: return True
        index = self.indexForChar(prefix[0])
        return self.startsWith1(prefix[1:], node.childs[index])

    def indexForChar(self, c:str) -> int:
        return ord(c) - ord('a')



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abbbba")
print(obj.search("abbaba"))
print(obj.startsWith("aba"))
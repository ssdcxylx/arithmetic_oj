# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-17 08:34:00
# LastEditTime: 2020-02-17 08:34:00
# LastEditors: ssdcxy
# Description: 单词接龙
# FilePath: /arithmetic_oj/LeetCode/P0127.py

import json
from typing import List
from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                intermediate_word = current_word[:i]  "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
        

        

def stringToString(input):
    return input[1:-1]

def stringToStringArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            beginWord = stringToString(line)
            line = next(lines)
            endWord = stringToString(line)
            line = next(lines)
            wordList = stringToStringArray(line)
            
            ret = Solution().ladderLength(beginWord, endWord, wordList)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
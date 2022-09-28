# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-28 09:20:01
# LastEditTime: 2020-03-28 09:52:11
# LastEditors: ssdcxy
# Description: 单词的压缩编码
# FilePath: /arithmetic_oj/LeetCode/P0820.py

import json
from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordSet = set(words)
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in wordSet:
                    wordSet.remove(word[i:])
        ans = 0
        for word in wordSet:
            ans += len(word)
        return ans + len(wordSet)
                
        

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
            words = stringToStringArray(line)
            
            ret = Solution().minimumLengthEncoding(words)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
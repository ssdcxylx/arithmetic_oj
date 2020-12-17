# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-17 19:04:21
# LastEditTime: 2020-03-17 19:12:55
# LastEditors: ssdcxy
# Description: 拼写单词
# FilePath: /arithmetic_oj/LeetCode/P1160.py

import json
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        import collections
        ans = 0
        cnt = collections.Counter(chars)
        for word in words:
            cur = collections.Counter(word)
            if all(cur[i] <= cnt[i] for i in word):
                ans += len(word)
        return ans


def stringToStringArray(input):
    return json.loads(input)

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            line = lines.next()
            words = stringToStringArray(line)
            line = lines.next()
            chars = stringToString(line)
            
            ret = Solution().countCharacters(words, chars)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
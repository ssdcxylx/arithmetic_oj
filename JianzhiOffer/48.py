# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 08:24:34
# LastEditTime: 2020-03-12 08:42:52
# LastEditors: ssdcxy
# Description: 最长不含重复字符的子字符串
# FilePath: /arithmetic_oj/JianzhiOffer/48.py

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = tail = 0
        _max = 0
        n = len(s)
        while tail < n:
            if s[tail] not in s[head:tail]:
                _max = max(tail-head+1, _max)
            else:
                while s[tail] in s[head:tail]:
                    head += 1
            tail += 1
        return _max

def stringToString(input):
    return input[1:-1]

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
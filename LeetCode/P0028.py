# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 09:41:54
# LastEditTime: 2020-03-21 10:00:33
# LastEditors: ssdcxy
# Description: 实现 strStr()
# FilePath: /arithmetic_oj/LeetCode/P0028.py

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle: return 0
        m, n = len(haystack), len(needle)
        if m < n: return -1
        for i in range(0, m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1

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
            haystack = stringToString(line);
            line = next(lines)
            needle = stringToString(line);
            
            ret = Solution().strStr(haystack, needle)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
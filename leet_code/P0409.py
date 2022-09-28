# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 11:27:10
# LastEditTime: 2020-03-03 11:39:50
# LastEditors: ssdcxy
# Description: 最长回文串
# FilePath: /arithmetic_oj/LeetCode/P0409.py

class Solution:
    def longestPalindrome(self, s: str) -> int:
        lst = [0 for i in range(52)]
        for c in s:
            if ord(c) <= 90:
                lst[ord(c)-65] += 1
            else:
                lst[ord(c)-65-7] += 1
        res = 0
        for i in lst:
            res += (i//2)*2
        if res < len(s):
            res += 1
        return res
        
        

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
            
            ret = Solution().longestPalindrome(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
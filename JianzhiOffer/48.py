# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 08:24:34
# LastEditTime: 2020-12-06 12:12:14
# LastEditors: ssdcxy
# Description: 最长不含重复字符的子字符串
# FilePath: /arithmetic_oj/JianzhiOffer/48.py

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        left = right = 0
        _max = 0
        while right < n:
            if s[right] not in s[left:right]:
               _max = max(right-left+1, _max)
            else:
                left += 1
                while s[right] in s[left:right]:
                    left += 1
            right += 1
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
# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-04 09:59:36
# LastEditTime: 2020-03-04 10:10:22
# LastEditors: ssdcxy
# Description: 计数二进制子串
# FilePath: /arithmetic_oj/LeetCode/P0696.py

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_size, cur_size, count = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_size += 1
            else:
                pre_size = cur_size
                cur_size = 1
            if pre_size >= cur_size:
                count += 1
        return count

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
            
            ret = Solution().countBinarySubstrings(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
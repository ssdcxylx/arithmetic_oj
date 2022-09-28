# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-23 15:51:24
# LastEditTime: 2020-12-23 15:51:32
# LastEditors: ssdcxy
# Description: 字符串中的第一个唯一字符
# FilePath: /arithmetic_oj/LeetCode/P0387.py

class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        counter = collections.Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            
            ret = Solution().firstUniqChar(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
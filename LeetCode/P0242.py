# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 11:19:13
# LastEditTime: 2020-03-03 11:23:47
# LastEditors: ssdcxy
# Description: 有效的字母异位词
# FilePath: /arithmetic_oj/LeetCode/P0242.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1 = [0 for i in range(26)]
        lst2 = [0 for i in range(26)]
        for c in s:
            lst1[ord(c)-97] += 1
        for c in t:
            lst2[ord(c)-97] += 1
        return lst1 == lst2


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
            line = next(lines)
            t = stringToString(line);
            
            ret = Solution().isAnagram(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
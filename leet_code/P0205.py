# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 11:43:25
# LastEditTime: 2020-03-03 11:56:49
# LastEditors: ssdcxy
# Description: 同构字符串
# FilePath: /arithmetic_oj/LeetCode/P0205.py

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst1 = [0 for i in range(256)]
        lst2 = [0 for i in range(256)]
        for i in range(len(s)):
            a, b = s[i], t[i]
            if lst1[ord(a)] != lst2[ord(b)]:
                return False
            lst1[ord(a)] = i+1
            lst2[ord(b)] = i+1
        return True


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
            
            ret = Solution().isIsomorphic(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
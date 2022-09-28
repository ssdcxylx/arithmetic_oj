# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 09:31:00
# LastEditTime: 2020-03-03 09:41:45
# LastEditors: ssdcxy
# Description: 有效的括号
# FilePath: /arithmetic_oj/LeetCode/P0020.py

class Solution:
    def isValid(self, s: str) -> bool:
        lst1 = list()
        for c in s:
            if lst1:
                if c == "]" and lst1[-1] == "[":
                    lst1.pop()
                elif c == "}" and lst1[-1] == "{":
                    lst1.pop()
                elif c == ")" and lst1[-1] == "(":
                    lst1.pop()
                else:
                    lst1.append(c)
            else:
                lst1.append(c)
        return not lst1


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
            
            ret = Solution().isValid(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
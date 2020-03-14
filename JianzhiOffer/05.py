# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-09 21:40:38
# LastEditTime: 2020-03-09 21:46:16
# LastEditors: ssdcxy
# Description: 替换空格
# FilePath: /arithmetic_oj/JianzhiOffer/05.py

class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return ''.join(res)

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
            
            ret = Solution().replaceSpace(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
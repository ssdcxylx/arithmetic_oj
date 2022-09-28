# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:07:31
# LastEditTime: 2020-12-13 12:07:50
# LastEditors: ssdcxy
# Description: 左旋转字符串
# FilePath: /arithmetic_oj/JianzhiOffer/58-2.py

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[:n] = s[:n][::-1]
        s[n:] = s[n:][::-1]
        return "".join(s[::-1])

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
            line = next(lines)
            n = int(line);
            
            ret = Solution().reverseLeftWords(s, n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
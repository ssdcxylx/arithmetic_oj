# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:02:59
# LastEditTime: 2020-12-11 12:07:57
# LastEditors: ssdcxy
# Description: 翻转单词顺序
# FilePath: /arithmetic_oj/JianzhiOffer/58-1.py

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        n = len(s)
        left = right = n
        res = []
        while right:
            while left and s[left-1] != " ":
                left -= 1
            res.append(s[left:right])
            while left and s[left-1] == " ":
                left -= 1
            right = left
        return " ".join(res)
        

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
            
            ret = Solution().reverseWords(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
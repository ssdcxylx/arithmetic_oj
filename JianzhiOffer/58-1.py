# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:02:59
# LastEditTime: 2020-03-12 14:06:49
# LastEditors: ssdcxy
# Description: 翻转单词顺序
# FilePath: /arithmetic_oj/JianzhiOffer/58-1.py

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(' ')
        while '' in lst:
            lst.remove('')
        return ' '.join(lst[::-1])
        

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
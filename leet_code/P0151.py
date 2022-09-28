# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-04-10 16:29:47
# LastEditTime: 2020-04-10 16:34:03
# LastEditors: ssdcxy
# Description: 翻转字符串里的单词
# FilePath: /arithmetic_oj/LeetCode/P0151.py

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return s
        lst = s.strip().split(' ')
        while '' in lst:
            lst.remove('')
        return ' '.join(lst[::-1])

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
            
            ret = Solution().reverseWords(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
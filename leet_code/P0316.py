# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-19 11:09:02
# LastEditTime: 2020-12-19 11:34:14
# LastEditors: ssdcxy
# Description: 去除重复字母
# FilePath: /arithmetic_oj/LeetCode/P0316.py

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        stack = []
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return ''.join(stack)

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
            
            ret = Solution().removeDuplicateLetters(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
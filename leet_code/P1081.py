# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-19 11:36:11
# LastEditTime: 2020-12-19 12:07:00
# LastEditors: ssdcxy
# Description: 不同字符的最小子序列
# FilePath: /arithmetic_oj/LeetCode/P1081.py

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        seen = set()
        stack = []
        for c in s:
            if c not in seen:
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
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
            
            ret = Solution().smallestSubsequence(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-19 10:30:21
# LastEditTime: 2020-12-19 10:58:53
# LastEditors: ssdcxy
# Description: 移掉K位数字
# FilePath: /arithmetic_oj/LeetCode/P0402.py

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num: return '0'
        if not k: return num
        remain = len(num) - k
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


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
            num = stringToString(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().removeKdigits(num, k)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
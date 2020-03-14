# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 20:38:54
# LastEditTime: 2020-03-10 21:24:30
# LastEditors: ssdcxy
# Description: 栈的压入、弹出序列
# FilePath: /arithmetic_oj/JianzhiOffer/31.py

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack

def stringToIntegerList(input):
    return json.loads(input)

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
            pushed = stringToIntegerList(line);
            line = next(lines)
            popped = stringToIntegerList(line);
            
            ret = Solution().validateStackSequences(pushed, popped)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
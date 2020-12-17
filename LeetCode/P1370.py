# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-11-25 20:27:58
# LastEditTime: 2020-11-25 20:43:08
# LastEditors: ssdcxy
# Description: 上升下降字符串
# FilePath: /arithmetic_oj/LeetCode/P1370.py

class Solution:
    def sortString(self, s: str) -> str:
        ord_a = ord('a')
        count = [0] * 26
        for c in s:
            count[ord(c) - ord_a] += 1
        n = len(s)
        res = []
        while len(res) < s:
            for i in range(26):
                if count[i]:
                    res.append(chr(i + ord_a))
                    count[i] -= 1
            for i in range(25, -1, -1):
                if count[i]:
                    res.append(chr(i + ord_a))
                    count[i] -= 1
        return "".join(res)
             
        
            
            


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
            
            ret = Solution().sortString(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
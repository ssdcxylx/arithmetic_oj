# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 10:21:33
# LastEditTime: 2020-03-21 10:59:02
# LastEditors: ssdcxy
# Description:  外观数列
# FilePath: /arithmetic_oj/LeetCode/P0038.py

class Solution:
    def countAndSay(self, n: int) -> str:
        nums = []
        nums.append("1")
        if n==1: return nums[0]
        for i in range(1, n):
            p = []
            s = ""
            for x in nums[i-1]:
                if not p or x == p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)
            s += str(len(p))
            s += p[0]
            nums.append(s)
        return nums[n-1]

                
                


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
            n = int(line);
            
            ret = Solution().countAndSay(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
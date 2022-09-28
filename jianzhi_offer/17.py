# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:19:07
# LastEditTime: 2020-11-26 10:58:03
# LastEditors: ssdcxy
# Description: 打印从1到最大的n位数
# FilePath: /arithmetic_oj/JianzhiOffer/17.py

import json
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # def increment():
        #     isOver = True
        #     nTaskOver = 0
        #     for i in range(n-1, -1, -1):
        #         nSum = nTaskOver + number[i]
        #         if i == n-1:
        #             nSum += 1
        #         if nSum >= 10:
        #             if i == 0:
        #                 return False
        #             else:
        #                 nSum -= 10
        #                 nTaskOver = 1
        #                 number[i] = nSum
        #         else:
        #             number[i] = nSum
        #             return True
        #     return not isOver
        # def printNumber():
        #     ans = 0
        #     for i in range(n):
        #         if number[i]:
        #             ans += (10 ** (n - i - 1) * number[i])
        #     return ans
        # number = [0] * n
        # res = []
        # while increment():
        #     res.append(printNumber())
        # return res
        def dfs(x):
            nonlocal left, count_nine
            if x == n:
                s = ''.join(num[left:])
                if s != '0': res.append(int(s))
                if n - left == count_nine: left -= 1
                return
            for i in range(10):
                num[x] = str(i)
                if i == 9: count_nine += 1
                dfs(x+1)
            count_nine -= 1
        num, res = ['0'] * n, []
        left, count_nine = n-1, 0
        dfs(0)
        return res
            


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().printNumbers(n)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 21:36:01
# LastEditTime: 2020-12-06 11:42:08
# LastEditors: ssdcxy
# Description: 把数字翻译成字符串
# FilePath: /arithmetic_oj/JianzhiOffer/46.py

class Solution:
    def translateNum(self, num: int) -> int:
        # num = str(num)
        # n = len(num)
        # a = b = 1
        # for i in range(2, n+1):
        #     a, b = (a + b if "10" <= s[i-2:i] <= "25" else a), a
        # return a
        def recursive(i):
            if not i: return 1
            if "10" <= num[i-2:i] <= "25":
                return recursive(i-1) + recursive(i-2)
            else:
                return recursive(i-1)
        num = str(num)
        n = len(num)
        return recursive(n)
       

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
            num = int(line);
            
            ret = Solution().translateNum(num)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
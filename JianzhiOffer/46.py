# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 21:36:01
# LastEditTime: 2020-03-11 21:50:06
# LastEditors: ssdcxy
# Description: 把数字翻译成字符串
# FilePath: /arithmetic_oj/JianzhiOffer/46.py

class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(1, n):
            if num[i-1] == "0" or num[i-1:i+1] > "25":
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i] + dp[i-1]
        return dp[n]
        
            
        

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
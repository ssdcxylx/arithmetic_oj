# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 15:18:05
# LastEditTime: 2020-02-22 15:57:55
# LastEditors: ssdcxy
# Description: 计数质数
# FilePath: /arithmetic_oj/LeetCode/P0204.py

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0

        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                isPrime[i*i:n:i] = [0] * ((n-i*i-1)//i+1)
        return sum(isPrime)
            

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
            
            ret = Solution().countPrimes(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
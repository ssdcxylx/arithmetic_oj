# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-22 15:18:05
# LastEditTime: 2020-12-03 10:26:28
# LastEditors: ssdcxy
# Description: 计数质数
# FilePath: /arithmetic_oj/LeetCode/P0204.py

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrime = [1] * n
        primes = []
        isPrime[0] = isPrime[1] = 0
        for i in range(2, n):
            if isPrime[i]: primes.append(i)
            for prime in primes:
                if prime * i >= n:
                    break
                else:
                    isPrime[prime*i] = 0
                    if not i % prime:
                        break
        return len(primes)
            

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
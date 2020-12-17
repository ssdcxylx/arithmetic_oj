# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-28 09:54:52
# LastEditTime: 2020-03-28 10:26:22
# LastEditors: ssdcxy
# Description: 卡牌分组
# FilePath: /arithmetic_oj/LeetCode/P0914.py

import json
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            if not b: return a
            return gcd(b, a%b)
        n = len(deck)
        if n < 2: return False
        cnt = [0] * 10000
        for x in deck:
            cnt[x] += 1
        tmp = cnt[deck[0]]
        for i in range(1, 1000):
            if cnt[i] == 0: continue
            if cnt[i] == 1: return False
            tmp = gcd(tmp, cnt[i])
            if tmp == 1: return False
        return True
            


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
            deck = stringToIntegerList(line);
            
            ret = Solution().hasGroupsSizeX(deck)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
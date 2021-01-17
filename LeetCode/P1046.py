# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-31 21:08:46
# LastEditTime: 2020-12-31 21:36:34
# LastEditors: ssdcxy
# Description: 最后一块石头的重量
# FilePath: /arithmetic_oj/LeetCode/P1046.py

import json
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def build_heap():
            nonlocal n
            for i in range(n>>1, -1, -1):
                sink(i)
        def sink(i):
            nonlocal n
            while 2 * i + 1 < n:
                left = 2 * i + 1
                right = 2 * i + 2
                if right < n:
                    mx = left if stones[left] >= stones[right] else right
                else:
                    mx = left
                if stones[mx] <= stones[i]: break
                stones[i], stones[mx] = stones[mx], stones[i]
                i = mx
        def swim(i):
            while i > 0 and stones[(i-1)>>1] < stones[i]:
                stones[i], stones[(i-1)>>1] = stones[(i-1)>>1], stones[i]
                i = ((i-1)>>1)
        def get_max():
            nonlocal n
            mx = stones[0]
            stones[0] = None
            stones[0], stones[n-1] = stones[n-1], stones[0]
            n -= 1
            sink(0)
            return mx
        def push(v):
            nonlocal n
            stones[n] = v
            swim(n)
            n += 1
        n = len(stones)
        build_heap()
        while n > 1:
            y = get_max()
            x = get_max()
            if x != y:
                push(y-x)
        if not stones: return 0
        return stones[0]

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
            stones = stringToIntegerList(line);
            
            ret = Solution().lastStoneWeight(stones)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
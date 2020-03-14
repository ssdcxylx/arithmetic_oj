# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-16 16:37:37
# LastEditTime: 2020-02-16 16:37:39
# LastEditors: ssdcxy
# Description: 完全平方数  
# FilePath: /arithmetic_oj/LeetCode/P0279.py

from typing import List
import queue

class Solution:
    
    def numSquares(self, n: int) -> int:
        squares = self.generateSquares(n)
        _queue = queue.Queue()
        marked = [False for i in range(n+1)]
        _queue.put(n)
        marked[n] = True
        level = 0
        while not _queue.empty():
            size = _queue.qsize()
            level += 1
            while size > 0:
                size -= 1
                cur = _queue.get()
                for square in squares:
                    next = cur - square
                    if next < 0:
                        break
                    if next == 0:
                        return level
                    if marked[next]:
                        continue
                    marked[next] = True
                    _queue.put(next)
        return n


    def generateSquares(self, n: int) -> List:
        squares = list()
        square = 1
        diff = 3
        while square <= n:
            squares.append(square)
            square += diff
            diff += 2
        return squares


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
            
            ret = Solution().numSquares(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
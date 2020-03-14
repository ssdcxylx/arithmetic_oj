# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 09:02:08
# LastEditTime: 2020-03-10 09:21:06
# LastEditors: ssdcxy
# Description: 机器人的运动范围
# FilePath: /arithmetic_oj/JianzhiOffer/13.py

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue, visited = [(0,0,0,0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i+1, j, si + 1 if (i+1) % 10 else si - 8, sj))
            queue.append((i, j+1, si, sj + 1 if (j+1) % 10 else sj - 8))
        return len(visited)

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
            m = int(line);
            line = next(lines)
            n = int(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().movingCount(m, n, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
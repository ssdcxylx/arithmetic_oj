# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-04 10:52:11
# LastEditTime: 2020-03-05 08:59:48
# LastEditors: ssdcxy
# Description: 课程表
# FilePath: /arithmetic_oj/LeetCode/P0207.py

import json
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            nonlocal isPossible
            if not isPossible:
                return
            visited[i] = 1
            for j in tmp[i]:
                if visited[j] == 0:
                    dfs(j)
                elif visited[j] == 1:
                    isPossible = False
            visited[i] = -1
            return True
        tmp = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for pre, cur in prerequisites:
            tmp[cur].append(pre)
        isPossible = True
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return isPossible

def stringToInt(input):
    return int(input)

def stringToInt2dArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            numCourses = stringToInt(line)
            line = next(lines)
            prerequisites = stringToInt2dArray(line)
            
            ret = Solution().canFinish(numCourses, prerequisites)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
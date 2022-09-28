# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 07:53:37
# LastEditTime: 2020-03-05 09:00:03
# LastEditors: ssdcxy
# Description: 课程表 II
# FilePath: /arithmetic_oj/LeetCode/P0210.py

from typing import List
import json

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            res.append(i)
        tmp = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        res = []
        for pre, cur in prerequisites:
            tmp[cur].append(pre)
        isPossible = True
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return res[::-1] if isPossible else []

def stringToInt(input):
    return int(input)

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().findOrder(numCourses, prerequisites)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
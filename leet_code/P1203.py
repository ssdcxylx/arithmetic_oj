# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-12 17:19:37
# LastEditTime: 2021-01-14 09:47:32
# LastEditors: ssdcxy
# Description: 项目管理
# FilePath: /arithmetic_oj/LeetCode/P1203.py

from typing import List
import json

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topologicalSort(adj: List[int], inDegree: List[int], n: int):
            res = []
            queue = list()
            for i in range(n):
                if not inDegree[i]:
                    queue.append(i)
            while queue:
                front = queue.pop(0)
                res.append(front)
                for i in adj[front]:
                    inDegree[i] -= 1
                    if not inDegree[i]:
                        queue.append(i)
            if len(res) == n:
                return res
            return []

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        groupAdj = [[] for i in range(m)]
        itemAdj = [[] for j in range(n)]

        groupsIndegree = [0 for i in range(m)]
        itemsIndegree = [0 for i in range(n)]
        
        for i in range(n):
            currentGroup = group[i]
            for beforeItem in beforeItems[i]:
                beforeGroup = group[beforeItem]
                if beforeGroup != currentGroup:
                    groupAdj[beforeGroup].append(currentGroup)
                    groupsIndegree[currentGroup] += 1
        
        for i in range(n):
            for beforeItem in beforeItems[i]:
                itemAdj[beforeItem].append(i)
                itemsIndegree[i] += 1
        
        groupsList = topologicalSort(groupAdj, groupsIndegree, m)
        if not groupsList:
            return []
        itemsList = topologicalSort(itemAdj, itemsIndegree, n)
        if not itemsList:
            return []
        
        groups2Items = dict()
        for items in itemsList:
            if group[items] not in groups2Items:
                groups2Items[group[items]] = []
            groups2Items[group[items]].append(items)
        
        res = []
        for groups in groupsList:
            if groups in groups2Items:
                res += groups2Items.get(groups)
        return res

def stringToInt(input):
    return int(input)

def stringToIntegerList(input):
    return json.loads(input)

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
            line = lines.next()
            n = stringToInt(line)
            line = lines.next()
            m = stringToInt(line)
            line = lines.next()
            group = stringToIntegerList(line)
            line = lines.next()
            beforeItems = stringToInt2dArray(line)
            
            ret = Solution().sortItems(n, m, group, beforeItems)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
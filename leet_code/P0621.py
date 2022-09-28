# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-18 10:34:48
# LastEditTime: 2020-12-18 10:56:16
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/LeetCode/P0621.py

import json

class Solution(object):
    def leastInterval(self, tasks, n):
        # length = len(tasks)
        # ts = [0] * 26
        # for task in tasks:
        #     ts[ord(task)-ord('A')] += 1
        # most = max(ts)
        # res = (most-1) * (n+1)
        # for i in ts:
        #     if i == most:
        #         res += 1
        # return res if res > length else length
        import collections
        counter = collections.Counter(tasks)
        m = len(counter)
        freq = list(counter.values())
        nextValid = [1] * m
        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if freq[j] > 0)
            time = max(minNextValid, time)
            best = -1
            for j in range(m):
                if freq[j] and nextValid[j] <= time:
                    if best == -1 or freq[j] > freq[best]:
                        best = j
            nextValid[best] = time + n + 1
            freq[best] -= 1
        return time


def stringToCharArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            tasks = stringToCharArray(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().leastInterval(tasks, n)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
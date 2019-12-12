# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-09 22:05:56
# LastEditTime: 2019-12-10 20:26:05
# LastEditors: ssdcxy
# Description: 根据身高重建队列
# FilePath: /arithmetic_oj/LeetCode/P0406.py


import json
from typing import List


class Solution(object):
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people = sorted(people, key=lambda i: i[1])
        # n = len(people)
        # for i in range(1, n):
        #     count = people[i][1]
        #     for j in range(0, i):
        #         if people[j][0] >= people[i][0]:
        #             if count != 0:
        #                 count -= 1
        #             else:
        #                 temp = people[i]
        #                 people.remove(people[i])
        #                 people.insert(j, temp)
        #                 break
        # return people
        people = sorted(people, key=lambda i: (-i[0], i[1]))
        q = list()
        for x in people:
            q.insert(x[1], x)
        return q


def stringToInt2dArray(input):
    return json.loads(input)


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            people = stringToInt2dArray(line)

            ret = Solution().reconstructQueue(people)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

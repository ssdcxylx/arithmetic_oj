# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-19 21:59:58
# LastEditTime: 2020-02-20 07:48:41
# LastEditors: ssdcxy
# Description: 复原ip地址
# FilePath: /arithmetic_oj/LeetCode/P0093.py

import json
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1
        
        def update_count(curr_pos):
            segment = s[curr_pos + 1 : n]
            if valid(segment):
                segments.append(segment)
                output.append(".".join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            for curr_pos in range(prev_pos+1, min(n-1, prev_pos+4)):
                segment = s[prev_pos + 1: curr_pos + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_count(curr_pos)
                    else:
                        backtrack(curr_pos, dots-1)
                    segments.pop()
        n = len(s)
        output, segments = [], []
        backtrack()
        return output
                    
        

def stringToString(input):
    return input[1:-1]

def stringArrayToString(input):
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
            s = stringToString(line)
            
            ret = Solution().restoreIpAddresses(s)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-11 10:51:02
# LastEditTime: 2020-12-11 11:12:31
# LastEditors: ssdcxy
# Description: Dota2 参议院
# FilePath: /arithmetic_oj/LeetCode/P0649.py

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        import collections
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0]+n)
            else:
                dire.append(dire[0]+n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"
        

def stringToString(input):
    return input[1:-1]

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
            senate = stringToString(line);
            
            ret = Solution().predictPartyVictory(senate)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
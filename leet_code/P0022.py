# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 09:24:00
# LastEditTime: 2020-03-21 09:35:57
# LastEditors: ssdcxy
# Description: 括号生成
# FilePath: /arithmetic_oj/LeetCode/P0022.py

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            nonlocal n
            if len(s) == 2 * n:
                res.append(s)
                return 
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        res = []
        backtrack('', 0, 0)
        return res
        
            

def stringToInt(input):
    return int(input)

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
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
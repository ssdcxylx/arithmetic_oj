# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 08:39:06
# LastEditTime: 2020-03-11 08:48:05
# LastEditors: ssdcxy
# Description: 将数组分成和相等的三个部分
# FilePath: /arithmetic_oj/LeetCode/P1013.py

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0: return False
        target = s // 3
        i, cur, n = 0, 0, len(A)
        while i < n:
            cur += A[i]
            i += 1
            if cur == target:
                break
        if cur != target: return False
        while i < n - 1:
            cur += A[i]
            i += 1
            if cur == target * 2:
                return True
        return False

        
        

def stringToIntegerList(input):
    return json.loads(input)

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
            A = stringToIntegerList(line);
            
            ret = Solution().canThreePartsEqualSum(A)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
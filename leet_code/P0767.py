# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-11-30 11:06:21
# LastEditTime: 2020-11-30 13:00:26
# LastEditors: ssdcxy
# Description: 重构字符串
# FilePath: /arithmetic_oj/LeetCode/P0767.py

class Solution:
    def reorganizeString(self, S: str) -> str:
        import collections
        import heapq
        if len(S) < 2:
            return S
        n = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (n + 1) // 2:
            return ""
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))
        if queue:
            ans.append(queue[0][1])
        return "".join(ans)
        


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
            S = stringToString(line);
            
            ret = Solution().reorganizeString(S)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
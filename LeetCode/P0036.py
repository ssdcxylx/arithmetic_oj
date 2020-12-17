# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 10:09:47
# LastEditTime: 2020-03-21 10:19:06
# LastEditors: ssdcxy
# Description: 有效的数独
# FilePath: /arithmetic_oj/LeetCode/P0036.py



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

def stringToChar2dArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            board = stringToChar2dArray(line)
            
            ret = Solution().isValidSudoku(board)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
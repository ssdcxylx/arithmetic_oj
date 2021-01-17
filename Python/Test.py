# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-10-12 08:57:00
# LastEditTime: 2020-12-23 18:56:25
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/Python/Test.py

# import sys
# n = int(sys.stdin.readline().strip())
# for i in range(n):
#     lst = []
#     m = int(sys.stdin.readline().strip())
#     for j in range(m):
#         ops = sys.stdin.readline().strip().split()
#         if len(ops) > 1:
#             [op, num] = ops
#         else:
#             op = ops[0] 
#         num = int(num)
#         if op == "PUSH":
#             lst.append(num)
#         elif op == "TOP":
#             if not lst:
#                 print(-1)
#             else:
#                 print(lst[0])
#         elif op == "POP":
#             if not lst:
#                 print(-1)
#             else:
#                 lst.pop(0)
#         elif op == "SIZE":
#             print(len(lst))
#         elif op == "CLEAR":
#             lst.clear()

    

# import sys
# import math
# m = int(sys.stdin.readline().strip())
# for i in range(m):
#     n = int(sys.stdin.readline().strip())
#     lst_a = [[]] * n
#     for j in range(n):
#        lst_a[j] = list(map(int, sys.stdin.readline().strip().split()))
#     lst_b = [[]] * n
#     flag = False
#     for j in range(n):
#         lst_b[j] = list(map(int, sys.stdin.readline().strip().split()))
#         if lst_b[j] in lst_a:
#             flag = True
#     if flag:
#         print("%.3f"%0.000)
#     else:
#         _min = float('inf')
#         for j in range(n):
#             for k in range(n):
#                 dis = math.sqrt(math.pow(lst_a[j][0] - lst_b[k][0], 2) + math.pow(lst_a[j][1] - lst_b[k][1], 2))
#                 if dis < _min:
#                     _min = dis
#         print("%.3f"%_min)
        

# import sys
# m = int(sys.stdin.readline().strip())
# lst1 = []
# lst2 = []
# for j in range(m):
#     ops = sys.stdin.readline().strip().split()
#     if len(ops) > 1:
#         [op, num] = ops
#         num = int(num)
#     else:
#         op = ops[0] 
#     if op == "add":
#         lst1.append(num)
#     elif op == "poll":
#         if not lst2:
#             if len(lst1) > 1:
#                lst2 = lst1[::-1]
#                lst2.pop()
#             lst1.clear()
#         else:
#             lst2.pop()
#     elif op == "peek":
#         if not lst2:
#             if len(lst1) == 1:
#                 print(lst1[0])

#             else:
#                 lst2 = lst1[::-1]
#                 print(lst2[-1])
#                 lst1.clear() 
#         else:
#             print(lst2[-1])

# import sys
# import math
# n = int(sys.stdin.readline().strip())
# for i in range(n):
#     [x, k] = list(map(int, sys.stdin.readline().strip().split()))
#     tmp = x
#     cur = 0
#     while tmp:
#         tmp //= 2
#         cur += 1
#     if k >= cur:
#         print(-1)
#     else:
#         delta = x - (1<<(cur-1))
#         if delta % 1 != 0:
#             delta -= 1
#         print((1 << (k-1)) + (delta >> (cur - k)))


import sys

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        
class Solution:
    def reverse(self, root, k):
        if not root: return None
        if not k: return root
        stack = []
        cur = root
        res = ListNode()
        tmp = res
        while cur:
            begin = cur
            while begin and len(stack) < k:
                stack.append(begin)
                begin = begin.next
            if len(stack) == k:
                cur = begin
                while stack:
                    tmp.next = stack.pop()
                    tmp = tmp.next
            else:
                break
        tmp.next = cur
        return res.next

if __name__ == "__main__":
    line = sys.stdin.readline()
    n = int(line)
    line = sys.stdin.readline()
    line = line.split(' ')
    root = ListNode()
    tmp = root
    for node in line:
        tmp.next = ListNode(int(node))
        tmp = tmp.next
    line = sys.stdin.readline()
    k = int(line)  
    solution = Solution()
    res = solution.reverse(root.next, k)
    while res:
        print(res.val, end="")
        res = res.next
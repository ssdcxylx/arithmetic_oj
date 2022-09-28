# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-11-22 20:23:21
# LastEditTime: 2020-11-22 22:16:35
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/JianzhiOffer/Test.py

            

nums = [2, 3, 5, 4, 3, 2, 6, 7]

n = len(nums)
start = 0
end = n

def count_range(start, end):
    if not nums:
        return 0
    count = 0
    for i in range(n):
        if start <= nums[i] <= end:
            count += 1
    return count

while start < end:
    mid = (start + end) >> 1
    left = count_range(start, mid)
    right = count_range(mid+1, end)
    if left > mid:
        end = mid
    else:
        start = mid + 1
print(mid)




        
        
    

    
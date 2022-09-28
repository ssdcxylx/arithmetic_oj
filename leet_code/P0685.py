# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 09:58:08
# LastEditTime: 2020-03-05 10:22:37
# LastEditors: ssdcxy
# Description: 冗余连接 II
# FilePath: /arithmetic_oj/LeetCode/P0685.py

from typing import List
import json

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        多的边有这么三种情况：
        1.指向树的根节点，这样所有的节点入度都是1，这样的话说明有环，从后往前依次删去一条边，如果删完之后依然满足所有节点联通，说明这条边是多余的
        2.指向自己，也就是说这个边的原点和终点是一样的，这个可以直接在第一遍遍历的时候判断出来
        3.指向树中间的某个节点k,那么指向节点k就会有两个边，也就是k的入度会是2，这样的话这两条边肯定有一个是多的。删掉其中的一个如果依然联通，说明这条边是多的。
        '''
        cache={} #保存点v为终点的边的编号
        max_N=0
        in_degree2=[]
        for i,e in enumerate(edges):
            u,v=e
            if u==v:
                return e
            max_N=max([max_N,u,v])
            if v not in cache:
                cache[v]=i
            else:
                in_degree2=[cache[v],i]
                break
                
        if len(in_degree2)==0: #说明没有入度为2的点，说明多的线连到了root节点，存在一个环
            for i in range(len(edges)-1,-1,-1): #从最后一个边删，如果删完图还是联通的说明这个边是多余的
                if self.is_graph_connected(edges[:i]+edges[i+1:]):
                    return edges[i]
        else: # 说明有入度为2的点，则指向该点的两条边一定有一条是多的
            later_edge_idx=max(in_degree2)
            if self.is_graph_connected(edges[:later_edge_idx]+edges[later_edge_idx+1:]):
                return edges[later_edge_idx]
            else:
                return edges[min(in_degree2)]
        return 
    
    
    def is_graph_connected(self,edges):
        max_N=len(edges)+1 # n条边有n+1个顶点
        self.father=[i for i in range(max_N+1)]
        for e in edges:
            u,v=e
            self.union(u,v)
        
        father_1=self.find(1)
        for i in range(1,max_N+1):
            if father_1 != self.find(i):
                return False
        return True

    
    def find(self,cur):
        while self.father[cur]!=cur:
            self.father[cur]=self.father[self.father[cur]]
            cur=self.father[cur]
        return cur

    def union(self,u,v):
        
        fu=self.find(u)
        fv=self.find(v)
        if fu!=fv:
            self.father[fu]=fv
        return True
                    

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            edges = stringToInt2dArray(line)
            
            ret = Solution().findRedundantDirectedConnection(edges)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
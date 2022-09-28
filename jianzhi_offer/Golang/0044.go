package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func largestValues(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}
	queue := []*TreeNode{root}
	n := len(queue)
	for n > 0 {
		cur := math.MinInt32
		for i := 0; i < n; i++ {
			node := queue[0]
			cur = max(cur, node.Val)
			queue = queue[1:]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		ans = append(ans, cur)
		n = len(queue)
	}

	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

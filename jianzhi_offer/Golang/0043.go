package main

import "math/bits"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type CBTInserter struct {
	root *TreeNode
	cnt  int
}

func Constructor(root *TreeNode) CBTInserter {
	q := []*TreeNode{root}
	cnt := 0
	for len(q) > 0 {
		cnt++
		node := q[0]
		q = q[1:]
		if node.Left != nil {
			q = append(q, node.Left)
		}
		if node.Right != nil {
			q = append(q, node.Right)
		}
	}
	return CBTInserter{
		root: root,
		cnt:  cnt,
	}
}

func (this *CBTInserter) Insert(v int) int {
	this.cnt++
	child := &TreeNode{Val: v}
	node := this.root
	for i := bits.Len(uint(this.cnt)) - 2; i > 0; i-- {
		if this.cnt>>i&1 == 0 {
			node = node.Left
		} else {
			node = node.Right
		}
	}
	if this.cnt&1 == 0 {
		node.Left = child
	} else {
		node.Right = child
	}
	return node.Val
}

func (this *CBTInserter) Get_root() *TreeNode {
	return this.root
}

package main

type Node struct {
	Val  int
	Next *Node
}

func insert(aNode *Node, x int) *Node {
	newNode := &Node{x, nil}
	if aNode == nil {
		newNode.Next = newNode
		return newNode
	}
	head := aNode
	for aNode.Next != head {
		if x >= aNode.Val && x <= aNode.Next.Val {
			break
		}
		if aNode.Val > aNode.Next.Val {
			if x > aNode.Val || x < aNode.Next.Val {
				break
			}
		}
		aNode = aNode.Next
	}
	next := aNode.Next
	aNode.Next = newNode
	newNode.Next = next
	return head
}

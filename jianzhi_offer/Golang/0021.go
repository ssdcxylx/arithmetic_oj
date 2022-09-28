package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	d := &ListNode{0, head}
	a, b := head, d
	for i := 0; i < n; i++ {
		a = a.Next
	}
	for ; a != nil; a = a.Next {
		b = b.Next
	}
	b.Next = b.Next.Next
	return d.Next
}

package main

type ListNode struct {
	Val int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	front := head
	var recursive func(*ListNode) bool
	recursive = func(cur *ListNode) bool {
		if cur != nil {
			if !recursive(cur.Next) {
				return false
			}
			if cur.Val != front.Val {
				return false
			}
			front = front.Next
		}
		return true
	}
	return recursive(head)
}
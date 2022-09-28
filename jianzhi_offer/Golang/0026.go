package main

type ListNode struct {
	Val int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		fast = fast.Next.Next
		slow = slow.Next
	}
	return slow
}

func reverse(head *ListNode) *ListNode {
	var prev, cur *ListNode = nil, head
	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
}

func merge(l1, l2 *ListNode) {
	var tmp1, tmp2 *ListNode
	for l1 != nil && l2 != nil {
		tmp1 = l1.Next
		tmp2 = l2.Next

		l1.Next = l2
		l1 = tmp1
		l2.Next = l1
		l2 = tmp2
	}
}

func reorderList(head *ListNode) {
	if head == nil {
		return
	}
	mid := middleNode(head)
	l1 := head
	l2 := mid.Next
	mid.Next = nil
	l2 = reverse(l2)
	merge(l1, l2)
}


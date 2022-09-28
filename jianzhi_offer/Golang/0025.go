package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) (ans *ListNode) {
	var stack1, stack2 []int
	for l1 != nil {
		stack1 = append(stack1, l1.Val)
		l1 = l1.Next
	}
	for l2 != nil {
		stack2 = append(stack2, l2.Val)
		l2 = l2.Next
	}
	carry := 0
	len1, len2 := len(stack1), len(stack2)
	for len1 > 0 || len2 > 0 || carry > 0 {
		a, b := 0, 0
		if len1 > 0 {
			a = stack1[len1-1]
			stack1 = stack1[:len1-1]
			len1--
		}
		if len2 > 0 {
			b = stack2[len2-1]
			stack2 = stack2[:len2-1]
			len2--
		}
		cur := a + b + carry
		carry = cur / 10
		cur = cur % 10
		p := &ListNode{Val: cur, Next: ans}
		ans = p
	}
	return ans
}

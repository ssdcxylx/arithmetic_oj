package main

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func flatten(root *Node) *Node {
	var reverse func(cur *Node) *Node
	reverse = func(cur *Node) (prev *Node) {
		for cur != nil {
			next := cur.Next
			if cur.Child != nil {
				head := cur.Child
				tail := reverse(head)

				head.Prev = cur
				cur.Next = head

				if next != nil {
					tail.Next = next
					next.Prev = tail
				}

				cur.Child = nil
				prev = tail
			} else {
				prev = cur
			}
			cur = next
		}
		return
	}
	reverse(root)
	return root
}

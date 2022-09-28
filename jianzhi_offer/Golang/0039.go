package main

func largestRectangleArea(heights []int) (ans int) {
	n := len(heights)
	left, right := make([]int, n), make([]int, n)
	for i:=0; i<n; i++ {
		right[i] = n
	}
	stack := []int{}
	for i, height := range heights {
		for len(stack)>0 && height <= heights[stack[len(stack)-1]] {
			right[stack[len(stack)-1]] = i
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	for i:=0; i<n; i++ {
		ans = max(ans, (right[i]-left[i]-1)*heights[i])
	}
	return 
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
} 
package main

func dailyTemperatures(temperatures []int) []int {
	ans := make([]int, len(temperatures))
	stack := []int{}
	for i, temperature := range temperatures {
		for len(stack)>0 && temperature > temperatures[stack[len(stack)-1]] {
			prevIdx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[prevIdx] = i-prevIdx
		}
		stack = append(stack, i)
	}
	return ans
}
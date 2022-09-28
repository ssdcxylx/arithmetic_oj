package main

import "strconv"

func evalRPN(tokens []string) int {
	stack := make([]int, len(tokens)/2+1)
	cur := 0
	for _, token := range tokens {
		val, err := strconv.Atoi(token)
		if err == nil {
			stack[cur] = val
		} else {
			cur -= 2
			num1, num2 := stack[cur], stack[cur+1]
			switch token {
			case "+":
				stack[cur] = num1 + num2
			case "-":
				stack[cur] = num1 - num2
			case "*":
				stack[cur] = num1 * num2
			default:
				stack[cur] = num1 / num2
			}
		}
		cur++
	}
	return stack[0]
}

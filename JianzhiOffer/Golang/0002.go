package main

import (
	"strconv"
)

func addBinary(a string, b string) string {
	res := ""
	carry := 0
	lenA, lenB := len(a), len(b)
	n := max(lenA, lenB) 
	for i := 0; i < n; i++ {
		if (i < lenA) {
			carry += int(a[lenA - i - 1] - '0')
		}
		if (i < lenB) {
			carry += int(b[lenB - i - 1] - '0')
		}
		res = strconv.Itoa(carry%2) + res
		carry >>= 1
	}
    if carry > 0 {
        res = "1" + res
    }
    return res
}

func max(x, y int) int {
	if (x > y) {
		return x
	}
	return y
}
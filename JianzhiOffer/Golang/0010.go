package main

import (
	"fmt"
)

func subarraySum(nums []int, k int) (ans int) {
    mp := map[int]int{}
	pre := 0
	mp[0] = 1
	for _, num := range nums {
		pre += num
		if _, ok := mp[pre-k]; ok {
			ans += mp[pre-k]
		}
		mp[pre] += 1
	}
	return
}

func main() {
	fmt.Println(subarraySum([]int{-1,-1,-1}, 0))
}
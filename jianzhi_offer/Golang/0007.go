package main

import (
	"sort"
)

func threeSum(nums []int) [][]int {
    res := make([][]int, 0)
	n := len(nums)
	sort.Ints(nums)
	for i := 0; i < n; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		k := n-1
		target := -nums[i]
		for j := i+1; j < n; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}
			for j < k && nums[j] + nums[k] > target {
				k--
			}
			if j == k {
				break
			}
			if nums[j] + nums[k] == target {
				res = append(res, []int{nums[i], nums[j], nums[k]})
			}
		}
	}
	return res
}

func main() {
	threeSum([]int{3,0,-2,-1,1,2})
}
func findMaxLength(nums []int) (ans int) {
	mp := map[int]int{0:-1}
	counter := 0
	for i, num := range nums {
		if num == 1 {
			counter++
		} else {
			counter--
		}
		if pre, ok := mp[counter]; ok {
			ans = max(ans, i-pre)
		} else {
			mp[counter] = i
		}
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
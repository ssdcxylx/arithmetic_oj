package main

func lengthOfLongestSubstring(s string) (ans int) {
	mp := map[byte]bool{}
	j, n := -1, len(s)
	for i := range s {
		if i != 0 {
			mp[s[i-1]] = false
		}
		for ; j+1 < n && !mp[s[j+1]]; j++ {
			mp[s[j+1]] = true
		}
		ans = max(ans, j-i+1)
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
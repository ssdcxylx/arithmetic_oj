package main

func isAlienSorted(words []string, order string) bool {
	mp := map[byte]int{}
	for i, _ := range order {
		mp[order[i]] = i
	}
	for i := 0; i < len(words)-1; i++ {
		j := 0
		l := min(len(words[i]), len(words[i+1]))
		for j < l {
			if mp[words[i][j]] > mp[words[i+1][j]] {
				return false
			} else if mp[words[i][j]] < mp[words[i+1][j]] {
				break
			}
			j++
		}
		if j == l && len(words[i]) > len(words[i+1]) {
			return false
		}
	}
	return true
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

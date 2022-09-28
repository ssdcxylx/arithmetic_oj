package main

func checkInclusion(s1 string, s2 string) bool {
    flags := make([]int, 26)
	for _, c := range s1 {
		flags[c-'a']--
	}
	i, n := 0, len(s1)
	for j, c := range s2 {
		x := c-'a'
		flags[x]++
		for flags[x] > 0 {
			flags[s2[i]-'a']--
			i++
		}
		if j-i+1 == n {
			return true
		}
	}
	return false
}
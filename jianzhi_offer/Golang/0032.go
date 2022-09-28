package main

func isAnagram(s string, t string) bool {
	if s == t {
		return false
	}
	cnts := make([]int, 26)
	for _, c := range s {
		cnts[c-'a']++
	}
	for _, c := range t {
		if cnts[c-'a'] == 0 {
			return false
		}
		cnts[c-'a']--
	}
	for _, cnt := range cnts {
		if cnt > 0 {
			return false
		}
	}
	return true
}

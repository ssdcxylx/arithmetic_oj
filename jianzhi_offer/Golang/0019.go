package main

func validPalindrome(s string) bool {
	return valid(s, true)
}

func valid(s string, first bool) bool {
	i, n := 0, len(s)
	for i < n-i-1 {
		if s[i] != s[n-i-1] {
			if first {
				return valid(s[i+1:n-i], false) || valid(s[i:n-i-1], false)
			}
			return false
		}
		i++
	}
	return true
}

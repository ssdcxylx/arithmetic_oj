package main

import "math"

func minWindow(s string, t string) string {
	tCnts, rCnts := make([]int, 52), make([]int, 52)
	index := func(c byte) byte {
		if c >= 'a' {
			return c - 'a'
		}
		return c - 'A' + 26
	}
	check := func() bool {
		for i := 0; i < 52; i++ {
			if rCnts[i] < tCnts[i] {
				return false
			}
		}
		return true
	}
	for i := range t {
		tCnts[index(t[i])]++
	}
	l, ansL, ansR, ansLen := 0, -1, -1, math.MaxInt32
	for r := range s {
		if tCnts[index(s[r])] > 0 {
			rCnts[index(s[r])]++
		}
		for ; check() && l <= r; l++ {
			if r-l+1 < ansLen {
				ansL, ansR = l, r
				ansLen = r - l + 1
			}
			if tCnts[index(s[l])] > 0 {
				rCnts[index(s[l])]--
			}
		}
	}
	if ansL == -1 {
		return ""
	}
	return s[ansL : ansR+1]
}

package main

func countSubstrings(s string) (ans int) {
	t := "$#"
	for _, c := range s {
		t += string(c) + "#"
	}
	n := len(t)
	t += "!"

	f := make([]int, n)
	maxI, maxR := 0, 0
	for i := 1; i < n; i++ {
		if i <= maxR {
			f[i] = min(maxR-i+1, f[2*maxI-i])
		} else {
			f[i] = 1
		}
		for t[i+f[i]] == t[i-f[i]] {
			f[i]++
		}
		if i+f[i]-1 > maxR {
			maxI = i
			maxR = i + f[i] - 1
		}
		ans += f[i] / 2
	}
	return
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

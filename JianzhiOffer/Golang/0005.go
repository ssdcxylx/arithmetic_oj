func maxProduct(words []string) int {
	ans := 0
	masks := map[int]int{}
	for _, word := range words {
		mask := 0
		for _, ch := range word {
			mask |= (1 << (ch - 'a'))
		}
		if len(word) > masks[mask] {
			masks[mask] = len(word)
		}
	}

	for x, lenX := range masks {
		for y, lenY := range masks {
			if x & y == 0 && lenX * lenY > ans {
				ans = lenX * lenY
			}
		}
	}
	return ans
}
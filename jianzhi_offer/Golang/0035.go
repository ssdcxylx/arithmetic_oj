func findMinDifference(timePoints []string) int {
	if len(timePoints) > 1440 {
		return 0
	}
	ans := 1440
	sort.Strings(timePoints)
	l := len(timePoints)
	prev := getMinutes(timePoints[0])
	for i := 1; i < l; i++ {
		cur := getMinutes(timePoints[i])
		ans = min(ans, cur-prev)
		prev = cur
	}
	ans = min(ans, 1440-getMinutes(timePoints[l-1])+getMinutes(timePoints[0]))
	return ans
}

func getMinutes(timePoint string) int {
	return getNum(timePoint[0])*600 + getNum(timePoint[1])*60 + getNum(timePoint[3])*10 + getNum(timePoint[4])
}

func getNum(c byte) int {
	return int(c - '0')
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
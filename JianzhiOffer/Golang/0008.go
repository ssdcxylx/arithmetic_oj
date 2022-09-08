func minSubArrayLen(target int, nums []int) int {
    n := len(nums)
    start, end := 0, 0
    ans := math.MaxInt32
    sum := 0
    for end < n {
        sum += nums[end]
        for sum >= target {
            ans = min(ans, end - start + 1)
            sum -= nums[start]
            start ++
        }
        end++
    }
    if ans == math.MaxInt32 {
        return 0
    }
    return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
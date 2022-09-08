func numSubarrayProductLessThanK(nums []int, k int) int {
    ans := 0
    i, mult := 0, 1
    for j, num := range nums {
        mult *= num
        for ; i <= j && mult >= k; i++ {
            mult /= nums[i]
        }
        ans += j - i + 1
    }
    return ans
}
func pivotIndex(nums []int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    sum := 0
    for i, num := range nums {
        if 2 * sum + num == total {
            return i
        }
        sum += num
    }
    return -1
}
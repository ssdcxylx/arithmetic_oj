func twoSum(numbers []int, target int) []int {
    low, high := 0, len(numbers) - 1
    for sum := numbers[low] + numbers[high]; sum != target; sum = numbers[low] + numbers[high]  {
        if sum > target {
            high--
        } else {
            low++
        }
    }
    return []int{low, high}
}
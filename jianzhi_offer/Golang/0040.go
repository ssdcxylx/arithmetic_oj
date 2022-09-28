func maximalRectangle(matrix []string) (ans int) {
    if len(matrix) == 0 {
        return 0
    }
    m, n := len(matrix), len(matrix[0])
    total := make([][]int, m)
    for i, row := range matrix {
        total[i] = make([]int, n)
        for j, v := range row {
            if v == '0' {
                continue
            }
            if i == 0 {
                total[i][j] = 1
            } else {
                total[i][j] = total[i-1][j]+1
            }
        }
    }
    for i, row := range total {
        stack := []int{}
        left, right := make([]int, n), make([]int, n)
        for j:=0; j<n; j++ {
            right[j] = n
        }
        for j, val := range row {
            for len(stack) > 0 && val <= total[i][stack[len(stack)-1]] {
                right[stack[len(stack)-1]] = j
                stack = stack[:len(stack)-1]
            }
            if len(stack) == 0 {
                left[j] = -1
            } else {
                left[j] = stack[len(stack)-1]
            }
            stack = append(stack, j)
        }
        for j:=0; j<n; j++ {
            ans = max(ans, (right[j]-left[j]-1) * row[j])
        }
    }
    return 
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
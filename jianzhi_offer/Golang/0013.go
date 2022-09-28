package main

type NumMatrix struct {
    sums [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    sums := make([][]int, len(matrix))
	if (len(matrix) == 0) {
		return
	}
	sums[0] = make([]int, len(matrix[0])+1)
	for i, row := range matrix {
		sums[i+1] = make([]int, len(row)+1)
		for j, val := range row {
			sums[i+1][j+1] = sums[i+1][j] + sums[i][j+1] - sums[i][j] + val
		}
	}
	return NumMatrix{sums}
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	return this.sums[row2+1][col2+1] - this.sums[row2+1][col1] - this.sums[row1][col2+1] + this.sums[row1][col1]
}
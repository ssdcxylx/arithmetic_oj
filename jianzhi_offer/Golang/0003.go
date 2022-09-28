package main

func count(x int) (ans int) {
    for ; x > 0; x &= (x - 1) {
        ans += 1
    }
    return
}

func countBits(n int) []int {
    res := make([]int, n+1)
    for i := range res {
		res[i] = count(i)
    }
    return res
}

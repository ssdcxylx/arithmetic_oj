package main

func divide(a int, b int) int {
	// 处理补码无符号右移产生的问题
	if a == -1 {
			if b == -1 {
					return 1
			} else if b == 1{
					return -1
			} else {
					return 0
			}
	}
	// 处理溢出
	if a == -(1 << 31) && b == -1 {
			return (1 << 31) - 1
	}
	flag := ((a > 0) && (b < 0)) || ((a < 0) && (b > 0))
	if a < 0 {
			a = -a
	}
	if b < 0 {
			b = -b
	}
	res := 0    
	for i := 31; i >= 0; i-- {
			if (a >> i) - b >= 0 {
					a -= (b << i)
					res += (1 << i)
			}
	}
	if flag {
			return -res
	}
	return res
}
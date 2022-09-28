package main

type MovingAverage struct {
	size, sum int
	queue     []int
}

/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {
	return MovingAverage{
		size: size,
	}
}

func (this *MovingAverage) Next(val int) float64 {
	if len(this.queue) == this.size {
		this.sum -= this.queue[0]
		this.queue = this.queue[1:len(this.queue)]
	}
	this.queue = append(this.queue, val)
	this.sum += val
	return float64(this.sum) / float64(len(this.queue))
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * obj := Constructor(size);
 * param_1 := obj.Next(val);
 */

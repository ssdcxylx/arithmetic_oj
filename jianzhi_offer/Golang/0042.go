package main

type RecentCounter []int

func Constructor() (_ RecentCounter) { return }

func (this *RecentCounter) Ping(t int) int {
	*this = append(*this, t)
	for (*this)[0] < t-3000 {
		*this = (*this)[1:]
	}
	return len(*this)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */

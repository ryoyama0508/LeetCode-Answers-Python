package main

import "math"

func main() {
	println(maxProfit([]int{7, 2, 0, 3, 1}))
}

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}

	buy := math.MaxInt32
	println(buy)
	var max int
	for i := 0; i < len(prices); i++ {
		if buy > prices[i] {
			buy = prices[i]
			println(buy)
		} else {
			pro := prices[i] - buy
			if pro > max {
				max = pro
			}
		}
	}
	return max
}

/* max, lowest := 0, 0
for i := 1; i < len(prices); i++ {
	if prices[i] < prices[lowest] {
		lowest = i
	} else if cur := prices[i] - prices[lowest]; cur > max {
		max = cur
	}
}
return max */

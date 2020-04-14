package main

import (
	"fmt"
)

func main() {
	fmt.Println(maxSubArray([]int{1, 2}))

}

func maxSubArray(nums []int) int {

	var max int
	var newnums []int
	if len(nums) == 1 {
		max = nums[0]
		return max
	}
	newnums = nums
	for headindex, num := range nums {
		if num <= 0 {
			newnums = headRemove(nums, headindex)
		} else {
			break
		}
	}

	if len(newnums) == 0 { //全部消えた
		var belowzeromax int
		for i := 0; i < len(nums); i++ {
			if i == 0 {
				belowzeromax = nums[i]
			}
			if belowzeromax < nums[i] {
				belowzeromax = nums[i]
			}
		}
		max = belowzeromax

		return max
	}
	fmt.Println(len(newnums))
	if len(newnums) == 0 {
		newnums = nums
	}
	if len(newnums) == 1 {
		max = newnums[0]
		return max
	}
	for tailindex := len(newnums) - 1; ; tailindex-- { //ここ
		if newnums[tailindex] <= 0 {
			newnums = tailRemove(newnums, newnums[tailindex])
		} else {
			break
		}
	}
	if len(newnums) == 1 {
		max = newnums[0]
		return max
	}
	fmt.Println(newnums)

	var sum int
	var store []int
	var maxnumsofar int
	for n := 0; n < len(newnums); n++ {
		for i := n; i < len(newnums); i++ {
			println(i)
			sum += newnums[i]
			store = append(store, sum)

		}
		for m := 0; m < len(store); m++ {
			if store[m] > maxnumsofar {

				maxnumsofar = store[m]
			}
		}
		sum = 0
		store = []int{}
	}
	return maxnumsofar
}

func headRemove(slice []int, s int) []int {
	var newnums []int
	newnums = append(newnums, slice[s+1:]...)
	return newnums
}

func tailRemove(slice []int, s int) []int {
	var newnums []int
	newnums = append(newnums, slice[:len(slice)-1]...)
	return newnums
}
func remove(slice []int, s int) []int {
	if s >= len(slice) {
		return slice
	}
	return append(slice[:s], slice[s+1:]...)
}
func insert(slice []int, pos int, ele int) []int {
	newslice := append(slice[:pos+1], slice[pos:]...)
	newslice[pos] = ele
	return newslice
}

/* return findSubArray(nums, 0, len(nums)-1)
}

func findCrossSubArray(nums []int, left int, right int) int {

	mid := left + (right-left)/2
	leftSum := math.MinInt32
	rightSum := math.MinInt32

	sum := 0

	for i := mid; i >= left; i-- {
		sum += nums[i]
		if sum > leftSum {
			leftSum = sum
		}
	}

	sum = 0
	for i := mid + 1; i <= right; i++ {
		sum += nums[i]
		if sum > rightSum {
			rightSum = sum
		}
	}

	return leftSum + rightSum
}

func findSubArray(nums []int, left int, right int) int {
	if left == right {
		return nums[left]
	}

	mid := left + (right-left)/2 //3



	a := findSubArray(nums, left, mid)
	b := findSubArray(nums, mid+1, right)
	c := findCrossSubArray(nums, left, right)

	fmt.Println(a)
	fmt.Println(b)


	if a > b {
		if a > c {
			return a
		} else {
			return c
		}
	} else {
		if b > c {
			return b
		} else {
			return c
		}
	}
} */

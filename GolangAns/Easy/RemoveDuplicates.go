package main

import "fmt"

func main(){
	fmt.Printf("%x ", removeDuplicates([]int{1,2,3,4,5}))
}

func removeDuplicates(nums []int) int{
	nlen := len(nums)
	if nlen == 0 {
		return 0
	}
	
	curIdx, prev := 0, nums[0]
	for i := 0; i < nlen; i++ {
		if nums[i] !=  prev  {
			curIdx++
			nums[curIdx] = nums[i]
			prev = nums[i]
		}
	}
	return curIdx + 1
}
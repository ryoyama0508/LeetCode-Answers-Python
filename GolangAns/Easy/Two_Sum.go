package main

import "fmt"

func main() {
	nums := []int{2, 7, 11, 15}
	twoSum(nums, 9)
	fmt.Println(twoSum(nums, 9))
}
func twoSum(nums []int, target int) []int {
	x, y := 0, 1
	for x < len(nums) {
		for ; y < len(nums); y++ {
			if nums[x]+nums[y] == target {
				return []int{x, y}
			}
		}
		x++
		y = x + 1
	}
	return nil
}

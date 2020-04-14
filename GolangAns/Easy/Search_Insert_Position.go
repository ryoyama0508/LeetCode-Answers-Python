package main

func main() {
	println(searchInsert([]int{1, 3}, 3))
}

func searchInsert(nums []int, target int) int {

	var result int
	for i := 0; i < len(nums); i++ { // i!=len(nums)
		if nums[i] == target {
			result = i
		} else if i < len(nums)-1 {
			if nums[i] < target && target < nums[i+1] {
				result = i + 1
			}
		} else if target < nums[0] {
			result = 0
		} else if target > nums[len(nums)-1] {
			result = len(nums)
		}
	}
	return result
}

package main

import "fmt"

func main() {
	print(singleNumber([]int{3, 1, -2, 1, 3}))
}

func singleNumber(nums []int) int {
	m := map[int]int{}
	sum := 0

	for i := range nums {
		if m[nums[i]] == 0 {
			m[nums[i]] = nums[i]
			sum += nums[i]
		} else {
			delete(m, nums[i])
			sum -= nums[i]
		}
	}
	fmt.Println(m)
	return sum

}

//マップの初期化情報の確認　ハッシュ関数も

/* var result int
	var first int
	if len(nums) == 1 {
		return nums[0]
	}
L:
	for i := 0; i < len(nums); {
		first = nums[i]
		print(first)
		for l := 1; l < len(nums); l++ {
			if first == nums[l] {
				nums = delete(nums, l)
				nums = delete(nums, 0)
				fmt.Println(nums)
				if len(nums) == 1 {
					return nums[0]
				}
				continue L
			}
		}
		result = first
		break
	}

	return result
}

func delete(s []int, i int) []int {
	if i >= len(s) {
		return s
	}
	return append(s[:i], s[i+1:]...)

} */

//this is blute force so far

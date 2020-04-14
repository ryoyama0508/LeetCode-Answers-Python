package main

import "fmt"

//BinaryTreeinput ...
type BinaryTreeinput struct {
	num          int
	leftPointer  *BinaryTreeinput
	rightPointer *BinaryTreeinput
}

func main() {
	nums := BinaryTreeinput{
		num: 1,
		leftPointer: &BinaryTreeinput{
			num: 2,
			leftPointer: &BinaryTreeinput{
				num:          3,
				leftPointer:  nil,
				rightPointer: nil,
			},
			rightPointer: &BinaryTreeinput{
				num:          4,
				leftPointer:  nil,
				rightPointer: nil,
			},
		},
		rightPointer: &BinaryTreeinput{
			num: 5,
			leftPointer: &BinaryTreeinput{
				num:          6,
				leftPointer:  nil,
				rightPointer: nil,
			},
			rightPointer: &BinaryTreeinput{
				num:          7,
				leftPointer:  nil,
				rightPointer: nil,
			},
		},
	}
	result := binaryTree(nums)

	fmt.Println(result)
}

func binaryTree(randomNums BinaryTreeinput) []int {
	retTree := []int{}
	for i, j := 0, 1; i < len(randomNums)-1; i++ {
		retTree[j] = randomNums[i]
		j = 2 * j
	}
}

package main

import (
	"fmt"
)

func main() {
	fmt.Println("result", climbStairs(35))
}

func climbStairs(n int) int {
	total := 1

	syo := n / 2
	amari := n % 2
	if n%2 == 0 {
		total++
		syo--
		amari += 2
	}
	for syo > 0 {
		total += patterns(syo, amari) //3 1
		fmt.Println(syo, amari)
		fmt.Println(total)
		syo--
		amari += 2
	}
	return total
}

func patterns(step2 int, step1 int) int {
	topTmp := step2 + step1
	step1Tmp := step1
	top := 1
	bottom := 1
	for step1Tmp > 0 {
		top *= topTmp
		bottom *= step1Tmp
		topTmp--
		step1Tmp--
	}
	ret := top / bottom
	return ret
}

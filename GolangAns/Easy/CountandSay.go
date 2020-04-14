package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Printf("%v", countAndSay(4))

}

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	if n == 2 {
		return "11"
	}
	var result []byte
	resultstring := "11"
	for l := 0; l != n-2; l++ {
		println(l)
		for index := 0; index < len(resultstring); { //i=1　毎回の数字をつくる　iは何桁目をみるか
			num := resultstring[index]
			lastindex := index
			for i := index; i < len(resultstring); i++ {
				if num != resultstring[i] {
					break
				}
				lastindex = i
			}
			length := lastindex - index + 1

			result = append(result, []byte(strconv.Itoa(length))...)
			result = append(result, num)

			index = lastindex + 1
		}
		resultstring = string(result)
	}
	return resultstring
}

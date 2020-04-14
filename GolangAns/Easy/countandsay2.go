package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(countAndSay(6))
}

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	result := handle([]byte("1"), n-1)
	return string(result)
}

func handle(s []byte, n int) []byte {
	if n == 0 {
		return s
	}
	result, index, inputLength := []byte{}, 0, len(s)

	for index < inputLength { //inputの容量に達するまでindexを増やしていく
		currentValue := s[index]   //数字の中身
		lastRepeatedIndex := index //区切りの時点のindexを
		println(lastRepeatedIndex)

		for i := index; i < inputLength; i++ { //桁を比べていって数字が異なったら長さを図る
			if currentValue != s[i] { //隣と違ったら区切って一回追加する current valueは区切りッタ最初の数
				break
			}

			lastRepeatedIndex = i //桁が同じならばLRIを足していく
		}

		length := lastRepeatedIndex - index + 1 //長さ図る

		result = append(result, []byte(strconv.Itoa(length))...)
		result = append(result, currentValue) //入れる

		index = lastRepeatedIndex + 1 //同じだった桁の次からindexを撮り始める
	}

	return handle(result, n-1)
}

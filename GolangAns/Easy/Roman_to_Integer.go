package main

import (
	"strings"
)

func main() {
	println(romanToInt("MCMXCIV"))
}

func romanToInt(s string) int {
	/* I             1
	V             5
	X             10
	L             50
	C             100
	D             500
	M             1000 */
	splitedRoman := strings.Split(s, "")
	sum := 0
	for n := 0; n < len(splitedRoman); n++ {
		a := splitedRoman[n]
		println(splitedRoman[n])
		if a == "I" {
			sum++
		} else if a == "V" {
			sum += 5
			if n > 0 {
				if splitedRoman[n-1] == "I" {
					sum -= 2
				}
			}
		} else if a == "X" {
			sum += 10
			if n > 0 {
				if splitedRoman[n-1] == "I" {
					sum -= 2
				}
			}
		} else if a == "L" {
			sum += 50
			if n > 0 {
				if splitedRoman[n-1] == "X" {
					sum -= 20
				}
			}
		} else if a == "C" {
			sum += 100
			if n > 0 {
				if splitedRoman[n-1] == "X" {
					sum -= 20
				}
			}
		} else if a == "D" {
			sum += 500
			if n > 0 {
				if splitedRoman[n-1] == "C" {
					sum -= 200
				}
			}
		} else if a == "M" {
			sum += 1000
			if n > 0 {
				if splitedRoman[n-1] == "C" {
					sum -= 200
				}
			}
		}
	}
	return sum
}

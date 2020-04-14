package main

func main() {
	println(palindrome(121))
}

func palindrome(x int) bool {
	reversed := 0
	origin := x

	if x < 0 {
		return false
	}
	for x != 0 {
		pop := x % 10
		x = x / 10

		reversed = (reversed * 10) + pop
	}
	println(origin)
	println(reversed)
	if origin != reversed {
		return false
	}
	return true
}

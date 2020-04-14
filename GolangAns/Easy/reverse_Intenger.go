package main

func main() {
	println(reverse(-123))
}

func reverse(x int) int {
	var pop int
	reversed := 0
	var MaxInt int32 = 2147483647

	if x > int(MaxInt) || x < -int(MaxInt) {
		return 0
	}
	for x != 0 {
		pop = x % 10
		x = x / 10

		reversed = (reversed * 10) + pop
	}

	if reversed > int(MaxInt) {
		return 0
	}
	return reversed

}

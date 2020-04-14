package main

import "fmt"

func main() {
	/* str := "a"
	b := str[0]
	println(b)
	strtwo := "abc"
	println(strtwo[0])
	for _, r := range str {
		fmt.Println(r)
	} */
	//all are rune
	//rune can be caliculated each other

	s := "Gopherはかわいい"
	fmt.Println(s[0:7])
	fmt.Println(string([]rune(s)[0:7]))
}
func reverse(s []string) []string {
	var newarr []string
	for n := 0; n < len(s)-1; n++ {
		lastStr := s[len(s)-n]
		newarr = append(newarr, lastStr)
	}
	return newarr
}

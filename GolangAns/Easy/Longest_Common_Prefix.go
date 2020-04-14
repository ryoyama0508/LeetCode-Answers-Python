package main

func main() {
	println(longestCommonPrefix([]string{"aa", "a"}))
}
func longestCommonPrefix(strs []string) string {
	var longestCommonPrefix []byte
	for i := 0; i < len(strs); i++ {
		if i == 0 {
			longestCommonPrefix = []byte(strs[i])
			continue
		}
		byted := []byte(strs[i])
		if len(byted) == 0 {
			return ""
		}
		for l, m := 0, 0; l < len(longestCommonPrefix) && m < len(byted); l++ {
			if len(longestCommonPrefix) > len(byted) {
				longestCommonPrefix = unset(len(byted), longestCommonPrefix)
			}
			if longestCommonPrefix[l] != byted[m] {
				longestCommonPrefix = unset(l, longestCommonPrefix)
				if len(longestCommonPrefix) == 0 {
					return ""
				}
				break
			}
			m++
		}
	}
	ret := string(longestCommonPrefix)
	return ret
}

func unset(i int, s []byte) []byte {
	if i >= len(s) {
		return s
	}
	return append(s[:i])

}

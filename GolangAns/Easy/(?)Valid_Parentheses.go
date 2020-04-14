package main

func main() {
	println(isValid("((())"))
}
func isValid(s string) bool {
	var c byte
	stack := make([]byte, 0)
	m := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}
	println(len(m))
	// byte の：表示がわからない　（この並びは何）
	for i := 0; i < len(s); i++ {
		c = s[i] //byteとstring のかんけいせいが謎？
		if c == '(' || c == '[' || c == '{' {
			stack = append(stack, c)
		} else {
			if v, ok := m[c]; ok { // byte に対して　ok　って何？
				if !pop(v, &stack) {
					return false
				}
			} else {
				return false
			}
		}
	}
	if len(stack) != 0 {
		return false
	}
	return true
}

func pop(c byte, stack *[]byte) bool {
	l := len(*stack) //なんバイトなのか調べている
	if l < 1 {
		return false
	}
	//１個目ならfalse
	var poped byte
	*stack, poped = (*stack)[:l-1], (*stack)[l-1]

	if poped != c {
		return false
	}
	return true
}

/* 順番と残しがないかのチェック */
/* 1, to check the order, gotta use stack. when face the open ,then put into stack
2, when find close, we gotta check if pop(top of the stack is open or not) is close
3, if not we return false */

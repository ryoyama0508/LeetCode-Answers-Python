package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	mergeTwoLists()
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil{
		return l1
	}
	var ret, n1, n2 *ListNode

	if l1.Val < l2.Val{
		ret, n1, n2 = l1, l1.Next, l2
	} else{
		ret, n1, n2 = l2, l2.Next, l1
	}
	n:= ret
	for n1!=nil && n2!= nil{
		if n1.Val< n2.Val{
			n.Next,n1= n1, n1.Next 
		}else {
			n.Next,n2= n2, n2.Next
		}
		n= n.Next
	}

		if n1==nil{
			n.Next= n2
		}else if n2==nil{
			n.Next= n1
		}
		return ret
	
}

/* The idea is to use a new linked list to merge two sorted linked lists.
Then we only need to compare the two linked lists from the beginning.
The new linked list pointers point to the nodes with small values ​​each time, compare them in turn, and finally, one of them.
When the linked list reaches the end, we only need to point the new linked list pointer to another pointer that is not at the end of the linked list. */
